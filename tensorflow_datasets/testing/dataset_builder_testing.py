# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base DatasetBuilderTestCase to test a DatasetBuilder base class."""

import collections
import contextlib
import difflib
import hashlib
import itertools
import numbers
import os
import textwrap
from typing import Iterator, List, Optional, Union
from unittest import mock

from absl import logging
from absl.testing import parameterized
from etils import epath
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import load
from tensorflow_datasets.core import utils
from tensorflow_datasets.core import visibility
from tensorflow_datasets.core.download import checksums
from tensorflow_datasets.testing import feature_test_case
from tensorflow_datasets.testing import test_utils

# `os` module Functions for which tf.io.gfile equivalent should be preferred.
FORBIDDEN_OS_FUNCTIONS = (
    "chmod",
    "chown",
    "link",
    "listdir",
    "lstat",
    "makedirs",
    "mkdir",
    "mknod",
    "open",
    "pathconf",
    "readlink",
    "remove",
    "removedirs",
    "rename",
    "renames",
    "rmdir",
    "stat",
    "statvfs",
    "symlink",
    "unlink",
    "walk",
)
FORBIDDEN_OS_PATH_FUNCTIONS = (
    "exists",
    "isdir",
    "isfile",
)

_ORGINAL_NP_LOAD = np.load


def _np_load(file_, mmap_mode=None, allow_pickle=False, **kwargs):
  if not hasattr(file_, "read"):
    raise AssertionError(
        "You MUST pass a `tf.io.gfile.GFile` or file-like object to `np.load`.")
  if allow_pickle:
    raise AssertionError("Unpicling files is forbidden for security reasons.")
  return _ORGINAL_NP_LOAD(file_, mmap_mode, allow_pickle, **kwargs)


class DatasetBuilderTestCase(parameterized.TestCase,
                             feature_test_case.SubTestCase):
  """Inherit this class to test your DatasetBuilder class.

  You must set the following class attributes:

    * DATASET_CLASS: class object of DatasetBuilder you want to test.

  You may set the following class attributes:

    * VERSION: `str`. The version used to run the test. eg: '1.2.*'.
      Defaults to None (canonical version).
    * BUILDER_CONFIG_NAMES_TO_TEST: `list[str | tfds.core.BuilderConfig]`,
      the list of builder configs that should be tested. If None, all the
      BUILDER_CONFIGS from the class will be tested.
    * DL_EXTRACT_RESULT: `dict[str, str]`, the returned result of mocked
      `download_and_extract` method. The values should be the path of files
      present in the `fake_examples` directory, relative to that directory.
      If not specified, path to `fake_examples` will always be returned.
    * DL_EXTRACT_ONLY_RESULT: `dict[str, str]`, the returned result of mocked
      `extract` method. The values should be the path of files present in the
      `fake_examples` directory, relative to that directory. If not specified:
      will call DownloadManager `extract` method.
    * DL_DOWNLOAD_RESULT: `dict[str, str]`, the returned result of mocked
      `download_and_extract` method. The values should be the path of files
      present in the `fake_examples` directory, relative to that directory.
      If not specified: will use DL_EXTRACT_RESULT (this is due to backwards
      compatibility and will be removed in the future).
    * EXAMPLE_DIR: `str`, the base directory in in which fake examples are
      contained. Optional; defaults to `<dataset dir>/dummy_data/`.
    * OVERLAPPING_SPLITS: `list[str]`, splits containing examples from other
      splits (e.g. a "example" split containing pictures from other splits).
    * MOCK_OUT_FORBIDDEN_OS_FUNCTIONS: `bool`, defaults to True. Set to False to
      disable checks preventing usage of `os` or builtin functions instead of
      recommended `tf.io.gfile` API.
    * SKIP_CHECKSUMS: Checks that the urls called by `dl_manager.download`
      are registered.
    * SKIP_TF1_GRAPH_MODE: Runs in eager mode only.

  This test case will check for the following:

   - the dataset builder is correctly registered, i.e. `tfds.load(name)` works;
   - the dataset builder can read the fake examples stored in
       testing/test_data/fake_examples/{dataset_name};
   - the dataset builder can produce serialized data;
   - the dataset builder produces a valid Dataset object from serialized data
     - in eager mode;
     - in graph mode.
   - the produced Dataset examples have the expected dimensions and types;
   - the produced Dataset has and the expected number of examples;
   - a example is not part of two splits, or one of these splits is whitelisted
       in OVERLAPPING_SPLITS.
  """

  DATASET_CLASS = None
  VERSION = None
  BUILDER_CONFIG_NAMES_TO_TEST: Optional[List[Union[
      str, dataset_builder.BuilderConfig]]] = None
  DL_EXTRACT_RESULT: Optional[str] = None
  DL_EXTRACT_ONLY_RESULT: Optional[str] = None
  DL_DOWNLOAD_RESULT: Optional[str] = None
  EXAMPLE_DIR = None
  OVERLAPPING_SPLITS = []
  MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = True
  SKIP_CHECKSUMS = False
  SKIP_TF1_GRAPH_MODE = False

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    name = cls.__name__
    # Check class has the right attributes
    if cls.DATASET_CLASS is None or not callable(cls.DATASET_CLASS):
      raise AssertionError(
          "Assign your DatasetBuilder class to %s.DATASET_CLASS." % name)

    cls._available_cm = visibility.set_availables_tmp([
        visibility.DatasetType.TFDS_PUBLIC,
    ])
    cls._available_cm.__enter__()

  @classmethod
  def tearDownClass(cls):
    super().tearDownClass()
    cls._available_cm.__exit__(None, None, None)

  def setUp(self):
    super(DatasetBuilderTestCase, self).setUp()
    self.patchers = []
    self.builder = self._make_builder()

    if self.MOCK_OUT_FORBIDDEN_OS_FUNCTIONS:
      self._mock_out_forbidden_os_functions()

    # Track the urls which are downloaded to validate the checksums
    # The `dl_manager.download` and `dl_manager.download_and_extract` are
    # patched to record the urls in `_download_urls`.
    # Calling `dl_manager.download_checksums` stop the url
    # registration (as checksums are stored remotelly)
    # `_test_checksums` validates the recorded urls.
    self._download_urls = set()
    self._stop_record_download = False

  def tearDown(self):
    super(DatasetBuilderTestCase, self).tearDown()
    for patcher in self.patchers:
      patcher.stop()

  @utils.classproperty
  @classmethod
  @utils.memoize()
  def dummy_data(cls) -> epath.Path:  # pylint: disable=no-self-argument
    """Path to the `dummy_data/` directory."""
    if cls is DatasetBuilderTestCase:  # Required for build_api_docs
      return None  # pytype: disable=bad-return-type

    dummy_data_expected = cls.DATASET_CLASS.code_path.parent / "dummy_data"
    fake_example_dir = epath.Path(test_utils.fake_examples_dir())
    if cls.EXAMPLE_DIR is not None:
      dummy_data_found = epath.Path(cls.EXAMPLE_DIR)
      dummy_data_expected = dummy_data_found  # Dir to display in the error
    elif dummy_data_expected.exists():
      dummy_data_found = dummy_data_expected
    else:
      dummy_data_found = fake_example_dir / cls.DATASET_CLASS.name

    if not dummy_data_found.exists():
      err_msg = f"Dummy data not found in: {dummy_data_expected}"
      raise ValueError(err_msg)
    return dummy_data_found

  def _mock_out_forbidden_os_functions(self):
    """Raises error if forbidden os functions are called instead of gfile."""
    err = AssertionError("Do not use `os`, but `tf.io.gfile` module instead. "
                         "This makes code compatible with more filesystems.")
    sep = os.path.sep
    mock_os_path = mock.Mock(os.path, wraps=os.path)
    mock_os_path.sep = sep
    for fop in FORBIDDEN_OS_PATH_FUNCTIONS:
      getattr(mock_os_path, fop).side_effect = err
    mock_os = mock.Mock(os, path=mock_os_path, fspath=os.fspath)
    for fop in FORBIDDEN_OS_FUNCTIONS:
      if os.name == "nt" and not hasattr(os, fop):
        continue  # Not all `os` functions are available on Windows (ex: chmod).
      getattr(mock_os, fop).side_effect = err
    os_patcher = mock.patch(
        self.DATASET_CLASS.__module__ + ".os", mock_os, create=True)
    os_patcher.start()
    self.patchers.append(os_patcher)

    mock_builtins = __builtins__.copy()  # pytype: disable=module-attr
    mock_builtins["open"] = mock.Mock(side_effect=err)
    open_patcher = mock.patch(self.DATASET_CLASS.__module__ + ".__builtins__",
                              mock_builtins)
    open_patcher.start()
    self.patchers.append(open_patcher)

    # It's hard to mock open within numpy, so mock np.load.
    np_load_patcher = mock.patch("numpy.load", _np_load)
    np_load_patcher.start()
    self.patchers.append(np_load_patcher)

  def test_baseclass(self):
    self.assertIsInstance(
        self.builder, dataset_builder.DatasetBuilder,
        "Dataset class must inherit from `dataset_builder.DatasetBuilder`.")
    # Since class was instantiated and base class is ABCMeta, then we know
    # all needed methods were implemented.

  def test_registered(self):
    self.assertIn(self.builder.name,
                  load.list_builders(with_community_datasets=False,))

  def test_info(self):
    info = self.builder.info
    self.assertIsInstance(info, dataset_info.DatasetInfo)
    self.assertEqual(self.builder.name, info.name)

  def _add_url(self, url_or_urls):
    if self._stop_record_download:
      # Stop record the checksums if dl_manager.download_checksums has been
      # called (as checksums may be stored remotelly)
      return
    if isinstance(url_or_urls, download.resource.Resource):
      self._download_urls.add(url_or_urls.url)
    else:
      self._download_urls.add(url_or_urls)

  def _get_dl_extract_result(self, url):
    tf.nest.map_structure(self._add_url, url)
    del url
    if self.DL_EXTRACT_RESULT is None:
      return self.dummy_data
    return tf.nest.map_structure(
        lambda fname: self.dummy_data / fname,
        self.DL_EXTRACT_RESULT,
    )

  def _get_dl_extract_only_result(self, url):
    if self.DL_EXTRACT_ONLY_RESULT:
      tf.nest.map_structure(self._add_url, url)
      return tf.nest.map_structure(
          lambda fname: self.dummy_data / fname,
          self.DL_EXTRACT_ONLY_RESULT,
      )

  def _get_dl_download_result(self, url):
    tf.nest.map_structure(self._add_url, url)
    if self.DL_DOWNLOAD_RESULT is None:
      # This is only to be backwards compatible with old approach.
      # In the future it will be replaced with using self.dummy_data.
      return self._get_dl_extract_result(url)
    return tf.nest.map_structure(
        lambda fname: self.dummy_data / fname,
        self.DL_DOWNLOAD_RESULT,
    )

  def _download_checksums(self, url):
    self._stop_record_download = True

  def _make_builder(self, config=None):
    return self.DATASET_CLASS(  # pylint: disable=not-callable
        data_dir=self.tmp_dir,
        config=config,
        version=self.VERSION)

  @test_utils.run_in_graph_and_eager_modes()
  def test_download_and_prepare_as_dataset(self):
    if not tf.executing_eagerly() and self.SKIP_TF1_GRAPH_MODE:
      logging.warning("Skipping tests in non-eager mode")
      return

    # Extract configs to test
    configs_to_test: List[Union[str, dataset_builder.BuilderConfig]] = []
    if self.BUILDER_CONFIG_NAMES_TO_TEST:
      for config in self.BUILDER_CONFIG_NAMES_TO_TEST:  # pylint: disable=not-an-iterable
        if isinstance(config, dataset_builder.BuilderConfig):
          configs_to_test.append(config)
        elif config in self.builder.builder_configs:
          # Append the `name` rather than the config due to
          # https://github.com/tensorflow/datasets/issues/2348
          configs_to_test.append(config)
        else:
          raise ValueError(f"Invalid config {config} specified in test."
                           f"Available: {list(self.builder.builder_configs)}")
    else:
      configs_to_test.extend(cfg.name for cfg in self.builder.BUILDER_CONFIGS)

    print(f"Total configs: {len(configs_to_test)}")
    if configs_to_test:
      for config in configs_to_test:
        config_name = config if isinstance(config, str) else config.name
        with self._subTest(config_name):
          print(f"Testing config {config_name}")
          builder = self._make_builder(config=config)
          self._download_and_prepare_as_dataset(builder)
    else:
      self._download_and_prepare_as_dataset(self.builder)

    if not self.SKIP_CHECKSUMS:
      with self._subTest("url_checksums"):
        self._test_checksums()

  def _test_checksums(self):
    # If no call to `dl_manager.download`, then no need to check url presence.
    if not self._download_urls:
      return

    err_msg = (
        "Did you forget to record checksums with `--register_checksums` ? See "
        "instructions at: "
        "hhttps://www.tensorflow.org/datasets/add_dataset#run_the_generation_codeIf"
        " want to opt-out of checksums validation, please add `SKIP_CHECKSUMS "
        "= True` to the `DatasetBuilderTestCase`.\n")
    url_infos = self.DATASET_CLASS.url_infos
    filepath = self.DATASET_CLASS._checksums_path  # pylint: disable=protected-access
    # Legacy checksums: Search in `checksums/` dir
    if url_infos is None:
      legacy_filepath = checksums._checksum_paths().get(self.builder.name)  # pylint: disable=protected-access
      if legacy_filepath and legacy_filepath.exists():
        filepath = legacy_filepath
        url_infos = checksums.load_url_infos(filepath)
    # Checksums not present neither in legacy nor package
    if url_infos is None:
      raise FileNotFoundError(
          f"Checksums file not found at: {filepath}\n"
          f"{err_msg}\n"
      )

    missing_urls = self._download_urls - set(url_infos.keys())
    self.assertEmpty(
        missing_urls,
        f"Some urls checksums are missing at: {filepath}\n{err_msg}")

  def _download_and_prepare_as_dataset(self, builder):
    # Provide the manual dir only if builder has MANUAL_DOWNLOAD_INSTRUCTIONS
    # set.

    missing_dir_mock = mock.PropertyMock(
        side_effect=Exception("Missing MANUAL_DOWNLOAD_INSTRUCTIONS"))

    manual_dir = (
        self.dummy_data
        if builder.MANUAL_DOWNLOAD_INSTRUCTIONS else missing_dir_mock)

    patches = {
        "download_and_extract": self._get_dl_extract_result,
        "download": self._get_dl_download_result,
        "download_checksums": self._download_checksums,
        "manual_dir": manual_dir,
        "download_dir": self.dummy_data
    }
    if self.DL_EXTRACT_ONLY_RESULT:
      patches["extract"] = self._get_dl_extract_only_result

    with mock.patch.multiple(
        "tensorflow_datasets.core.download.DownloadManager", **patches):
      # For Beam datasets, set-up the runner config
      beam_runner = None

      download_config = download.DownloadConfig(
          compute_stats=download.ComputeStatsMode.SKIP,
          beam_runner=beam_runner,
      )
      with self._test_key_not_local_path(builder):
        builder.download_and_prepare(download_config=download_config)

    with self._subTest("as_dataset"):
      self._assertAsDataset(builder)

    with self._subTest("num_examples"):
      self._assertNumSamples(builder)

    with self._subTest("reload"):
      # When reloading the dataset, metadata should been reloaded too.

      builder_reloaded = self._make_builder(config=builder.builder_config)
      self._assertNumSamples(builder_reloaded)

      # After reloading, as_dataset should still be working
      with self._subTest("as_dataset"):
        self._assertAsDataset(builder_reloaded)

    with self._subTest("config_description"):
      self._test_description_builder_config(builder)

  @contextlib.contextmanager
  def _test_key_not_local_path(self, builder) -> Iterator[None]:
    if not isinstance(builder, dataset_builder.GeneratorBasedBuilder):
      yield  # Do not test non-generator builder
      return

    original_generate_examples = builder._generate_examples  # pylint: disable=protected-access

    def _iter_examples(generator):
      for key, ex in generator:
        self._assert_key_valid(key)
        yield key, ex

    def new_generate_examples(*args, **kwargs):
      examples = original_generate_examples(*args, **kwargs)
      try:
        import apache_beam as beam  # pylint: disable=g-import-not-at-top
      except ImportError:
        beam = None
      if beam and isinstance(examples, (beam.PCollection, beam.PTransform)):
        return examples  # Beam keys not supported for now
      elif isinstance(examples, collections.abc.Iterable):
        return _iter_examples(examples)
      else:  # Unexpected
        return examples

    with mock.patch.object(builder, "_generate_examples",
                           new_generate_examples):
      yield

  def _assert_key_valid(self, key):
    if isinstance(key, str) and os.fspath(self.dummy_data) in key:
      err_msg = ("Key yield in '_generate_examples' method "
                 f"contain user directory path: {key}.\n"
                 "This makes the dataset example order non-deterministic. "
                 "Please use `filepath.name`, or `os.path.basename` instead.")
      raise ValueError(err_msg)

  def _assertAsDataset(self, builder):
    split_to_checksums = {}  # {"split": set(examples_checksums)}
    for split_name, expected_examples_number in self.SPLITS.items():
      ds = builder.as_dataset(split=split_name)
      spec = tf.data.DatasetSpec.from_value(ds)
      compare_shapes_and_types(
          builder.info.features.get_tensor_info(),
          # We use _element_spec because element_spec was added in TF2.5+.
          element_spec=spec._element_spec,  # pylint: disable=protected-access
      )
      examples = list(
          dataset_utils.as_numpy(builder.as_dataset(split=split_name)))
      split_to_checksums[split_name] = set(checksum(rec) for rec in examples)
      self.assertLen(examples, expected_examples_number)
    for (split1, hashes1), (split2, hashes2) in itertools.combinations(
        split_to_checksums.items(), 2):
      if (split1 in self.OVERLAPPING_SPLITS or
          split2 in self.OVERLAPPING_SPLITS):
        continue
      self.assertFalse(
          hashes1.intersection(hashes2),
          ("Splits '%s' and '%s' are overlapping. Are you sure you want to "
           "have the same objects in those splits? If yes, add one one of "
           "them to OVERLAPPING_SPLITS class attribute.") % (split1, split2))

  def _assertNumSamples(self, builder):
    for split_name, expected_num_examples in self.SPLITS.items():
      self.assertEqual(
          builder.info.splits[split_name].num_examples, expected_num_examples,
          f"Number of examples in split '{split_name}' "
          "do not match what is expected.")
    self.assertEqual(
        builder.info.splits.total_num_examples,
        sum(self.SPLITS.values()),
    )

  def _test_description_builder_config(self, builder):
    # Do not test on external datasets for backward compatibility
    # TODO(tfds): Update once datasets are migrated
    if "tensorflow_datasets" not in self.DATASET_CLASS.__module__:
      return

    # If configs specified, ensure they are all valid
    if builder.builder_config and builder.builder_config.description:
      err_msg = textwrap.dedent("""\
          The BuilderConfig description should be a one-line description of
          the config.
          It shouldn't be the same as `builder.info.description` to avoid
          redundancy. Both `config.description` and `builder.info.description`
          will be displayed in the catalog.
          """)
      ratio = difflib.SequenceMatcher(
          None,
          builder.builder_config.description,
          builder.info.description,
      ).ratio()
      if ratio > 0.9:
        raise AssertionError(err_msg)


def checksum(example):
  """Computes the md5 for a given example."""

  def _bytes_flatten(flat_str, element):
    """Recursively flatten an element to its byte representation."""
    if isinstance(element, numbers.Number):
      # In python3, bytes(-3) is not allowed (or large numbers),
      # so convert to str to avoid problems.
      element = str(element)
    if isinstance(element, dict):
      for k, v in sorted(element.items()):
        flat_str.append(k)
        _bytes_flatten(flat_str, v)
    elif isinstance(element, str):
      if hasattr(element, "decode"):
        # Python2 considers bytes to be str, but are almost always latin-1
        # encoded bytes here. Extra step needed to avoid DecodeError.
        element = element.decode("latin-1")
      flat_str.append(element)
    elif isinstance(element,
                    (tf.RaggedTensor, tf.compat.v1.ragged.RaggedTensorValue)):
      flat_str.append(str(element.to_list()))
    elif isinstance(element, (np.ndarray, np.generic)):
      # tf.Tensor() returns np.array of dtype object, which don't work
      # with x.to_bytes(). So instead convert numpy into list.
      if element.dtype.type is np.object_:
        flat_str.append(str(tuple(element.shape)))
        flat_str.append(str(list(element.ravel())))
      else:
        flat_str.append(element.tobytes())
    elif isinstance(element, dataset_utils._IterableDataset):  # pylint: disable=protected-access
      for nested_e in element:
        _bytes_flatten(flat_str, nested_e)
    else:
      flat_str.append(bytes(element))
    return flat_str

  flat_str = _bytes_flatten([], example)
  flat_bytes = [
      s.encode("utf-8") if not isinstance(s, bytes) else s for s in flat_str
  ]
  flat_bytes = b"".join(flat_bytes)

  hash_ = hashlib.md5()
  hash_.update(flat_bytes)
  return hash_.hexdigest()


def compare_shapes_and_types(tensor_info, element_spec):
  """Compare shapes and types between TensorInfo and Dataset types/shapes."""
  for feature_name, (feature_info,
                     spec) in utils.zip_dict(tensor_info, element_spec):
    if isinstance(spec, tf.data.DatasetSpec):
      # We use _element_spec because element_spec was added in TF2.5+.
      compare_shapes_and_types(feature_info, spec._element_spec)  # pylint: disable=protected-access
    elif isinstance(feature_info, dict):
      compare_shapes_and_types(feature_info, spec)
    else:
      # Some earlier versions of TF don't expose dtype and shape for the
      # RaggedTensorSpec, so we use the protected versions.
      if feature_info.dtype != spec._dtype:  # pylint: disable=protected-access
        raise TypeError(
            f"Feature {feature_name} has type {feature_info} but expected {spec}"
        )
      utils.assert_tf_shape_match(
          tf.TensorShape(feature_info.shape), spec._shape)  # pylint: disable=protected-access

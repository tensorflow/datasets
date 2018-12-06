# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Base TestCase to test a DatasetBuilder base class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import itertools
import os

import promise
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import test_utils
from tensorflow_datasets.core.utils import tf_utils


# `os` module Functions for which tf.gfile equivalent should be preferred.
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

# TODO(b/119906277): Rm
COMPUTE_STATS_BLACKLIST = ["diabetic_retinopathy_detection"]


class TestCase(test_utils.SubTestCase):
  """Inherit this class to test your DatasetBuilder class.

  You must set the following class attributes:
    DATASET_CLASS: class object of DatasetBuilder you want to test.

  You may set the following class attributes:
    DL_EXTRACT_RESULT: `dict[str]`, the returned result of mocked
      `download_and_extract` method. The values should be the path of files
      present in the `fake_examples` directory, relative to that directory.
      If not specified, path to `fake_examples` will always be returned.
    OVERLAPPING_SPLITS: `list[str]`, splits containing examples from other
      splits (e.g. a "example" split containing pictures from other splits).
    MOCK_OUT_FORBIDDEN_OS_FUNCTIONS: `bool`, defaults to True. Set to False to
      disable checks preventing usage of `os` or builtin functions instead of
      recommended `tf.gfile` API.

  This test case will check for the following:
   - the dataset builder is correctly registered, i.e. `tfds.load(name)` works;
   - the dataset builder can read the fake examples stored in
       testing/test_data/fake_examples/${dataset_name};
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
  DL_EXTRACT_RESULT = None
  OVERLAPPING_SPLITS = []
  MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = True

  @classmethod
  def setUpClass(cls):
    super(TestCase, cls).setUpClass()
    name = cls.__name__
    # Check class has the right attributes
    if cls.DATASET_CLASS is None or not callable(cls.DATASET_CLASS):
      raise AssertionError(
          "Assign your DatasetBuilder class to %s.DATASET_CLASS." % name)

  def setUp(self):
    # New data_dir and builder for each test
    self.data_dir = test_utils.make_tmp_dir(self.get_temp_dir())
    self.builder = self.DATASET_CLASS(data_dir=self.data_dir)  # pylint: disable=not-callable
    self.example_dir = os.path.join(
        os.path.dirname(__file__),
        "test_data/fake_examples/%s" % self.builder.name)
    if self.MOCK_OUT_FORBIDDEN_OS_FUNCTIONS:
      self._mock_out_forbidden_os_functions()

  def _mock_out_forbidden_os_functions(self):
    """Raise error if forbidden os functions are called instead of tf.gfile."""
    err = AssertionError("Do not use `os`, but `tf.gfile` module instead.")
    mock_os = tf.test.mock.Mock(os, path=os.path)
    for fop in FORBIDDEN_OS_FUNCTIONS:
      getattr(mock_os, fop).side_effect = err
    tf.test.mock.patch(self.DATASET_CLASS.__module__ + ".os", mock_os).start()
    mock_builtins = __builtins__.copy()
    mock_builtins["open"] = tf.test.mock.Mock(side_effect=err)
    tf.test.mock.patch(
        self.DATASET_CLASS.__module__ + ".__builtins__",
        mock_builtins
        ).start()

  def test_baseclass(self):
    self.assertIsInstance(
        self.builder, dataset_builder.DatasetBuilder,
        "Dataset class must inherit from `dataset_builder.DatasetBuilder`.")
    # Since class was instantiated and base class is ABCMeta, then we know
    # all needed methods were implemented.

  def test_registered(self):
    self.assertIn(self.builder.name, registered.list_builders(),
                  "Dataset was not registered.")

  def test_info(self):
    info = self.builder.info
    self.assertIsInstance(info, dataset_info.DatasetInfo)
    self.assertEquals(self.builder.name, info.name)

  def _get_dl_extract_result(self, url, async_=False):
    del url
    if self.DL_EXTRACT_RESULT is None:
      res = self.example_dir
    else:
      res = {k: os.path.join(self.example_dir, v)
             for k, v in self.DL_EXTRACT_RESULT.items()}
    result_p = promise.Promise.resolve(res)
    return async_ and result_p or res

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_download_and_prepare_as_dataset(self):
    # TODO(b/119906277): Remove here and checks below. compute_stats should
    # always be True for testing.
    compute_stats = self.builder.name not in COMPUTE_STATS_BLACKLIST

    with tf.test.mock.patch.multiple(
        "tensorflow_datasets.core.download.DownloadManager",
        download_and_extract=self._get_dl_extract_result,
        extract=self._get_dl_extract_result,
        manual_dir=self.example_dir,
    ):
      self.builder.download_and_prepare(compute_stats=compute_stats)

    with self._subTest("as_dataset"):
      self._assertAsDataset(self.builder)

    if compute_stats:
      with self._subTest("num_examples"):
        self._assertNumSamples(self.builder)

    with self._subTest("reload"):
      # When reloading the dataset, metadata should been reloaded too.
      builder_reloaded = self.DATASET_CLASS(data_dir=self.data_dir)  # pylint: disable=not-callable

      if compute_stats:
        self._assertNumSamples(builder_reloaded)

      # After reloading, as_dataset should still be working
      with self._subTest("as_dataset"):
        self._assertAsDataset(builder_reloaded)

  def _check_split(self, dataset):
    """Check given split has right types and shapes."""
    for component, (expected_type, expected_shapes) in self.SPEC.items():
      output_type = dataset.output_types[component]
      self.assertEqual(
          expected_type, output_type,
          "Component %s doesn't have type %s, but %s." %
          (component, expected_type, output_type))
      shapes = dataset.output_shapes[component]
      tf_utils.assert_shape_match(shapes, expected_shapes)

  def _assertAsDataset(self, builder):
    split_to_checksums = {}  # {"split": set(examples_checksums)}
    for split_name, expected_examples_number in self.SPLITS.items():
      dataset = builder.as_dataset(split=split_name)
      self._check_split(dataset)
      examples = list(builder.numpy_iterator(split=split_name))
      split_to_checksums[split_name] = set(checksum(rec) for rec in examples)
      self.assertEqual(len(examples), expected_examples_number)
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
          builder.info.splits[split_name].num_examples,
          expected_num_examples,
      )
    self.assertEqual(
        builder.info.num_examples,
        sum(self.SPLITS.values()),
    )


def checksum(example):
  """Computes the md5 for a given example."""
  hash_ = hashlib.md5()
  for key, val in sorted(example.items()):
    hash_.update(key.encode("utf-8"))
    # TODO(b/120124306): This will only work for "one-level"
    #                    dictionary. We might need a better solution here.
    if isinstance(val, dict):
      for k, v in sorted(val.items()):
        hash_.update(k.encode("utf-8"))
        hash_.update(v)
    else:
      hash_.update(val)
  return hash_.hexdigest()


main = tf.test.main

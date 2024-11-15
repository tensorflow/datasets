# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Test utilities."""

from __future__ import annotations

import contextlib
import dataclasses
import datetime
import functools
import hashlib
import json
import os
import pathlib
import subprocess
import tempfile
from typing import Any, Iterator, Mapping, Sequence
from unittest import mock

from etils import epath
from etils import epy
import numpy as np
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import features
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


_GCS_ACCESS_FNS = {
    'original_info': utils.gcs_utils.gcs_dataset_info_files,
    'dummy_info': lambda _: [],
    'original_datasets': utils.gcs_utils.is_dataset_on_gcs,
    'dummy_datasets': lambda _: False,
}


@contextlib.contextmanager
def tmp_dir(dirname=None):
  """Context manager for a temporary directory."""
  tmp = make_tmp_dir(dirname)
  yield tmp
  rm_tmp_dir(tmp)


def make_tmp_dir(dirname=None):
  """Make a temporary directory."""
  if dirname and not tf.io.gfile.exists(dirname):
    tf.io.gfile.makedirs(dirname)
  return tempfile.mkdtemp(dir=dirname)


def rm_tmp_dir(dirname):
  """Rm temporary directory."""
  tf.io.gfile.rmtree(dirname)


def remake_dir(d):
  """Possibly deletes and recreates directory."""
  if tf.io.gfile.exists(d):
    tf.io.gfile.rmtree(d)
  tf.io.gfile.makedirs(d)


def fake_examples_dir():
  return os.path.join(os.path.dirname(__file__), 'test_data', 'fake_examples')


@dataclasses.dataclass
class _PathState:
  """Track the metadata associated with the path."""

  is_gcs: bool
  is_abs: bool


class MockFs(object):
  """This util wraps mock for the `tf.io.gfile` / `epath.Path` API.

  This allow to test code which uses absolute paths / GCS path while keeping
  tests hermetic.

  Usage:

  ```
  with MockFs() as fs:
    # GCS example
    fs.add_file('gs://bucket/dir/file.txt')

    assert tf.io.gfile.glob('gs://bucket/*/file.txt') == [
        'gs://bucket/dir/file.txt',
    ]

    # This also works with absolute paths
    tf.io.gfile.makedirs('/path/to/')
    with tf.io.gfile.GFile('/path/to/file.txt', 'w') as f:
      f.write('Content of file.txt')
  ```

  Internally, this is done by converting absolute path into local tmp paths:

  * `/absolute/path` -> `/tmp/mocked_file_system/absolute/path`
  * `gs://path` -> `/tmp/mocked_file_system/gs/path`
  """

  def __init__(self):
    self._cm = None
    self._tmp_dir = None

  def __enter__(self):
    self._cm = self.contextmanager()
    return self._cm.__enter__()

  def __exit__(self, exc_type, exc_value, traceback):
    assert self._cm, 'Context manager uninitialized.'
    return self._cm.__exit__(exc_type, exc_value, traceback)

  @contextlib.contextmanager
  def contextmanager(self) -> Iterator['MockFs']:
    """Activate the mock file system."""
    with self.mock():
      yield self

  @contextlib.contextmanager
  def mock(self):
    with tempfile.TemporaryDirectory() as tmp_dir_:
      assert not self._tmp_dir
      self._tmp_dir = pathlib.Path(tmp_dir_)
      with self._mock() as m:
        yield m
      self._tmp_dir = None
      # TODO(epot): recursivelly record all

  def _to_tmp(self, p, *, with_state: bool = False):
    """Normalize the path by returning `tmp_path / p`."""
    assert self._tmp_dir, 'Temp directory uninitialized.'
    # If `p` was a `epath.Path`, it doesn't matter the value of `is_gcs`
    # as returned values will be normalized anyway.
    p_str = os.fspath(p)
    state = _PathState(
        is_gcs=p_str.startswith('gs://'),
        is_abs=p_str.startswith('/'),
    )
    if state.is_gcs:
      p = os.fspath(p).replace('gs://', '/big' + 'store/', 1)
    p = pathlib.Path(p)
    if p.anchor:
      p = pathlib.Path(*p.parts[1:])  # Strip leading `/`
    assert not p.is_absolute()
    out_p = self._tmp_dir / p

    # Propagate `is_gcs`, so results are consistents:
    # * tf.io.gfile.glob('gs://')
    # * tf.io.gfile.glob('/big' + 'store/')
    if with_state:
      return out_p, state
    else:
      return out_p

  def _to_abs(self, p, *, state: _PathState):
    """Normalize the output to strip the `tmp_path`."""
    assert self._tmp_dir, 'Temp directory uninitialized.'
    tmp_path = os.fspath(self._tmp_dir)
    assert p.startswith(tmp_path)
    p = p[len(tmp_path) :]  # Strip the tmp path
    if state.is_gcs:
      assert p.startswith('/big' + 'store/')
      p = p.replace('/big' + 'store/', 'gs://', 1)
    elif not state.is_abs:
      assert p.startswith('/')
      p = p[len('/') :]
    return p

  def _validate_out(self, out):
    """Sanity check to avoid leaking accidentally the `self.tmp_dir`."""
    if isinstance(out, list):
      assert not any(elem.startswith('/') for elem in out)
    elif not isinstance(out, (bool, type(None))):
      raise TypeError(
          f'Unexpected return type {out!r} for MockFs, please open an issue'
      )
    return out

  def add_file(self, path, content=None) -> None:
    """Add a file, creating all parent directories."""
    path = os.fspath(path)
    content = content or f'Content of {path}'
    fpath = self._to_tmp(path)
    fpath.parent.mkdir(parents=True, exist_ok=True)  # pytype: disable=attribute-error
    fpath.write_text(content)  # pytype: disable=attribute-error

  def read_file(self, path) -> str:
    return self._to_tmp(path).read_text()  # pytype: disable=attribute-error

  def _mock_open(self, original_fn, p, mode='r', **kwargs):
    return original_fn(self._to_tmp(p), mode, **kwargs)

  def _mock_fn(self, original_fn, p, **kwargs):
    return self._validate_out(original_fn(self._to_tmp(p), **kwargs))

  def _mock_fn_2_args(self, original_fn, p, p2, **kwargs):
    return self._validate_out(
        original_fn(
            self._to_tmp(p),
            self._to_tmp(p2),
            **kwargs,
        )
    )

  def _mock_glob(self, original_fn, p):
    p, state = self._to_tmp(p, with_state=True)
    p_outs = original_fn(os.fspath(p))  # tf.io.glob does not accept `pathlib`
    return [self._to_abs(p_out, state=state) for p_out in p_outs]

  def _mock_walk(self, original_fn, p):
    p, state = self._to_tmp(p, with_state=True)
    for root, subdirs, filenames in original_fn(p):
      yield (self._to_abs(root, state=state), subdirs, filenames)

  def _mock(self):
    return mock_gfile(
        exists=self._mock_fn,
        listdir=self._mock_fn,
        isdir=self._mock_fn,
        remove=self._mock_fn,
        rmtree=self._mock_fn,
        mkdir=self._mock_fn,
        makedirs=self._mock_fn,
        open=self._mock_open,
        rename=self._mock_fn_2_args,
        replace=self._mock_fn_2_args,
        copy=self._mock_fn_2_args,
        glob=self._mock_glob,
        walk=self._mock_walk,
    )

  def print_tree(self) -> None:
    print(_get_folder_str(self._tmp_dir))


def _get_folder_str(root_dir: pathlib.Path | None) -> str:
  """Get the tree structure."""
  if not root_dir:
    raise ValueError('Root dir undefined. Cannot find folder.')

  lines = epy.Lines()
  for p in root_dir.iterdir():
    if p.is_dir():
      lines += f'{p.name}/'
      with lines.indent():
        subfolder_str = _get_folder_str(p)
        if subfolder_str:
          lines += subfolder_str
    else:
      lines += p.name
  return lines.join()


@contextlib.contextmanager
def mock_gfile(**fns: Any) -> Iterator[None]:
  """Patch `tf.io.gfile.GFile` and `epath.Path`.

  Example: Validate `exists` usage:

  ```
  def new_exists(old_exists, path):
    assert not os.fspath(path).startswith('gs://')
    return old_exists(path)

  with mock_gfile(exists=new_exists)
  ```

  Args:
    **fns: Functions to overwrite. Have signature: `fn(original_fn, *args,
      **kwargs)`. (note the first function argument which allow to access the
      original function)

  Yields:
    None
  """
  # Process epath kwargs
  epath_kwargs = {k: fn for k, fn in fns.items() if k != 'walk'}

  # Process gfile kwargs
  epath_to_gfile_mapping = {
      'open': 'GFile',
  }
  gfile_kwargs = {}
  for k, fn in fns.items():
    if k == 'replace':
      continue
    gfile_k = epath_to_gfile_mapping.get(k, k)
    original_fn = getattr(tf.io.gfile, gfile_k)
    mocked_fn = functools.wraps(original_fn)(functools.partial(fn, original_fn))
    gfile_kwargs[gfile_k] = mocked_fn

  with contextlib.ExitStack() as stack:
    cm_epath = epath.testing.mock_epath(**epath_kwargs)
    cm_gfile = mock_tf('tf.io.gfile', **gfile_kwargs)
    stack.enter_context(cm_epath)
    stack.enter_context(cm_gfile)
    yield


@contextlib.contextmanager
def mock_tf(symbol_name: str, *args: Any, **kwargs: Any) -> Iterator[None]:
  """Patch TF API.

  This function is similar to `mock.patch.object`, but patch both
  `tf.Xyz` and `tf.compat.v2.Xyz`.

  Args:
    symbol_name: Symbol to patch (e.g. `tf.io.gfile`)
    *args: Arguments to forward to `mock.patch.object`
    **kwargs: Arguments to forward to `mock.patch.object`

  Yields:
    None
  """

  tf_symbol, *tf_submodules, symbol_name = symbol_name.split('.')
  if tf_symbol != 'tf':
    raise ValueError('Symbol name to patch should start by `tf`.')

  with contextlib.ExitStack() as stack:
    # Recursivelly load the submodules/subobjects (e.g. `tf.io.gfile`)
    module = tf
    for submodule in tf_submodules:
      module = getattr(module, submodule)
    getattr(module, symbol_name)  # Trigger the lazy-loading of the TF API.
    if kwargs:  # Patch each attribute individually
      assert not args
      for k, v in kwargs.items():
        stack.enter_context(
            mock.patch.object(getattr(module, symbol_name), k, v)
        )
    else:
      # Patch the module/object
      stack.enter_context(
          mock.patch.object(module, symbol_name, *args, **kwargs)
      )
    yield


def run_in_graph_and_eager_modes(func=None, config=None, use_gpu=True):
  """Execute the decorated test in both graph mode and eager mode.

  This function returns a decorator intended to be applied to test methods in
  a `test_case.TestCase` class. Doing so will cause the contents of the test
  method to be executed twice - once in graph mode, and once with eager
  execution enabled. This allows unittests to confirm the equivalence between
  eager and graph execution.

  NOTE: This decorator can only be used when executing eagerly in the
  outer scope.

  For example, consider the following unittest:

  ```python
  class SomeTest(tfds.testing.TestCase):

    @tfds.testing.run_in_graph_and_eager_modes
    def test_foo(self):
      x = tf.constant([1, 2])
      y = tf.constant([3, 4])
      z = tf.add(x, y)
      self.assertAllEqual([4, 6], self.evaluate(z))

  if __name__ == '__main__':
    tfds.testing.test_main()
  ```

  This test validates that `tf.add()` has the same behavior when computed with
  eager execution enabled as it does when constructing a TensorFlow graph and
  executing the `z` tensor with a session.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.
    config: An optional config_pb2.ConfigProto to use to configure the session
      when executing graphs.
    use_gpu: If True, attempt to run as many operations as possible on GPU.

  Returns:
    Returns a decorator that will run the decorated test method twice:
    once by constructing and executing a graph in a session and once with
    eager execution enabled.
  """

  def decorator(f):
    """Decorator for a method."""

    def decorated(self, *args, **kwargs):
      """Run the decorated test method."""
      if not tf.executing_eagerly():
        raise ValueError(
            'Must be executing eagerly when using the '
            'run_in_graph_and_eager_modes decorator.'
        )

      with self.subTest('eager_mode'):
        f(self, *args, **kwargs)
        self.tearDown()

      with self.subTest('graph_mode'):
        with tf.Graph().as_default():
          self.setUp()
          with self.test_session(use_gpu=use_gpu, config=config):
            f(self, *args, **kwargs)

    return decorated

  if func is not None:
    return decorator(func)

  return decorator


@contextlib.contextmanager
def disable_gcs_access() -> Iterator[None]:
  """Disable GCS access."""
  with mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils.gcs_dataset_info_files',
      _GCS_ACCESS_FNS['dummy_info'],
  ), mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils.is_dataset_on_gcs',
      _GCS_ACCESS_FNS['dummy_datasets'],
  ), mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils._is_gcs_disabled',
      True,
  ):
    yield


@contextlib.contextmanager
def enable_gcs_access() -> Iterator[None]:
  """Enable GCS access."""
  with mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils.gcs_dataset_info_files',
      _GCS_ACCESS_FNS['original_info'],
  ), mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils.is_dataset_on_gcs',
      _GCS_ACCESS_FNS['original_datasets'],
  ), mock.patch(
      'tensorflow_datasets.core.utils.gcs_utils._is_gcs_disabled',
      False,
  ):
    yield


class DummyDatasetSharedGenerator(
    dataset_builder.GeneratorBasedBuilder,
    skip_registration=True,
):
  """Test DatasetBuilder."""

  VERSION = utils.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Release notes 1.0.0',
      '2.0.0': 'Release notes 2.0.0',
  }
  SUPPORTED_VERSIONS = [
      '2.0.0',
      '0.0.9',
      '0.0.8',
      utils.Version('0.0.7', tfds_version_to_prepare='v1.0.0'),
  ]

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({'x': tf.int64}),
        supervised_keys=('x', 'x'),
    )

  def _split_generators(self, dl_manager):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    del dl_manager
    return {
        'train': self._generate_examples(range_=range(20)),
        'test': self._generate_examples(range_=range(20, 30)),
    }

  def _generate_examples(self, range_):
    for i in range_:
      yield i, {'x': i}


class DummyMnist(
    dataset_builder.GeneratorBasedBuilder,
    skip_registration=True,
):
  """Test DatasetBuilder."""

  VERSION = utils.Version('3.0.1')

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            'image': features.Image(shape=(28, 28, 1)),
            'label': features.ClassLabel(num_classes=10),
        }),
        description='Mnist description.',
    )

  def _split_generators(self, dl_manager):
    return {
        'train': self._generate_examples(),
        'test': self._generate_examples(),
    }

  def _generate_examples(self):
    for i in range(20):
      yield i, {
          'image': np.ones((28, 28, 1), dtype=np.uint8),
          'label': i % 10,
      }


class DummyDataset(
    dataset_builder.GeneratorBasedBuilder,
    skip_registration=True,
):
  """Minimal DatasetBuilder."""

  VERSION = utils.Version('1.0.0')

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            'id': np.int64,
        }),
        supervised_keys=('id', 'id'),
        description='Minimal DatasetBuilder.',
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {
        'train': self._generate_examples(),
    }

  def _generate_examples(self):
    for i in range(3):
      yield i, {'id': i}


class DummyBeamDataset(DummyDataset, skip_registration=True):
  """Minimal beam DatasetBuilder."""

  def _generate_examples(self):
    beam = lazy_imports_lib.lazy_imports.apache_beam
    return beam.Create(list(range(3))) | beam.Map(lambda i: (i, {'id': i}))


def test_main():
  """Entrypoint for tests."""
  tf.test.main()


@contextlib.contextmanager
def mock_kaggle_api(err_msg=None):
  """Mock out the kaggle CLI.

  Args:
    err_msg: `str`, if provided, the kaggle CLI will raise a CalledProcessError
      and this will be the command output.

  Yields:
    None, context will have kaggle CLI mocked out.
  """

  def check_output(command_args, encoding=None):
    """Mock subprocess.check_output for download call."""
    assert encoding
    assert command_args[2] == 'download'
    competition_or_dataset = command_args[-1]
    if err_msg:
      raise subprocess.CalledProcessError(1, command_args, err_msg)
    out_dir = command_args[command_args.index('--path') + 1]
    fpath = os.path.join(out_dir, 'output.txt')
    with tf.io.gfile.GFile(fpath, 'w') as f:
      f.write(competition_or_dataset)
    return 'Downloading {} to {}'.format(competition_or_dataset, fpath)

  with mock.patch('subprocess.check_output', check_output):
    yield


class DummySerializer(example_serializer.Serializer):
  """To mock example_serializer.ExampleSerializer."""

  def __init__(self, specs):
    del specs
    super().__init__(example_specs={})

  def serialize_example(self, example):
    return bytes(example)


class DummyParser(object):
  """To mock example_parser.ExampleParser."""

  def __init__(self, specs):
    del specs

  def parse_example(self, ex):
    return ex


def assert_features_equal(features0, features1) -> None:
  """Asserts that the 2 nested FeatureConnector structure match."""
  _assert_features_equal(
      features.features_dict.to_feature(features0),
      features.features_dict.to_feature(features1),
  )


def _assert_features_equal(features0, features1) -> None:
  tf.nest.map_structure(_assert_feature_equal, features0, features1)


def _assert_feature_equal(feature0, feature1):
  """Assert that 2 features are equals."""
  assert type(feature0) == type(feature1)  # pylint: disable=unidiomatic-typecheck
  assert repr(feature0) == repr(feature1)
  assert feature0.shape == feature1.shape
  assert feature0.dtype == feature1.dtype
  assert feature0.np_dtype == feature1.np_dtype
  assert feature0.tf_dtype == feature1.tf_dtype
  if isinstance(feature0, features.FeaturesDict):
    _assert_features_equal(dict(feature0), dict(feature1))
  if isinstance(feature0, features.Sequence):
    assert feature0._length == feature1._length  # pylint: disable=protected-access
    _assert_features_equal(feature0.feature, feature1.feature)
  if isinstance(feature0, features.ClassLabel):
    assert feature0.names == feature1.names


class DummyDatasetCollection(
    dataset_collection_builder.DatasetCollection,
    skip_registration=True,
):
  """Minimal Dataset Collection builder."""

  @property
  def info(self) -> dataset_collection_builder.DatasetCollectionInfo:
    return dataset_collection_builder.DatasetCollectionInfo.from_cls(
        dataset_collection_class=self.__class__,
        description='my description',
        release_notes={
            '1.0.0': 'notes 1.0.0',
            '1.1.0': 'notes 1.1.0',
            '2.0.0': 'notes 2.0.0',
        },
        citation="""
        @misc{citekey,
          author       = "",
          title        = "",
          year         = ""
        }
        """,
    )

  @property
  def datasets(self) -> Mapping[str, Mapping[str, naming.DatasetReference]]:
    return {
        '1.0.0': naming.references_for({
            'a': 'a/c:1.2.3',
            'b': 'b/d:2.3.4',
        }),
        '1.1.0': naming.references_for({
            'a': 'a/c:1.2.3',
            'c': 'c/e:3.5.7',
        }),
        '2.0.0': naming.references_for({
            'a': 'a/c:1.3.5',
            'b': 'b/d:2.4.8',
            'c': 'c/e:3.5.7',
        }),
    }


@contextlib.contextmanager
def set_current_datetime(now_datetime: datetime.datetime) -> Iterator[None]:
  """Mocks datetime.datetime.now()."""

  class MockDatetime(datetime.datetime):

    @classmethod
    def now(cls, tz=None) -> datetime.datetime:
      return now_datetime

  with mock.patch.object(datetime, 'datetime', new=MockDatetime):
    yield


@contextlib.contextmanager
def dummy_croissant_file(
    dataset_name: str = 'DummyDataset',
    entries: Sequence[dict[str, Any]] | None = None,
    raw_data_filename: epath.PathLike = 'raw_data.jsonl',
    croissant_filename: epath.PathLike = 'croissant.json',
) -> Iterator[epath.Path]:
  """Yields temporary path to a dummy Croissant file.

  The function creates a temporary directory that stores raw data files and the
  Croissant JSON-LD.

  Args:
    dataset_name: The name of the dataset.
    entries: A list of dictionaries representing the dataset's entries. Each
      dictionary should contain an 'index' and a 'text' key. If None, the
      function will create two entries with indices 0 and 1 and dummy text.
    raw_data_filename: Filename of the raw data file.
    croissant_filename: Filename of the Croissant JSON-LD file.
  """
  if entries is None:
    entries = [{'index': i, 'text': f'Dummy example {i}'} for i in range(2)]

  fields = [
      mlc.Field(
          id='jsonl/index',
          name='jsonl/index',
          description='The sample index.',
          data_types=mlc.DataType.INTEGER,
          source=mlc.Source(
              file_object='raw_data',
              extract=mlc.Extract(column='index'),
          ),
      ),
      mlc.Field(
          id='jsonl/text',
          name='jsonl/text',
          description='The dummy sample text.',
          data_types=mlc.DataType.TEXT,
          source=mlc.Source(
              file_object='raw_data',
              extract=mlc.Extract(column='text'),
          ),
      ),
  ]

  record_sets = [
      mlc.RecordSet(
          id='jsonl',
          name='jsonl',
          description='Dummy record set.',
          fields=fields,
      )
  ]

  with tempfile.TemporaryDirectory() as tempdir:
    tempdir = epath.Path(tempdir)

    # Write raw examples to tempdir/data.
    raw_data_dir = tempdir / 'data'
    raw_data_dir.mkdir()
    raw_data_file = raw_data_dir / raw_data_filename
    raw_data_file.write_text('\n'.join(map(json.dumps, entries)))

    # Get the actual raw file's hash, set distribution and metadata.
    raw_data_file_content = raw_data_file.read_text()
    sha256 = hashlib.sha256(raw_data_file_content.encode()).hexdigest()
    distribution = [
        mlc.FileObject(
            id='raw_data',
            name='raw_data',
            description='File with the data.',
            encoding_format='application/jsonlines',
            content_url=f'data/{raw_data_filename}',
            sha256=sha256,
        ),
    ]
    dummy_metadata = mlc.Metadata(
        name=dataset_name,
        description='Dummy description.',
        cite_as=(
            '@article{dummyarticle, title={title}, author={author},'
            ' year={2020}}'
        ),
        url='https://dummy_url',
        distribution=distribution,
        record_sets=record_sets,
        version='1.2.0',
        license='Public',
    )

    # Write Croissant JSON-LD to tempdir.
    croissant_file = tempdir / croissant_filename
    croissant_file.write_text(json.dumps(dummy_metadata.to_json(), indent=2))

    yield croissant_file

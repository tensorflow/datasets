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

"""Test utilities."""

import contextlib
import io
import os
import subprocess
import tempfile
from typing import Any, Iterator
from unittest import mock

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils


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


class MockFs(object):
  """This util wraps mock for the `tf.io.gfile` API.

  Usage:

  ```
  fs = MockFs()
  with fs.mock():

    fs.add_file('/path/to/file1', 'Content of file 1')

    assert tf.io.gfile.exists('/path/to/file1')
    with tf.io.gfile.GFile('/path/to/file2', 'w') as f:
      f.write('Content of file 2')
    tf.io.gfile.rename('/path/to/file1', '/path/to/file1_moved')

    assert fs.files == {
        '/path/to/file2': 'Content of file 2',
        '/path/to/file1_moved': 'Content of file 1',
    }
  ```

  Attributes:
    files: Dict[str, str], mapping existing files -> file content
  """

  def __init__(self):
    self.files = {}
    self._cm = None

  def __enter__(self):
    self._cm = self.contextmanager()
    return self._cm.__enter__()

  def __exit__(self, exc_type, exc_value, traceback):
    return self._cm.__exit__(exc_type, exc_value, traceback)

  @contextlib.contextmanager
  def contextmanager(self) -> Iterator['MockFs']:
    """Open the file."""
    with self.mock():
      yield self

  def add_file(self, path, content=None) -> None:
    path = os.fspath(path)
    content = 'Content of {}'.format(path) if content is None else content
    self.files[path] = content

  def _list_directory(self, path):
    path = os.fspath(path)
    path = path.rstrip(os.path.sep) + os.path.sep  # Make sure path is a `dir/`
    return list({
        # Extract `path/<dirname>/...` -> `<dirname>`
        os.path.relpath(p, path).split(os.path.sep)[0]
        for p in self.files
        if p.startswith(path)
    })

  @contextlib.contextmanager
  def _open(self, path, mode='r'):
    """Patch `tf.io.gfile.GFile`."""
    path = os.fspath(path)
    if mode.startswith('w'):
      self.add_file(path, '')
    is_binary = 'b' in mode

    if path not in self.files:
      raise FileNotFoundError(f'File {path} does not exists.')
    content = self.files[path]
    if is_binary:
      fobj = io.BytesIO(content.encode('utf-8'))
    else:
      fobj = io.StringIO(content)

    with fobj as f:
      yield f
      new_content = f.getvalue()  # Update the content

    self.files[path] = new_content.decode('utf-8') if is_binary else new_content  # pytype: disable=attribute-error

  def _rename(self, from_, to, overwrite=False):
    from_ = os.fspath(from_)
    to = os.fspath(to)
    if not overwrite and to in self.files:
      raise FileExistsError('Cannot overwrite: {} -> {}'.format(from_, to))  # pytype: disable=name-error
    if from_ not in self.files:
      raise FileNotFoundError('Cannot rename unknown file: {}'.format(from_))  # pytype: disable=name-error
    self.files[to] = self.files.pop(from_)

  def _exists(self, path: str) -> bool:
    """Returns True, if any file/directory exists."""
    path = os.fspath(path)
    path = path.rstrip(os.path.sep)  # Normalize path
    # Check full path existence
    if path in self.files:
      return True
    # Check parent directory
    path = path + os.path.sep
    if any(f.startswith(path) for f in self.files):
      return True
    return False

  def mock(self):
    return mock_tf(
        'tf.io.gfile',
        exists=self._exists,
        makedirs=lambda _: None,
        # Used to get name of file as downloaded:
        listdir=self._list_directory,
        GFile=self._open,
        rename=self._rename,
    )


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
  # pylint: disable=g-import-not-at-top,reimported
  import tensorflow as tf_lib1
  import tensorflow as tf_lib2
  # pylint: enable=g-import-not-at-top,reimported

  tf_symbol, *tf_submodules, symbol_name = symbol_name.split('.')
  if tf_symbol != 'tf':
    raise ValueError('Symbol name to patch should start by `tf`.')

  with contextlib.ExitStack() as stack:
    # Patch both `tf` and `tf.compat.v2`
    for tf_lib in (tf_lib1, tf_lib2):
      # Recursivelly load the submodules/subobjects (e.g. `tf.io.gfile`)
      module = tf_lib
      for submodule in tf_submodules:
        module = getattr(module, submodule)
      getattr(module, symbol_name)  # Trigger the lazy-loading of the TF API.
      # Patch the module/object
      stack.enter_context(
          mock.patch.object(module, symbol_name, *args, **kwargs))
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
        raise ValueError('Must be executing eagerly when using the '
                         'run_in_graph_and_eager_modes decorator.')

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


class DummyDatasetSharedGenerator(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = utils.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Release notes 1.0.0',
      '2.0.0': 'Release notes 2.0.0'
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


class DummyMnist(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = utils.Version('1.0.0')

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
            'id': tf.int64,
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


class DummySerializer(object):
  """To mock example_serializer.ExampleSerializer."""

  def __init__(self, specs):
    del specs

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
  if isinstance(feature0, features.FeaturesDict):
    _assert_features_equal(dict(feature0), dict(feature1))
  if isinstance(feature0, features.Sequence):
    assert feature0._length == feature1._length  # pylint: disable=protected-access
    _assert_features_equal(feature0.feature, feature1.feature)
  if isinstance(feature0, features.ClassLabel):
    assert feature0.names == feature1.names

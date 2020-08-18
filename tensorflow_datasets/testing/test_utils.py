# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
import functools
import io
import os
import subprocess
import tempfile
from typing import Iterator

from absl.testing import absltest

import dill
import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import features
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import utils
from tensorflow_datasets.testing import test_case


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
    content = 'Content of {}'.format(path) if content is None else content
    self.files[path] = content

  def _list_directory(self, path):
    path = path.rstrip(os.path.sep) + os.path.sep  # Make sure path is a `dir/`
    return list({
        # Extract `path/<dirname>/...` -> `<dirname>`
        os.path.relpath(p, path).split(os.path.sep)[0]
        for p in self.files if p.startswith(path)
    })

  @contextlib.contextmanager
  def _open(self, path, mode='r'):
    """Patch `tf.io.gfile.GFile`."""
    if mode.startswith('w'):
      self.add_file(path, '')
    is_binary = 'b' in mode

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
    if not overwrite and to in self.files:
      raise FileExistsError('Cannot overwrite: {} -> {}'.format(from_, to))  # pytype: disable=name-error
    if from_ not in self.files:
      raise FileNotFoundError('Cannot rename unknown file: {}'.format(from_))  # pytype: disable=name-error
    self.files[to] = self.files.pop(from_)

  def mock(self):
    return absltest.mock.patch.object(
        tf.io,
        'gfile',
        exists=lambda path: path in self.files,
        makedirs=lambda _: None,
        # Used to get name of file as downloaded:
        listdir=self._list_directory,
        GFile=self._open,
        rename=self._rename,
    )


class FeatureExpectationItem(object):
  """Test item of a FeatureExpectation."""

  def __init__(
      self,
      value,
      expected=None,
      expected_serialized=None,
      decoders=None,
      dtype=None,
      shape=None,
      raise_cls=None,
      raise_msg=None):
    self.value = value
    self.expected = expected
    self.expected_serialized = expected_serialized
    self.decoders = decoders
    self.dtype = dtype
    self.shape = shape
    if not decoders and (dtype is not None or shape is not None):
      raise ValueError('dtype and shape should only be set with transform')
    self.raise_cls = raise_cls
    self.raise_msg = raise_msg


class SubTestCase(test_case.TestCase):
  """Adds subTest() context manager to the TestCase if supported.

  Note: To use this feature, make sure you call super() in setUpClass to
  initialize the sub stack.
  """

  @classmethod
  def setUpClass(cls):
    super(SubTestCase, cls).setUpClass()
    cls._sub_test_stack = []

  @contextlib.contextmanager
  def _subTest(self, test_str):
    self._sub_test_stack.append(test_str)
    sub_test_str = '/'.join(self._sub_test_stack)
    with self.subTest(sub_test_str):
      yield
    self._sub_test_stack.pop()

  def assertAllEqualNested(self, d1, d2):
    """Same as assertAllEqual but compatible with nested dict."""
    if isinstance(d1, dict):
      # assertAllEqual do not works well with dictionaries so assert
      # on each individual elements instead
      zipped_examples = utils.zip_nested(d1, d2, dict_only=True)
      utils.map_nested(
          lambda x: self.assertAllEqual(x[0], x[1]),
          zipped_examples,
          dict_only=True,
      )
    else:
      self.assertAllEqual(d1, d2)


def run_in_graph_and_eager_modes(func=None,
                                 config=None,
                                 use_gpu=True):
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

      # Run eager block
      f(self, *args, **kwargs)
      self.tearDown()

      # Run in graph mode block
      with tf.Graph().as_default():
        self.setUp()
        with self.test_session(use_gpu=use_gpu, config=config):
          f(self, *args, **kwargs)

    return decorated

  if func is not None:
    return decorator(func)

  return decorator


class RaggedConstant(object):
  """Container of tf.ragged.constant values.

  This simple wrapper forward the arguments to delay the RaggedTensor
  construction after `@run_in_graph_and_eager_modes` has been called.
  This is required to avoid incompabilities between Graph/eager.
  """

  def __init__(self, *args, **kwargs):
    self._args = args
    self._kwargs = dict(kwargs)

  def build(self):
    return tf.ragged.constant(*self._args, **self._kwargs)


class FeatureExpectationsTestCase(SubTestCase):
  """Tests FeatureExpectations with full encode-decode."""

  @run_in_graph_and_eager_modes()
  def assertFeature(
      self,
      feature,
      shape,
      dtype,
      tests,
      serialized_info=None,
      skip_feature_tests=False,
      test_attributes=None):
    """Test the given feature against the predicates."""

    with self._subTest('feature'):
      self._assert_feature(
          feature=feature,
          shape=shape,
          dtype=dtype,
          tests=tests,
          serialized_info=serialized_info,
          skip_feature_tests=skip_feature_tests,
          test_attributes=test_attributes,
      )
    # TODO(tfds): Remove `skip_feature_tests` after text encoders are removed
    if not skip_feature_tests:
      # Test the feature again to make sure that feature restored from config
      # behave similarly.
      with self._subTest('feature_roundtrip'):
        new_feature = feature.from_json_content(feature.to_json_content())
        self._assert_feature(
            feature=new_feature,
            shape=shape,
            dtype=dtype,
            tests=tests,
            serialized_info=serialized_info,
            skip_feature_tests=skip_feature_tests,
            test_attributes=test_attributes,
        )

  def _assert_feature(
      self,
      feature,
      shape,
      dtype,
      tests,
      serialized_info=None,
      skip_feature_tests=False,
      test_attributes=None):
    with self._subTest('shape'):
      self.assertEqual(feature.shape, shape)
    with self._subTest('dtype'):
      self.assertEqual(feature.dtype, dtype)

    # Check the serialized features
    if serialized_info:
      with self._subTest('serialized_info'):
        self.assertEqual(
            serialized_info,
            feature.get_serialized_info(),
        )

    if not skip_feature_tests and test_attributes:
      for key, value in test_attributes.items():
        self.assertEqual(getattr(feature, key), value)

    # Create the feature dict
    fdict = features.FeaturesDict({'inner': feature})
    fdict._set_top_level()  # pylint: disable=protected-access

    for i, test in enumerate(tests):
      with self._subTest(str(i)):
        self.assertFeatureTest(
            fdict=fdict,
            test=test,
            feature=feature,
            shape=shape,
            dtype=dtype,
        )

  def assertFeatureTest(self, fdict, test, feature, shape, dtype):
    """Test that encode=>decoding of a value works correctly."""
    # test feature.encode_example can be pickled and unpickled for beam.
    dill.loads(dill.dumps(feature.encode_example))

    input_value = {'inner': test.value}

    if test.raise_cls is not None:
      with self._subTest('raise'):
        if not test.raise_msg:
          raise ValueError(
              'test.raise_msg should be set with {} for test {}'.format(
                  test.raise_cls, type(feature)))
        with self.assertRaisesWithPredicateMatch(
            test.raise_cls, test.raise_msg):
          features_encode_decode(fdict, input_value, decoders=test.decoders)
    else:
      # Test the serialization only
      if test.expected_serialized is not None:
        with self._subTest('out_serialize'):
          self.assertEqual(
              test.expected_serialized,
              feature.encode_example(test.value),
          )

      # Test serialization + decoding from disk
      with self._subTest('out'):
        out_tensor, out_numpy = features_encode_decode(
            fdict,
            input_value,
            decoders={'inner': test.decoders},
        )
        out_tensor = out_tensor['inner']
        out_numpy = out_numpy['inner']

        # Assert the returned type match the expected one
        with self._subTest('dtype'):
          out_dtypes = tf.nest.map_structure(lambda s: s.dtype, out_tensor)
          self.assertEqual(out_dtypes, test.dtype or feature.dtype)
        with self._subTest('shape'):
          # For shape, because (None, 3) match with (5, 3), we use
          # tf.TensorShape.assert_is_compatible_with on each of the elements
          expected_shape = feature.shape if test.shape is None else test.shape
          out_shapes = utils.zip_nested(out_tensor, expected_shape)
          utils.map_nested(
              lambda x: x[0].shape.assert_is_compatible_with(x[1]),
              out_shapes
          )

        # Assert value
        with self._subTest('out_value'):
          # Eventually construct the tf.RaggedTensor
          expected = tf.nest.map_structure(
              lambda t: t.build() if isinstance(t, RaggedConstant) else t,
              test.expected)
          self.assertAllEqualNested(out_numpy, expected)

        # Assert the HTML representation works
        if not test.decoders:
          with self._subTest('repr'):
            self._test_repr(feature, out_numpy)

  def _test_repr(
      self,
      feature: features.FeatureConnector,
      out_numpy: np.ndarray,
  ) -> None:
    """Test that the HTML repr works."""
    # pylint: disable=protected-access
    flat_example = feature._flatten(out_numpy)
    flat_features = feature._flatten(feature)
    flat_serialized_info = feature._flatten(feature.get_serialized_info())
    # pylint: enable=protected-access
    for ex, f, spec in zip(flat_example, flat_features, flat_serialized_info):
      # Features with multi-data not supported
      if isinstance(spec, dict):
        continue
      elif spec.sequence_rank == 0:
        text = f.repr_html(ex)
      elif spec.sequence_rank == 1:
        text = f.repr_html_batch(ex)
      elif spec.sequence_rank > 1:
        text = f.repr_html_ragged(ex)
      self.assertIsInstance(text, str)


def features_encode_decode(features_dict, example, decoders):
  """Runs the full pipeline: encode > write > tmp files > read > decode."""
  # Encode example
  encoded_example = features_dict.encode_example(example)

  # Serialize/deserialize the example
  specs = features_dict.get_serialized_info()
  serializer = example_serializer.ExampleSerializer(specs)
  parser = example_parser.ExampleParser(specs)

  serialized_example = serializer.serialize_example(encoded_example)
  ds = tf.data.Dataset.from_tensors(serialized_example)
  ds = ds.map(parser.parse_example)

  # Decode the example
  decode_fn = functools.partial(
      features_dict.decode_example,
      decoders=decoders,
  )
  ds = ds.map(decode_fn)

  if tf.executing_eagerly():
    out_tensor = next(iter(ds))
  else:
    out_tensor = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
  out_numpy = dataset_utils.as_numpy(out_tensor)
  return out_tensor, out_numpy


class DummyDatasetSharedGenerator(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = utils.Version('1.0.0')
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
    return [
        splits.SplitGenerator(
            name=splits.Split.TRAIN,
            gen_kwargs={'range_': range(20)}),
        splits.SplitGenerator(
            name=splits.Split.TEST,
            gen_kwargs={'range_': range(20, 30)}),
    ]

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
    return [
        splits.SplitGenerator(
            name=splits.Split.TRAIN,
            gen_kwargs=dict()),
        splits.SplitGenerator(
            name=splits.Split.TEST,
            gen_kwargs=dict()),
    ]

  def _generate_examples(self):
    for i in range(20):
      yield i, {
          'image': np.ones((28, 28, 1), dtype=np.uint8),
          'label': i % 10,
      }


def test_main():
  """Entrypoint for tests."""
  tf.enable_v2_behavior()
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

  with absltest.mock.patch('subprocess.check_output', check_output):
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

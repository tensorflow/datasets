# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import os
import subprocess
import tempfile

from absl.testing import absltest

import dill
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter
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


class FeatureExpectationItem(object):
  """Test item of a FeatureExpectation."""

  def __init__(
      self,
      value,
      expected=None,
      expected_serialized=None,
      raise_cls=None,
      raise_msg=None):
    self.value = value
    self.expected = expected
    self.expected_serialized = expected_serialized
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
    sub_test_not_implemented = True
    if sub_test_not_implemented:
      yield
    else:
      self._sub_test_stack.append(test_str)
      sub_test_str = "/".join(self._sub_test_stack)
      with self.subTest(sub_test_str):
        yield
      self._sub_test_stack.pop()


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
  tf.compat.v1.enable_eager_execution()

  class SomeTest(testing.TestCase):

    @testing.run_in_graph_and_eager_modes
    def test_foo(self):
      x = tf.constant([1, 2])
      y = tf.constant([3, 4])
      z = tf.add(x, y)
      self.assertAllEqual([4, 6], self.evaluate(z))

  if __name__ == "__main__":
    testing.test_main()
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
        raise ValueError("Must be executing eagerly when using the "
                         "run_in_graph_and_eager_modes decorator.")

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


class FeatureExpectationsTestCase(SubTestCase):
  """Tests FeatureExpectations with full encode-decode."""

  @run_in_graph_and_eager_modes()
  def assertFeature(self, feature, shape, dtype, tests, serialized_info=None):
    """Test the given feature against the predicates."""

    # Check the shape/dtype
    with self._subTest("shape"):
      self.assertEqual(feature.shape, shape)
    with self._subTest("dtype"):
      self.assertEqual(feature.dtype, dtype)

    # Check the serialized features
    if serialized_info is not None:
      with self._subTest("serialized_info"):
        self.assertEqual(
            serialized_info,
            feature.get_serialized_info(),
        )

    # Create the feature dict
    fdict = features.FeaturesDict({"inner": feature})
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

    # self._process_subtest_exp(e)
    input_value = {"inner": test.value}

    if test.raise_cls is not None:
      with self._subTest("raise"):
        if not test.raise_msg:
          raise ValueError(
              "test.raise_msg should be set with {} for test {}".format(
                  test.raise_cls, type(feature)))
        with self.assertRaisesWithPredicateMatch(
            test.raise_cls, test.raise_msg):
          features_encode_decode(fdict, input_value)
    else:
      # Test the serialization only
      if test.expected_serialized is not None:
        with self._subTest("out_serialize"):
          self.assertEqual(
              test.expected_serialized,
              feature.encode_example(test.value),
          )

      # Assert the returned type match the expected one
      with self._subTest("out"):
        out = features_encode_decode(fdict, input_value, as_tensor=True)
        out = out["inner"]
        with self._subTest("dtype"):
          out_dtypes = utils.map_nested(lambda s: s.dtype, out)
          self.assertEqual(out_dtypes, feature.dtype)
        with self._subTest("shape"):
          # For shape, because (None, 3) match with (5, 3), we use
          # tf.TensorShape.assert_is_compatible_with on each of the elements
          out_shapes = utils.zip_nested(out, feature.shape)
          utils.map_nested(
              lambda x: x[0].shape.assert_is_compatible_with(x[1]),
              out_shapes
          )

      # Test serialization + decoding from disk
      with self._subTest("out_value"):
        decoded_examples = features_encode_decode(fdict, input_value)
        decoded_examples = decoded_examples["inner"]
        if isinstance(decoded_examples, dict):
          # assertAllEqual do not works well with dictionaries so assert
          # on each individual elements instead
          zipped_examples = utils.zip_nested(
              test.expected,
              decoded_examples,
              dict_only=True,
          )
          utils.map_nested(
              lambda x: self.assertAllEqual(x[0], x[1]),
              zipped_examples,
              dict_only=True,
          )
        else:
          self.assertAllEqual(test.expected, decoded_examples)


def features_encode_decode(features_dict, example, as_tensor=False):
  """Runs the full pipeline: encode > write > tmp files > read > decode."""
  # Encode example
  encoded_example = features_dict.encode_example(example)

  with tmp_dir() as tmp_dir_:
    tmp_filename = os.path.join(tmp_dir_, "tmp.tfrecord")

    # Read/write the file
    file_adapter = file_format_adapter.TFRecordExampleAdapter(
        features_dict.get_serialized_info())
    file_adapter.write_from_generator(
        generator_fn=lambda: [encoded_example],
        output_files=[tmp_filename],
    )
    dataset = file_adapter.dataset_from_filename(tmp_filename)

    # Decode the example
    dataset = dataset.map(features_dict.decode_example)

    if not as_tensor:  # Evaluate to numpy array
      for el in dataset_utils.as_numpy(dataset):
        return el
    else:
      if tf.executing_eagerly():
        return next(iter(dataset))
      else:
        return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()


class DummyDatasetSharedGenerator(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = utils.Version("1.0.0")

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": tf.int64}),
        supervised_keys=("x", "x"),
    )

  def _split_generators(self, dl_manager):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    del dl_manager
    return [splits.SplitGenerator(
        name=[splits.Split.TRAIN, splits.Split.TEST],
        num_shards=[2, 1],
    )]

  def _generate_examples(self):
    for i in range(30):
      yield {"x": i}


class DummyMnist(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = utils.Version("1.0.0")

  def __init__(self, *args, **kwargs):
    self._num_shards = kwargs.pop("num_shards", 10)
    super(DummyMnist, self).__init__(*args, **kwargs)

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            "image": features.Image(shape=(28, 28, 1)),
            "label": features.ClassLabel(num_classes=10),
        }),
    )

  def _split_generators(self, dl_manager):
    return [
        splits.SplitGenerator(
            name=splits.Split.TRAIN,
            num_shards=self._num_shards,
            gen_kwargs=dict()),
        splits.SplitGenerator(
            name=splits.Split.TEST,
            num_shards=1,
            gen_kwargs=dict()),
    ]

  def _generate_examples(self):
    for i in range(20):
      yield {
          "image": np.ones((28, 28, 1), dtype=np.uint8),
          "label": i % 10,
      }


def test_main():
  """Entrypoint for tests."""
  tf.compat.v1.enable_eager_execution()
  tf.test.main()


@contextlib.contextmanager
def mock_kaggle_api(filenames=None, err_msg=None):
  """Mock out the kaggle CLI.

  Args:
    filenames: `list<str>`, names of the competition files.
    err_msg: `str`, if provided, the kaggle CLI will raise a CalledProcessError
      and this will be the command output.

  Yields:
    None, context will have kaggle CLI mocked out.
  """

  def make_mock_files_call(filenames, err_msg):
    """Mock subprocess.check_output for files call."""

    def check_output(command_args):
      assert command_args[2] == "files"
      if err_msg:
        raise subprocess.CalledProcessError(1, command_args,
                                            tf.compat.as_bytes(err_msg))
      return tf.compat.as_bytes(
          "\n".join(["name,size,creationDate"] +
                    ["%s,34MB,None\n" % fname for fname in filenames]))

    return check_output

  def make_mock_download_call():
    """Mock subprocess.check_output for download call."""

    def check_output(command_args):
      assert command_args[2] == "download"
      fname = command_args[command_args.index("--file") + 1]
      out_dir = command_args[command_args.index("--path") + 1]
      fpath = os.path.join(out_dir, fname)
      with tf.io.gfile.GFile(fpath, "w") as f:
        f.write(fname)
      return tf.compat.as_bytes("Downloading %s to %s" % (fname, fpath))

    return check_output

  def make_mock_check_output(filenames, err_msg):
    """Mock subprocess.check_output for both calls."""

    files_call = make_mock_files_call(filenames, err_msg)
    dl_call = make_mock_download_call()

    def check_output(command_args):
      if command_args[2] == "files":
        return files_call(command_args)
      else:
        assert command_args[2] == "download"
        return dl_call(command_args)

    return check_output

  with absltest.mock.patch("subprocess.check_output",
                           make_mock_check_output(filenames, err_msg)):
    yield

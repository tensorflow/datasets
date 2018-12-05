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

"""Test utilities."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import os
import tempfile

import tensorflow as tf

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import utils


@contextlib.contextmanager
def tmp_dir(dirname=None):
  tmp = make_tmp_dir(dirname)
  yield tmp
  rm_tmp_dir(tmp)


def tfds_dir():
  """Path to tensorflow_datasets directory."""
  return os.path.dirname(os.path.dirname(__file__))


def make_tmp_dir(dirname=None):
  if dirname and not tf.gfile.Exists(dirname):
    tf.gfile.MakeDirs(dirname)
  return tempfile.mkdtemp(dir=dirname)


def rm_tmp_dir(dirname):
  tf.gfile.DeleteRecursively(dirname)


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


class FeatureExpectation(object):
  """Object defining a featureConnector test."""

  def __init__(self, name, feature, shape, dtype, tests, serialized_info=None):
    self.name = name
    self.feature = feature
    self.shape = shape
    self.dtype = dtype
    self.tests = tests
    self.serialized_info = serialized_info


class SubTestCase(tf.test.TestCase):
  """Adds subTest() context manager to the TestCase if supported.

  Note: To use this feature, make sure you call super() in setUpClass to
  initialize the sub stack.
  """

  @classmethod
  def setUpClass(cls):
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


class FeatureExpectationsTestCase(SubTestCase):
  """Tests FeatureExpectations with full encode-decode."""

  @property
  def expectations(self):
    raise NotImplementedError

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    for exp in self.expectations:
      with self._subTest(exp.name):
        self._process_exp(exp)

  def _process_exp(self, exp):

    # Check the shape/dtype
    with self._subTest("shape"):
      self.assertEqual(exp.feature.shape, exp.shape)
    with self._subTest("dtype"):
      self.assertEqual(exp.feature.dtype, exp.dtype)

    # Check the serialized features
    if exp.serialized_info is not None:
      with self._subTest("serialized_info"):
        self.assertEqual(
            exp.serialized_info,
            exp.feature.get_serialized_info(),
        )

    # Create the feature dict
    fdict = features.FeaturesDict({exp.name: exp.feature})
    for i, test in enumerate(exp.tests):
      with self._subTest(str(i)):
        # self._process_subtest_exp(e)
        input_value = {exp.name: test.value}

        if test.raise_cls is not None:
          with self._subTest("raise"):
            if not test.raise_msg:
              raise ValueError(
                  "test.raise_msg should be set with {}for test {}".format(
                      test.raise_cls, exp.name))
            with self.assertRaisesWithPredicateMatch(
                test.raise_cls, test.raise_msg):
              features_encode_decode(fdict, input_value)
        else:
          # Test the serialization only
          if test.expected_serialized is not None:
            with self._subTest("out_serialize"):
              self.assertEqual(
                  test.expected_serialized,
                  exp.feature.encode_example(test.value),
              )

          # Assert the returned type match the expected one
          with self._subTest("out"):
            out = features_encode_decode(fdict, input_value, as_tensor=True)
            out = out[exp.name]
            with self._subTest("dtype"):
              out_dtypes = utils.map_nested(lambda s: s.dtype, out)
              self.assertEqual(out_dtypes, exp.feature.dtype)
            with self._subTest("shape"):
              # For shape, because (None, 3) match with (5, 3), we use
              # tf.TensorShape.assert_is_compatible_with on each of the elements
              out_shapes = utils.zip_nested(out, exp.feature.shape)
              utils.map_nested(
                  lambda x: x[0].shape.assert_is_compatible_with(x[1]),
                  out_shapes
              )

          # Test serialization + decoding from disk
          with self._subTest("out_value"):
            decoded_examples = features_encode_decode(fdict, input_value)
            decoded_examples = decoded_examples[exp.name]
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
      for el in dataset_utils.iterate_over_dataset(dataset):
        return el
    else:
      if tf.executing_eagerly():
        return next(iter(dataset))
      else:
        return dataset.make_one_shot_iterator().get_next()

# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Test case util to test `tfds.features.FeatureConnector`."""

import contextlib
import functools

import dill
import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import features
from tensorflow_datasets.core import utils
from tensorflow_datasets.testing import test_case
from tensorflow_datasets.testing import test_utils


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
          # recursively call assertAllEqualNested in case there is a dataset.
          lambda x: self.assertAllEqualNested(x[0], x[1]),
          zipped_examples,
          dict_only=True,
      )
    elif isinstance(d1, (tf.data.Dataset, dataset_utils._IterableDataset)):  # pylint: disable=protected-access
      # Checks length and elements of the dataset. At the moment, more than one
      # level of nested datasets is not supported.
      self.assertEqual(len(d1), len(d2))
      for ex1, ex2 in zip(d1, d2):
        self.assertAllEqualNested(ex1, ex2)
    else:
      self.assertAllEqual(d1, d2)


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

  @test_utils.run_in_graph_and_eager_modes()
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
    self.assertFeatureEagerOnly(feature, shape, dtype, tests, serialized_info,
                                skip_feature_tests, test_attributes)

  def assertFeatureEagerOnly(self,
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
        with test_utils.tmp_dir() as config_dir:
          feature.save_config(config_dir)
          new_feature = feature.from_config(config_dir)
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

          def _get_dtype(s):
            if isinstance(s, tf.data.Dataset):
              return tf.nest.map_structure(_get_dtype, s.element_spec)
            else:
              return s.dtype

          out_dtypes = tf.nest.map_structure(_get_dtype, out_tensor)
          self.assertEqual(out_dtypes, test.dtype or feature.dtype)
        with self._subTest('shape'):
          # For shape, because (None, 3) match with (5, 3), we use
          # tf.TensorShape.assert_is_compatible_with on each of the elements
          expected_shape = feature.shape if test.shape is None else test.shape

          def _get_shape(s):
            if isinstance(s, tf.data.Dataset):
              return utils.map_nested(_get_shape, s.element_spec)
            else:
              return s.shape

          out_shapes = utils.map_nested(_get_shape, out_tensor)

          shapes_tuple = utils.zip_nested(out_shapes, expected_shape)
          utils.map_nested(lambda x: x[0].assert_is_compatible_with(x[1]),
                           shapes_tuple)

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
      # TODO(tfds): Should use `as_dataframe._get_feature` instead, to
      # correctly compute for `sequence_rank` for subclasses like `Video`.
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

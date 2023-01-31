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

"""Test case util to test `tfds.features.FeatureConnector`."""

import contextlib
import dataclasses
import functools
from typing import Any, Optional, Type

import dill
from etils import enp
import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.utils import tree_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.testing import test_case
from tensorflow_datasets.testing import test_utils


@dataclasses.dataclass
class FeatureExpectationItem:
  """Test item of a FeatureExpectation.

  Should be passed to `assertFeature` method of `FeatureExpectationsTestCase`.

  Each `FeatureExpectationItem` test an example serialization/deserialization (
  `feature.encode_example` -> `example_serializer.serialize_example` ->
  `example_parse.parse_example` -> `feature.decode_example`).

  Attributes:
    value: Input to `features.encode_example`
    expected: Expected output after `features.decode_example`
    expected_np: Expected output after `features.decode_example_np`
    expected_serialized: Optional
    decoders: Optional `tfds.decode.Decoder` objects (to overwrite the default
      `features.decode_example`). See
      https://www.tensorflow.org/datasets/decode.
    dtype: If `decoders` is provided, the output of `decode_example` is checked
      against this value (otherwise, output is checked against `features.dtype`)
    shape: If `decoders` is provided, the output of `decode_example` is checked
      against this value (otherwise, output is checked against `features.shape`)
    raise_cls: Expected error raised during `features.encode_example`. When set
      `expected` and `expected_serialized` should be `None`.
    raise_cls_np: Expected error raised during `features.encode_example_np`.
      When set `expected_np` and `expected_serialized_np` should be `None`.
    raise_msg: Expected error message regex.
    atol: If provided, compare float values with this precision (use default
      otherwise).
  """

  value: Any
  expected: Optional[Any] = None
  expected_np: Optional[np.ndarray] = None
  expected_serialized: Optional[Any] = None
  decoders: Optional[utils.TreeDict[Any]] = None
  dtype: Optional[tf.dtypes.DType] = None
  shape: Optional[utils.Shape] = None
  raise_cls: Optional[Type[Exception]] = None
  raise_cls_np: Optional[Type[Exception]] = None
  raise_msg: Optional[str] = None
  atol: Optional[float] = None

  def __post_init__(self):
    if not self.decoders and (self.dtype is not None or self.shape is not None):
      raise ValueError('dtype and shape should only be set with transform')


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

  def assertAllEqualNested(self, d1, d2, *, atol: Optional[float] = None):
    """Same as assertAllEqual but compatible with nested dict.

    Args:
      d1: First element to compare
      d2: Second element to compare
      atol: If given, perform a close float comparison. Otherwise, perform an
        exact comparison
    """
    if isinstance(d1, dict):
      # assertAllEqual do not works well with dictionaries so assert
      # on each individual elements instead
      zipped_examples = utils.zip_nested(d1, d2, dict_only=True)
      utils.map_nested(
          # recursively call assertAllEqualNested in case there is a dataset.
          lambda x: self.assertAllEqualNested(x[0], x[1], atol=atol),
          zipped_examples,
          dict_only=True,
      )
    elif isinstance(d1, (tf.data.Dataset, dataset_utils._IterableDataset)):  # pylint: disable=protected-access
      # Checks length and elements of the dataset. At the moment, more than one
      # level of nested datasets is not supported.
      self.assertEqual(len(d1), len(d2))
      for ex1, ex2 in zip(d1, d2):
        self.assertAllEqualNested(ex1, ex2, atol=atol)
    elif atol:
      self.assertAllClose(d1, d2, atol=atol)
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
      # TODO(b/227584124): remove this parameter after fixing this bug
      test_tensor_spec=True,
      skip_feature_tests=False,
      test_attributes=None,
  ):
    """Test the given feature against the predicates."""
    self.assertFeatureEagerOnly(
        feature=feature,
        shape=shape,
        dtype=dtype,
        tests=tests,
        serialized_info=serialized_info,
        test_tensor_spec=test_tensor_spec,
        skip_feature_tests=skip_feature_tests,
        test_attributes=test_attributes,
    )

  def assertFeatureEagerOnly(
      self,
      feature,
      shape,
      dtype,
      tests,
      serialized_info=None,
      test_tensor_spec=True,
      skip_feature_tests=False,
      test_attributes=None,
  ):
    """Test the given feature against the predicates."""

    with self._subTest('feature'):
      self._assert_feature(
          feature=feature,
          shape=shape,
          dtype=dtype,
          tests=tests,
          serialized_info=serialized_info,
          test_tensor_spec=test_tensor_spec,
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
            test_tensor_spec=test_tensor_spec,
            skip_feature_tests=skip_feature_tests,
            test_attributes=test_attributes,
        )
      with self._subTest('feature_proto_roundtrip'):
        with test_utils.tmp_dir() as config_dir:
          feature_proto = feature.to_proto()
          feature.save_metadata(config_dir, feature_name=None)
          new_feature = feature_lib.FeatureConnector.from_proto(feature_proto)
          new_feature.load_metadata(config_dir, feature_name=None)
          self._assert_feature(
              feature=new_feature,
              shape=shape,
              dtype=dtype,
              tests=tests,
              serialized_info=serialized_info,
              test_tensor_spec=test_tensor_spec,
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
      test_tensor_spec=True,
      skip_feature_tests=False,
      test_attributes=None,
  ):
    with self._subTest('shape'):
      self.assertEqual(feature.shape, shape)
    with self._subTest('dtype'):
      self.assertEqual(feature.dtype, dtype)
      tree_utils.map_structure(enp.lazy.is_np_dtype, feature.np_dtype)
      tree_utils.map_structure(enp.lazy.is_tf_dtype, feature.tf_dtype)

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

    # Check whether the following doesn't raise an exception
    fdict.catalog_documentation()

    for i, test in enumerate(tests):
      with self._subTest(str(i)):
        self.assertFeatureTest(
            fdict=fdict,
            test=test,
            feature=feature,
            shape=shape,
            dtype=dtype,
            test_tensor_spec=test_tensor_spec,
        )

  def assertFeatureTest(
      self, fdict, test, feature, shape, dtype, test_tensor_spec: bool = True
  ):
    """Test that encode=>decoding of a value works correctly."""
    # test feature.encode_example can be pickled and unpickled for beam.
    dill.loads(dill.dumps(feature.encode_example))

    input_value = {'inner': test.value}

    if test.raise_cls is not None or test.raise_cls_np is not None:
      if test.raise_cls is not None:
        with self._subTest('raise'):
          if not test.raise_msg:
            raise ValueError(
                'test.raise_msg should be set with {} for test {}'.format(
                    test.raise_cls, type(feature)
                )
            )
          with self.assertRaisesWithPredicateMatch(
              test.raise_cls, test.raise_msg
          ):
            features_encode_decode(fdict, input_value, decoders=test.decoders)
      if test.raise_cls_np is not None:
        with self._subTest('raise_np'):
          if not test.raise_msg:
            raise ValueError(
                'test.raise_msg should be set with {} for test {}'.format(
                    test.raise_cls_np, type(feature)
                )
            )
          with self.assertRaisesWithPredicateMatch(
              test.raise_cls_np, test.raise_msg
          ):
            features_encode_decode_np(
                fdict, input_value, decoders=test.decoders
            )
    else:
      # Test the serialization only
      if test.expected_serialized is not None:
        with self._subTest('out_serialize'):
          self.assertEqual(
              test.expected_serialized,
              feature.encode_example(test.value),
          )

      # Test serialization + decoding from disk for NumPy worflow
      if test.expected_np is not None:
        with self._subTest('out_np'):
          out_numpy = features_encode_decode_np(
              fdict,
              input_value,
              decoders={'inner': test.decoders},
          )
          with self._subTest('out_np_value'):
            np.testing.assert_array_equal(out_numpy['inner'], test.expected)

      # Test serialization + decoding from disk
      with self._subTest('out'):
        out_tensor, out_numpy, out_element_spec = features_encode_decode(
            fdict,
            input_value,
            decoders={'inner': test.decoders},
        )
        out_tensor = out_tensor['inner']
        out_numpy = out_numpy['inner']
        out_element_spec = out_element_spec['inner']

        if test_tensor_spec:
          with self._subTest('tensor_spec'):
            assert feature.get_tensor_spec() == out_element_spec

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
          utils.map_nested(
              lambda x: x[0].assert_is_compatible_with(x[1]), shapes_tuple
          )

        # Assert value
        with self._subTest('out_value'):
          # Eventually construct the tf.RaggedTensor
          expected = tf.nest.map_structure(
              lambda t: t.build() if isinstance(t, RaggedConstant) else t,
              test.expected,
          )
          self.assertAllEqualNested(out_numpy, expected, atol=test.atol)

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
  # Serialize/deserialize the example using TensorFlow methods.
  serialized_example = features_dict.serialize_example(example)

  decode_fn = functools.partial(
      features_dict.deserialize_example,
      decoders=decoders,
  )
  ds = tf.data.Dataset.from_tensors(serialized_example)
  ds = ds.map(decode_fn)

  if tf.executing_eagerly():
    out_tensor = next(iter(ds))
  else:
    out_tensor = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
  out_numpy = dataset_utils.as_numpy(out_tensor)
  return out_tensor, out_numpy, ds.element_spec


def features_encode_decode_np(features_dict, example, decoders):
  """Runs the full pipeline: encode > write > tmp files > read > decode."""
  # Serialize/deserialize the example using NumPy methods.
  serialized_example = features_dict.serialize_example(example)
  deserialized_example = features_dict.deserialize_example_np(
      serialized_example, decoders=decoders
  )
  return deserialized_example

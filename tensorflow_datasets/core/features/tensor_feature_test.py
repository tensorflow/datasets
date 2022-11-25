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

# coding=utf-8
"""Tests for tensorflow_datasets.core.features.tensor_feature."""

from absl.testing import parameterized
import jax.numpy as jnp
import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib


class FeatureTensorTest(
    testing.FeatureExpectationsTestCase,
    parameterized.TestCase,
):

  @parameterized.parameters([
      (np.float32, features_lib.Encoding.NONE),
      (tf.float32, features_lib.Encoding.NONE),
      (np.float32, features_lib.Encoding.ZLIB),
      (tf.float32, features_lib.Encoding.ZLIB),
      (np.float32, features_lib.Encoding.BYTES),
      (tf.float32, features_lib.Encoding.BYTES),
  ])
  def test_shape_static(self, dtype, encoding: features_lib.Encoding):
    np_input = np.random.rand(2, 3).astype(np.float32)
    array_input = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(2, 3),
            dtype=dtype,
            encoding=encoding,
        ),
        dtype=dtype,
        shape=(2, 3),
        tests=[
            # Np array
            testing.FeatureExpectationItem(
                value=np_input,
                expected=np_input,
            ),
            # Python array
            testing.FeatureExpectationItem(
                value=array_input,
                expected=array_input,
            ),
            # Invalid dtype
            testing.FeatureExpectationItem(
                # On Windows, np default dtype is `int32`
                value=np.random.randint(256, size=(2, 3), dtype=np.int64),
                raise_cls=ValueError,
                raise_msg='int64 do not match',
            ),
            # Invalid shape
            testing.FeatureExpectationItem(
                value=np.random.rand(2, 4).astype(np.float32),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ],
        test_attributes={
            '_encoding': encoding,
        },
    )

  @parameterized.parameters([
      (np.int32, features_lib.Encoding.NONE),
      (tf.int32, features_lib.Encoding.NONE),
      (np.int32, features_lib.Encoding.ZLIB),
      (tf.int32, features_lib.Encoding.ZLIB),
      (np.int32, features_lib.Encoding.BYTES),
      (tf.int32, features_lib.Encoding.BYTES),
  ])
  def test_shape_dynamic(self, dtype, encoding: features_lib.Encoding):
    np_input_dynamic_1 = np.random.randint(256, size=(2, 3, 2), dtype=np.int32)
    np_input_dynamic_2 = np.random.randint(256, size=(5, 3, 2), dtype=np.int32)

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(None, 3, 2),
            dtype=dtype,
            encoding=encoding,
        ),
        dtype=dtype,
        shape=(None, 3, 2),
        tests=[
            testing.FeatureExpectationItem(
                value=np_input_dynamic_1,
                expected=np_input_dynamic_1,
            ),
            testing.FeatureExpectationItem(
                value=np_input_dynamic_2,
                expected=np_input_dynamic_2,
            ),
            # Invalid shape
            testing.FeatureExpectationItem(
                value=np.random.randint(256, size=(2, 3, 1), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ])

  @parameterized.parameters([
      (np.int32, features_lib.Encoding.NONE),
      (tf.int32, features_lib.Encoding.NONE),
      (np.int32, features_lib.Encoding.ZLIB),
      (tf.int32, features_lib.Encoding.ZLIB),
      (np.int32, features_lib.Encoding.BYTES),
      (tf.int32, features_lib.Encoding.BYTES),
  ])
  def test_shape_dynamic_none_second(self, dtype,
                                     encoding: features_lib.Encoding):
    np_input_dynamic_1 = np.random.randint(256, size=(3, 2, 2), dtype=np.int32)
    np_input_dynamic_2 = np.random.randint(256, size=(3, 5, 2), dtype=np.int32)

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(3, None, 2),  # None not at the first position.
            dtype=dtype,
            encoding=encoding,
        ),
        dtype=dtype,
        shape=(3, None, 2),
        tests=[
            testing.FeatureExpectationItem(
                value=np_input_dynamic_1,
                expected=np_input_dynamic_1,
            ),
            testing.FeatureExpectationItem(
                value=np_input_dynamic_2,
                expected=np_input_dynamic_2,
            ),
            # Invalid shape
            testing.FeatureExpectationItem(
                value=np.random.randint(256, size=(2, 3, 1), dtype=np.int32),
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ])

  @parameterized.parameters([
      # (features_lib.Encoding.NONE,),  # Multiple unknown dims requires bytes
      (np.uint8, features_lib.Encoding.ZLIB),
      (tf.uint8, features_lib.Encoding.ZLIB),
      (np.uint8, features_lib.Encoding.BYTES),
      (tf.uint8, features_lib.Encoding.BYTES),
  ])
  def test_features_shape_dynamic_multi_none(self, dtype,
                                             encoding: features_lib.Encoding):
    x = np.random.randint(256, size=(2, 3, 1), dtype=np.uint8)
    x_other_shape = np.random.randint(256, size=(4, 4, 1), dtype=np.uint8)
    wrong_shape = np.random.randint(256, size=(2, 3, 2), dtype=np.uint8)

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(None, None, 1),
            dtype=dtype,
            encoding=encoding,
        ),
        shape=(None, None, 1),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=x,
                expected=x,
            ),
            testing.FeatureExpectationItem(
                value=x_other_shape,
                expected=x_other_shape,
            ),
            testing.FeatureExpectationItem(
                value=wrong_shape,  # Wrong shape
                raise_cls=ValueError,
                raise_msg='are incompatible',
            ),
        ],
    )

  @parameterized.parameters([
      # NONE only support single unknown dim, not 2.
      (np.uint8, features_lib.Encoding.BYTES, (2, None, 1)),
      (tf.uint8, features_lib.Encoding.BYTES, (2, None, 1)),
      (np.uint8, features_lib.Encoding.ZLIB, (None, None, 1)),
      (tf.uint8, features_lib.Encoding.ZLIB, (None, None, 1)),
      (np.uint8, features_lib.Encoding.BYTES, (None, None, 1)),
      (tf.uint8, features_lib.Encoding.BYTES, (None, None, 1)),
  ])
  def test_features_multi_none_sequence(
      self,
      dtype,
      encoding: features_lib.Encoding,
      shape,
  ):
    x = np.random.randint(256, size=(3, 2, 3, 1), dtype=np.uint8)
    x_other_shape = np.random.randint(256, size=(3, 2, 2, 1), dtype=np.uint8)

    self.assertFeature(
        feature=features_lib.Sequence(
            features_lib.Tensor(
                shape=shape,
                dtype=dtype,
                encoding=encoding,
            ),),
        shape=(None,) + shape,
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=x,
                expected=x,
            ),
            testing.FeatureExpectationItem(
                value=x_other_shape,
                expected=x_other_shape,
            ),
            # TODO(epot): Is there a way to catch if the user try to encode
            # tensors with different shapes ?
        ],
    )

  @parameterized.parameters([
      (np.bool_, features_lib.Encoding.NONE),
      (tf.bool, features_lib.Encoding.NONE),
      (np.bool_, features_lib.Encoding.ZLIB),
      (tf.bool, features_lib.Encoding.ZLIB),
      (np.bool_, features_lib.Encoding.BYTES),
      (tf.bool, features_lib.Encoding.BYTES),
  ])
  def test_bool_flat(self, dtype, encoding: features_lib.Encoding):
    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(),
            dtype=dtype,
            encoding=encoding,
        ),
        dtype=dtype,
        shape=(),
        tests=[
            testing.FeatureExpectationItem(
                value=np.array(True),
                expected=True,
            ),
            testing.FeatureExpectationItem(
                value=np.array(False),
                expected=False,
            ),
            testing.FeatureExpectationItem(
                value=True,
                expected=True,
            ),
            testing.FeatureExpectationItem(
                value=False,
                expected=False,
            ),
        ])

  @parameterized.parameters([
      (np.bool_, features_lib.Encoding.NONE),
      (tf.bool, features_lib.Encoding.NONE),
      (np.bool_, features_lib.Encoding.ZLIB),
      (tf.bool, features_lib.Encoding.ZLIB),
      (np.bool_, features_lib.Encoding.BYTES),
      (tf.bool, features_lib.Encoding.BYTES),
  ])
  def test_bool_array(self, dtype, encoding: features_lib.Encoding):
    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(3,),
            dtype=dtype,
            encoding=encoding,
        ),
        dtype=np.bool_,
        shape=(3,),
        tests=[
            testing.FeatureExpectationItem(
                value=np.array([True, True, False]),
                expected=[True, True, False],
            ),
            testing.FeatureExpectationItem(
                value=[True, False, True],
                expected=[True, False, True],
            ),
        ])

  @parameterized.parameters([
      (np.object_, features_lib.Encoding.NONE),
      (tf.string, features_lib.Encoding.NONE),
      # Bytes encoding not supported for tf.string
  ])
  def test_string(self, dtype, encoding: features_lib.Encoding):
    nonunicode_text = 'hello world'
    unicode_text = u'你好'

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(),
            dtype=dtype,
            encoding=encoding,
        ),
        shape=(),
        dtype=np.object_,
        tests=[
            # Non-unicode
            testing.FeatureExpectationItem(
                value=nonunicode_text,
                expected=tf.compat.as_bytes(nonunicode_text),
            ),
            # Unicode
            testing.FeatureExpectationItem(
                value=unicode_text,
                expected=tf.compat.as_bytes(unicode_text),
            ),
            # Empty string
            testing.FeatureExpectationItem(
                value='',
                expected=b'',
            ),
            # Trailing zeros
            testing.FeatureExpectationItem(
                value=b'abc\x00\x00',
                expected=b'abc\x00\x00',
            ),
        ],
    )

    self.assertFeature(
        feature=features_lib.Tensor(
            shape=(2, 1),
            dtype=dtype,
            encoding=encoding,
        ),
        shape=(2, 1),
        dtype=np.object_,
        tests=[
            testing.FeatureExpectationItem(
                value=[[nonunicode_text], [unicode_text]],
                expected=[
                    [tf.compat.as_bytes(nonunicode_text)],
                    [tf.compat.as_bytes(unicode_text)],
                ],
            ),
            testing.FeatureExpectationItem(
                value=[nonunicode_text, unicode_text],  # Wrong shape
                raise_cls=ValueError,
                raise_msg='(2,) and (2, 1) must have the same rank',
            ),
            testing.FeatureExpectationItem(
                value=[['some text'], [123]],  # Wrong dtype
                raise_cls=TypeError,
                raise_msg='Expected binary or unicode string, got 123',
            ),
        ],
    )


def test_invalid_input():
  with pytest.raises(ValueError, match='Multiple unknown dimensions'):
    features_lib.Tensor(
        shape=(2, None, None),
        dtype=np.uint8,
    ).encode_example(None)

  with pytest.raises(ValueError, match='Multiple unknown dimensions'):
    features_lib.Tensor(
        shape=(2, None, None),
        dtype=tf.uint8,
    ).encode_example(None)

  with pytest.raises(
      NotImplementedError,
      match='does not support `encoding=` when dtype is string'):
    features_lib.Tensor(
        shape=(2, 1),
        dtype=np.str_,
        encoding=features_lib.Encoding.BYTES,
    )

  with pytest.raises(
      NotImplementedError,
      match='does not support `encoding=` when dtype is string'):
    features_lib.Tensor(
        shape=(2, 1),
        dtype=tf.string,
        encoding=features_lib.Encoding.BYTES,
    )


def test_jax_bfloat16():
  features = features_lib.FeaturesDict({
      'data':
          features_lib.Tensor(shape=(1,), dtype=tf.bfloat16, encoding='bytes')
  })
  data = {
      'data': jnp.array([6.], dtype=jnp.bfloat16),
  }
  features.encode_example(data)

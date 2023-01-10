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

"""Tests for tensorflow_datasets.core.example_serializer."""

from absl.testing import parameterized
import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.utils import py_utils


class ExampleSerializerTest(parameterized.TestCase, testing.SubTestCase):

  def assertRaggedFieldEqual(self, dict1, dict2):
    self.assertIsInstance(dict1, dict)
    self.assertIsInstance(dict2, dict)
    self.assertEqual(set(dict1.keys()), set(dict2.keys()))
    for k, (field1, field2) in py_utils.zip_dict(dict1, dict2):
      with self._subTest(k):
        # Compare the example_data
        self.assertAllEqual(field1[0], field2[0])
        # Compare the tensor_info
        self.assertEqual(field1[1], field2[1])

  @parameterized.parameters((np.int64), (tf.int64))
  def test_ragged_dict_to_tf_example(self, dtype):
    example_data = {
        'input': [[1, 2, 3], [], [4, 5]],
    }
    tensor_info = {
        'input': feature_lib.TensorInfo(
            shape=(
                None,
                None,
            ),
            dtype=dtype,
            sequence_rank=2,
        ),
    }
    ex_proto = example_serializer._dict_to_tf_example(example_data, tensor_info)
    feature = ex_proto.features.feature
    self.assertEqual(
        [1, 2, 3, 4, 5],
        list(feature['input/ragged_flat_values'].int64_list.value),
    )
    self.assertEqual(
        [3, 0, 2],
        list(feature['input/ragged_row_lengths_0'].int64_list.value),
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_ragged_dict_to_tf_example_empty(self, dtype):
    example_data = {
        'input': [],
    }
    tensor_info = {
        'input': feature_lib.TensorInfo(
            shape=(
                None,
                None,
            ),
            dtype=dtype,
            sequence_rank=2,
        ),
    }
    ex_proto = example_serializer._dict_to_tf_example(example_data, tensor_info)
    feature = ex_proto.features.feature
    self.assertEqual(
        [],
        list(feature['input/ragged_flat_values'].int64_list.value),
    )
    self.assertEqual(
        [],
        list(feature['input/ragged_row_lengths_0'].int64_list.value),
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields(self, dtype):
    # Nested `Sequence(Sequence(tf.int64))`
    example_data = [
        [1, 2, 3],
        [],
        [4, 5],
    ]
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            None,
        ),
        dtype=dtype,
        sequence_rank=2,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertRaggedFieldEqual(
        out,
        {
            'ragged_flat_values': (
                np.array([1, 2, 3, 4, 5]),
                feature_lib.TensorInfo(shape=(None,), dtype=np.int64),
            ),
            'ragged_row_lengths_0': (
                [3, 0, 2],
                feature_lib.TensorInfo(shape=(None,), dtype=np.int64),
            ),
        },
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields_np(self, dtype):
    # List of np.array.
    example_data = [
        np.array([1, 2, 3], dtype=np.int64),
        np.array([], dtype=np.int64),
        np.array([4, 5], dtype=np.int64),
    ]
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            None,
        ),
        dtype=dtype,
        sequence_rank=2,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertRaggedFieldEqual(
        out,
        {
            'ragged_flat_values': (
                np.array([1, 2, 3, 4, 5]),
                feature_lib.TensorInfo(shape=(None,), dtype=np.int64),
            ),
            'ragged_row_lengths_0': (
                [3, 0, 2],
                feature_lib.TensorInfo(shape=(None,), dtype=np.int64),
            ),
        },
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields_empty_np(self, dtype):
    # List of np.array.
    example_data = [
        np.array([], dtype=np.int64),
        np.array([], dtype=np.int64),
    ]
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            None,
        ),
        dtype=dtype,
        sequence_rank=2,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertRaggedFieldEqual(
        out,
        {
            'ragged_flat_values': (
                np.zeros(shape=(0,), dtype=np.int64),
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
            'ragged_row_lengths_0': (
                [0, 0],
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
        },
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields_empty(self, dtype):
    # List of empty values
    example_data = [[], [], []]
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            None,
        ),
        dtype=dtype,
        sequence_rank=2,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertRaggedFieldEqual(
        out,
        {
            'ragged_flat_values': (
                np.zeros(shape=(0,), dtype=np.int64),
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
            'ragged_row_lengths_0': (
                [0, 0, 0],
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
        },
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields_all_empty(self, dtype):
    # Empty list
    example_data = []
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            None,
        ),
        dtype=dtype,
        sequence_rank=2,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertRaggedFieldEqual(
        out,
        {
            'ragged_flat_values': (
                np.zeros(shape=(0,), dtype=np.int64),
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
            'ragged_row_lengths_0': (
                np.zeros(shape=(0,), dtype=np.int64),
                feature_lib.TensorInfo(shape=(None,), dtype=tf.int64),
            ),
        },
    )

  @parameterized.parameters((np.int64), (tf.int64))
  def test_add_ragged_fields_single_level_sequence(self, dtype):
    # Single level sequence
    example_data = [
        [1, 2],
        [2, 3],
        [4, 5],
    ]
    tensor_info = feature_lib.TensorInfo(
        shape=(
            None,
            2,
        ),
        dtype=dtype,
        sequence_rank=1,
    )
    out = example_serializer._add_ragged_fields(example_data, tensor_info)
    self.assertAllEqual(
        out[0],
        [
            [1, 2],
            [2, 3],
            [4, 5],
        ],
    )
    self.assertEqual(out[1], tensor_info)

  @parameterized.parameters((np.int64), (tf.int64))
  def test_item_to_tf_feature_incorrect_shape(self, dtype):
    # Test shape check in _item_to_tf_feature raises ValueError.
    example_item = [1, 2, 3, 4, 5]
    tensor_info = feature_lib.TensorInfo(shape=(4,), dtype=dtype)
    with self.assertRaises(ValueError):
      example_serializer._item_to_tf_feature(example_item, tensor_info)

  @parameterized.parameters((np.object_), (tf.string))
  def test_item_to_tf_feature_string_check(self, dtype):
    # Test string check in _item_to_tf_feature raises ValueError.
    example_item = [1, 2, 3, 4, 5]
    tensor_info = feature_lib.TensorInfo(shape=(5,), dtype=dtype)
    with self.assertRaisesRegex(
        ValueError,
        'Unsupported value: (.*)\nCould not convert to bytes list.',
    ):
      example_serializer._item_to_tf_feature(example_item, tensor_info)

  @parameterized.parameters((np.int64), (tf.int64))
  def test_dict_to_tf_example_error_reraise(self, dtype):
    # Test error reraise in _dict_to_tf_example.
    example_data = {'input': [1, 2, 3]}
    tensor_info = {
        'input': feature_lib.TensorInfo(
            shape=(2,),
            dtype=dtype,
        ),
    }
    with self.assertRaisesRegex(
        ValueError, 'Error while serializing feature `input`:'
    ):
      example_serializer._dict_to_tf_example(example_data, tensor_info)


class AsBytesTest(parameterized.TestCase):

  @parameterized.parameters(
      (b'thisisbytes', b'thisisbytes'),
      ('thisisbytes', b'thisisbytes'),
      (bytearray([1, 2, 3]), b'\x01\x02\x03'),
  )
  def test_as_bytes(self, input_args, expected_output):
    self.assertEqual(example_serializer._as_bytes(input_args), expected_output)


if __name__ == '__main__':
  testing.test_main()

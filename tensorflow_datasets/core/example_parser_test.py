# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.example_parser."""

import numpy as np
import pytest
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.proto import tf_example_pb2
from tensorflow_datasets.proto import tf_feature_pb2


def test_example_parser_np():
  features = features_lib.FeaturesDict({
      'feature': features_lib.FeaturesDict({
          'nested_text': features_lib.Text(),
          'nested_float': np.float32,
      }),
      'array_of_ints': features_lib.Tensor(shape=(2,), dtype=np.int8),
      'array_of_unknown_shape': features_lib.Tensor(
          shape=(None,), dtype=np.uint16
      ),
      'ragged_tensor': features_lib.Sequence(
          features_lib.Sequence(
              features_lib.Tensor(shape=(2,), dtype=np.int32),
          ),
      ),
      'ragged_tensor_without_length': features_lib.Sequence(
          features_lib.Sequence(np.str_),
      ),
  })
  serialized_example = tf_example_pb2.Example(
      features=tf_feature_pb2.Features(
          feature={
              'feature/nested_text': tf_feature_pb2.Feature(
                  bytes_list=tf_feature_pb2.BytesList(value=[b'thisistext'])
              ),
              'feature/nested_float': tf_feature_pb2.Feature(
                  float_list=tf_feature_pb2.FloatList(value=[1.0])
              ),
              'array_of_ints': tf_feature_pb2.Feature(
                  int64_list=tf_feature_pb2.Int64List(value=[2, 3])
              ),
              'array_of_unknown_shape': tf_feature_pb2.Feature(
                  int64_list=tf_feature_pb2.Int64List(value=[4, 5, 6])
              ),
              'ragged_tensor/ragged_flat_values': tf_feature_pb2.Feature(
                  int64_list=tf_feature_pb2.Int64List(value=[0, 1, 2, 3, 4, 5])
              ),
              'ragged_tensor/ragged_row_lengths_0': tf_feature_pb2.Feature(
                  int64_list=tf_feature_pb2.Int64List(value=[2, 0, 1])
              ),
              'ragged_tensor_without_length/ragged_flat_values': (
                  tf_feature_pb2.Feature(
                      bytes_list=tf_feature_pb2.BytesList(
                          value=[b'abcd', b'efg', b'hij']
                      )
                  )
              ),
              'ragged_tensor_without_length/ragged_row_lengths_0': (
                  tf_feature_pb2.Feature(
                      int64_list=tf_feature_pb2.Int64List(value=[2, 0, 1])
                  )
              ),
          }
      )
  ).SerializeToString()
  expected_np = {
      'feature': {'nested_text': b'thisistext', 'nested_float': 1.0},
      'array_of_ints': np.asarray([2, 3], dtype=np.int8),
      'array_of_unknown_shape': np.asarray([4, 5, 6], dtype=np.uint16),
      'ragged_tensor': [
          [[0, 1], [2, 3]],
          [],
          [[4, 5]],
      ],
      'ragged_tensor_without_length': [
          [b'abcd', b'efg'],
          [],
          [b'hij'],
      ],
  }
  example_specs = features.get_tensor_info()
  example_parser_np = example_parser.ExampleParserNp(example_specs)
  parsed_example = example_parser_np.parse_example(serialized_example)
  assert isinstance(parsed_example['array_of_ints'], np.ndarray)
  assert isinstance(parsed_example['array_of_unknown_shape'], np.ndarray)
  assert parsed_example['array_of_ints'].dtype == np.int8
  assert parsed_example['array_of_unknown_shape'].dtype == np.uint16
  np.testing.assert_equal(parsed_example, expected_np)


def test_key_error_exception_if_example_specs_is_malformed():
  features = features_lib.FeaturesDict({'doesnotexist': features_lib.Text()})
  serialized_example = tf_example_pb2.Example(
      features=tf_feature_pb2.Features(
          feature={
              'array_of_ints': tf_feature_pb2.Feature(
                  int64_list=tf_feature_pb2.Int64List(value=[2, 3, 4])
              ),
          }
      )
  ).SerializeToString()
  example_specs = features.get_tensor_info()
  example_parser_np = example_parser.ExampleParserNp(example_specs)
  with pytest.raises(
      KeyError,
      match='(.|\n)*array_of_ints is found in the feature, but not in*',
  ):
    example_parser_np.parse_example(serialized_example)


@pytest.mark.parametrize(
    ('flat_values', 'row_lengths', 'shape', 'expected'),
    (
        (
            [0, 1, 2],  # flat_values
            [[1, 0, 2]],  # row_lengths
            (None,),  # shape
            [  # expected
                [0],
                [],
                [1, 2],
            ],
        ),
        (
            [0, 1, 2, 3, 4, 10, 11, 12, 13, 14],  # flat_values
            [[3, 3], [3, 0, 2, 2, 2, 1]],  # row_lengths
            (None, None, None),  # shape
            [  # expected
                [[0, 1, 2], [], [3, 4]],
                [[10, 11], [12, 13], [14]],
            ],
        ),
        (
            [1, 2, 3, 4, 5, 10, 11, 12, 13, 14],  # flat_values
            [[3, 3], [3, 0, 2, 2, 2, 1]],  # row_lengths
            (None, 3, None),  # shape
            [  # expected
                [[1, 2, 3], [], [4, 5]],
                [[10, 11], [12, 13], [14]],
            ],
        ),
    ),
)
def test_reshape_deep_ragged_tensor(flat_values, row_lengths, shape, expected):
  np.testing.assert_equal(
      example_parser.reshape_ragged_tensor(flat_values, row_lengths, shape),
      expected,
  )


def test_full_row_lengths():
  assert list(
      example_parser._full_row_lengths(
          [1, 2, 3, 4, 10, 11, 12, 13, 14],
          [[2, 0, 1]],
          (None, None, 3),
      )
  ) == [[3, 3, 3], [2, 0, 1]]
  assert list(
      example_parser._full_row_lengths(
          [1, 2, 3, 4, 10, 11, 12, 13, 14],
          [[3, 3], [3, 0, 2, 2, 2, 1]],
          (None, 3, None),
      )
  ) == [[3, 0, 2, 2, 2, 1], [3, 3]]

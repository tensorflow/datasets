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

"""Tests for tensorflow_datasets.core.example_parser."""

import numpy as np
import pytest
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import features as features_lib

import tensorflow as tf
example_pb2 = tf.train
feature_pb2 = tf.train


def test_example_parser_np():
  features = features_lib.FeaturesDict({
      'feature': features_lib.FeaturesDict({
          'nested_text': features_lib.Text(),
          'nested_float': np.float32,
      }),
      'array_of_ints': features_lib.Tensor(shape=(2,), dtype=np.int8),
  })
  serialized_example = example_pb2.Example(
      features=feature_pb2.Features(
          feature={
              'feature/nested_text': feature_pb2.Feature(
                  bytes_list=feature_pb2.BytesList(value=[b'thisistext'])
              ),
              'feature/nested_float': feature_pb2.Feature(
                  float_list=feature_pb2.FloatList(value=[1.0])
              ),
              'array_of_ints': feature_pb2.Feature(
                  int64_list=feature_pb2.Int64List(value=[2, 3])
              ),
          }
      )
  ).SerializeToString()
  expected_np = {
      'feature': {'nested_text': b'thisistext', 'nested_float': 1.0},
      'array_of_ints': np.asarray([2, 3], dtype=np.int8),
  }
  example_specs = features.get_tensor_info()
  example_parser_np = example_parser.ExampleParserNp(example_specs)
  parsed_example = example_parser_np.parse_example(serialized_example)
  assert isinstance(parsed_example['array_of_ints'], np.ndarray)
  assert parsed_example['array_of_ints'].dtype == np.int8
  np.testing.assert_equal(parsed_example, expected_np)


def test_raise_exception_if_example_has_wrong_shape():
  features = features_lib.FeaturesDict(
      {
          'array_of_ints': features_lib.Tensor(shape=(2,), dtype=np.int8),
      }
  )
  serialized_example = example_pb2.Example(
      features=feature_pb2.Features(
          feature={
              'array_of_ints': feature_pb2.Feature(
                  int64_list=feature_pb2.Int64List(value=[2, 3, 4])
              ),
          }
      )
  ).SerializeToString()
  example_specs = features.get_tensor_info()
  example_parser_np = example_parser.ExampleParserNp(example_specs)
  with pytest.raises(
      ValueError, match='(.|\n)*cannot reshape array of size 3 into shape (2,)*'
  ):
    example_parser_np.parse_example(serialized_example)


def test_key_error_exception_if_example_specs_is_malformed():
  features = features_lib.FeaturesDict({'doesnotexist': features_lib.Text()})
  serialized_example = example_pb2.Example(
      features=feature_pb2.Features(
          feature={
              'array_of_ints': feature_pb2.Feature(
                  int64_list=feature_pb2.Int64List(value=[2, 3, 4])
              ),
          }
      )
  ).SerializeToString()
  example_specs = features.get_tensor_info()
  example_parser_np = example_parser.ExampleParserNp(example_specs)
  with pytest.raises(
      RuntimeError,
      match='(.|\n)*array_of_ints is found in the feature, but not in*',
  ):
    example_parser_np.parse_example(serialized_example)

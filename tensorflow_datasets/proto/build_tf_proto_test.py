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

"""proto tests."""

import pytest  # pylint: disable=unused-import
from tensorflow_datasets.proto import build_tf_proto


TFProto = build_tf_proto.TFProto

@pytest.mark.parametrize('tf_proto', [TFProto.EXAMPLE, TFProto.FEATURE])
def test_protos_did_not_change_on_tensorflow_side(tf_proto):
  """Read the docstring of `build_tf_proto.py` to understand this test."""
  tf_proto_content = build_tf_proto.get_tf_proto_content_from_github(tf_proto)
  tfds_proto_path = build_tf_proto.get_tfds_proto_path(tf_proto)
  with tfds_proto_path.open('rb') as tfds_proto_file:
    try:
      assert tfds_proto_file.read() == tf_proto_content
    except AssertionError as exception:
      raise FileExistsError(
          f'{tf_proto.value} proto changed on TensorFlow side. Please,'
          ' regenerate the Python files using'
          ' "tensorflow_datasets/proto/build_tf_proto.py".'
      ) from exception


def test_remove_comments():
  file_content = b"""
      syntax = "proto3";
      // This is a comment.
      // This is also a comment.
      message Feature {  // Inline comment.
        // Each feature can be exactly one kind.
        oneof kind {
          BytesList bytes_list = 1;
          // Indented comment.
          FloatList float_list = 2; // Comment // in another comment.
          Int64List int64_list = 3;
        }
      }
      """
  expected_file_content = b"""
      syntax = "proto3";
      message Feature {
        oneof kind {
          BytesList bytes_list = 1;
          FloatList float_list = 2;
          Int64List int64_list = 3;
        }
      }
      """
  assert expected_file_content == build_tf_proto.remove_comments(file_content)

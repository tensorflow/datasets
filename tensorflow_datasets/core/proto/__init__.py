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

"""Public API of the proto package."""
# pylint: disable=g-import-not-at-top


def _get():
  from tensorflow_datasets.core.proto import dataset_info_generated_pb2 as dataset_info_pb2_
  from tensorflow_datasets.core.proto.dataset_info_generated_pb2 import SplitInfo as SplitInfo_
  from google.protobuf import json_format as json_format_
  return dataset_info_pb2_, SplitInfo_, json_format_


dataset_info_pb2, SplitInfo, json_format = _get()  # pylint: disable=invalid-name
del _get

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

"""Tests for laion400m_dataset_builder."""
from tensorflow_datasets.core.dataset_builders.laion import laion400m_dataset_builder
import tensorflow_datasets.public_api as tfds

_EXAMPLES_IN_SHARD = [1, 2, 3]


class TestDummyLaion400mDataset(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = laion400m_dataset_builder.DummyLaion400mDataset
  SPLITS = {'train': len(_EXAMPLES_IN_SHARD)}

  @classmethod
  def setUpClass(cls):
    cls.DATASET_CLASS.EXAMPLES_IN_SHARD = _EXAMPLES_IN_SHARD
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()

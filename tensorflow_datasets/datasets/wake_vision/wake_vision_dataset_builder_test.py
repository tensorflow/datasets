# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Tests for wake_vision dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.wake_vision import wake_vision_dataset_builder


class WakeVisionTest(testing.DatasetBuilderTestCase):
  """Tests for wake_vision dataset."""

  DATASET_CLASS = wake_vision_dataset_builder.Builder
  SPLITS = {
      'train_large': 16,
      'train_quality': 4,
      'validation': 11,
      'test': 10,
  }

  DL_EXTRACT_RESULT = {
      'train_images': [
          'wake-vision-train-dummy-1.tar.gz',
          'wake-vision-train-dummy-2.tar.gz',
      ],
      'validation_images': ['wake-vision-validation-dummy.tar.gz'],
      'test_images': ['wake-vision-test-dummy.tar.gz'],
      'train_large_metadata': 'wake_vision_train_large.csv',
      'train_quality_metadata': 'wake_vision_train_quality.csv',
      'validation_metadata': 'wake_vision_validation.csv',
      'test_metadata': 'wake_vision_test.csv',
  }


if __name__ == '__main__':
  testing.test_main()

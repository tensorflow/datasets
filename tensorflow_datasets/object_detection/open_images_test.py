# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Tests for open_images dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import open_images


class OpenImagesV42012Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = open_images.OpenImagesV4
  SPLITS = {  # Expected number of examples on each split.
      'train': 512,
      'test': 36,
      'validation': 12,
  }
  DL_EXTRACT_RESULT = {
      'train_images': ['s3-tar_train_sha1_%s.tar' % i
                       for i in '0123456789abcdef'],
      'test_images': 's3-tar_test_sha2.tar',
      'validation_images': 's3-tar_validation_sha3.tar',
      'train_human_labels': 'train-human-labels.csv',
      'train_machine_labels': 'train-machine-labels.csv',
      'test_human_labels': 'test-human-labels.csv',
      'test_machine_labels': 'test-machine-labels.csv',
      'validation_human_labels': 'validation-human-labels.csv',
      'validation_machine_labels': 'validation-machine-labels.csv',
      'train-annotations-bbox': 'train-annotations-bbox.csv',
      'test-annotations-bbox': 'test-annotations-bbox.csv',
      'validation-annotations-bbox': 'validation-annotations-bbox.csv',
  }


if __name__ == '__main__':
  testing.test_main()

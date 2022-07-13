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

"""Tests for Beans dataset."""

from tensorflow_datasets.image_classification import beans
import tensorflow_datasets.testing as tfds_test

beans._IMAGE_SHAPE = (None, None, 3)  # pylint: disable=protected-access


class BeansTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = beans.Beans

  SPLITS = {
      'train': 3,
      'test': 3,
      'validation': 3,
  }

  DL_EXTRACT_RESULT = [
      'beans_train.zip', 'beans_validation.zip', 'beans_test.zip'
  ]


if __name__ == '__main__':
  tfds_test.test_main()

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

"""Tests for horses or humans data loading."""

from tensorflow_datasets.image_classification import horses_or_humans
import tensorflow_datasets.testing as tfds_test

horses_or_humans._IMAGE_SHAPE = (None, None, 3)  # pylint: disable=protected-access


class HorsesOrHumansTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = horses_or_humans.HorsesOrHumans

  SPLITS = {
      'train': 2,
      'test': 2,
  }

  DL_EXTRACT_RESULT = ['hoh_train.zip', 'hoh_test.zip']


if __name__ == '__main__':
  tfds_test.test_main()

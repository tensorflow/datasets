# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for Rock, Paper, Scissors data module."""

from tensorflow_datasets.image_classification import rock_paper_scissors
import tensorflow_datasets.testing as tfds_test

rock_paper_scissors._IMAGE_SHAPE = (None, None, 3)  # pylint: disable=protected-access


class RockPaperScissorsTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = rock_paper_scissors.RockPaperScissors

  SPLITS = {
      'train': 3,
      'test': 3,
  }

  DL_EXTRACT_RESULT = ['rps_train.zip', 'rps_test.zip']


if __name__ == '__main__':
  tfds_test.test_main()

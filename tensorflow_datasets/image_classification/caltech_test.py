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

"""Tests for Caltech data loading."""
from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import caltech


class Caltech101Test(testing.DatasetBuilderTestCase):

  DATASET_CLASS = caltech.Caltech101

  SPLITS = {
      'train': 3,
      'test': 3,
  }

  def setUp(self):
    super(Caltech101Test, self).setUp()
    caltech._TRAIN_POINTS_PER_CLASS = 1


if __name__ == '__main__':
  testing.test_main()

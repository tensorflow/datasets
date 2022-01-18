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

"""Tests for cats_vs_dogs data loading."""
from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import cats_vs_dogs

cats_vs_dogs._NUM_CORRUPT_IMAGES = 0  # pylint: disable=protected-access


class CatsVsDogsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cats_vs_dogs.CatsVsDogs

  SPLITS = {'train': 4}
  DL_EXTRACT_RESULT = 'cats_vs_dogs.zip'


if __name__ == '__main__':
  testing.test_main()

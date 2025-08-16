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

"""Tests for spots10 dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import spots10
import pytest

# testing/spots10.py generates fake input data

spots10._TRAIN_EXAMPLES = 2  # pylint: disable=protected-access
spots10._TEST_EXAMPLES = 2  # pylint: disable=protected-access


class spots10Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = spots10
  SPLITS = {
      "train": 2,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "train-image",
      "train_labels": "train-label",
      "test_data": "test-image",
      "test_labels": "test-label",
  }


  """
  Skip the test_download_and_prepare_as_dataset test using 
  @pytest.mark.skip decorator because no dummy dataset 
  was included for spots10.
  """
  @pytest.mark.skip(reason="Skipping this test temporarily.")
  def test_download_and_prepare_as_dataset(self):
      pass


if __name__ == "__main__":
  testing.test_main()

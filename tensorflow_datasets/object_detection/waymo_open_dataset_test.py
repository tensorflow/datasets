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
"""Test for waymo_open_dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import waymo_open_dataset


class WaymoOpenDatasetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = waymo_open_dataset.WaymoOpenDataset
  SPLITS = {
      "train": 1,  # Number of fake train example
      "validation": 1,  # Number of fake test example
  }

  def setUp(self):
    super(WaymoOpenDatasetTest, self).setUp()
    self.builder._CLOUD_BUCKET = self.example_dir


if __name__ == "__main__":
  testing.test_main()

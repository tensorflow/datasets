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

"""Test for waymo_open_dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import waymo_open_dataset


class WaymoOpenDatasetTest(testing.DatasetBuilderTestCase):
  """Waymo Open Dataset tests."""

  DATASET_CLASS = waymo_open_dataset.WaymoOpenDataset
  BUILDER_CONFIG_NAMES_TO_TEST = ["v1.0"]
  SPLITS = {
      "train": 1,  # Number of fake train example
      "validation": 1,  # Number of fake validation example
  }

  def setUp(self):
    """Set up Waymo Open Dataset tests."""
    super(WaymoOpenDatasetTest, self).setUp()
    for config in waymo_open_dataset.WaymoOpenDataset.BUILDER_CONFIGS:
      config.cloud_bucket = self.example_dir


if __name__ == "__main__":
  testing.test_main()

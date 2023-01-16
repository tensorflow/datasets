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

"""Test for the PlantLeaves dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.plant_leaves import plant_leaves_dataset_builder


class PlantLeavesTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = plant_leaves_dataset_builder.Builder
  SPLITS = {"train": 22}
  # NOTE: Must match file names in the test directory.
  DL_EXTRACT_RESULT = {
      fname: fname
      for fname in [
          "{0:04d}_1.JPG".format(label_number) for label_number in range(1, 23)
      ]
  }


if __name__ == "__main__":
  testing.test_main()

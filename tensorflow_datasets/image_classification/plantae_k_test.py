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

"""Test for the PlantLeaves dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import plantae_k


class PlantaeKTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = plantae_k.PlantaeK
  # See note below about the +1
  SPLITS = {"train": 16 + 1}
  _LABEL_TAGS = [
      "apple_d", "apple_h", "apricot_d", "apricot_h", "cherry_d", "cherry_h",
      "cranberry_d", "cranberry_h", "grapes_d", "grapes_h", "peach_d",
      "peach_h", "pear_d", "pear_h", "walnut_d", "walnut_h", "walnut-h"
  ]
  # NOTE: Must match file names in the test directory. Due to bug in file naming
  # we have to have both walnut_d and walnut_h for healthy walnut.
  DL_EXTRACT_RESULT = {
      fname: fname
      for fname in ["{}1.JPG".format(label_tag) for label_tag in _LABEL_TAGS]
  }


if __name__ == "__main__":
  testing.test_main()

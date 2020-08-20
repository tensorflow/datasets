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

"""CLIC dataset."""

from tensorflow_datasets.image import clic
import tensorflow_datasets.public_api as tfds


class ClicTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = clic.CLIC
  SPLITS = {
      "train": 1,
      "validation": 1,
      "test": 1,
  }
  DL_EXTRACT_RESULT = {
      "mobile_train": "train",
      "prof_train": "skip",
      "mobile_val": "skip",
      "prof_val": "valid",
      "mobile_test": "skip",
      "prof_test": "test",
  }

if __name__ == "__main__":
  tfds.testing.test_main()


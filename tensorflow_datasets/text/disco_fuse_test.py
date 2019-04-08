# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""DiscoFuse Test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.text import disco_fuse


class DiscoFuseTest(testing.DatasetBuilderTestCase):
  """DiscoFuse Test"""
  DATASET_CLASS = disco_fuse.DiscoFuse
  BUILDER_CONFIG_NAMES_TO_TEST = ["wikipedia"]
  SPLITS = {
      "train": 9,  # Number of fake train example
      "test": 3,
      "dev": 3,
      "train_balanced": 9,  # Number of fake train example
      "test_balanced": 3,
      "dev_balanced": 3
  }
  OVERLAPPING_SPLITS = ["train_balanced", "test_balanced", "dev_balanced"]

if __name__ == "__main__":
  testing.test_main()

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
"""Test for div2k dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import div2k


class Div2kTestBicubicX(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["bicubic_x2"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
      "train_hr_url": "",
      "valid_hr_url": "",
      "train_lr_url": "DIV2K_train_LR_bicubic_X2",
      "valid_lr_url": "DIV2K_valid_LR_bicubic_X2",
  }


class Div2kTestUnknownX(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  BUILDER_CONFIG_NAMES_TO_TEST = ["unknown_x2"]
  SPLITS = {
      "train": 1,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = {
      "train_hr_url": "",
      "valid_hr_url": "",
      "train_lr_url": "DIV2K_train_LR_unknown_X2",
      "valid_lr_url": "DIV2K_valid_LR_unknown_X2",
  }


if __name__ == "__main__":
  testing.test_main()

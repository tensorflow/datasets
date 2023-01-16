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

"""Tests for camelyon_patch.py."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.patch_camelyon import patch_camelyon_dataset_builder


class PatchCamelyonTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = patch_camelyon_dataset_builder.Builder

  SPLITS = {
      'train': 5,
      'test': 4,
      'validation': 3,
  }

  DL_EXTRACT_RESULT = {
      'train_x': 'camelyonpatch_level_2_split_train_x.h5',
      'train_y': 'camelyonpatch_level_2_split_train_y.h5',
      'test_x': 'camelyonpatch_level_2_split_test_x.h5',
      'test_y': 'camelyonpatch_level_2_split_test_y.h5',
      'valid_x': 'camelyonpatch_level_2_split_valid_x.h5',
      'valid_y': 'camelyonpatch_level_2_split_valid_y.h5',
  }


if __name__ == '__main__':
  testing.test_main()

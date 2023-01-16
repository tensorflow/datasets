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

"""Test for LVIS dataset."""

from tensorflow_datasets.datasets.lvis import lvis_dataset_builder
import tensorflow_datasets.public_api as tfds


class LvisTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for LVIS dataset."""

  DATASET_CLASS = lvis_dataset_builder.Builder
  SPLITS = {
      'train': 2,
      'validation': 1,
      'test': 1,
  }
  DL_EXTRACT_RESULT = {
      'train_annotation': '',
      'train_images': '',
      'validation_annotation': '',
      'validation_images': '',
      'test_annotation': '',
      'test_images': '',
  }


if __name__ == '__main__':
  tfds.testing.test_main()

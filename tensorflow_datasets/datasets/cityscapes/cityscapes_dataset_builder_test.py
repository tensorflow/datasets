# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for Cityscapes dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.cityscapes import cityscapes_dataset_builder


class CityscapesSegmentationTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation']
  SPLITS = {
      'train': 3,
      'validation': 1,
      'test': 2,
  }


class CityscapesSegmentationExtraTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation_extra']
  SPLITS = {
      'train': 3,
      'train_extra': 4,
      'validation': 1,
  }


class CityscapesStereoDisparityTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ['stereo_disparity']
  SPLITS = {
      'train': 3,
      'validation': 1,
      'test': 2,
  }


class CityscapesStereoDisparityExtraTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ['stereo_disparity_extra']
  SPLITS = {
      'train': 3,
      'train_extra': 4,
      'validation': 1,
  }


if __name__ == '__main__':
  testing.test_main()

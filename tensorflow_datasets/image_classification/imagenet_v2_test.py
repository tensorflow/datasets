# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for ImageNet-v2 image classification dataset."""
from tensorflow_datasets.image_classification import imagenet_v2
import tensorflow_datasets.public_api as tfds


class ImagenetV2Test(tfds.testing.DatasetBuilderTestCase):

  BUILDER_CONFIG_NAMES_TO_TEST = [
      'matched-frequency', 'threshold-0.7', 'topimages'
  ]

  DATASET_CLASS = imagenet_v2.ImagenetV2
  SPLITS = {
      'test': 10,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = ''


if __name__ == '__main__':
  tfds.testing.test_main()

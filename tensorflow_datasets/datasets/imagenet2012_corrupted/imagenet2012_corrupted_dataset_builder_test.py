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

"""Tests for corrupted_imagenet."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.imagenet2012_corrupted import imagenet2012_corrupted_dataset_builder


class Imagenet2012CorruptedTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = [  # pylint: disable=g-long-ternary
      "gaussian_noise_1",
      "shot_noise_2",
      "impulse_noise_3",
      "defocus_blur_4",
      "glass_blur_5",
      "motion_blur_1",
      "zoom_blur_2",
      "snow_3",
      "frost_4",
      "fog_5",
      "brightness_1",
      "contrast_2",
      "elastic_transform_3",
      "pixelate_4",
      "jpeg_compression_5",
      "gaussian_blur_1",
      "saturate_2",
      "spatter_3",
      "speckle_noise_4",
  ]

  DATASET_CLASS = imagenet2012_corrupted_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on the train/validation splits.
      "validation": 10,
  }
  DL_EXTRACT_RESULT = [
      "ILSVRC2012_img_train.tar",
      "ILSVRC2012_img_val.tar",
  ]
  DL_DOWNLOAD_RESULT = [
      "frost1.png",
      "frost2.png",
      "frost3.png",
      "frost4.jpg",
      "frost5.jpg",
      "frost6.jpg",
  ]


if __name__ == "__main__":
  testing.test_main()

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

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.imagenet_resized import imagenet_resized_dataset_builder


class ImagenetResizedTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = [
      "8x8",
  ]
  DATASET_CLASS = imagenet_resized_dataset_builder.Builder
  SPLITS = {
      "train": 3,
      "validation": 1,
  }

  DL_EXTRACT_RESULT = ["Imagenet8_train_npz.zip", "Imagenet8_val_npz.zip"]


if __name__ == "__main__":
  testing.test_main()

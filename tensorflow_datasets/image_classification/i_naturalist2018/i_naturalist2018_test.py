# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""i_naturalist2018 dataset."""

from tensorflow_datasets.image_classification.i_naturalist2018 import i_naturalist2018
import tensorflow_datasets.public_api as tfds


class INaturalist2018Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for i_naturalist2018 dataset."""

  DATASET_CLASS = i_naturalist2018.INaturalist2018
  SPLITS = {
      "train": 4,  # Number of fake train example
      "validation": 3,  # Number of fake val example
      "test": 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      "test_images": "test2018.tar.gz",
      "train_annos": "train_annos",
      "val_annos": "val_annos",
      "trainval_images": "train_val2018.tar.gz",
      "categories": "categories",
  }
  SKIP_CHECKSUMS = True


if __name__ == "__main__":
  tfds.testing.test_main()

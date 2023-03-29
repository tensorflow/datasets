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

"""Tests for imagenet2012_fewshot_dataset_builder."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.imagenet2012_fewshot import imagenet2012_fewshot_dataset_builder
import tensorflow_datasets.public_api as tfds

imagenet2012_fewshot_dataset_builder.Builder.PNG_IMAGES = ["n01440764_1.JPEG"]
imagenet2012_fewshot_dataset_builder.Builder.CMYK_IMAGES = [
    "n01440764_2.JPEG",
    "n01440764_3.JPEG",
]

imagenet2012_fewshot_dataset_builder.SUBSET2FILES = {
    "1shot": tfds.core.tfds_path(
        "datasets/imagenet2012_fewshot/dummy_data/1shot.txt"
    ),
}
imagenet2012_fewshot_dataset_builder.TUNE_FILE = tfds.core.tfds_path(
    "datasets/imagenet2012_fewshot/dummy_data/tune.txt"
)


class Imagenet2012FewshotTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagenet2012_fewshot_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["1shot"]
  SPLITS = {  # Expected number of examples on each split.
      "train": 1,
      "tune": 1,
      "validation": 10,
  }
  DL_EXTRACT_RESULT = [
      "ILSVRC2012_img_train.tar",
      "ILSVRC2012_img_val.tar",
  ]


if __name__ == "__main__":
  testing.test_main()

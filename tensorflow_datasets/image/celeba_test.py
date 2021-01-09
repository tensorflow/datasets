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

"""Tests for tensorflow_datasets.image.celeba."""
from tensorflow_datasets import testing
from tensorflow_datasets.image import celeba


class CelebATest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = celeba.CelebA

  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }

  DL_EXTRACT_RESULT = {
      "img_align_celeba": "img_align_celeba.zip",
      "list_eval_partition": "list_eval_partition.txt",
      "list_attr_celeba": "list_attr_celeba.txt",
      "landmarks_celeba": "list_landmarks_align_celeba.txt",
  }


if __name__ == "__main__":
  testing.test_main()

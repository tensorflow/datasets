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

"""Wikipedia-based Image Text (WIT) Dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.vision_language.wit import wit


class WitTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for wit dataset."""

  DATASET_CLASS = wit.Wit
  SPLITS = {
      'train': 3,
      'val': 1,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'train': ['train-00000-of-00009.tsv'],
      'val': ['val-00000-of-00005.tsv'],
      'test': ['test-00000-of-00005.tsv'],
  }


if __name__ == '__main__':
  tfds.testing.test_main()

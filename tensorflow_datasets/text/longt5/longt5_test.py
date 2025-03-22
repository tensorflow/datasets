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

"""Tests for the longt5 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.longt5 import longt5


class Longt5MediaSumTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for the media_sum config of the longt5 dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['media_sum']
  DATASET_CLASS = longt5.Longt5
  SKIP_CHECKSUMS = True  # All data is manually downloaded.
  SPLITS = {
      'train': 3,
      'val': 1,
      'test': 1,
  }


class Longt5NaturalQuestionsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for the natural_questions config of the longt5 dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['natural_questions']
  DATASET_CLASS = longt5.Longt5
  SPLITS = {
      'train': 3,
      'validation': 2,
  }

  DL_DOWNLOAD_RESULT = {
      'train': ['nq-train-00.jsonl.gz', 'nq-train-01.jsonl.gz'],
      'validation': ['nq-dev-00.jsonl.gz'],
  }


if __name__ == '__main__':
  tfds.testing.test_main()

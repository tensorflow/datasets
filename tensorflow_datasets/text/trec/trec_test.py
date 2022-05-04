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

"""trec dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.trec import trec


class TrecTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for trec dataset."""

  DATASET_CLASS = trec.Trec
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      "train": "train_5500.label",
      "test": "TREC_10.label",
  }


if __name__ == "__main__":
  tfds.testing.test_main()

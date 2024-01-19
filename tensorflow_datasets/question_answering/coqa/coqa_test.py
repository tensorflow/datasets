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

"""coqa dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering.coqa import coqa


class CoqaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for coqa dataset."""

  DATASET_CLASS = coqa.Coqa
  SPLITS = {
      "train": 1,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
      "train": "coqa-train-v1.0.json",
      "test": "coqa-dev-v1.0.json",
  }


if __name__ == "__main__":
  tfds.testing.test_main()

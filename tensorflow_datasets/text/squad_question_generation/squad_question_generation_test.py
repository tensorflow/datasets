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

"""squad_question_generation dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.squad_question_generation import squad_question_generation


class SquadQuestionGenerationSplitDuTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for squad_question_generation (split_du) dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ["split_du"]
  DATASET_CLASS = squad_question_generation.SquadQuestionGeneration
  SPLITS = {
      "train": 3,  # Number of fake train example
      "validation": 1,  # Number of fake dev example
      "test": 1,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = {
      "train": "split_du/train.json",
      "dev": "split_du/dev.json",
      "test": "split_du/test.json",
  }


class SquadQuestionGenerationSplitZhouTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for squad_question_generation (split_zhou) dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ["split_zhou"]
  DATASET_CLASS = squad_question_generation.SquadQuestionGeneration
  SPLITS = {
      "train": 3,  # Number of fake train example
      "validation": 1,  # Number of fake dev example
      "test": 1,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = {
      "train": "split_zhou/train-v1.1.json",
      "dev": "split_zhou/dev-v1.1.json",
      "mapping": "split_zhou/",
      "redistribute": "split_zhou/",
  }


if __name__ == "__main__":
  tfds.testing.test_main()

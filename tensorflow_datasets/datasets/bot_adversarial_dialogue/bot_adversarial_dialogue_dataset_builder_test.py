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

"""bot_adversarial_dialogue dataset."""

from tensorflow_datasets.datasets.bot_adversarial_dialogue import bot_adversarial_dialogue_dataset_builder
import tensorflow_datasets.public_api as tfds


class BotAdversarialDialogueDatasetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for dialogue_datasets config."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['dialogue_datasets']
  DATASET_CLASS = bot_adversarial_dialogue_dataset_builder.Builder
  SPLITS = {
      'train': 5,
      'valid': 3,
      'test': 2,
  }


class BotAdversarialDialogueHumanNonadvEvalDatasetTest(
    tfds.testing.DatasetBuilderTestCase
):
  """Tests for bot_adversarial_dialogue dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['human_nonadv_safety_eval']
  DATASET_CLASS = bot_adversarial_dialogue_dataset_builder.Builder
  SPLITS = {
      'test': 2,
  }


if __name__ == '__main__':
  tfds.testing.test_main()

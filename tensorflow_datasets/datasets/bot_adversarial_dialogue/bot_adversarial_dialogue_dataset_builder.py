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

"""bot_adversarial_dialogue dataset."""

import os
from typing import Any, Mapping

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils import bool_utils
import tensorflow_datasets.public_api as tfds


_BOT_ADVERSARIAL_DIALOGUE_DATASETS_VERSION = "v0.2"
_HUMAN_NONADV_SAFETY_EVAL_TESTSET_VERSION = "v0.1"

# Class labels in "dialogue_datasets" and "human_nonadv_safety_eval" configs.
_LABELS = tfds.features.ClassLabel(names=["__ok__", "__notok__"])

# Features which are common to all configs.
_COMMON_FEATURES = {
    "id": tfds.features.Text(doc="The id of the sample."),
    "text": tfds.features.Text(doc="The utterance to classify."),
    "episode_done": np.bool_,
    "labels": _LABELS,
}

# Config-specific features.
_DIALOGUE_FEATURES = {
    "dialogue_id": np.float32,
    "round_id": np.float32,
    "speaker_to_eval": tfds.features.Text(
        doc="The speaker of the utterances labeled."
    ),
    "bot_persona": tfds.features.Sequence(
        tfds.features.Text(doc="The persona impersonated by the bot.")
    ),
}
_CONFIG_FEATURES = {
    "dialogue_datasets": tfds.features.FeaturesDict(
        {**_DIALOGUE_FEATURES, **_COMMON_FEATURES}
    ),
    "human_nonadv_safety_eval": tfds.features.FeaturesDict(_COMMON_FEATURES),
}


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for bot_adversarial_dialogue dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name="dialogue_datasets",
          description=(
              "The dialogue datasets, divided in train, validation and test"
              " splits."
          ),
      ),
      tfds.core.BuilderConfig(
          name="human_nonadv_safety_eval",
          description=(
              "An human safety evaluation set evaluated by crowdsourced workers"
              " for offensiveness. "
          ),
      ),
  ]
  DEFAULT_CONFIG_NAME = "dialogue_datasets"

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=_CONFIG_FEATURES[self.builder_config.name],
        supervised_keys=None,
        homepage="https://github.com/facebookresearch/ParlAI/tree/main/parlai/tasks/bot_adversarial_dialogue",
        license="https://github.com/facebookresearch/ParlAI/blob/main/LICENSE",
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    bot_adversarial_dialogue_home = (
        "http://parl.ai/downloads/bot_adversarial_dialogue/"
    )

    if self.builder_config.name == "dialogue_datasets":
      path = dl_manager.download_and_extract(
          os.path.join(
              bot_adversarial_dialogue_home,
              f"dialogue_datasets_{_BOT_ADVERSARIAL_DIALOGUE_DATASETS_VERSION}.tar.gz",
          )
      )
      folder_name = "bot_adversarial_dialogue_datasets_with_persona"
      return {
          "train": self._generate_examples(
              path / f"{folder_name}/train.txt",
              split_name="train",
          ),
          "valid": self._generate_examples(
              path / f"{folder_name}/valid.txt",
              split_name="valid",
          ),
          "test": self._generate_examples(
              path / f"{folder_name}/test.txt",
              split_name="test",
          ),
      }

    else:
      path = dl_manager.download_and_extract(
          os.path.join(
              bot_adversarial_dialogue_home,
              f"human_nonadv_safety_eval_{_HUMAN_NONADV_SAFETY_EVAL_TESTSET_VERSION}.tar.gz",
          )
      )

      return {
          "test": self._generate_examples(
              path / "human_nonadv_safety_eval/test.txt",
              split_name="human_nonadv_safety_eval",
          ),
      }

  def _generate_examples(self, path, split_name=str):
    """Yields examples."""

    def _preprocess_row(row: str) -> str:
      """Preprocesses a dataset row using ParlAI format.

      This function is based on:
      https://github.com/facebookresearch/ParlAI/blob/9974b947fb2e801dc5608f495828532c2a714742/parlai/utils/misc.py#L639

      Args:
        row: An unprocessed row from the bot_adversarial_dialogue dataset.

      Returns:
        A processed row, in which special characters are properly formatted.
      """
      row = str(row)
      row = row.replace("\\t", "\t")
      row = row.replace("\\n", "\n")
      row = row.replace("__PIPE__", "|")
      return row

    def _get_row_features(row: str) -> Mapping[str, Any]:
      """Extracts dialogue features from a dataset row."""
      row_features = {}
      for field in row.split("\t"):
        key, value = field.split(":", maxsplit=1)
        row_features[key] = value
      return row_features

    # Indices to keep track of the dialogue turns as the conversation unfolds.
    previous_conversation_round = 0
    dialogue_id = 0

    with epath.Path(path).open() as f:
      for i, row in enumerate(f):
        example_id = f"{split_name}_{i}"
        cleaned_row = _preprocess_row(row)
        row_features = _get_row_features(cleaned_row)

        example = {
            "id": row_features.get("id", example_id),
            "labels": row_features["labels"],
            "episode_done": bool_utils.parse_bool(row_features["episode_done"]),
        }

        if self.builder_config.name == "dialogue_datasets":
          conversation_acts = row_features["text"].split("\n")
          conversation_len = len(conversation_acts)

          if conversation_len < previous_conversation_round:
            previous_conversation_round = 0
            dialogue_id += 1
          else:
            previous_conversation_round += 1

          # Remove the "your persona: ..." prefix from the bot persona
          # specifications.
          bot_persona = [
              str_.strip().split(": ", 1)[-1]
              for str_ in row_features["bot_persona"].strip().split("\n")
          ]

          example.update({
              "round_id": conversation_len - 1,
              "dialogue_id": dialogue_id,
              "text": conversation_acts[-1],
              "bot_persona": bot_persona,
              "speaker_to_eval": row_features["speaker_to_eval"],
          })

        else:
          example["text"] = row_features["text"]

        yield example_id, example

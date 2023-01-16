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

"""quac dataset."""

from __future__ import annotations

import json

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DATA_URL = "https://s3.amazonaws.com/my89public/quac/"

_MODULE = "QuAC"


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for quac dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "context": tfds.features.Text(),
            "followup": tfds.features.Text(),
            "yesno": tfds.features.Text(),
            "question": tfds.features.Text(),
            "answers": tfds.features.Sequence({
                "text": tfds.features.Text(),
                "answer_start": np.int32,
            }),
            "orig_answer": tfds.features.FeaturesDict({
                "text": tfds.features.Text(),
                "answer_start": np.int32,
            }),
            "section_title": tfds.features.Text(),
            "background": tfds.features.Text(),
            "title": tfds.features.Text(),
        }),
        homepage="https://quac.ai/",
        supervised_keys=("context", "answers"),
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerator."""

    expected_paths = dl_manager.download_and_extract({
        "train": _DATA_URL + "train_v0.2.json",
        "val": _DATA_URL + "val_v0.2.json",
    })

    return {
        "train": self._generate_examples(expected_paths["train"]),
        "validation": self._generate_examples(expected_paths["val"]),
    }

  def _generate_examples(self, filepath):
    """Yields examples based on filepath."""
    with epath.Path(filepath).open() as f:
      row = json.loads(f.readline())
      for data in row["data"]:
        section_title = data["section_title"]
        background = data["background"]
        tilte = data["title"]
        for paragraph in data["paragraphs"]:
          context = paragraph["context"]
          for qa in paragraph["qas"]:
            yield qa["id"], {
                "context": context,
                "followup": qa["followup"],
                "yesno": qa["yesno"],
                "question": qa["question"],
                "answers": qa["answers"],
                "orig_answer": qa["orig_answer"],
                "section_title": section_title,
                "background": background,
                "title": tilte,
            }

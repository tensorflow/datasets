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

"""BoolQ Dataset."""

from __future__ import annotations

import json

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_HOMEPAGE_URL = "https://github.com/google-research-datasets/boolean-questions"

_TRAIN_DOWNLOAD_URL = "https://storage.googleapis.com/boolq/train.jsonl"
_VALIDATION_DOWNLOAD_URL = "https://storage.googleapis.com/boolq/dev.jsonl"


class Builder(tfds.core.GeneratorBasedBuilder):
  """The Bool Q dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "question": tfds.features.Text(),
            "passage": tfds.features.Text(),
            "answer": np.bool_,
            "title": tfds.features.Text(),
        }),
        homepage=_HOMEPAGE_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_paths = dl_manager.download({
        "train": _TRAIN_DOWNLOAD_URL,
        "validation": _VALIDATION_DOWNLOAD_URL,
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "file_path": file_paths["train"],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "file_path": file_paths["validation"],
            },
        ),
    ]

  def _generate_examples(self, file_path):
    """Yields Examples.

    Args:
      file_path: Path of the train/validation json files

    Yields:
      The next examples
    """

    with epath.Path(file_path).open() as f:
      if file_path.suffix == ".jsonl":
        for index, line in enumerate(f):
          row = json.loads(line)
          key = index
          example = {
              "question": row["question"],
              "passage": row["passage"],
              "answer": row["answer"],
              "title": row["title"],
          }
          yield key, example

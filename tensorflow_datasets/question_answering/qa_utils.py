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

"""Shared utilities for QA datasets."""
from __future__ import annotations

import json

from absl import logging
from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds


def squadlike_features():
  return tfds.features.FeaturesDict({
      "id": np.str_,
      "title": tfds.features.Text(),
      "context": tfds.features.Text(),
      "question": tfds.features.Text(),
      "answers": tfds.features.Sequence({
          "text": tfds.features.Text(),
          "answer_start": np.int32,
      }),
  })


def generate_squadlike_examples(filepath):
  """Parses a SQuAD-like JSON, yielding examples with `squadlike_features`."""
  logging.info("generating examples from = %s", filepath)

  # We first re-group the answers, which may be flattened (e.g., by XTREME).
  qas = {}
  with epath.Path(filepath).open() as f:
    squad = json.load(f)
    for article in squad["data"]:
      title = article.get("title", "")
      for paragraph in article["paragraphs"]:
        context = paragraph["context"]
        for qa in paragraph["qas"]:
          qa["title"] = title
          qa["context"] = context
          id_ = qa["id"]
          if id_ in qas:
            qas[id_]["answers"].extend(qa["answers"])
          else:
            qas[id_] = qa

    for id_, qa in qas.items():
      answer_starts = [answer["answer_start"] for answer in qa["answers"]]
      answers = [answer["text"] for answer in qa["answers"]]
      yield id_, {
          "title": qa["title"],
          "context": qa["context"],
          "question": qa["question"],
          "id": id_,
          "answers": {
              "answer_start": answer_starts,
              "text": answers,
          },
      }

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

"""Reddit dataset using tldr as summaries."""

from __future__ import annotations

import json
import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://zenodo.org/record/1043504/files/corpus-webis-tldr-17.zip?download=1"

_DOCUMENT = "content"
_SUMMARY = "summary"
_ADDITIONAL_FEATURES = [
    "author",
    "body",
    "normalizedBody",
    "subreddit",
    "subreddit_id",
    "id",
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """Reddit Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {k: np.str_ for k in _ADDITIONAL_FEATURES + [_DOCUMENT, _SUMMARY]}
        ),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/webis-de/webis-tldr-17-corpus",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": os.path.join(dl_path, "corpus-webis-tldr-17.json")
            },
        )
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    with tf.io.gfile.GFile(path, "rb") as f:
      for i, line in enumerate(f):
        # possible keys are:
        #   author: string (nullable = true)
        #   body: string (nullable = true)
        #   normalizedBody: string (nullable = true)
        #   content: string (nullable = true)
        #   content_len: long (nullable = true)
        #   summary: string (nullable = true)
        #   summary_len: long (nullable = true)
        #   id: string (nullable = true)
        #   subreddit: string (nullable = true)
        #   subreddit_id: string (nullable = true)
        #   title: string (nullable = true)
        d = json.loads(line)
        if _SUMMARY in d and _DOCUMENT in d:
          yield i, {
              k: d.get(k, "")
              for k in _ADDITIONAL_FEATURES + [_DOCUMENT, _SUMMARY]
          }

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

"""real_toxicity_prompts dataset."""
import json
from etils import epath
import numpy as np

import tensorflow_datasets.public_api as tfds


# Features describing toxicity annotations of prompts and continuations.
_TOXIC_FEATURES = tfds.features.FeaturesDict({
    "text": tfds.features.Text(),
    "profanity": np.float32,
    "sexually_explicit": np.float32,
    "identity_attack": np.float32,
    "flirtation": np.float32,
    "threat": np.float32,
    "insult": np.float32,
    "severe_toxicity": np.float32,
    "toxicity": np.float32,
})


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for real_toxicity_prompts dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""

    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "filename": tfds.features.Text(),
            "begin": np.int32,
            "end": np.int32,
            "challenging": np.bool_,
            "prompt": _TOXIC_FEATURES,
            "continuation": _TOXIC_FEATURES,
        }),
        supervised_keys=None,
        homepage="https://github.com/allenai/real-toxicity-prompts",
        license="https://github.com/allenai/real-toxicity-prompts/blob/master/LICENSE",
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        "https://ai2-public-datasets.s3.amazonaws.com/realtoxicityprompts/realtoxicityprompts-data.tar.gz"
    )

    return {
        "train": self._generate_examples(
            path / "realtoxicityprompts-data/prompts.jsonl"
        ),
    }

  def _generate_examples(self, path):
    """Yields examples."""

    def _get_toxic_features(row_toxic_data):
      return {f: row_toxic_data[f] for f in _TOXIC_FEATURES.keys()}

    def _get_row_features(row_data):
      row_features = {
          "filename": row_data["filename"],
          "begin": row_data["begin"],
          "end": row_data["end"],
          "challenging": row_data["challenging"],
          "prompt": _get_toxic_features(row_data["prompt"]),
          "continuation": _get_toxic_features(row_data["continuation"]),
      }
      return row_features

    with epath.Path(path).open() as f:
      for i, row in enumerate(f):
        row_data = json.loads(row)
        yield i, _get_row_features(row_data)

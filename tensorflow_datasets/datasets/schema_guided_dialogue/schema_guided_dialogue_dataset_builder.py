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

"""schema_guided_dialogue dataset."""

from __future__ import annotations

import json

import numpy as np
import tensorflow_datasets.public_api as tfds

_DATA_URL = (
    "https://github.com/google-research-datasets/dstc8-schema-guided-dialogue"
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for schema_guided_dialogue dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            # The previous system utterance if one exists.
            "utterances": tfds.features.Sequence(tfds.features.Text()),
            # TODO(arunchaganty): include frame and state annotations
            "first_speaker": tfds.features.ClassLabel(names=["USER", "SYSTEM"]),
            "metadata": {
                "services": tfds.features.Sequence(
                    {
                        "name": np.str_,
                        # TODO(arunchaganty): include service definitions
                    }
                )
            },
        }),
        supervised_keys=None,
        homepage=_DATA_URL,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        _DATA_URL + "/archive/refs/heads/master.zip"
    )

    return {
        "train": self._generate_examples(
            path / "dstc8-schema-guided-dialogue-master" / "train"
        ),
        "dev": self._generate_examples(
            path / "dstc8-schema-guided-dialogue-master" / "dev"
        ),
        "test": self._generate_examples(
            path / "dstc8-schema-guided-dialogue-master" / "test"
        ),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # TODO(arunchaganty): load the services schemas from "schema.json".

    for f in path.glob("*.json"):
      if f.name.endswith("schema.json"):
        continue

      for datum in json.loads(f.read_text()):
        id_ = datum["dialogue_id"]
        utterances = [turn["utterance"] for turn in datum["turns"]]
        first_speaker = datum["turns"][0]["speaker"]

        yield id_, {
            "utterances": utterances,
            "first_speaker": first_speaker,
            # TODO(arunchaganty): include frame and state annotations
            "metadata": {
                # TODO(arunchaganty): include schema definitions
                "services": [
                    {
                        "name": service,
                    }
                    for service in datum["services"]
                ],
            },
        }

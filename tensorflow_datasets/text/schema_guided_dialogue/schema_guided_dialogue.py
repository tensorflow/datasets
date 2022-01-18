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

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The Schema-Guided Dialogue (SGD) dataset consists of over 20k annotated
multi-domain, task-oriented conversations between a human and a virtual
assistant. These conversations involve interactions with services and APIs
spanning 20 domains, ranging from banks and events to media, calendar, travel,
and weather. For most of these domains, the dataset contains multiple different
APIs, many of which have overlapping functionalities but different interfaces,
which reflects common real-world scenarios. The wide range of available
annotations can be used for intent prediction, slot filling, dialogue state
tracking, policy imitation learning, language generation, user simulation
learning, among other tasks in large-scale virtual assistants. Besides these,
the dataset has unseen domains and services in the evaluation set to quantify
the performance in zero-shot or few shot settings.
"""

_CITATION = """
@article{rastogi2019towards,
  title={Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset},
  author={Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
  journal={arXiv preprint arXiv:1909.05855},
  year={2019}
}
"""

_DATA_URL = "https://github.com/google-research-datasets/dstc8-schema-guided-dialogue"


class SchemaGuidedDialogue(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for schema_guided_dialogue dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # The previous system utterance if one exists.
            "utterances": tfds.features.Sequence(tfds.features.Text()),
            # TODO(arunchaganty): include frame and state annotations
            "first_speaker": tfds.features.ClassLabel(names=["USER", "SYSTEM"]),
            "metadata": {
                "services":
                    tfds.features.Sequence({
                        "name": tf.string,
                        # TODO(arunchaganty): include service definitions
                    })
            }
        }),
        supervised_keys=None,
        homepage=_DATA_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_DATA_URL +
                                           "/archive/refs/heads/master.zip")

    return {
        "train":
            self._generate_examples(
                path / "dstc8-schema-guided-dialogue-master" / "train"),
        "dev":
            self._generate_examples(
                path / "dstc8-schema-guided-dialogue-master" / "dev"),
        "test":
            self._generate_examples(
                path / "dstc8-schema-guided-dialogue-master" / "test"),
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
                "services": [{
                    "name": service,
                } for service in datum["services"]],
            },
        }

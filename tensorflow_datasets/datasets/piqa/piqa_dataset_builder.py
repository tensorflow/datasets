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

"""Physical Interaction QA Dataset."""

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_PIQA_URL = "https://storage.googleapis.com/ai2-mosaic/public/physicaliqa/physicaliqa-train-dev.zip"


def _read_json(json_path):
  data = []
  with epath.Path(json_path).open() as f:
    for line in f:
      if line:
        data.append(json.loads(line))
  return data


class Builder(tfds.core.GeneratorBasedBuilder):
  """Physical Interaction QA."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "goal": tfds.features.Text(),
            "sol1": tfds.features.Text(),
            "sol2": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=2),
        }),
        homepage="https://leaderboard.allenai.org/physicaliqa/submissions/get-started",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extracted_path = dl_manager.download_and_extract(_PIQA_URL)

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_path": os.path.join(
                    extracted_path, "physicaliqa-train-dev/train.jsonl"
                ),
                "label_path": os.path.join(
                    extracted_path, "physicaliqa-train-dev/train-labels.lst"
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "data_path": os.path.join(
                    extracted_path, "physicaliqa-train-dev/dev.jsonl"
                ),
                "label_path": os.path.join(
                    extracted_path, "physicaliqa-train-dev/dev-labels.lst"
                ),
            },
        ),
    ]

  def _generate_examples(self, data_path, label_path):
    """Yields examples."""

    examples = _read_json(data_path)
    labels = _read_json(label_path)

    data = zip(examples, labels)

    for index, (example, label) in enumerate(data):
      example["label"] = label
      yield index, example

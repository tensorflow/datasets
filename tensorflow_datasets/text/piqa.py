# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Bisk2020,
  author = {Yonatan Bisk and Rowan Zellers and
            Ronan Le Bras and Jianfeng Gao
            and Yejin Choi},
  title = {PIQA: Reasoning about Physical Commonsense in
           Natural Language},
  booktitle = {Thirty-Fourth AAAI Conference on
               Artificial Intelligence},
  year = {2020},
}
"""

_DESCRIPTION = """
Physical IQa: Physical Interaction QA, a new commonsense QA benchmark for naive physics
reasoning focusing on how we interact with everyday objects in everyday situations. This
dataset focuses on affordances of objects, i.e., what actions each physical object affords
(e.g., it is possible to use a shoe as a doorstop), and what physical interactions a group
of objects afford (e.g., it is possible to place an apple on top of a book, but not the
other way around). The dataset requires reasoning about both the prototypical use of
objects (e.g., shoes are used for walking) and non-prototypical but practically plausible
use of objects (e.g., shoes can be used as a doorstop). The dataset includes 20,000 QA
pairs that are either multiple-choice or true/false questions.
"""

_PIQA_URL = "https://storage.googleapis.com/ai2-mosaic/public/physicaliqa/physicaliqa-train-dev.zip"


def _read_json(json_path):
  data = []
  with tf.io.gfile.GFile(json_path) as f:
    for line in f:
      if line:
        data.append(json.loads(line))
  return data


class PIQA(tfds.core.GeneratorBasedBuilder):
  """Physical Interaction QA."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "goal": tfds.features.Text(),
            "sol1": tfds.features.Text(),
            "sol2": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=2),
        }),
        homepage="https://leaderboard.allenai.org/physicaliqa/submissions/get-started",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extracted_path = dl_manager.download_and_extract(_PIQA_URL)

    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_path":
                    os.path.join(extracted_path,
                                 "physicaliqa-train-dev/train.jsonl"),
                "label_path":
                    os.path.join(extracted_path,
                                 "physicaliqa-train-dev/train-labels.lst"),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "data_path":
                    os.path.join(extracted_path,
                                 "physicaliqa-train-dev/dev.jsonl"),
                "label_path":
                    os.path.join(extracted_path,
                                 "physicaliqa-train-dev/dev-labels.lst"),
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

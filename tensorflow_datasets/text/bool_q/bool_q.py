# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{clark2019boolq,
  title =     {BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions},
  author =    {Clark, Christopher and Lee, Kenton and Chang, Ming-Wei, and Kwiatkowski, Tom and Collins, Michael, and Toutanova, Kristina},
  booktitle = {NAACL},
  year =      {2019},
}
"""

_DESCRIPTION = """
BoolQ is a question answering dataset for yes/no questions containing 15942 examples.
These questions are naturally occurring, they are generated in unprompted and unconstrained settings.

Each example is a triplet of (question, passage, answer),
with the title of the page as optional additional context.
The text-pair classification setup is similar to existing
natural language inference tasks.
"""

_HOMEPAGE_URL = "https://github.com/google-research-datasets/boolean-questions"

_TRAIN_DOWNLOAD_URL = "https://storage.googleapis.com/boolq/train.jsonl"
_VALIDATION_DOWNLOAD_URL = "https://storage.googleapis.com/boolq/dev.jsonl"


class BoolQ(tfds.core.GeneratorBasedBuilder):
  """The Bool Q dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "question": tfds.features.Text(),
            "passage": tfds.features.Text(),
            "answer": tf.bool,
            "title": tfds.features.Text(),
        }),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
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
        )
    ]

  def _generate_examples(self, file_path):
    """Yields Examples.

    Args:
      file_path: Path of the train/validation json files

    Yields:
      The next examples
    """

    with tf.io.gfile.GFile(file_path) as f:
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

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

"""ai2_arc dataset, with IR retrieved sentences from Aristo Corpus."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_HOMEPAGE = "https://allenai.org/data/arc"
_URL = "http://aristo-data.s3.amazonaws.com/custom-datasets/ARC-IR10V8.zip"


class Ai2ArcWithIRConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Ai2ARCWithIR."""

  def __init__(self, **kwargs):
    """BuilderConfig for Ai2ArcWithIR.

    Args:
      **kwargs: keyword arguments forwarded to super.
    """
    super(Ai2ArcWithIRConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs
    )


class Builder(tfds.core.GeneratorBasedBuilder):
  """The AI2 ARC dataset with Information Retrieval.

  Compared to the normal AI2 corpus, this adds a paragraph containing retrieved
  facts similar to the question + answers.

  Retrieved sentences are obtained following the UnifiedQA paper:
  https://arxiv.org/abs/2005.00700
  """

  BUILDER_CONFIGS = [
      Ai2ArcWithIRConfig(
          name="ARC-Challenge-IR",
          description="""\
          Challenge Set of 2590 "hard" questions (those that both a retrieval and a co-occurrence method fail to answer correctly)
          """,
      ),
      Ai2ArcWithIRConfig(
          name="ARC-Easy-IR",
          description="""\
          Easy Set of 5197 questions for the ARC Challenge.
          """,
      ),
  ]

  def _info(self):
    # Most questions have four possible answers, but a few have five.
    options = ["A", "B", "C", "D", "E"]
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "question": tfds.features.Text(),
            "choices": tfds.features.Sequence({
                "text": tfds.features.Text(),
                "label": tfds.features.ClassLabel(names=options),
            }),
            "answerKey": tfds.features.ClassLabel(names=options),
            "paragraph": tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage=_HOMEPAGE,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract(_URL)
    base_path = os.path.join(dl_dir, "ARC-IR10V8")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": os.path.join(base_path, "train.jsonl"),
                "split": self.builder_config.name,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "filepath": os.path.join(base_path, "dev.jsonl"),
                "split": self.builder_config.name,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepath": os.path.join(base_path, "test.jsonl"),
                "split": self.builder_config.name,
            },
        ),
    ]

  def _generate_examples(self, filepath: str, split: str):
    """Yields examples."""
    # Generally labels are in the format "A", "B", "C", "D" but sometimes
    # they are in the format "1", "2", "3", "4". We convert the later to the
    # former for consistency.
    n_to_l = dict(zip("1 2 3 4 5".split(), "A B C D E".split()))
    # IDs to keep:
    # Those that start with ARCEZ_ for the easy set
    # Those that start with ARCCH_ for the challenge set
    prefix = {"ARC-Easy-IR": "ARCEZ_", "ARC-Challenge-IR": "ARCCH_"}[split]
    with epath.Path(filepath).open() as f:
      for row in f:
        data = json.loads(row)
        if not data["id"].startswith(prefix):
          continue
        answerkey = n_to_l.get(data["answerKey"], data["answerKey"])
        id_ = data["id"].replace(prefix, "")
        question = data["question"]["stem"]
        choices = data["question"]["choices"]
        text_choices = [choice["text"] for choice in choices]
        label_choices = [
            n_to_l.get(choice["label"], choice["label"]) for choice in choices
        ]
        paragraph = data["para"]
        yield id_, {
            "id": id_,
            "answerKey": answerkey,
            "question": question,
            "choices": {"text": text_choices, "label": label_choices},
            "paragraph": paragraph,
        }

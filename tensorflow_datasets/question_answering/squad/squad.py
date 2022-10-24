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

"""SQUAD: The Stanford Question Answering Dataset."""

from __future__ import annotations

import json
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_CITATION = """\
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
"""

_DESCRIPTION = """\
Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable.
"""

_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
_HOMEPAGE_URL = "https://rajpurkar.github.io/SQuAD-explorer/"


def _v2_features():
  return tfds.features.FeaturesDict({
      "id":
          tf.string,
      "title":
          tfds.features.Text(),
      "context":
          tfds.features.Text(),
      "plausible_answers":
          tfds.features.Sequence({
              "text": tfds.features.Text(),
              "answer_start": tf.int32,
          }),
      "question":
          tfds.features.Text(),
      "is_impossible":
          tf.bool,
      "answers":
          tfds.features.Sequence({
              "text": tfds.features.Text(),
              "answer_start": tf.int32,
          }),
  })


def _generate_v2_examples(filepath):
  """Returns v2 examples."""
  with epath.Path(filepath).open() as f:
    squad = json.load(f)
    for article in squad["data"]:
      title = article.get("title", "")
      for paragraph in article["paragraphs"]:
        context = paragraph["context"]
        for qa in paragraph["qas"]:
          id_ = qa["id"]

          #  Not all examples have plausible answers
          if "plausible_answers" not in qa:
            qa["plausible_answers"] = []

          question = qa["question"]
          is_impossible = qa["is_impossible"]

          plausible_answer_starts = [
              plausible_answer["answer_start"]
              for plausible_answer in qa["plausible_answers"]
          ]
          plausible_answers = [
              plausible_answer["text"]
              for plausible_answer in qa["plausible_answers"]
          ]

          answer_starts = [answer["answer_start"] for answer in qa["answers"]]
          answers = [answer["text"] for answer in qa["answers"]]

          yield id_, {
              "title": title,
              "context": context,
              "question": question,
              "id": id_,
              "plausible_answers": {
                  "answer_start": plausible_answer_starts,
                  "text": plausible_answers,
              },
              "answers": {
                  "answer_start": answer_starts,
                  "text": answers,
              },
              "is_impossible": is_impossible,
          }


class SquadConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SQUAD."""

  def __init__(self, *, train_file, dev_file, **kwargs):

    super(SquadConfig, self).__init__(**kwargs)
    self.train_file = train_file
    self.dev_file = dev_file


class Squad(tfds.core.GeneratorBasedBuilder):
  """SQUAD: The Stanford Question Answering Dataset."""

  BUILDER_CONFIGS = [
      SquadConfig(
          name="v1.1",
          description="Version 1.1.0 of SQUAD",
          train_file="train-v1.1.json",
          dev_file="dev-v1.1.json",
      ),
      SquadConfig(
          name="v2.0",
          description="Version 2.0.0 of SQUAD",
          train_file="train-v2.0.json",
          dev_file="dev-v2.0.json",
      ),
  ]

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0":
          "Fixes issue with small number of examples (19) where answer spans "
          "are misaligned due to context white-space removal.",
  }

  def _info(self):

    if self.builder_config.name == "v1.1":
      features_dict = qa_utils.squadlike_features()
    elif self.builder_config.name == "v2.0":
      features_dict = _v2_features()
    else:
      raise AssertionError("Dataset version should be either 1.1 or 2.0")

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features_dict,
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    urls_to_download = {
        "train": os.path.join(_URL, self.builder_config.train_file),
        "dev": os.path.join(_URL, self.builder_config.dev_file)
    }
    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepath": downloaded_files["train"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": downloaded_files["dev"]}),
    ]

  def _generate_examples(self, filepath):

    if self.builder_config.name == "v1.1":
      return qa_utils.generate_squadlike_examples(filepath)
    return _generate_v2_examples(filepath)

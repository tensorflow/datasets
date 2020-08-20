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

"""SQUAD: The Stanford Question Answering Dataset."""

import os

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


class SquadConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SQUAD."""


class Squad(tfds.core.GeneratorBasedBuilder):
  """SQUAD: The Stanford Question Answering Dataset. Version 1.1."""
  _URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
  _DEV_FILE = "dev-v1.1.json"
  _TRAINING_FILE = "train-v1.1.json"

  BUILDER_CONFIGS = [
      SquadConfig(
          name="plain_text",
          version=tfds.core.Version(
              "1.0.0",
              "New split API (https://tensorflow.org/datasets/splits)"),
          description="Plain text",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=qa_utils.SQUADLIKE_FEATURES,
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        homepage="https://rajpurkar.github.io/SQuAD-explorer/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    urls_to_download = {
        "train": os.path.join(self._URL, self._TRAINING_FILE),
        "dev": os.path.join(self._URL, self._DEV_FILE)
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
    return qa_utils.generate_squadlike_examples(filepath)

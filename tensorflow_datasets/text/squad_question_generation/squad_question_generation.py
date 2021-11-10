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

"""squad_question_generation dataset."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_CITATION = """\
@article{zhou2017neural,
  title={Neural Question Generation from Text: A Preliminary Study},
  author={Zhou, Qingyu and Yang, Nan and Wei, Furu and Tan, Chuanqi and Bao, Hangbo and Zhou, Ming},
  journal={arXiv preprint arXiv:1704.01792},
  year={2017}
}
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
Question generation using squad dataset and data split described in
'Neural Question Generation from Text: A Preliminary Study'.
"""

_URLS = {
    "train":
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json",
    "dev":
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json",
    "mapping":
        "https://res.qyzhou.me/qas_id_in_squad.zip",
}
_HOMEPAGE_URL = "https://github.com/magic282/NQG"


class SquadQuestionGeneration(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for squad_question_generation dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial build.",
  }

  def _info(self):
    """Returns the dataset metadata."""
    features_dict = qa_utils.SQUADLIKE_FEATURES
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features_dict,
        supervised_keys=("context", "question"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(_URLS)
    mapping_dir = os.path.join(dl_paths["mapping"], "qas_id_in_squad")
    return {
        tfds.Split.TRAIN:
            self._generate_examples(dl_paths["train"],
                                    os.path.join(mapping_dir, "train.txt.id")),
        tfds.Split.VALIDATION:
            self._generate_examples(
                dl_paths["dev"],
                os.path.join(mapping_dir, "dev.txt.shuffle.dev.id")),
        tfds.Split.TEST:
            self._generate_examples(
                dl_paths["dev"],
                os.path.join(mapping_dir, "dev.txt.shuffle.test.id")),
    }

  def _generate_examples(self, data_path: str, mapping_path: str):
    """Yields examples."""
    with tf.io.gfile.GFile(mapping_path, "r") as f:
      ids = set(f.read().splitlines())
    for k, ex in qa_utils.generate_squadlike_examples(data_path):
      if k in ids:
        yield k, ex

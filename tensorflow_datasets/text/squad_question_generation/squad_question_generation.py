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
Question generation using squad dataset and data split described in 'Neural
Question Generation from Text: A Preliminary Study' (Zhou et al, 2017).
"""

_URLS = {
    "train":
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json",
    "dev":
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json",
    "mapping":
        "https://res.qyzhou.me/qas_id_in_squad.zip",
    "redistribute":
        "https://res.qyzhou.me/redistribute.zip"
}
_HOMEPAGE_URL = "https://github.com/magic282/NQG"


_CONTEXT_SENTENCE = "context_sentence"
_CONTEXT_PASSAGE = "context_passage"
_ANSWER = "answer"
_QUESTION = "question"


class SquadQuestionGeneration(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for squad_question_generation dataset."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "1.0.0":
          """
          Initial build with unique SQuAD QAS ids in each split, using
          passage-level context.
          """,
      "2.0.0":
          """
          Matches the original split of (Zhou et al, 2017), allows both
          sentence- and passage-level contexts, and uses answers from
          (Zhou et al, 2017).
          """,
  }

  def _info(self):
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _CONTEXT_SENTENCE: tfds.features.Text(),
            _CONTEXT_PASSAGE: tfds.features.Text(),
            _ANSWER: tfds.features.Text(),
            _QUESTION: tfds.features.Text(),
        }),
        supervised_keys=(_CONTEXT_PASSAGE, _QUESTION),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(_URLS)
    mapping_dir = os.path.join(dl_paths["mapping"], "qas_id_in_squad")
    redistribute_raw_dir = os.path.join(dl_paths["redistribute"],
                                        "redistribute/raw")

    return {
        tfds.Split.TRAIN:
            self._generate_examples(
                dl_paths["train"], os.path.join(mapping_dir, "train.txt.id"),
                os.path.join(redistribute_raw_dir, "train.txt")),
        tfds.Split.VALIDATION:
            self._generate_examples(
                dl_paths["dev"],
                os.path.join(mapping_dir, "dev.txt.shuffle.dev.id"),
                os.path.join(redistribute_raw_dir, "dev.txt.shuffle.dev")),
        tfds.Split.TEST:
            self._generate_examples(
                dl_paths["dev"],
                os.path.join(mapping_dir, "dev.txt.shuffle.test.id"),
                os.path.join(redistribute_raw_dir, "dev.txt.shuffle.test")),
    }

  def _generate_examples(self, squad_data_path: str, mapping_path: str,
                         qgen_data_path: str):
    r"""Yields question generation examples.

    Args:
      squad_data_path: Path to SQuAD json file.
      mapping_path:  File with SQuAD map id for the example in Zhou et al.
        splits.
      qgen_data_path:  File with examples in "TokenizedInputSentence\t
        AnswerStartAndEndPosition\tParsingTreeOfInputSentence\t
        PoSTagOfInputSentence\tNERTagsOfInputSentence\tTokenizedQuestion\t
        UntokenizedInputSentence\tAnswerStartCharIndex\tAnswer\t
        UntokenizedQuestion" format per line.

    Yields:
      key and example dict.
    """
    squad_data = {}
    for k, ex in qa_utils.generate_squadlike_examples(squad_data_path):
      squad_data[k] = ex

    with tf.io.gfile.GFile(mapping_path, "r") as mapping_file:
      with tf.io.gfile.GFile(qgen_data_path, "r") as qgen_data_file:
        for (ex_id, (squad_id, qgen_data)) in enumerate(
            zip(mapping_file.read().splitlines(),
                qgen_data_file.read().splitlines())):
          (_, _, _, _, _, _, context_sentence, _, answer,
           question) = qgen_data.split("\t")
          context_passage = squad_data[squad_id]["context"]
          yield str(ex_id).zfill(7), {
              _CONTEXT_SENTENCE: context_sentence,
              _CONTEXT_PASSAGE: context_passage,
              _ANSWER: answer,
              _QUESTION: question
          }

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

"""squad_question_generation dataset."""

import json
import os
import textwrap

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_CITATION_DU_ET_AL = textwrap.dedent(
    """\
@inproceedings{du-etal-2017-learning,
    title = "Learning to Ask: Neural Question Generation for Reading Comprehension",
    author = "Du, Xinya  and Shao, Junru  and Cardie, Claire",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1123",
    doi = "10.18653/v1/P17-1123",
    pages = "1342--1352",
}
"""
)

_DATA_URLS_DU_ET_AL = {
    "train": "https://raw.githubusercontent.com/xinyadu/nqg/master/data/raw/train.json",
    "dev": (
        "https://raw.githubusercontent.com/xinyadu/nqg/master/data/raw/dev.json"
    ),
    "test": "https://raw.githubusercontent.com/xinyadu/nqg/master/data/raw/test.json",
}

_HOMEPAGE_URL_DU_ET_AL = "https://github.com/xinyadu/nqg"

_CITATION_ZHOU_ET_AL = textwrap.dedent(
    """\
@inproceedings{du-etal-2017-learning,
    title = "Learning to Ask: Neural Question Generation for Reading Comprehension",
    author = "Du, Xinya  and Shao, Junru  and Cardie, Claire",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P17-1123",
    doi = "10.18653/v1/P17-1123",
    pages = "1342--1352",
}
"""
)

_DATA_URLS_ZHOU_ET_AL = {
    "train": (
        "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json"
    ),
    "dev": "https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json",
    "mapping": "https://res.qyzhou.me/qas_id_in_squad.zip",
    "redistribute": "https://res.qyzhou.me/redistribute.zip",
}

_HOMEPAGE_URL_ZHOU_ET_AL = "https://github.com/magic282/NQG"

_CITATION_SQUAD = textwrap.dedent(
    """\
@inproceedings{rajpurkar-etal-2016-squad,
    title = "{SQ}u{AD}: 100,000+ Questions for Machine Comprehension of Text",
    author = "Rajpurkar, Pranav  and Zhang, Jian  and Lopyrev, Konstantin  and Liang, Percy",
    booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2016",
    address = "Austin, Texas",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D16-1264",
    doi = "10.18653/v1/D16-1264",
    pages = "2383--2392",
}
"""
)

_DESCRIPTION = """\
Question generation using squad dataset using data splits described in 'Neural
Question Generation from Text: A Preliminary Study' (Zhou et al, 2017) and
'Learning to Ask: Neural Question Generation for Reading Comprehension' (Du et
al, 2017).
"""

_CONTEXT_SENTENCE = "context_sentence"
_CONTEXT_PASSAGE = "context_passage"
_ANSWER = "answer"
_QUESTION = "question"


class SquadQuestionGenerationConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Squad Question Generation."""

  def __init__(self, *, features, data_urls, citation, **kwargs):
    """BuilderConfig for Squad Question Generation.

    Args:
      features: `tfds.features.FeaturesDict`, specific feature dict for the
        dataset.
      data_urls: `dict`, urls to download the files from
      citation: `string`, citation for the data set
      **kwargs: keyword arguments forwarded to super.
    """
    super(SquadQuestionGenerationConfig, self).__init__(**kwargs)
    self.features = features
    self.data_urls = data_urls
    self.citation = citation


class SquadQuestionGeneration(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for squad_question_generation dataset."""

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "1.0.0": """
          Initial build with unique SQuAD QAS ids in each split, using
          passage-level context (Zhou et al, 2017).
          """,
      "2.0.0": """
          Matches the original split of (Zhou et al, 2017), allows both
          sentence- and passage-level contexts, and uses answers from
          (Zhou et al, 2017).
          """,
      "3.0.0": """
          Added the split of (Du et al, 2017) also.
          """,
  }
  BUILDER_CONFIGS = [
      SquadQuestionGenerationConfig(
          name="split_du",
          description=textwrap.dedent(
              """\
          Answer independent question generation from passage-level contexts
          (Du et al, 2017).
          """
          ),
          features=tfds.features.FeaturesDict({
              _CONTEXT_PASSAGE: tfds.features.Text(),
              _ANSWER: tfds.features.Text(),
              _QUESTION: tfds.features.Text(),
          }),
          data_urls=_DATA_URLS_DU_ET_AL,
          citation=_CITATION_DU_ET_AL,
      ),
      SquadQuestionGenerationConfig(
          name="split_zhou",
          description=textwrap.dedent(
              """\
          Answer-span dependent question generation from sentence- and
          passage-level contexts (Zhou et al, 2017).
          """
          ),
          features=tfds.features.FeaturesDict({
              _CONTEXT_SENTENCE: tfds.features.Text(),
              _CONTEXT_PASSAGE: tfds.features.Text(),
              _ANSWER: tfds.features.Text(),
              _QUESTION: tfds.features.Text(),
          }),
          data_urls=_DATA_URLS_ZHOU_ET_AL,
          citation=_CITATION_ZHOU_ET_AL,
      ),
  ]

  def _info(self):
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(self.builder_config.features),
        homepage=_HOMEPAGE_URL_DU_ET_AL + "\n" + _CITATION_ZHOU_ET_AL,
        citation=self.builder_config.citation + "\n" + _CITATION_SQUAD,
        supervised_keys=(_CONTEXT_PASSAGE, _QUESTION),
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract(self.builder_config.data_urls)

    if self.builder_config.name == "split_du":
      return {
          tfds.Split.TRAIN: self._generate_examples(dl_paths["train"]),
          tfds.Split.VALIDATION: self._generate_examples(dl_paths["dev"]),
          tfds.Split.TEST: self._generate_examples(dl_paths["test"]),
      }
    elif self.builder_config.name == "split_zhou":
      mapping_dir = os.path.join(dl_paths["mapping"], "qas_id_in_squad")
      redistribute_raw_dir = os.path.join(
          dl_paths["redistribute"], "redistribute/raw"
      )
      return {
          tfds.Split.TRAIN: self._generate_examples(
              dl_paths["train"],
              os.path.join(mapping_dir, "train.txt.id"),
              os.path.join(redistribute_raw_dir, "train.txt"),
          ),
          tfds.Split.VALIDATION: self._generate_examples(
              dl_paths["dev"],
              os.path.join(mapping_dir, "dev.txt.shuffle.dev.id"),
              os.path.join(redistribute_raw_dir, "dev.txt.shuffle.dev"),
          ),
          tfds.Split.TEST: self._generate_examples(
              dl_paths["dev"],
              os.path.join(mapping_dir, "dev.txt.shuffle.test.id"),
              os.path.join(redistribute_raw_dir, "dev.txt.shuffle.test"),
          ),
      }

  def _generate_examples(
      self, squad_data_path, mapping_path=None, qgen_data_path=None
  ):
    r"""Yields question generation examples.

    Args:
      squad_data_path: Path to SQuAD json file.
      mapping_path:  File with SQuAD map id for the example in Zhou et al.
        splits.
      qgen_data_path:  File with examples in "TokenizedInputSentence\t
        AnswerStartAndEndPosition\tParsingTreeOfInputSentence\t
        PoSTagOfInputSentence\tNERTagsOfInputSentence\tTokenizedQuestion\t
        UntokenizedInputSentence\tAnswerStartCharIndex\tAnswer\t
        UntokenizedQuestion" format per line, for the Zhou et al. splits.

    Yields:
      key and example dict.
    """
    if self.builder_config.name == "split_du":
      # The file format slightly differs from the original SQuAD JSON format.
      with epath.Path(squad_data_path).open() as f:
        squad_data = json.load(f)
        for article in squad_data:
          for paragraph in article["paragraphs"]:
            context = paragraph["context"]
            for qa in paragraph["qas"]:
              yield qa["id"], {
                  _CONTEXT_PASSAGE: context,
                  _ANSWER: qa["answers"][0]["text"],
                  _QUESTION: qa["question"],
              }
    elif self.builder_config.name == "split_zhou":
      squad_data = {}
      for k, ex in qa_utils.generate_squadlike_examples(squad_data_path):
        squad_data[k] = ex
      with tf.io.gfile.GFile(mapping_path, "r") as mapping_file:
        with tf.io.gfile.GFile(qgen_data_path, "r") as qgen_data_file:
          for ex_id, (squad_id, qgen_data) in enumerate(
              zip(
                  mapping_file.read().splitlines(),
                  qgen_data_file.read().splitlines(),
              )
          ):
            (_, _, _, _, _, _, context_sentence, _, answer, question) = (
                qgen_data.split("\t")
            )
            context_passage = squad_data[squad_id]["context"]
            yield str(ex_id).zfill(7), {
                _CONTEXT_SENTENCE: context_sentence,
                _CONTEXT_PASSAGE: context_passage,
                _ANSWER: answer,
                _QUESTION: question,
            }

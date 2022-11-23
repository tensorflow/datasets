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

"""qrecc dataset."""

import json

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
A dataset containing 14K conversations with 81K question-answer pairs. QReCC is built on questions from TREC CAsT, QuAC and Google Natural Questions.
"""

_CITATION = """
@article{qrecc,
  title={Open-Domain Question Answering Goes Conversational via Question Rewriting},
  author={Anantha, Raviteja and Vakulenko, Svitlana and Tu, Zhucheng and Longpre, Shayne and Pulman, Stephen and Chappidi, Srinivas},
  journal={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  year={2021}
}
"""

_DATASET_URL = "https://github.com/apple/ml-qrecc/blob/main/dataset/qrecc_data.zip?raw=true"


class QReCC(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for QReCC dataset."""

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
            "context":
                tfds.features.Sequence(tfds.features.Text()),
            "question":
                tfds.features.Text(),
            "question_rewrite":
                tfds.features.Text(),
            "answer":
                tfds.features.Text(),
            "answer_url":
                tfds.features.Text(),
            "conversation_id":
                tfds.features.Scalar(
                    tf.int32, doc="The id of the conversation."),
            "turn_id":
                tfds.features.Scalar(
                    tf.int32,
                    doc="The id of the conversation turn, within a conversation."
                ),
            "source":
                tfds.features.Text(
                    doc="The original source of the data -- either QuAC, CAsT or Natural Questions"
                ),
        }),
        supervised_keys=None,
        homepage="https://github.com/apple/ml-qrecc",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Downloads the data and defines the splits
    data_dir = dl_manager.download_and_extract(_DATASET_URL)

    # Returns the Dict[split names, Iterator[Key, Example]]
    return {
        tfds.Split.TRAIN:
            self._generate_examples(path=data_dir / "qrecc_train.json"),
        tfds.Split.TEST:
            self._generate_examples(path=data_dir / "qrecc_test.json"),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    data = json.loads(path.read_text())
    for idx, row in enumerate(data):
      yield idx, {
          "context": row["Context"],
          "question": row["Question"],
          "question_rewrite": row["Rewrite"],
          "answer": row["Answer"],
          "answer_url": row["Answer_URL"],
          "conversation_id": row["Conversation_no"],
          "turn_id": row["Turn_no"],
          "source": row["Conversation_source"],
      }

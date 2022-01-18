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

"""A question-answering dataset with a focus on sentence composition."""

import json
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{allenai:qasc,
      author    = {Tushar Khot and Peter Clark and Michal Guerquin and Peter Jansen and Ashish Sabharwal},
      title     = {QASC: A Dataset for Question Answering via Sentence Composition},
      journal   = {arXiv:1910.11473v2},
      year      = {2020},
}
"""

_DESCRIPTION = """
QASC is a question-answering dataset with a focus on sentence composition. It consists of 9,980 8-way multiple-choice
questions about grade school science (8,134 train, 926 dev, 920 test), and comes with a corpus of 17M sentences.
"""

_DOWNLOAD_URL = "http://data.allenai.org/downloads/qasc/qasc_dataset.tar.gz"
_HOMEPAGE_URL = "https://allenai.org/data/qasc"


class Qasc(tfds.core.GeneratorBasedBuilder):
  """QaSC Dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id":
                tfds.features.Text(),
            "question":
                tfds.features.Text(),
            "choices":
                tfds.features.Sequence({
                    "text": tfds.features.Text(),
                    "label": tfds.features.Text()
                }),
            "answerKey":
                tfds.features.Text(),
            "fact1":
                tfds.features.Text(),
            "fact2":
                tfds.features.Text(),
            "combinedfact":
                tfds.features.Text(),
            "formatted_question":
                tfds.features.Text(),
        }),
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract({"QASC_Dataset": _DOWNLOAD_URL})
    data_dir = os.path.join(dl_dir["QASC_Dataset"], "QASC_Dataset")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepath": os.path.join(data_dir, "train.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"filepath": os.path.join(data_dir, "test.jsonl")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": os.path.join(data_dir, "dev.jsonl")},
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""

    with tf.io.gfile.GFile(filepath, "r") as f:
      for row in f:
        data = json.loads(row)
        answerkey = data.get("answerKey", "")
        id_ = data["id"]
        question = data["question"]["stem"]
        choices = data["question"]["choices"]
        text_choices = [choice["text"] for choice in choices]
        label_choices = [choice["label"] for choice in choices]
        fact1 = data.get("fact1", "")
        fact2 = data.get("fact2", "")
        combined_fact = data.get("combinedfact", "")
        formatted_question = data.get("formatted_question", "")
        yield id_, {
            "id": id_,
            "answerKey": answerkey,
            "question": question,
            "choices": {
                "text": text_choices,
                "label": label_choices
            },
            "fact1": fact1,
            "fact2": fact2,
            "combinedfact": combined_fact,
            "formatted_question": formatted_question,
        }

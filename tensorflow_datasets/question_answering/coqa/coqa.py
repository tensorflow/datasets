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

"""A Conversational Question Answering Challenge."""

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{reddy2018coqa,
    title={CoQA: A Conversational Question Answering Challenge},
    author={Siva Reddy and Danqi Chen and Christopher D. Manning},
    year={2018},
    eprint={1808.07042},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

_DESCRIPTION = """\
CoQA: A Conversational Question Answering Challenge
"""

_TRAIN_DATA_URL = "https://nlp.stanford.edu/data/coqa/coqa-train-v1.0.json"
_DEV_DATA_URL = "https://nlp.stanford.edu/data/coqa/coqa-dev-v1.0.json"
_HOMEPAGE_URL = "https://stanfordnlp.github.io/coqa/"


class Coqa(tfds.core.GeneratorBasedBuilder):
  """A Conversational Question Answering Challenge."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "source":
                tfds.features.Text(),
            "story":
                tfds.features.Text(),
            "questions":
                tfds.features.Sequence(tfds.features.Text()),
            "answers":
                tfds.features.Sequence({
                    "input_text": tfds.features.Text(),
                    "answer_start": tf.int32,
                    "answer_end": tf.int32,
                }),
        }),
        supervised_keys=None,
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    urls_to_download = {"train": _TRAIN_DATA_URL, "test": _DEV_DATA_URL}
    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepath": downloaded_files["train"],
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepath": downloaded_files["test"],
            }),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""

    with tf.io.gfile.GFile(filepath, "r") as f:
      data = json.load(f)
      for row in data["data"]:
        questions = [question["input_text"] for question in row["questions"]]
        story = row["story"]
        source = row["source"]
        answers_start = [answer["span_start"] for answer in row["answers"]]
        answers_end = [answer["span_end"] for answer in row["answers"]]
        answers = [answer["input_text"] for answer in row["answers"]]
        yield row["id"], {
            "source": source,
            "story": story,
            "questions": questions,
            "answers": {
                "input_text": answers,
                "answer_start": answers_start,
                "answer_end": answers_end
            },
        }

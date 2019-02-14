# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

from absl import logging
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

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

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """BuilderConfig for SQUAD.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      **kwargs: keyword arguments forwarded to super.
    """
    super(SquadConfig, self).__init__(**kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())


class Squad(tfds.core.GeneratorBasedBuilder):
  """SQUAD: The Stanford Question Answering Dataset. Version 1.1."""
  _URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
  _DEV_FILE = "dev-v1.1.json"
  _TRAINING_FILE = "train-v1.1.json"

  BUILDER_CONFIGS = [
      SquadConfig(
          name="plain_text",
          version="0.0.1",
          description="Plain text",
      ),
      SquadConfig(
          name="bytes",
          version="0.0.1",
          description=("Uses byte-level text encoding with "
                       "`tfds.features.text.ByteTextEncoder`"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder=tfds.features.text.ByteTextEncoder()),
      ),
      SquadConfig(
          name="subwords8k",
          version="0.0.1",
          description=("Uses `tfds.features.text.SubwordTextEncoder` with 8k "
                       "vocab size"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              vocab_size=2**13),
      ),
      SquadConfig(
          name="subwords32k",
          version="0.0.2",
          description=("Uses `tfds.features.text.SubwordTextEncoder` with "
                       "32k vocab size"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              vocab_size=2**15),
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "context":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "question":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "first_answer":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
        }),
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        urls=["https://rajpurkar.github.io/SQuAD-explorer/"],
        citation=_CITATION,
    )

  def _vocab_text_gen(self, filepath):
    for ex in self._generate_examples(filepath):
      # "first_answer" is a substring of "context" so not need to add it here
      yield " ".join([ex["question"], ex["context"]])

  def _split_generators(self, dl_manager):
    urls_to_download = {
        "train": os.path.join(self._URL, self._TRAINING_FILE),
        "dev": os.path.join(self._URL, self._DEV_FILE)
    }
    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    # Generate shared vocabulary
    # maybe_build_from_corpus uses SubwordTextEncoder if that's configured
    self.info.features["context"].maybe_build_from_corpus(
        self._vocab_text_gen(downloaded_files["train"]))
    encoder = self.info.features["context"].encoder
    # Use maybe_set_encoder because the encoder may have been restored from
    # package data.
    self.info.features["question"].maybe_set_encoder(encoder)
    self.info.features["first_answer"].maybe_set_encoder(encoder)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={"filepath": downloaded_files["train"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={"filepath": downloaded_files["dev"]}),
    ]

  def _generate_examples(self, filepath):
    """This function returns the examples in the raw (text) form."""
    logging.info("generating examples from = %s", filepath)
    with tf.io.gfile.GFile(filepath) as f:
      squad = json.load(f)
      for article in squad["data"]:
        if "title" in article:
          title = article["title"].strip()
        else:
          title = ""
        for paragraph in article["paragraphs"]:
          context = paragraph["context"].strip()
          for qa in paragraph["qas"]:
            question = qa["question"].strip()
            id_ = qa["id"]

            answer_starts = [answer["answer_start"] for answer in qa["answers"]]
            answers = [answer["text"].strip() for answer in qa["answers"]]

            # Features currently used are "context", "question", and "answers".
            # Others are extracted here for the ease of future expansions.
            example = {
                "title": title,
                "context": context,
                "question": question,
                "id": id_,
                "answer_starts": answer_starts,
                "answers": answers,
            }
            yield {
                "question": example["question"],
                # TODO(b/121176753): return all the answers.
                "first_answer": example["answers"][0],
                "context": example["context"]
            }

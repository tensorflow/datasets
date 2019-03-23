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

"""The Stanford Question Answering Dataset - 2.0"""

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
@article{DBLP:journals/corr/abs-1806-03822,
  author    = {Pranav Rajpurkar and
               Robin Jia and
               Percy Liang},
  title     = {Know What You Don't Know: Unanswerable Questions for SQuAD},
  journal   = {CoRR},
  volume    = {abs/1806.03822},
  year      = {2018},
  url       = {http://arxiv.org/abs/1806.03822},
  archivePrefix = {arXiv},
  eprint    = {1806.03822},
  timestamp = {Mon, 13 Aug 2018 16:48:21 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1806-03822},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """\
The Stanford Question Answering Dataset - 2.0 combines the 100,000 questions in SQuAD1.1 \
with over 50,000 new, unanswerable questions written adversarially by crowdworkers to look similar \
to answerable ones. To do well on dataset, systems must not only answer \
questions when possible, but also determine when no answer is supported by \
the paragraph and abstain from answering. SQuAD2.0 is a challenging natural \
language understanding task for existing models.
"""

class StanfordquadConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Stanford Question Answering Dataset - 2.0."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """BuilderConfig for Stanford Question Answering Dataset - 2.0.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      **kwargs: keyword arguments forwarded to super.
    """
    super(StanfordquadConfig, self).__init__(**kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())


class Stanfordquad(tfds.core.GeneratorBasedBuilder):
  """The Stanford Question Answering Dataset. Version 2.0."""
  _URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
  _DEV_FILE = "dev-v2.0.json"
  _TRAINING_FILE = "train-v2.0.json"

  BUILDER_CONFIGS = [
      StanfordquadConfig(
          name="plain_text",
          version="2.0.0",
          description="Plain text",
      ),
      StanfordquadConfig(
          name="bytes",
          version="2.0.0",
          description=("Uses byte-level text encoding with "
                       "`tfds.features.text.ByteTextEncoder`"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder=tfds.features.text.ByteTextEncoder()),
      ),
      StanfordquadConfig(
          name="subwords8k",
          version="2.0.0",
          description=("Uses `tfds.features.text.SubwordTextEncoder` with 8k "
                       "vocab size"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              vocab_size=2**13),
      ),
      StanfordquadConfig(
          name="subwords32k",
          version="2.0.0",
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
        urls=["https://rajpurkar.github.io/SQuAD-explorer/explore/v2.0/dev/"],
        citation=_CITATION,
    )





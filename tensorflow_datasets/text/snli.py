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

"""The Stanford NLI Corpus."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{snli:emnlp2015,
	Author = {Bowman, 
              Samuel R. and Angeli, 
              Gabor and Potts, Christopher, 
              and Manning, Christopher D.
            },
	Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
	Publisher = {Association for Computational Linguistics},
	Title = {A large annotated corpus for learning natural language inference},
	Year = {2015}
}
"""

_DESCRIPTION = """\
The SNLI corpus (version 1.0) is a collection of 570k human-written English sentence
pairs manually labeled for balanced classification with the labels entailment, contradiction,
and neutral, supporting the task of natural language inference (NLI), also known as recognizing
textual entailment (RTE). We aim for it to serve both as a benchmark for evaluating representational
systems for text, especially including those induced by representation learning methods,
as well as a resource for developing NLP models of any kind.
"""

ROOT_URL = "https://nlp.stanford.edu/projects/snli/snli_1.0.zip"

class SNLIConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SNLI."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """BuilderConfig for SNLI.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      **kwargs: keyword arguments forwarded to super.
    """
    super(SNLIConfig, self).__init__(**kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())


class SNLI(tfds.core.GeneratorBasedBuilder):
  """SNLI: The Stanford Natural Language Inference (SNLI) Corpus. Version 1.0"""

  BUILDER_CONFIGS = [
      SNLIConfig(
          name="plain_text",
          version="1.0.0",
          description="Plain text",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "text":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "hypothesis":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "judgements":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
        }),
        # No default supervised_keys (as we have to pass both text
        # and hypothesis as input).
        supervised_keys=None,
        urls=["https://nlp.stanford.edu/projects/snli/"],
        citation=_CITATION,
    )

  def _vocab_text_gen(self, filepath):
    for ex in self._generate_examples(filepath):
      yield " ".join([ex["text"], ex["hypothesis"], ex["judgements"]])

  def _split_generators(self, dl_manager):

    downloaded_dir = dl_manager.download_and_extract(ROOT_URL)
    snli_path = os.path.join(downloaded_dir, "snli_1.0")
    train_path = os.path.join(snli_path, "snli_1.0_train.txt")
    # Using dev as the default for eval.
    validation_path = os.path.join(snli_path, "snli_1.0_dev.txt")

    # Generate shared vocabulary
    # maybe_build_from_corpus uses SubwordTextEncoder if that's configured
    self.info.features["text"].maybe_build_from_corpus(
        self._vocab_text_gen(train_path))
    encoder = self.info.features["text"].encoder
    # Use maybe_set_encoder because the encoder may have been restored from
    # package data.
    self.info.features["text"].maybe_set_encoder(encoder)
    self.info.features["hypothesis"].maybe_set_encoder(encoder)
    self.info.features["judgements"].maybe_set_encoder(encoder)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={"filepath": train_path}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={"filepath": validation_path}),
    ]

  def _generate_examples(self, filepath):
    """Generate snli examples.

    Args:
      filepath: a string
    Yields:
      dictionaries containing "text", "hypothesis" and "judgements" strings
    """
    for idx, line in enumerate(tf.io.gfile.GFile(filepath, "rb")):
      if idx == 0: continue  # skip header
      line = tf.compat.as_text(line.strip())
      split_line = line.split("\t")
      # Works for both splits even though dev has some extra human labels.
      yield {
          "text": split_line[5],
          "hypothesis": split_line[6],
          "judgements": split_line[0]
      }


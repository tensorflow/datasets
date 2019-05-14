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

"""ParaCrawl (Bitextor) parallel open-source machine translation benchmark."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = ("Web-Scale Parallel Corpora for Official European Languages. "
                "English-{target_lang}.")

_BENCHMARK_URL = "https://paracrawl.eu/releases.html"

_CITATION = """\
@misc {paracrawl,
    title  = "ParaCrawl",
    year   = "2018",
    url    = "http://paracrawl.eu/download.html."
}
"""

_BASE_DATA_URL_FORMAT_STR = ("https://s3.amazonaws.com/web-language-models/"
                             "paracrawl/release4/en-{target_lang}.bicleaner07."
                             "txt.gz")

_TARGET_LANGUAGES = {
    "bg": "Bulgarian",
    "da": "Danish",
    "el": "Greek",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sv": "Swedish",
    "ga": "Irish",
    "hr": "Croatian",
    "mt": "Maltese",
    "lt": "Lithuanian",
    "hu": "Hungarian",
    "et": "Estonian",
    "de": "German",
    "fr": "French",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "pl": "Polish",
    "cs": "Czech",
    "ro": "Romanian",
    "fi": "Finnish",
    "lv": "Latvian"
}


class ParaCrawlConfig(tfds.core.BuilderConfig):
  """BuilderConfig for ParaCrawl."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, target_language=None, **kwargs):
    """BuilderConfig for ParaCrawl.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      target_language: Target language that will be used to translate to from
        English which is always the source language. It has to contain 2-letter
        coded strings. For example: "se", "hu".
      **kwargs: Keyword arguments forwarded to super.
    """
    # Validate the target language.
    if target_language not in _TARGET_LANGUAGES:
      raise ValueError("Invalid target language: %s " % target_language)

    # Initialize the base class.
    encoder_name = (
        text_encoder_config.name if text_encoder_config else "plain_text")
    name = "en%s_%s" % (target_language, encoder_name)

    description = ("Translation dataset from English to %s, uses encoder %s."
                  ) % (target_language, encoder_name)
    super(ParaCrawlConfig, self).__init__(
        name=name, description=description, **kwargs)

    # Store the attributes.
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())
    self.target_language = target_language
    self.data_url = _BASE_DATA_URL_FORMAT_STR.format(
        target_lang=target_language)


class ParaCrawl(tfds.core.GeneratorBasedBuilder):
  """ParaCrawl machine translation dataset."""

  BUILDER_CONFIGS = [
      # The version below does not refer to the version of the released
      # database. It only indicates the version of the TFDS integration.
      ParaCrawlConfig(target_language=target_language, version="0.1.0")
      for target_language, _ in _TARGET_LANGUAGES.items()
  ]

  def _info(self):
    target_language = self.builder_config.target_language
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION.format(
            target_lang=_TARGET_LANGUAGES[target_language]),
        features=tfds.features.Translation(
            languages=("en", target_language),
            encoder_config=self.builder_config.text_encoder_config),
        supervised_keys=("en", target_language),
        urls=[
            _BENCHMARK_URL,
            _BASE_DATA_URL_FORMAT_STR.format(target_lang=target_language)
        ],
        citation=_CITATION)

  def _vocab_text_gen(self, files, language):
    for ex in self._generate_examples(**files):
      yield ex[language]

  def _split_generators(self, dl_manager):
    # Download the data file.
    data_file = dl_manager.download_and_extract(
        {"data_file": self.builder_config.data_url})

    # Return the single split of the data.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, num_shards=10, gen_kwargs=data_file)
    ]

  def _generate_examples(self, data_file):
    """This function returns the examples in the raw (text) form."""
    target_language = self.builder_config.target_language

    with tf.io.gfile.GFile(data_file) as f:
      for i, line in enumerate(f):
        line_parts = line.strip().split("\t")
        if len(line_parts) != 2:
          raise ValueError(("Wrong data format in line {}. The line '{}' does "
                            "not have exactly one delimiter.").format(i, line))
        source, target = line_parts[0].strip(), line_parts[1].strip()

        yield {"en": source, target_language: target}

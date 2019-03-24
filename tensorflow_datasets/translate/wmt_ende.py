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

"""English-German WMT translation dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import wmt


TRANSLATE_DATASETS = {
    "wmt13_commoncrawl_ende": wmt.TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        language_to_file={
            "en": "commoncrawl.de-en.en",
            "de": "commoncrawl.de-en.de",
        }),
    "wmt13_europarl_ende": wmt.TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        language_to_file={
            "en": "training/europarl-v7.de-en.en",
            "de": "training/europarl-v7.de-en.de",
        }),
    "wmt17_newstest13": wmt.TranslateData(
        url="http://data.statmt.org/wmt17/translation-task/dev.tgz",
        language_to_file={
            "en": "dev/newstest2013.en",
            "de": "dev/newstest2013.de",
        }),
    "wmt18_news_commentary_ende": wmt.TranslateData(
        url="http://data.statmt.org/wmt18/translation-task/training-parallel-nc-v13.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "training-parallel-nc-v13/news-commentary-v13.de-en.en",
            "de": "training-parallel-nc-v13/news-commentary-v13.de-en.de",
        }),
}


# Datasets used by T2T code for en-de translation.
T2T_ENDE_TRAIN = [
    "wmt18_news_commentary_ende", "wmt13_commoncrawl_ende",
    "wmt13_europarl_ende"
]
T2T_ENDE_DEV = ["wmt17_newstest13"]


class WmtTranslateEnde(wmt.WmtTranslate):
  """WMT English-German translation dataset."""
  IN_DEVELOPMENT = True

  BUILDER_CONFIGS = [
      wmt.WMTConfig(
          language_pair=("en", "de"),
          version="0.0.2",
          name_suffix="t2t",
          data={
              "train": T2T_ENDE_TRAIN,
              "dev": T2T_ENDE_DEV
          }),
      wmt.WMTConfig(
          language_pair=("en", "de"),
          version="0.0.2",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t",
          data={
              "train": T2T_ENDE_TRAIN,
              "dev": T2T_ENDE_DEV
          }),
  ]

  @property
  def translate_datasets(self):
    return TRANSLATE_DATASETS

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

"""English-French WMT Translate dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import wmt


TRANSLATE_DATASETS = {
    "wmt10_giga_fren_enfr": wmt.TranslateData(
        url="http://www.statmt.org/wmt10/training-giga-fren.tar",
        language_to_file={
            "en": "giga-fren.release2.fixed.en.gz",
            "fr": "giga-fren.release2.fixed.fr.gz",
        }),
    "wmt13_commoncrawl_enfr": wmt.TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        language_to_file={
            "en": "commoncrawl.fr-en.en",
            "fr": "commoncrawl.fr-en.fr",
        }),
    "wmt13_europarl_enfr": wmt.TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        language_to_file={
            "en": "training/europarl-v7.fr-en.en",
            "fr": "training/europarl-v7.fr-en.fr",
        }),
    "wmt13_undoc_enfr": wmt.TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-un.tgz",
        language_to_file={
            "en": "un/undoc.2000.fr-en.en",
            "fr": "un/undoc.2000.fr-en.fr",
        }),
    "wmt14_news_commentary_enfr": wmt.TranslateData(
        url="http://www.statmt.org/wmt14/training-parallel-nc-v9.tgz",
        language_to_file={
            "en": "training/news-commentary-v9.fr-en.en",
            "fr": "training/news-commentary-v9.fr-en.fr",
        }),
    "wmt17_newstest13": wmt.TranslateData(
        url="http://data.statmt.org/wmt17/translation-task/dev.tgz",
        language_to_file={
            "en": "dev/newstest2013.en",
            "fr": "dev/newstest2013.fr",
        }),
    "opennmt_1M_enfr_train": wmt.TranslateData(
        url="https://s3.amazonaws.com/opennmt-trainingdata/baseline-1M-enfr.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "baseline-1M-enfr/baseline-1M_train.en",
            "fr": "baseline-1M-enfr/baseline-1M_train.fr",
        }),
    "opennmt_1M_enfr_valid": wmt.TranslateData(
        url="https://s3.amazonaws.com/opennmt-trainingdata/baseline-1M-enfr.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "baseline-1M-enfr/baseline-1M_valid.en",
            "fr": "baseline-1M-enfr/baseline-1M_valid.fr",
        }),
}


T2T_ENFR_TRAIN_SMALL = ["opennmt_1M_enfr_train"]
T2T_ENFR_DEV_SMALL = ["opennmt_1M_enfr_valid"]

T2T_ENFR_TRAIN_LARGE = ["wmt13_commoncrawl_enfr", "wmt13_europarl_enfr",
                        "wmt14_news_commentary_enfr",
                        # TODO(b/119253909): figure out if we need this
                        # as a part of the train set (as it has data
                        # in a different file format).
                        # "wmt10_giga_fren_enfr",
                        "wmt13_undoc_enfr"]
T2T_ENFR_DEV_LARGE = ["wmt17_newstest13"]


class WmtTranslateEnfr(wmt.WmtTranslate):
  """English-French WMT translation dataset."""
  IN_DEVELOPMENT = True

  BUILDER_CONFIGS = [
      # EN-FR translations (matching the data used by Tensor2Tensor library).
      wmt.WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.2",
          name_suffix="t2t_small",
          data={
              "train": T2T_ENFR_TRAIN_SMALL,
              "dev": T2T_ENFR_DEV_SMALL
          }),
      wmt.WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.2",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t_small",
          data={
              "train": T2T_ENFR_TRAIN_SMALL,
              "dev": T2T_ENFR_DEV_SMALL
          }),
      wmt.WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.2",
          name_suffix="t2t_large",
          data={
              "train": T2T_ENFR_TRAIN_LARGE,
              "dev": T2T_ENFR_DEV_LARGE
          }),
      wmt.WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.2",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t_large",
          data={
              "train": T2T_ENFR_TRAIN_LARGE,
              "dev": T2T_ENFR_DEV_LARGE
          }),
  ]

  @property
  def translate_datasets(self):
    return TRANSLATE_DATASETS

# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for WMT translate dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.translate import wmt19


class TranslateDeEnWmt19Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = wmt19.Wmt19Translate
  BUILDER_CONFIG_NAMES_TO_TEST = ["de-en"]
  OVERLAPPING_SPLITS = ["validation"]

  DL_EXTRACT_RESULT = {
      "paracrawl_v3": ["sentences.de-en.tmx"],
      "newscommentary_v14": ["sentences.de-en.tsv"],
      "wikititles_v1": ["sentences.de-en.tsv"],
      "rapid_2019": ["rapid_2019"],
      "newstest2018": ["validation"],
  }

  SEQUENTUAL_DL_EXTRACT_RESULT = {
      "http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz": (
          "commoncrawl"
      ),
      "http://www.statmt.org/europarl/v9/training/europarl-v9.de-en.tsv.gz": (
          "sentences.de-en.tsv"
      ),
  }

  def _get_dl_extract_result(self, url):
    if not url:
      return []
    if isinstance(url, dict):
      return super()._get_dl_extract_result(url)
    return self.dummy_data / self.SEQUENTUAL_DL_EXTRACT_RESULT[url]

  SPLITS = {
      "train": 12,
      "validation": 2,
  }


class TranslateCsEnWmt19Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = wmt19.Wmt19Translate
  BUILDER_CONFIG_NAMES_TO_TEST = ["cs-en"]
  OVERLAPPING_SPLITS = ["validation"]

  DL_EXTRACT_RESULT = {
      "czeng17_filter": ["czeng"],
      "paracrawl_v3": ["sentences.cs-en.tmx"],
      "newscommentary_v14": ["sentences.cs-en.tsv"],
      "wikititles_v1": ["sentences.cs-en.tsv"],
      "newstest2018": ["validation"],
  }

  SEQUENTUAL_DL_EXTRACT_RESULT = {
      "http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz": (
          "commoncrawl"
      ),
      "http://www.statmt.org/europarl/v9/training/europarl-v9.cs-en.tsv.gz": (
          "sentences.cs-en.tsv"
      ),
  }

  def _get_dl_extract_result(self, url):
    if not url:
      return []
    if isinstance(url, dict):
      return super()._get_dl_extract_result(url)
    return self.dummy_data / self.SEQUENTUAL_DL_EXTRACT_RESULT[url]

  SPLITS = {
      "train": 13,
      "validation": 2,
  }


if __name__ == "__main__":
  testing.test_main()

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

"""WMT13: Translate dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import wmt

_URL = "http://www.statmt.org/wmt13/translation-task.html"
_CITATION = """
@InProceedings{bojar-EtAl:2013:WMT,
  author    = {Bojar, Ondrej  and  Buck, Christian  and  Callison-Burch, Chris  and  Federmann, Christian  and  Haddow, Barry  and  Koehn, Philipp  and  Monz, Christof  and  Post, Matt  and  Soricut, Radu  and  Specia, Lucia},
  title     = {Findings of the 2013 {Workshop on Statistical Machine Translation}},
  booktitle = {Proceedings of the Eighth Workshop on Statistical Machine Translation},
  month     = {August},
  year      = {2013},
  address   = {Sofia, Bulgaria},
  publisher = {Association for Computational Linguistics},
  pages     = {1--44},
  url       = {http://www.aclweb.org/anthology/W13-2201}
}

"""

_LANGUAGE_PAIRS = [(lang, "en") for lang in ["cs", "de", "fr", "es", "ru"]]


class Wmt13Translate(wmt.WmtTranslate):
  """WMT 13 translation datasets for all {xx, "en"} language pairs."""

  # Version history:
  # 1.0.0: S3 (new shuffling, sharding and slicing mechanism).
  BUILDER_CONFIGS = [
      wmt.WmtConfig(  # pylint:disable=g-complex-comprehension
          description="WMT 2013 %s-%s translation task dataset." % (l1, l2),
          url=_URL,
          citation=_CITATION,
          language_pair=(l1, l2),
          version=tfds.core.Version("1.0.0"),
      )
      for l1, l2 in _LANGUAGE_PAIRS
  ]

  @property
  def _subsets(self):
    return {
        tfds.Split.TRAIN: [
            "europarl_v7",
            "commoncrawl",
            "multiun",
            "newscommentary_v8",
            "gigafren",
            "wikiheadlines_ru",
            "yandexcorpus",
            "czeng_10",
        ],
        tfds.Split.VALIDATION: [
            "newstest2012",
            "newstest2011",
            "newstest2010",
            "newstest2009",
            "newstest2008",
            "newssyscomb2009",
        ],
        tfds.Split.TEST: ["newstest2013"],
    }

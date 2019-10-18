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

"""Gigaword summarization dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{graff2003english,
  title={English gigaword},
  author={Graff, David and Kong, Junbo and Chen, Ke and Maeda, Kazuaki},
  journal={Linguistic Data Consortium, Philadelphia},
  volume={4},
  number={1},
  pages={34},
  year={2003}
}

@article{Rush_2015,
   title={A Neural Attention Model for Abstractive Sentence Summarization},
   url={http://dx.doi.org/10.18653/v1/D15-1044},
   DOI={10.18653/v1/d15-1044},
   journal={Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing},
   publisher={Association for Computational Linguistics},
   author={Rush, Alexander M. and Chopra, Sumit and Weston, Jason},
   year={2015}
}
"""

_DESCRIPTION = """
Headline-generation on a corpus of article pairs from Gigaword consisting of
around 4 million articles. Train/test splits follows Rush_2015.

There are two features:
  - document: article.
  - summary: headline.

"""

_URL = "https://drive.google.com/uc?export=download&id=0B6N7tANPyVeBNmlSX19Ld2xDU1E"

_DOCUMENT = "document"
_SUMMARY = "summary"


class Gigaword(tfds.core.GeneratorBasedBuilder):
  """Gigaword summarization dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text()
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        urls=["https://github.com/harvardnlp/sent-summary"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    gigaword_path = os.path.join(dl_path, "sumdata")
    train_path = {
        _DOCUMENT:
            os.path.join(gigaword_path, "train/valid.article.filter.txt"),
        _SUMMARY:
            os.path.join(gigaword_path, "train/valid.title.filter.txt")
    }
    test_path = {
        _DOCUMENT: os.path.join(gigaword_path, "Giga/input.txt"),
        _SUMMARY: os.path.join(gigaword_path, "Giga/task1_ref0.txt")
    }
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": train_path},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": test_path},
        ),
    ]

  def _generate_examples(self, path=None):
    """Yields examples."""
    with tf.io.gfile.GFile(path[_DOCUMENT]) as f_d, tf.io.gfile.GFile(
        path[_SUMMARY]) as f_s:
      for i, (doc_text, sum_text) in enumerate(zip(f_d, f_s)):
        yield i, {_DOCUMENT: doc_text.strip(), _SUMMARY: sum_text.strip()}

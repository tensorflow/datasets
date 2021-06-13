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

# Lint as: python3
"""Natural Questions Open: A Benchmark for Open Domain Question Answering."""

import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{orqa,
title = {Latent Retrieval for Weakly Supervised Open Domain Question Answering},
author = {Lee, Kenton and Chang, Ming-Wei and Toutanova, Kristina},
year = {2019},
month = {01},
pages = {6086-6096},
booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
doi = {10.18653/v1/P19-1612}
}

@article{47761,
title = {Natural Questions: a Benchmark for Question Answering Research},
author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
year = {2019},
journal = {Transactions of the Association of Computational Linguistics}
}
"""

_DOWNLOAD_URL_FMT = 'https://raw.githubusercontent.com/google-research-datasets/natural-questions/a7a113c9fdc2d9986d624bd43b8a18d6d5779eaa/nq_open/NQ-open.{split}.jsonl'

_DESCRIPTION = """
The NQ-Open task, introduced by Lee et.al. 2019, is an open domain question \
answering benchmark that is derived from Natural Questions. The goal is to \
predict an English answer string for an input English question. All questions \
can be answered using the contents of English Wikipedia.
"""

_URL = 'https://github.com/google-research-datasets/natural-questions/tree/master/nq_open'


class NaturalQuestionsOpen(tfds.core.GeneratorBasedBuilder):
  """Natural Questions Open: A Benchmark for Open Domain Question Answering."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'question': tf.string,
            'answer': tfds.features.Sequence(tf.string)
        }),
        supervised_keys=None,
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    file_paths = dl_manager.download({
        'train': _DOWNLOAD_URL_FMT.format(split='train'),
        'validation': _DOWNLOAD_URL_FMT.format(split='dev'),
    })
    return [
        tfds.core.SplitGenerator(
            name=split, gen_kwargs={'file_path': file_path})
        for split, file_path in file_paths.items()
    ]

  def _generate_examples(self, file_path):
    """Parses split file and yields examples."""

    with tf.io.gfile.GFile(file_path) as f:
      for i, line in enumerate(f):
        yield i, json.loads(line)

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

"""English-Tamil parallel text corpus from Morphological Processing 2012"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


DESCRIPTION = """\
	The parallel corpora cover texts from bible, cinema and news domains.
"""

CITATION = """\
    @InProceedings {biblio:RaBoMorphologicalProcessing2012,
	title     = {Morphological Processing for English-Tamil Statistical Machine Translation},
	author    = {Loganathan Ramasamy and Ond{\v{r}}ej Bojar and Zden{\v{e}}k {\v{Z}}abokrtsk{\'{y}}},
	year      = {2012},
	pages     = {113--122},
	Booktitle = {Proceedings of the Workshop on Machine Translation and Parsing in Indian Languages ({MTPIL}-2012)},
}
"""

_DATA_URL = "http://ufal.mff.cuni.cz/~ramasamy/parallel/data/v2/en-ta-parallel-v2.tar.gz"

class EnTamParallelText(tfds.core.GeneratorBasedBuilder):
  """(en_tam_parallel_text): English_Tamil parallel text corpus"""

  VERSION = tfds.core.Version("0.0.3")
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=DESCRIPTION,
        features=tfds.features.Translation(
            languages=("en", "ta")),
        urls=['http://ufal.mff.cuni.cz/~ramasamy/parallel/html/'],
        supervised_keys=("en", "ta"),
        citation=CITATION,
    )

  def _split_generators(self, dl_manager):
    """Download the links and pass the filenames to split generator"""

    dl_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(dl_dir, 'en-ta-parallel-v2')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs={
                "source_file": os.path.join(data_dir, 'corpus.bcn.train.en'),
                "target_file": os.path.join(data_dir, 'corpus.bcn.train.ta')
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                "source_file": os.path.join(data_dir, 'corpus.bcn.dev.en'),
                "target_file": os.path.join(data_dir, 'corpus.bcn.dev.ta')
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={
                "source_file": os.path.join(data_dir, 'corpus.bcn.test.en'),
                "target_file": os.path.join(data_dir, 'corpus.bcn.test.ta')
            })]

  def _generate_examples(self, source_file, target_file):
    """Return id and (source, target) text pairs."""
    with tf.io.gfile.GFile(source_file) as f:
      source_sentences = f.read().strip().split("\n")
    with tf.io.gfile.GFile(target_file) as f:
      target_sentences = f.read().strip().split("\n")

    assert len(target_sentences) == len(
        source_sentences), "Sizes do not match: %d vs %d for %s vs %s." % (
            len(source_sentences), len(target_sentences), source_file,
            target_file)

    for idx, (source, target) in enumerate(
        zip(source_sentences, target_sentences)):
      result = {'en': source, 'ta': target}
      # Make sure that both translations are non-empty.
      if all(result.values()):
        yield idx, result
        

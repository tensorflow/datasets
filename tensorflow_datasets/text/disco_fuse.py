# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""DiscoFuse: A Large-Scale Dataset for Discourse-Based Sentence Fusion"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import api_utils

_CITATION = """
@InProceedings{GevaEtAl2019,
  title = {{DiscoFuse: A Large-Scale Dataset for Discourse-Based Sentence Fusion}},
  author = {Geva, Mor and Malmi, Eric and Szpektor, Idan and Berant, Jonathan},
  booktitle = {Proceedings of the 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics},
  note = {arXiv preprint arXiv:1902.10526},
  year = {2019}
}
"""

_DESCRIPTION = """
Sentence fusion is the task of joining several independent sentences into a 
single coherent text DiscoFuse was created by applying a rule-based splitting 
method on two corpora - sports articles crawled from the Web, and Wikipedia."""

_DATA_OPTIONS = ['wikipedia', 'sports']
_URLS = {'wikipedia': 'https://storage.googleapis.com/discofuse_dataset_v1/discofuse_v1_wikipedia.tar.gz',
         'sports': 'https://storage.googleapis.com/discofuse_dataset_v1/discofuse_v1_sports.tar.gz'}


class DiscoFuseConfig(tfds.core.BuilderConfig):
  """BuilderConfig for DiscoFuse."""

  @api_utils.disallow_positional_args
  def __init__(self, **kwargs):
    """BuilderConfig for DiscoFuse.
    Args:
      **kwargs: keyword arguments forwarded to super.
    """
    super(DiscoFuseConfig, self).__init__(**kwargs)


class DiscoFuse(tfds.core.GeneratorBasedBuilder):
  """DiscoFuse: A Large-Scale Dataset for Discourse-Based Sentence Fusion"""

  VERSION = tfds.core.Version('0.1.0')
  BUILDER_CONFIGS = [
      DiscoFuseConfig(
          name="wikipedia",
          version="0.0.1",
          description="DiscoFuse from Wikipedia Articles"),
      DiscoFuseConfig(
          name="sports",
          version="0.0.1",
          description="Sports from Sports Articles")
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "coherent_first_sentence": tfds.features.Text(),
            "coherent_second_sentence": tfds.features.Text(),
            "incoherent_first_sentence": tfds.features.Text(),
            "incoherent_second_sentence": tfds.features.Text(),
            "discourse_type": tfds.features.ClassLabel(names=[
                'PAIR_ANAPHORA',
                'PAIR_CONN',
                'PAIR_CONN_ANAPHORA',
                'PAIR_NONE',
                'SINGLE_APPOSITION',
                'SINGLE_CATAPHORA',
                'SINGLE_CONN_INNER',
                'SINGLE_CONN_INNER_ANAPHORA',
                'SINGLE_CONN_START',
                'SINGLE_RELATIVE',
                'SINGLE_S_COORD',
                'SINGLE_S_COORD_ANAPHORA',
                'SINGLE_VP_COORD']),
            "connective_string": tfds.features.Text(),
            "has_coref_type_pronoun": tfds.features.ClassLabel(
                num_classes=2),
            "has_coref_type_nominal": tfds.features.ClassLabel(
                num_classes=2)
        }),
        supervised_keys=None,
        urls=['https://github.com/google-research-datasets/discofuse'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    url = _URLS[self.builder_config.name]
    directory = dl_manager.download_and_extract(url)
    directory = os.path.join(directory, self.builder_config.name)
    train = os.path.join(directory, "train.tsv")
    dev = os.path.join(directory, "dev.tsv")
    test = os.path.join(directory, "test.tsv")
    train_balanced = os.path.join(directory, "train.tsv")
    dev_balanced = os.path.join(directory, "dev.tsv")
    test_balanced = os.path.join(directory, "test.tsv")

    return [
        tfds.core.SplitGenerator(
            name="train",
            num_shards=2,
            gen_kwargs={"directory": train},
        ),
        tfds.core.SplitGenerator(
            name="dev",
            num_shards=1,
            gen_kwargs={"directory": dev},
        ),
        tfds.core.SplitGenerator(
            name="test",
            num_shards=1,
            gen_kwargs={"directory": test},
        ),
        tfds.core.SplitGenerator(
            name="train_balanced",
            num_shards=1,
            gen_kwargs={"directory": train_balanced},
        ),
        tfds.core.SplitGenerator(
            name="dev_balanced",
            num_shards=1,
            gen_kwargs={"directory": dev_balanced},
        ),
        tfds.core.SplitGenerator(
            name="test_balanced",
            num_shards=1,
            gen_kwargs={"directory": test_balanced},
        ),
    ]

  def _generate_examples(self, directory):
    """Yields examples."""
    with tf.io.gfile.GFile(directory) as tsvfile:
      reader = csv.DictReader(tsvfile, dialect='excel-tab')
      for row in reader:
        row['has_coref_type_pronoun'] = int(
            float(row['has_coref_type_pronoun']))
        row['has_coref_type_nominal'] = int(
            float(row['has_coref_type_nominal']))
        yield row

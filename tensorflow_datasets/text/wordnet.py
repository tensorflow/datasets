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

"""wordnet dataset."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_LICENSE = """WordNet Release 3.0 This software and database is being provided
to you, the LICENSEE, by Princeton University under the following license. By
obtaining, using and/or copying this software and database, you agree that you
have read, understood, and will comply with these terms and conditions.:
Permission to use, copy, modify and distribute this software and database and
its documentation for any purpose and without fee or royalty is hereby granted,
provided that you agree to comply with the following copyright notice and
statements, including the disclaimer, and that the same appear on ALL copies of
the software, database and documentation, including modifications that you make
for internal use or for distribution. WordNet 3.0 Copyright 2006 by Princeton
University. All rights reserved. THIS SOFTWARE AND DATABASE IS PROVIDED "AS IS"
AND PRINCETON UNIVERSITY MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED. BY WAY OF EXAMPLE, BUT NOT LIMITATION, PRINCETON UNIVERSITY MAKES NO
REPRESENTATIONS OR WARRANTIES OF MERCHANT- ABILITY OR FITNESS FOR ANY PARTICULAR
PURPOSE OR THAT THE USE OF THE LICENSED SOFTWARE, DATABASE OR DOCUMENTATION WILL
NOT INFRINGE ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADEMARKS OR OTHER RIGHTS.
The name of Princeton University or Princeton may not be used in advertising or
publicity pertaining to distribution of the software and/or database. Title to
copyright in this software, database and any associated documentation shall at
all times remain with Princeton University and LICENSEE agrees to preserve same.
"""

_CITATION = """@article{10.1145/219717.219748,
author = {Miller, George A.},
title = {WordNet: A Lexical Database for English},
year = {1995},
issue_date = {Nov. 1995},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {38},
number = {11},
issn = {0001-0782},
url = {https://doi.org/10.1145/219717.219748},
doi = {10.1145/219717.219748},
journal = {Commun. ACM},
month = nov,
pages = {39--41},
numpages = {3}
}
"""

_DESCRIPTION = """WordNet is a large lexical database of English. Nouns, verbs,
adjectives and adverbs are grouped into sets of cognitive synonyms (synsets),
each expressing a distinct concept. Synsets are interlinked by means of
conceptual-semantic and lexical relations.
"""

_WN18_DESCRIPTION = """This WORDNET TENSOR DATA consists of a collection of
triplets (synset, relation_type, triplet) extracted from WordNet 3.0
(http://wordnet.princeton.edu). This data set can be seen as a 3-mode tensor
depicting ternary relationships between synsets. See
https://everest.hds.utc.fr/doku.php?id=en:transe.
"""

_WN18_CITATION = """@incollection{NIPS2013_5071,
title = {Translating Embeddings for Modeling Multi-relational Data},
author = {Bordes, Antoine and Usunier, Nicolas and Garcia-Duran, Alberto and Weston, Jason and Yakhnenko, Oksana},
booktitle = {Advances in Neural Information Processing Systems 26},
editor = {C. J. C. Burges and L. Bottou and M. Welling and Z. Ghahramani and K. Q. Weinberger},
pages = {2787--2795},
year = {2013},
publisher = {Curran Associates, Inc.},
url = {http://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf}
}
"""

_WN18RR_DESCRIPTION = """Same as WN18 but fixes test leakage through inverse
relations. See https://github.com/TimDettmers/ConvE.
"""

_WN18RR_CITATION = """@inproceedings{dettmers2018conve,
	Author = {Dettmers, Tim and Pasquale, Minervini and Pontus, Stenetorp and Riedel, Sebastian},
	Booktitle = {Proceedings of the 32th AAAI Conference on Artificial Intelligence},
	Title = {Convolutional 2D Knowledge Graph Embeddings},
	Url = {https://arxiv.org/abs/1707.01476},
	Year = {2018},
        pages  = {1811--1818},
  	Month = {February}
}
"""

_RELATIONS = [
    '_also_see',
    '_derivationally_related_form',
    '_has_part',
    '_hypernym',
    '_instance_hypernym',
    '_member_meronym',
    '_member_of_domain_region',
    '_member_of_domain_usage',
    '_similar_to',
    '_synset_domain_topic_of',
    '_verb_group',
]


def _make_wn18_metadata(synset_definitions_path):
  synsets = {}
  with tf.io.gfile.GFile(synset_definitions_path) as f:
    for line in f:
      synset_id, name, definition = line.strip().split('\t')
      synsets[synset_id] = dict(name=name, definition=definition)
  return dict(relations=_RELATIONS, synsets=synsets)


class WordnetConfig(tfds.core.BuilderConfig):
  """Configuration for `Wordnet`."""

  def __init__(self, name, path_prefix, description, citation, version):
    self._citation = citation
    self._path_prefix = path_prefix
    super(WordnetConfig, self).__init__(
        name=name, description=description, version=version)

  @property
  def citation(self):
    return '\n'.join([_CITATION, self._citation])

  def get_paths(self, dl_paths):
    root_dir = dl_paths[self.name]
    return (os.path.join(root_dir, self._path_prefix + 'train.txt'),
            os.path.join(root_dir, self._path_prefix + 'valid.txt'),
            os.path.join(root_dir, self._path_prefix + 'test.txt'))


class Wordnet(tfds.core.GeneratorBasedBuilder):
  """Builder for WordNet dataset."""

  BUILDER_CONFIGS = [
      WordnetConfig(
          name='WN18',
          path_prefix=os.path.join('wordnet-mlj12', 'wordnet-mlj12-'),
          description=_WN18_DESCRIPTION,
          citation=_WN18_CITATION,
          version=tfds.core.Version('0.1.0')),
      WordnetConfig(
          name='WN18RR',
          path_prefix='',
          description=_WN18RR_DESCRIPTION,
          citation=_WN18RR_CITATION,
          version=tfds.core.Version('0.1.0')),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'lhs': tfds.features.Text(),
            'relation': tfds.features.Text(),
            'rhs': tfds.features.Text(),
        }),
        homepage='https://wordnet.princeton.edu/',
        citation=self.builder_config.citation,
        metadata=tfds.core.MetadataDict(),
        redistribution_info=dict(license=_LICENSE),
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({
        'WN18':
            'https://everest.hds.utc.fr/lib/exe/fetch.php?media=en:wordnet-mlj12.tar.gz',
        'WN18RR':
            'https://github.com/TimDettmers/ConvE/raw/master/WN18RR.tar.gz',
    })
    # Metadata is at the configuration level and is the same for all splits.
    synset_definitions_path = os.path.join(dl_paths['WN18'], 'wordnet-mlj12',
                                           'wordnet-mlj12-definitions.txt')
    self.info.metadata.update(_make_wn18_metadata(synset_definitions_path))
    # Locate and output splits.
    train_path, val_path, test_path = self.builder_config.get_paths(dl_paths)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(triplets_path=train_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(triplets_path=val_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(triplets_path=test_path),
        ),
    ]

  def _generate_examples(self, triplets_path):
    """Yields examples."""
    with tf.io.gfile.GFile(triplets_path) as f:
      for i, line in enumerate(f):
        lhs, relation, rhs = line.strip().split('\t')
        yield i, {'lhs': lhs, 'relation': relation, 'rhs': rhs}

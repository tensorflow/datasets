# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""wiki_auto dataset for text simplification."""
import json

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{acl/JiangMLZX20,
  author    = {Chao Jiang and
               Mounica Maddela and
               Wuwei Lan and
               Yang Zhong and
               Wei Xu},
  editor    = {Dan Jurafsky and
               Joyce Chai and
               Natalie Schluter and
               Joel R. Tetreault},
  title     = {Neural {CRF} Model for Sentence Alignment in Text Simplification},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational
               Linguistics, {ACL} 2020, Online, July 5-10, 2020},
  pages     = {7943--7960},
  publisher = {Association for Computational Linguistics},
  year      = {2020},
  url       = {https://www.aclweb.org/anthology/2020.acl-main.709/}
}
"""

_DESCRIPTION = """
WikiAuto provides a set of aligned sentences from English Wikipedia and
Simple English Wikipedia as a resource to train sentence simplification
systems. The authors first crowd-sourced a set of manual alignments between
sentences in a subset of the Simple English Wikipedia and their corresponding
versions in English Wikipedia (this corresponds to the `manual` config),
then trained a neural CRF system to predict these alignments. The trained
model was then applied to the other articles in Simple English Wikipedia
with an English counterpart to create a larger corpus of aligned sentences
(corresponding to the `auto`, `auto_acl`, `auto_full_no_split`, and
`auto_full_with_split` configs here).
"""

_URLs = {
    'manual': {
        'dev':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-manual/dev.tsv',
        'test':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-manual/test.tsv',
    },
    'auto_acl': {
        'normal':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/ACL2020/train.src',
        'simple':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/ACL2020/train.dst',
    },
    'auto_full_no_split': {
        'normal':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_no_split/train.src',
        'simple':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_no_split/train.dst',
    },
    'auto_full_with_split': {
        'normal':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_with_split/train.src',
        'simple':
            'https://github.com/chaojiang06/wiki-auto/raw/master/wiki-auto/GEM2021/full_with_split/train.dst',
    },
    'auto': {
        'part_1':
            'https://dl.dropboxusercontent.com/sh/ohqaw41v48c7e5p/AAATBDhU1zpdcT5x5WgO8DMaa/wiki-auto-all-data/wiki-auto-part-1-data.json',
        'part_2':
            'https://dl.dropboxusercontent.com/sh/ohqaw41v48c7e5p/AAATgPkjo_tPt9z12vZxJ3MRa/wiki-auto-all-data/wiki-auto-part-2-data.json',
    },
}


class WikiAuto(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wiki_auto dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name='manual',
          description='A set of 10K Wikipedia sentence pairs aligned by crowd workers.'
      ),
      tfds.core.BuilderConfig(
          name='auto_acl',
          description='Sentence pairs aligned to train the ACL2020 system.'),
      tfds.core.BuilderConfig(
          name='auto_full_no_split',
          description='All automatically aligned sentence pairs without sentence splitting.'
      ),
      tfds.core.BuilderConfig(
          name='auto_full_with_split',
          description='All automatically aligned sentence pairs with sentence splitting.'
      ),
      tfds.core.BuilderConfig(
          name='auto',
          description='A large set of automatically aligned sentence pairs.')
  ]
  DEFAULT_CONFIG_NAME = 'auto'

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""

    if self.builder_config.name == 'manual':
      features = tfds.features.FeaturesDict({
          'alignment_label':
              tfds.features.ClassLabel(
                  names=['notAligned', 'aligned', 'partialAligned']),
          'normal_sentence_id':
              tfds.features.Text(),
          'simple_sentence_id':
              tfds.features.Text(),
          'normal_sentence':
              tfds.features.Text(),
          'simple_sentence':
              tfds.features.Text(),
          'GLEU-score':
              tf.float64,
      })
    elif (self.builder_config.name == 'auto_acl' or
          self.builder_config.name == 'auto_full_no_split' or
          self.builder_config.name == 'auto_full_with_split'):
      features = tfds.features.FeaturesDict({
          'normal_sentence': tfds.features.Text(),
          'simple_sentence': tfds.features.Text(),
      })
    else:
      features = tfds.features.FeaturesDict({
          'example_id':
              tfds.features.Text(),
          'normal': {
              'normal_article_id':
                  tf.int32,
              'normal_article_title':
                  tfds.features.Text(),
              'normal_article_url':
                  tfds.features.Text(),
              'normal_article_content':
                  tfds.features.Sequence({
                      'normal_sentence_id': tfds.features.Text(),
                      'normal_sentence': tfds.features.Text(),
                  }),
          },
          'simple': {
              'simple_article_id':
                  tf.int32,
              'simple_article_title':
                  tfds.features.Text(),
              'simple_article_url':
                  tfds.features.Text(),
              'simple_article_content':
                  tfds.features.Sequence({
                      'simple_sentence_id': tfds.features.Text(),
                      'simple_sentence': tfds.features.Text(),
                  }),
          },
          'paragraph_alignment':
              tfds.features.Sequence({
                  'normal_paragraph_id': tfds.features.Text(),
                  'simple_paragraph_id': tfds.features.Text(),
              }),
          'sentence_alignment':
              tfds.features.Sequence({
                  'normal_sentence_id': tfds.features.Text(),
                  'simple_sentence_id': tfds.features.Text(),
              }),
      })
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        supervised_keys=None,
        homepage='https://github.com/chaojiang06/wiki-auto',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    urls_to_download = _URLs[self.builder_config.name]
    data_dir = dl_manager.download_and_extract(urls_to_download)
    if self.builder_config.name in ['manual', 'auto']:
      return {
          spl: self._generate_examples(filepaths=data_dir, split=spl)
          for spl in data_dir
      }
    else:
      return {'full': self._generate_examples(filepaths=data_dir, split='full')}

  def _generate_examples(self, filepaths, split):
    """Yields examples."""

    if self.builder_config.name == 'manual':
      keys = [
          'alignment_label', 'simple_sentence_id', 'normal_sentence_id',
          'simple_sentence', 'normal_sentence', 'GLEU-score'
      ]

      with tf.io.gfile.GFile(filepaths[split]) as f:
        for id_, line in enumerate(f):
          values = line.strip().split('\t')
          dict_ = {}
          for k, v in zip(keys, values):
            dict_[k] = v
          yield id_, dict_

    elif (self.builder_config.name == 'auto_acl' or
          self.builder_config.name == 'auto_full_no_split' or
          self.builder_config.name == 'auto_full_with_split'):
      with tf.io.gfile.GFile(filepaths['normal']) as fi:
        with tf.io.gfile.GFile(filepaths['simple']) as fo:
          for id_, (norm_se, simp_se) in enumerate(zip(fi, fo)):
            yield id_, {
                'normal_sentence': norm_se,
                'simple_sentence': simp_se,
            }
    else:
      dataset_dict = json.load(tf.io.gfile.GFile(filepaths[split]))
      for id_, (eid, example_dict) in enumerate(dataset_dict.items()):
        res = {
            'example_id': eid,
            'normal': {
                'normal_article_id': example_dict['normal']['id'],
                'normal_article_title': example_dict['normal']['title'],
                'normal_article_url': example_dict['normal']['url'],
                'normal_article_content': {
                    'normal_sentence_id': [
                        sen_id for sen_id, sen_txt in example_dict['normal']
                        ['content'].items()
                    ],
                    'normal_sentence': [
                        sen_txt for sen_id, sen_txt in example_dict['normal']
                        ['content'].items()
                    ],
                },
            },
            'simple': {
                'simple_article_id': example_dict['simple']['id'],
                'simple_article_title': example_dict['simple']['title'],
                'simple_article_url': example_dict['simple']['url'],
                'simple_article_content': {
                    'simple_sentence_id': [
                        sen_id for sen_id, sen_txt in example_dict['simple']
                        ['content'].items()
                    ],
                    'simple_sentence': [
                        sen_txt for sen_id, sen_txt in example_dict['simple']
                        ['content'].items()
                    ],
                },
            },
            'paragraph_alignment': {
                'normal_paragraph_id': [
                    norm_id for simp_id, norm_id in example_dict.get(
                        'paragraph_alignment', [])
                ],
                'simple_paragraph_id': [
                    simp_id for simp_id, norm_id in example_dict.get(
                        'paragraph_alignment', [])
                ],
            },
            'sentence_alignment': {
                'normal_sentence_id': [
                    norm_id for simp_id, norm_id in example_dict.get(
                        'sentence_alignment', [])
                ],
                'simple_sentence_id': [
                    simp_id for simp_id, norm_id in example_dict.get(
                        'sentence_alignment', [])
                ],
            },
        }
        yield id_, res

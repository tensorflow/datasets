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

"""asqa dataset."""
import json

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
ASQA is the first long-form question answering dataset that focuses on ambiguous
factoid questions. Different from previous long-form answers datasets, each
question is annotated with both long-form answers and extractive question-answer
pairs, which should be answerable by the generated passage. A generated
long-form answer will be evaluated using both ROUGE and QA accuracy. We showed
that these evaluation metrics correlated with human judgment well. In this
repostory we release the ASQA dataset, together with the evaluation code:
`https://github.com/google-research/language/tree/master/language/asqa`
"""

_CITATION = """
@misc{https://doi.org/10.48550/arxiv.2204.06092,
doi = {10.48550/ARXIV.2204.06092},
url = {https://arxiv.org/abs/2204.06092},
author = {Stelmakh, Ivan and Luan, Yi and Dhingra, Bhuwan and Chang, Ming-Wei},
keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
title = {ASQA: Factoid Questions Meet Long-Form Answers},
publisher = {arXiv},
year = {2022},
copyright = {arXiv.org perpetual, non-exclusive license}
}
"""

_FEATURES = tfds.features.FeaturesDict({
    'sample_id':
        tf.int32,
    'ambiguous_question':
        tfds.features.Text(doc='Disambiguated question from AmbigQA.'),
    'qa_pairs':
        tfds.features.Sequence(
            tfds.features.FeaturesDict({
                'question':
                    tfds.features.Text(),
                'short_answers':
                    tfds.features.Sequence(
                        tfds.features.Text(),
                        doc='List of short answers from AmbigQA.'),
                'context':
                    tfds.features.Text(doc='Additional context provided.'),
                'wikipage':
                    tfds.features.Text(
                        doc='Title of the Wikipedia page the additional context was taken from.'
                    ),
            }),
            doc='Q&A pairs from AmbigQA which are used for disambiguation.'),
    'wikipages':
        tfds.features.Sequence(
            tfds.features.FeaturesDict({
                'title': tfds.features.Text(doc='Title of the Wikipedia page.'),
                'url': tfds.features.Text(doc='Link to the Wikipedia page.'),
            }),
            doc='List of Wikipedia pages visited by AmbigQA annotators.'),
    'annotations':
        tfds.features.Sequence(
            tfds.features.FeaturesDict({
                'long_answer':
                    tfds.features.Text(doc='Annotation.'),
                'knowledge':
                    tfds.features.Sequence(
                        tfds.features.FeaturesDict({
                            'content':
                                tfds.features.Text(
                                    doc='A passage from Wikipedia.'),
                            'wikipage':
                                tfds.features.Text(
                                    doc='Title of the Wikipedia page the passage was taken from.'
                                ),
                        }),
                        doc='List of additional knowledge pieces.'),
            }),
            doc='Long-form answers to the ambiguous question constructed by ASQA annotators.'
        ),
})


class Asqa(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for asqa dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=_FEATURES,
        supervised_keys=None,
        homepage='https://github.com/google-research/language/tree/master/language/asqa',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    file_path = dl_manager.download(
        'https://storage.googleapis.com/gresearch/ASQA/ASQA.json')

    with tf.io.gfile.GFile(file_path, 'r') as f:
      samples = json.load(f)

    return {
        'train': self._generate_examples(samples['train']),
        'dev': self._generate_examples(samples['dev']),
    }

  def _generate_examples(self, split_samples):
    """Yields examples."""

    def _add_feature(tfds_sample, split_sample, key):
      value = split_sample[key] if split_sample[key] else ''
      tfds_sample[key] = value

    def _iterate_and_add_features_in_dict(raw_sample_element,
                                          tfds_sample_element, feature_list):
      for element in raw_sample_element:
        tfds_dict = {}
        for feature in feature_list:
          _add_feature(tfds_dict, element, feature)
        tfds_sample_element.append(tfds_dict)

    for sample_id, split_sample in split_samples.items():
      tfds_sample = {
          'sample_id': sample_id,
          'ambiguous_question': split_sample['ambiguous_question'],
          'qa_pairs': [],
          'wikipages': [],
          'annotations': [],
      }

      # Add QA pairs.
      _iterate_and_add_features_in_dict(
          raw_sample_element=split_sample['qa_pairs'],
          tfds_sample_element=tfds_sample['qa_pairs'],
          feature_list=['question', 'short_answers', 'context', 'wikipage'])

      # Add Wikipages.
      for _, wikipage_info in split_sample['wikipages'].items():
        tfds_wikipage = {}
        _add_feature(tfds_wikipage, wikipage_info, 'title')
        _add_feature(tfds_wikipage, wikipage_info, 'url')
        tfds_sample['wikipages'].append(tfds_wikipage)

      # Add annotations.
      for annotation in split_sample['annotations']:
        tfds_annotation = {}
        _add_feature(tfds_annotation, annotation, 'long_answer')
        tfds_annotation['knowledge'] = []
        _iterate_and_add_features_in_dict(
            raw_sample_element=annotation['knowledge'],
            tfds_sample_element=tfds_annotation['knowledge'],
            feature_list=['content', 'wikipage'])
        tfds_sample['annotations'].append(tfds_annotation)

      yield sample_id, tfds_sample

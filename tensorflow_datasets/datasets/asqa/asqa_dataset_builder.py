# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


def _features():
  return tfds.features.FeaturesDict({
      'sample_id': np.int64,
      'ambiguous_question': tfds.features.Text(
          doc='Disambiguated question from AmbigQA.'
      ),
      'qa_pairs': tfds.features.Sequence(
          tfds.features.FeaturesDict({
              'question': tfds.features.Text(),
              'short_answers': tfds.features.Sequence(
                  tfds.features.Text(),
                  doc='List of short answers from AmbigQA.',
              ),
              'context': tfds.features.Text(doc='Additional context provided.'),
              'wikipage': tfds.features.Text(
                  doc=(
                      'Title of the Wikipedia page the additional context was'
                      ' taken from.'
                  )
              ),
          }),
          doc='Q&A pairs from AmbigQA which are used for disambiguation.',
      ),
      'wikipages': tfds.features.Sequence(
          tfds.features.FeaturesDict({
              'title': tfds.features.Text(doc='Title of the Wikipedia page.'),
              'url': tfds.features.Text(doc='Link to the Wikipedia page.'),
          }),
          doc='List of Wikipedia pages visited by AmbigQA annotators.',
      ),
      'annotations': tfds.features.Sequence(
          tfds.features.FeaturesDict({
              'long_answer': tfds.features.Text(doc='Annotation.'),
              'knowledge': tfds.features.Sequence(
                  tfds.features.FeaturesDict({
                      'content': tfds.features.Text(
                          doc='A passage from Wikipedia.'
                      ),
                      'wikipage': tfds.features.Text(
                          doc=(
                              'Title of the Wikipedia page the passage was'
                              ' taken from.'
                          )
                      ),
                  }),
                  doc='List of additional knowledge pieces.',
              ),
          }),
          doc=(
              'Long-form answers to the ambiguous question constructed by ASQA'
              ' annotators.'
          ),
      ),
  })


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for asqa dataset."""

  VERSION = tfds.core.Version('2.0.0')
  RELEASE_NOTES = {
      '2.0.0': 'Sample ID goes from int32 (overflowing) to int64.',
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=_features(),
        supervised_keys=None,
        homepage='https://github.com/google-research/language/tree/master/language/asqa',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    file_path = dl_manager.download(
        'https://storage.googleapis.com/gresearch/ASQA/ASQA.json'
    )

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

    def _iterate_and_add_features_in_dict(
        raw_sample_element, tfds_sample_element, feature_list
    ):
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
          feature_list=['question', 'short_answers', 'context', 'wikipage'],
      )

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
            feature_list=['content', 'wikipage'],
        )
        tfds_sample['annotations'].append(tfds_annotation)

      yield sample_id, tfds_sample

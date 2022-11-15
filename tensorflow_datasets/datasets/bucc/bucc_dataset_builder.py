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

"""bucc dataset."""
import csv
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_LANGS = ['de', 'fr', 'zh', 'ru']

_DATA_URLS = 'https://comparable.limsi.fr/bucc2018/'


class BuccConfig(tfds.core.BuilderConfig):
  """Configuration Class for Tatoeba."""

  def __init__(self, *, language, **kwargs):
    if language not in _LANGS:
      raise ValueError('language must be one of {}'.format(_LANGS))

    super(BuccConfig, self).__init__(**kwargs)
    self.language = language


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for bucc dataset."""
  BUILDER_CONFIGS = [
      BuccConfig(  # pylint: disable=g-complex-comprehension
          name='bucc_' + language,
          language=language,
      ) for language in _LANGS
  ]
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'source_sentence': tfds.features.Text(),
            'target_sentence': tfds.features.Text(),
            'source_id': tfds.features.Text(),
            'target_id': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://comparable.limsi.fr/bucc2018/',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    bucc_test_path = os.path.join(
        _DATA_URLS, 'bucc2018-{}-en.training-gold.tar.bz2'.format(
            self.builder_config.language))
    bucc_dev_path = os.path.join(
        _DATA_URLS, 'bucc2018-{}-en.sample-gold.tar.bz2'.format(
            self.builder_config.language))

    archive = dl_manager.download_and_extract({
        'bucc_test_dir': bucc_test_path,
        'bucc_dev_dir': bucc_dev_path
    })

    return {
        'validation':
            self._generate_examples(
                filepath=os.path.join(archive['bucc_dev_dir'], 'bucc2018',
                                      self.builder_config.language + '-en')),
        'test':
            self._generate_examples(
                filepath=os.path.join(archive['bucc_test_dir'], 'bucc2018',
                                      self.builder_config.language + '-en')),
    }

  def _generate_examples(self, filepath):
    """Yields examples."""
    files = sorted(tf.io.gfile.listdir(filepath))
    target_file = '/'
    source_file = '/'
    source_target_file = '/'
    for file in files:
      if file.endswith('en'):
        target_file = os.path.join(filepath, file)
      elif file.endswith('gold'):
        source_target_file = os.path.join(filepath, file)
      else:
        source_file = os.path.join(filepath, file)

    with epath.Path(target_file).open() as f:
      data = csv.reader(f, delimiter='\t')
      target_sentences = list(data)
    with epath.Path(source_file).open() as f:
      data = csv.reader(f, delimiter='\t')
      source_sentences = list(data)
    with epath.Path(source_target_file).open() as f:
      data = csv.reader(f, delimiter='\t')
      source_target_ids = list(data)
    for id_, pair in enumerate(source_target_ids):
      source_id = pair[0]
      target_id = pair[1]
      source_sent = ''
      target_sent = ''
      for i in range(len(source_sentences)):
        if source_sentences[i][0] == source_id:
          source_sent = source_sentences[i][1]
          source_id = source_sentences[i][0]
          break
      for j in range(len(target_sentences)):
        if target_sentences[j][0] == target_id:
          target_sent = target_sentences[j][1]
          target_id = target_sentences[j][0]
          break
      yield id_, {
          'source_sentence': source_sent,
          'target_sentence': target_sent,
          'source_id': source_id,
          'target_id': target_id,
      }

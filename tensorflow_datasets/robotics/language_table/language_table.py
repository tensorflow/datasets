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

"""language_table dataset."""

from typing import Any

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_DESCRIPTION = """
Datasets for [Language Table](https://github.com/google-research/language-table).
"""

_CITATION = """
@article{lynch2022interactive,
  title={Interactive Language: Talking to Robots in Real Time},
  author={Lynch, Corey and Wahid, Ayzaan and Tompson, Jonathan and Ding, Tianli and Betker, James and Baruch, Robert and Armstrong, Travis and Florence, Pete},
  journal={arXiv preprint arXiv:2210.06407},
  year={2022}
}
"""

_BUILDER_CONFIGS = [
    tfds.core.BuilderConfig(
        name='real',
        description=('Language-Table episodes on the real robot.')),
    tfds.core.BuilderConfig(
        name='sim', description=('Language-Table episodes in simulation.')),
    tfds.core.BuilderConfig(
        name='blocktoblock_sim',
        description=('Language-Table episodes in simulation for a single '
                     'block to block task.')),
    tfds.core.BuilderConfig(
        name='blocktoblock_4block_sim',
        description=('Language-Table episodes in simulation for a single '
                     '`block to block` task in a 4-block configuration.')),
    tfds.core.BuilderConfig(
        name='blocktoblock_oracle_sim',
        description=('Language-Table episodes in simulation for a single '
                     '`block to block` task with a scripted oracle.')),
    tfds.core.BuilderConfig(
        name='blocktoabsolute_oracle_sim',
        description=(
            'Language-Table episodes in simulation for a single `'
            'block to absolute location` task with a scripted oracle.')),
    tfds.core.BuilderConfig(
        name='blocktorelative_oracle_sim',
        description=(
            'Language-Table episodes in simulation for a single '
            '`block to relative location` task with a scripted oracle.')),
    tfds.core.BuilderConfig(
        name='blocktoblockrelative_oracle_sim',
        description=(
            'Language-Table episodes in simulation for a single '
            '`block to block relative location` task with a scripted oracle.')),
    tfds.core.BuilderConfig(
        name='separate_oracle_sim',
        description=('Language-Table episodes in simulation for a single '
                     '`separate blocks` task with a scripted oracle.')),
]


def _ds_name_to_directory(prefix: str, ds_name: str):
  """Returns data directory given a prefix and ds_name."""
  if ds_name == 'real':
    prefix = f'{prefix}/language_table/0.0.1/'
  elif ds_name == 'sim':
    prefix = f'{prefix}/language_table_sim/0.0.1/'
  elif ds_name == 'blocktoblock_sim':
    prefix = f'{prefix}/language_table_blocktoblock_sim/0.0.1/'
  elif ds_name == 'blocktoblock_4block_sim':
    prefix = f'{prefix}/language_table_blocktoblock_4block_sim/0.0.1/'
  elif ds_name == 'blocktoblock_oracle_sim':
    prefix = f'{prefix}/language_table_blocktoblock_oracle_sim/0.0.1/'
  elif ds_name == 'blocktoabsolute_oracle_sim':
    prefix = f'{prefix}/language_table_blocktoabsolute_oracle_sim/0.0.1/'
  elif ds_name == 'blocktorelative_oracle_sim':
    prefix = f'{prefix}/language_table_blocktorelative_oracle_sim/0.0.1/'
  elif ds_name == 'blocktoblockrelative_oracle_sim':
    prefix = f'{prefix}/language_table_blocktoblockrelative_oracle_sim/0.0.1/'
  elif ds_name == 'separate_oracle_sim':
    prefix = f'{prefix}/language_table_separate_oracle_sim/0.0.1/'
  else:
    raise ValueError('Unrecognized dataset name for Language-Table: %s' %
                     ds_name)
  return prefix


def _steps_features():
  return tfds.features.Dataset({
      'action':
          tfds.features.Tensor(shape=(2,), dtype=tf.float32),
      'is_first':
          tf.bool,
      'is_last':
          tf.bool,
      'is_terminal':
          tf.bool,
      'observation':
          tfds.features.FeaturesDict({
              'effector_target_translation':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float32),
              'effector_translation':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float32),
              'instruction':
                  tfds.features.Tensor(shape=(512,), dtype=tf.int32),
              'rgb':
                  tfds.features.Image(shape=(360, 640, 3), dtype=tf.uint8),
          }),
      'reward':
          tfds.features.Scalar(dtype=tf.float32),
  })


def _features():
  return tfds.features.FeaturesDict({
      'episode_id': tf.string,
      'steps': _steps_features(),
  })


# To encode, we use sequence instead of nested dataset. Otherwise, Beam has
# issues calculating the size of the yielded examples (b/219881125)
def _features_encode():
  return tfds.features.FeaturesDict({
      'episode_id': tf.string,
      'steps': tfds.features.Sequence(_steps_features()),
  })


class LanguageTable(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for language_table dataset."""

  VERSION = tfds.core.Version('0.0.1')
  RELEASE_NOTES = {
      '0.0.1': 'Initial release.',
  }
  BUILDER_CONFIGS = _BUILDER_CONFIGS
  _INPUT_FILE_PREFIX = 'gs://gresearch/robotics/'


  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        description=_DESCRIPTION,
        citation=_CITATION,
        features=_features(),
        supervised_keys=None,
        homepage='https://github.com/google-research/language-table',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_name = self.builder_config.name
    paths = {
        'file_paths': _ds_name_to_directory(self._INPUT_FILE_PREFIX, ds_name)
    }
    splits = {
        'train': self._generate_examples(paths),
    }
    return splits

  def _generate_examples_with_key(self, example):
    yield example['episode_id'], example

  def _generate_examples(self, paths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    file_paths = paths['file_paths']
    builder = tfds.builder_from_directory(file_paths)

    return tfds.beam.ReadFromTFDS(
        builder, split='train',
        decoders={'steps': tfds.decode.SkipDecoding()}) | beam.FlatMap(
            self._generate_examples_with_key) | beam.Map(tfds.as_numpy)

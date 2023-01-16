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

"""SummScreen Summarization dataset, non-anonymized, non-tokenized version."""

import json
import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DL_URLS = {
    # pylint: disable=line-too-long
    'tokenized': 'https://drive.google.com/uc?export=download&id=1BvdIllGBo9d2-bzXQRzWuJXB04XPVmfF',
    'untokenized': 'https://drive.google.com/uc?export=download&id=1tFpt32USOO2i1FWhtFTsyYyFzuRm2k36',
    # pylint: enable=line-too-long
}

_RECAP = 'recap'
_TRANSCRIPT = 'transcript'
_RECAP_SOURCE_FULL_NAMES = {
    'fd': 'ForeverDreaming',
    'tms': 'TVMegaSite',
}
_SPLITS = ['train', 'dev', 'test']


def _load_file(path):
  with tf.io.gfile.GFile(path, 'r') as f:
    return f.read()


def _load_json(path):
  return json.loads(_load_file(path))


def _load_jsonl(path):
  return [json.loads(line) for line in _load_file(path).strip().splitlines()]


def _get_filenames_dict(tokenized_path, recap_source: str):
  """Get dictionary of filenames for each split."""
  filenames_dict = {}
  for split in _SPLITS:
    tokenized_data = _load_jsonl(
        os.path.join(
            tokenized_path,
            'SummScreen',
            _RECAP_SOURCE_FULL_NAMES[recap_source],
            f'{recap_source}_{split}.json',
        )
    )
    filenames_dict[split] = [row['filename'] for row in tokenized_data]
  return filenames_dict


def _get_paths_dict(untokenized_path, recap_source, filenames_dict):
  """Get dictionary of example paths for each split."""
  paths_dict = {}
  for split, filenames in filenames_dict.items():
    paths_dict[split] = [
        os.path.join(untokenized_path, 'SummScreen_raw', recap_source, filename)
        for filename in filenames
    ]
  return paths_dict


class SummscreenConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Summscreen."""

  def __init__(self, *, recap_source=None, **kwargs):
    """BuilderConfig for Summscreen.

    Args:
      recap_source: str. The directory for the source of recaps to read.
      **kwargs: keyword arguments forwarded to super.
    """
    super(SummscreenConfig, self).__init__(**kwargs)
    self.recap_source = recap_source


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for non-tokenized, non-anonymized SummScreen dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
      SummscreenConfig(
          name='fd',
          description='ForeverDreaming',
          recap_source='fd',
      ),
      SummscreenConfig(
          name='tms',
          description='TVMegaSite',
          recap_source='tms',
      ),
  ]

  def _info(self):
    # Should return a tfds.core.DatasetInfo object
    if self._builder_config.recap_source == 'fd':
      features = tfds.features.FeaturesDict({
          _TRANSCRIPT: tfds.features.Text(),
          _RECAP: tfds.features.Text(),
          'episode_number': tfds.features.Text(),
          'episode_title': tfds.features.Text(),
          'show_title': tfds.features.Text(),
          'transcript_author': tfds.features.Text(),
      })
    elif self._builder_config.recap_source == 'tms':
      features = tfds.features.FeaturesDict({
          _TRANSCRIPT: tfds.features.Text(),
          _RECAP: tfds.features.Text(),
          'episode_summary': tfds.features.Text(),
          'show_title': tfds.features.Text(),
          'transcript_author': tfds.features.Tensor(
              shape=(None,), dtype=np.str_
          ),
          'recap_author': tfds.features.Text(),
      })
    else:
      raise KeyError(
          f'Unknown recap_source {self._builder_config.recap_source}'
      )

    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=(_TRANSCRIPT, _RECAP),
        homepage='https://github.com/mingdachen/SummScreen',
    )

  def _split_generators(self, dl_manager):
    dl_paths = dl_manager.download_and_extract(_DL_URLS)
    filenames_dict = _get_filenames_dict(
        tokenized_path=dl_paths['tokenized'],
        recap_source=self._builder_config.recap_source,
    )
    paths_dict = _get_paths_dict(
        untokenized_path=dl_paths['untokenized'],
        recap_source=self._builder_config.recap_source,
        filenames_dict=filenames_dict,
    )
    return {
        'train': self._generate_examples(paths=paths_dict['train']),
        'validation': self._generate_examples(paths=paths_dict['dev']),
        'test': self._generate_examples(paths=paths_dict['test']),
    }

  def _generate_examples(self, paths):
    for path in paths:
      example = _load_json(path)
      fname = os.path.basename(path)
      if self._builder_config.recap_source == 'fd':
        yield fname, {
            _TRANSCRIPT: '\n'.join(example['Transcript']),
            _RECAP: '\n'.join(example['Recap']),
            'episode_number': example['Episode Number'],
            'episode_title': example['Episode Title'],
            'show_title': example['Show Title'],
            'transcript_author': example['Transcript Author'],
        }
      elif self._builder_config.recap_source == 'tms':
        yield fname, {
            _TRANSCRIPT: '\n'.join(example['Transcript']),
            _RECAP: '\n'.join(example['Recap']),
            'episode_summary': '\n'.join(example['Episode Summary']),
            'show_title': example['Show Title'],
            'transcript_author': example['Transcript Author'],
            'recap_author': example['Recap Author'],
        }
      else:
        raise KeyError(
            f'Unknown recap_source {self._builder_config.recap_source}'
        )

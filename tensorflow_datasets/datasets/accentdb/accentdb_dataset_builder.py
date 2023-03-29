# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""AccentDB dataset."""

from __future__ import annotations

import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_LABELS = [
    'american',
    'australian',
    'bangla',
    'british',
    'indian',
    'malayalam',
    'odiya',
    'telugu',
    'welsh',
]

_DOWNLOAD_URL = 'https://drive.google.com/uc?export=download&id=1NO1NKQSpyq3DMLEwiqA-BHIqXli8vtIL'


class Builder(tfds.core.GeneratorBasedBuilder):
  """AccentDB dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=44100),
            'label': tfds.features.ClassLabel(names=_LABELS),
            'speaker_id': np.str_,
        }),
        supervised_keys=('audio', 'label'),
        homepage='https://accentdb.github.io/',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extract_path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'extract_path': extract_path},
        ),
    ]

  def _generate_examples(self, extract_path):
    """Yields examples."""
    data_path = os.path.join(extract_path, 'data')
    for accent in tf.io.gfile.listdir(data_path):
      accent_path = os.path.join(data_path, accent)
      for speaker in tf.io.gfile.listdir(accent_path):
        speaker_path = os.path.join(accent_path, speaker)
        speaker_id = f'{accent}_{speaker}'
        for file in tf.io.gfile.listdir(speaker_path):
          filepath = os.path.join(speaker_path, file)
          key = f'{accent}_{speaker}_{file}'
          yield key, {
              'audio': filepath,
              'label': accent,
              'speaker_id': speaker_id,
          }

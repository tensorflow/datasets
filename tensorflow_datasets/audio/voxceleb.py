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

"""The audio part of VoxCeleb dataset."""

import collections
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@InProceedings{Nagrani17,
	author       = "Nagrani, A. and Chung, J.~S. and Zisserman, A.",
	title        = "VoxCeleb: a large-scale speaker identification dataset",
	booktitle    = "INTERSPEECH",
	year         = "2017",
}
"""

_DESCRIPTION = """
An large scale dataset for speaker identification. This data is collected from
over 1,251 speakers, with over 150k samples in total.
This release contains the audio part of the voxceleb1.1 dataset.
"""

_HOMEPAGE = 'http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html'

IDEN_SPLITS_URL = (
    'http://www.robots.ox.ac.uk/~vgg/data/voxceleb/meta/iden_split.txt'
)
NUM_CLASSES = 1252


class Voxceleb(tfds.core.GeneratorBasedBuilder):
  """The VoxCeleb dataset for speaker identification."""

  VERSION = tfds.core.Version('1.2.1')

  RELEASE_NOTES = {'1.2.1': 'Add youtube_id field'}

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  manual_dir should contain the file vox_dev_wav.zip. The instructions for
  downloading this file are found in {}. This dataset requires registration.
  """.format(
      _HOMEPAGE
  )

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=16000),
            'label': tfds.features.ClassLabel(num_classes=NUM_CLASSES),
            'youtube_id': tfds.features.Text(),
        }),
        supervised_keys=('audio', 'label'),
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    zip_path = os.path.join(dl_manager.manual_dir, 'vox_dev_wav.zip')
    if not tf.io.gfile.exists(zip_path):
      raise AssertionError(
          'VoxCeleb requires manual download of the data. Please download '
          'the audio data and place it into: {}'.format(zip_path)
      )
    # Need to extract instead of reading directly from archive since reading
    # audio files from zip archive is not supported.
    extract_path = dl_manager.extract(zip_path)

    # Download the file defining the train/validation/test split on speakers.
    iden_splits_path = dl_manager.download({'iden_split': IDEN_SPLITS_URL})
    iden_splits = self._calculate_splits(iden_splits_path['iden_split'])

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'extract_path': extract_path,
                'file_names': iden_splits['train'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'extract_path': extract_path,
                'file_names': iden_splits['validation'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'extract_path': extract_path,
                'file_names': iden_splits['test'],
            },
        ),
    ]

  def _generate_examples(self, extract_path, file_names):
    """Yields examples."""
    for file_name in file_names:
      full_name = os.path.join(extract_path, 'wav', file_name)
      if not tf.io.gfile.exists(full_name):
        continue
      speaker, ytid, _ = file_name[: -len('.wav')].split('/')
      speaker_id = int(speaker[3:])
      example = {'audio': full_name, 'label': speaker_id, 'youtube_id': ytid}
      yield file_name, example

  def _calculate_splits(self, iden_splits_path):
    """Read the train/dev/test splits from VoxCeleb's iden_split.txt file."""
    data_splits = collections.defaultdict(set)
    with epath.Path(iden_splits_path).open() as f:
      for line in f:
        group, path = line.strip().split()
        split_name = {1: 'train', 2: 'validation', 3: 'test'}[int(group)]
        data_splits[split_name].add(path.strip())
    return data_splits

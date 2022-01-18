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

"""CREMA-D dataset."""

import collections
import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{cao2014crema,
  title={{CREMA-D}: Crowd-sourced emotional multimodal actors dataset},
  author={Cao, Houwei and Cooper, David G and Keutmann, Michael K and Gur, Ruben C and Nenkova, Ani and Verma, Ragini},
  journal={IEEE transactions on affective computing},
  volume={5},
  number={4},
  pages={377--390},
  year={2014},
  publisher={IEEE}
}
"""

_DESCRIPTION = """
CREMA-D is an audio-visual data set for emotion recognition. The data set
consists of facial and vocal emotional expressions in sentences spoken in a
range of basic emotional states (happy, sad, anger, fear, disgust, and neutral).
7,442 clips of 91 actors with diverse ethnic backgrounds were collected.
This release contains only the audio stream from the original audio-visual
recording.
The samples are splitted between train, validation and testing so that samples 
from each speaker belongs to exactly one split.
"""

_HOMEPAGE = 'https://github.com/CheyneyComputerScience/CREMA-D'

_CHECKSUMS_URL = 'https://storage.googleapis.com/tfds-data/manual_checksums/crema_d.txt'
SUMMARY_TABLE_URL = 'https://raw.githubusercontent.com/CheyneyComputerScience/CREMA-D/master/processedResults/summaryTable.csv'
WAV_DATA_URL = 'https://media.githubusercontent.com/media/CheyneyComputerScience/CREMA-D/master/AudioWAV/'
LABELS = ['NEU', 'HAP', 'SAD', 'ANG', 'FEA', 'DIS']


def _compute_split_boundaries(split_probs, n_items):
  """Computes boundary indices for each of the splits in split_probs.

  Args:
    split_probs: List of (split_name, prob), e.g. [('train', 0.6), ('dev', 0.2),
      ('test', 0.2)]
    n_items: Number of items we want to split.

  Returns:
    The item indices of boundaries between different splits. For the above
    example and n_items=100, these will be
    [('train', 0, 60), ('dev', 60, 80), ('test', 80, 100)].
  """
  if len(split_probs) > n_items:
    raise ValueError('Not enough items for the splits. There are {splits} '
                     'splits while there are only {items} items'.format(
                         splits=len(split_probs), items=n_items))
  total_probs = sum(p for name, p in split_probs)
  if abs(1 - total_probs) > 1E-8:
    raise ValueError('Probs should sum up to 1. probs={}'.format(split_probs))
  split_boundaries = []
  sum_p = 0.0
  for name, p in split_probs:
    prev = sum_p
    sum_p += p
    split_boundaries.append((name, int(prev * n_items), int(sum_p * n_items)))

  # Guard against rounding errors.
  split_boundaries[-1] = (split_boundaries[-1][0], split_boundaries[-1][1],
                          n_items)

  return split_boundaries


def _get_inter_splits_by_group(items_and_groups, split_probs, split_number):
  """Split items to train/dev/test, so all items in group go into same split.

  Each group contains all the samples from the same speaker ID. The samples are
  splitted between train, validation and testing so that samples from each
  speaker belongs to exactly one split.

  Args:
    items_and_groups: Sequence of (item_id, group_id) pairs.
    split_probs: List of (split_name, prob), e.g. [('train', 0.6), ('dev', 0.2),
      ('test', 0.2)]
    split_number: Generated splits should change with split_number.

  Returns:
    Dictionary that looks like {split name -> set(ids)}.
  """
  groups = sorted(set(group_id for item_id, group_id in items_and_groups))
  rng = np.random.RandomState(split_number)
  rng.shuffle(groups)

  split_boundaries = _compute_split_boundaries(split_probs, len(groups))
  group_id_to_split = {}
  for split_name, i_start, i_end in split_boundaries:
    for i in range(i_start, i_end):
      group_id_to_split[groups[i]] = split_name

  split_to_ids = collections.defaultdict(set)
  for item_id, group_id in items_and_groups:
    split = group_id_to_split[group_id]
    split_to_ids[split].add(item_id)

  return split_to_ids


class CremaD(tfds.core.GeneratorBasedBuilder):
  """The audio part of CREMA-D dataset for emotion recognition."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=16000),
            'label': tfds.features.ClassLabel(names=list(LABELS)),
            'speaker_id': tf.string
        }),
        supervised_keys=('audio', 'label'),
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_manager.download_checksums(_CHECKSUMS_URL)
    csv_path = dl_manager.download({'summary_table': SUMMARY_TABLE_URL})
    all_wav_files = []
    speaker_ids = []
    wav_names = []
    # These are file names which do do not exist in the github
    bad_files = set([
        'FileName', '1040_ITH_SAD_XX', '1006_TIE_NEU_XX', '1013_WSI_DIS_XX',
        '1017_IWW_FEA_XX'
    ])
    with tf.io.gfile.GFile(csv_path['summary_table']) as f:
      for line in f:
        wav_name = line.strip().split(',')[1].replace('"', '')
        if (not wav_name) or (wav_name in bad_files):
          continue
        wav_path = os.path.join(WAV_DATA_URL, '%s.wav' % wav_name)
        all_wav_files.append(wav_path)
        speaker_ids.append(wav_name.split('_')[0])
        wav_names.append(wav_name)
    all_wav_files = dl_manager.download({'all_files': all_wav_files})
    all_wav_files = list(zip(all_wav_files['all_files'], wav_names))
    wav_and_speaker_ids = list(zip(all_wav_files, speaker_ids))
    split_probs = [('train', 0.7), ('validation', 0.1), ('test', 0.2)]
    splits = _get_inter_splits_by_group(wav_and_speaker_ids, split_probs, 0)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'file_paths_and_names': splits['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'file_paths_and_names': splits['validation']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'file_paths_and_names': splits['test']},
        ),
    ]

  def _generate_examples(self, file_paths_and_names):
    """Yields examples."""
    for file_path, file_name in file_paths_and_names:
      speaker_id = file_name.split('_')[0]
      label = file_name.split('_')[2]
      example = {'audio': file_path, 'label': label, 'speaker_id': speaker_id}
      yield file_name, example

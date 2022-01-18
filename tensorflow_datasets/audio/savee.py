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

"""SAVEE dataset."""

import collections
import os
import re
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

LABEL_MAP = {
    'a': 'anger',
    'd': 'disgust',
    'f': 'fear',
    'h': 'happiness',
    'n': 'neutral',
    'sa': 'sadness',
    'su': 'surprise',
}

SPEAKERS = ['DC', 'JE', 'JK', 'KL']

_CITATION = """
@inproceedings{Vlasenko_combiningframe,
author = {Vlasenko, Bogdan and Schuller, Bjorn and Wendemuth, Andreas and Rigoll, Gerhard},
year = {2007},
month = {01},
pages = {2249-2252},
title = {Combining frame and turn-level information for robust recognition of emotions within speech},
journal = {Proceedings of Interspeech}
}
"""

_DESCRIPTION = """
SAVEE (Surrey Audio-Visual Expressed Emotion) is an emotion recognition
dataset. It consists of recordings from 4 male actors in 7 different emotions,
480 British English utterances in total. The sentences were chosen from the
standard TIMIT corpus and phonetically-balanced for each emotion.
This release contains only the audio stream from the original audio-visual
recording.
The data is split so that the training set consists of 2 speakers, and both the
validation and test set consists of samples from 1 speaker, respectively.
"""


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
  splitted so that all each speaker belongs to exactly one split.

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


class Savee(tfds.core.GeneratorBasedBuilder):
  """The audio part of SAVEE dataset for emotion recognition."""

  VERSION = tfds.core.Version('1.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain the file AudioData.zip. This file should be under
  Data/Zip/AudioData.zip in the dataset folder provided upon registration.
  You need to register at
  http://personal.ee.surrey.ac.uk/Personal/P.Jackson/SAVEE/Register.html in
  order to get the link to download the dataset.
  """

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=44100),
            'label': tfds.features.ClassLabel(names=list(LABEL_MAP.values())),
            'speaker_id': tf.string
        }),
        supervised_keys=('audio', 'label'),
        homepage='http://kahlan.eps.surrey.ac.uk/savee/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    zip_path = os.path.join(dl_manager.manual_dir, 'AudioData.zip')
    if not tf.io.gfile.exists(zip_path):
      raise AssertionError(
          'SAVEE requires manual download of the data. Please download '
          'the audio data and place it into: {}'.format(zip_path))
    # Need to extract instead of reading directly from archive since reading
    # audio files from zip archive is not supported.
    extract_path = dl_manager.extract(zip_path)

    items_and_groups = []
    for fname in tf.io.gfile.glob('{}/AudioData/*/*.wav'.format(extract_path)):
      folder, _ = os.path.split(fname)
      _, speaker_id = os.path.split(folder)
      items_and_groups.append((fname, speaker_id))

    split_probs = [('train', 0.6), ('validation', 0.2), ('test', 0.2)]
    splits = _get_inter_splits_by_group(items_and_groups, split_probs, 0)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'file_names': splits['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'file_names': splits['validation']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'file_names': splits['test']},
        ),
    ]

  def _generate_examples(self, file_names):
    """Yields examples."""
    for fname in file_names:
      folder, wavname = os.path.split(fname)
      _, speaker_id = os.path.split(folder)
      label_abbrev = re.match('^([a-zA-Z]+)', wavname).group(1)  # pytype: disable=attribute-error
      label = LABEL_MAP[label_abbrev]
      key = '{}_{}'.format(speaker_id, wavname.split('.')[0])
      yield key, {'audio': fname, 'label': label, 'speaker_id': speaker_id}

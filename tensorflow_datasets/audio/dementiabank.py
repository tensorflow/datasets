# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""DementiaBank dataset."""

import collections
import os
import textwrap
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{boller2005dementiabank,
  title={Dementiabank database guide},
  author={Boller, Francois and Becker, James},
  journal={University of Pittsburgh},
  year={2005}
}
"""

_DESCRIPTION = """
DementiaBank is a medical domain task. It contains 117 people diagnosed with
Alzheimer Disease, and 93 healthy people, reading a description of an image, and
the task is to classify these groups.
This release contains only the audio part of this dataset, without the text
features.
"""

_CONTROL_FOLDER = 'dementia/English/Pitt/Control/cookie'
_DEMENTIA_FOLDER = 'dementia/English/Pitt/Dementia/cookie'


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

  split_to_ids = collections.defaultdict(list)
  for item_id, group_id in items_and_groups:
    split = group_id_to_split[group_id]
    split_to_ids[split].append(item_id)

  return split_to_ids


class Dementiabank(tfds.core.GeneratorBasedBuilder):
  """The DementiaBank dataset for voice classification of Dementia."""

  VERSION = tfds.core.Version('1.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = textwrap.dedent("""
  manual dir should contain 2 folders with mp3 files:

  * {}
  * {}

  Which were downloaded from https://media.talkbank.org/dementia/English/Pitt/
  This dataset requires registration for downloading.
  """.format(_CONTROL_FOLDER, _DEMENTIA_FOLDER))

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='mp3', sample_rate=44100),
            'label': tfds.features.ClassLabel(names=['dementia', 'control']),
            'speaker_id': tf.string,
        }),
        supervised_keys=('audio', 'label'),
        homepage='https://dementia.talkbank.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    control_folder = os.path.join(dl_manager.manual_dir, _CONTROL_FOLDER)
    dementia_folder = os.path.join(dl_manager.manual_dir, _DEMENTIA_FOLDER)
    examples_and_speaker_ids = []
    for fname in tf.io.gfile.glob('{}/*.mp3'.format(control_folder)):
      _, short_name = os.path.split(fname)
      speaker_id, _ = short_name.split('-')
      example = {'audio': fname, 'label': 'control', 'speaker_id': speaker_id}
      examples_and_speaker_ids.append((example, speaker_id))
    for fname in tf.io.gfile.glob('{}/*.mp3'.format(dementia_folder)):
      _, short_name = os.path.split(fname)
      speaker_id, _ = short_name.split('-')
      example = {'audio': fname, 'label': 'dementia', 'speaker_id': speaker_id}
      examples_and_speaker_ids.append((example, speaker_id))
    split_probs = [('train', 0.7), ('validation', 0.1), ('test', 0.2)]
    splits = _get_inter_splits_by_group(examples_and_speaker_ids, split_probs,
                                        0)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'examples': splits['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'examples': splits['validation']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'examples': splits['test']},
        ),
    ]

  def _generate_examples(self, examples):
    """Yields examples."""
    for example in examples:
      _, key = os.path.split(example['audio'])
      yield key, example

# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""VoxForge dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import datetime
import io
import os
import textwrap
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{maclean2018voxforge,
  title={Voxforge},
  author={MacLean, Ken},
  journal={Ken MacLean.[Online]. Available: http://www.voxforge.org/home.[Acedido em 2012]},
  year={2018}
}
"""

_LAST_DATE = datetime.date(2020, 1, 1)

_DESCRIPTION = """
VoxForge is a language classification dataset. It consists of user submitted
audio clips submitted to the website. In this release, data from 6 languages
is collected - English, Spanish, French, German, Russian, and Italian.
Since the website is constantly updated, and for the sake of reproducibility,
this release contains only recordings submitted prior to {}.
The samples are splitted between train, validation and testing so that samples
from each speaker belongs to exactly one split.
""".format(_LAST_DATE.isoformat())

_HOMEPAGE = 'http://www.voxforge.org/'

_SAMPLE_RATE = 16000

_URLS_LIST_FILE = 'https://storage.googleapis.com/tfds-data/downloads/voxforge/voxforge_urls.txt'

LABELS = ['de', 'en', 'es', 'fr', 'it', 'ru']


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


def _wav_obj_to_samples(wav_obj):
  """Read a `tarfile.ExFileObject`."""
  sample_rate, samples = tfds.core.lazy_imports.scipy.io.wavfile.read(
      io.BytesIO(wav_obj.read()))
  return samples, sample_rate


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


class Voxforge(tfds.core.BeamBasedBuilder):
  """A Language classification dataset based on the VoxForge website."""

  VERSION = tfds.core.Version('1.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = textwrap.dedent("""
  VoxForge requires manual download of the audio archives. The complete list of
  archives can be found in {}. It can be downloaded using the following command:
  wget -i voxforge_urls.txt -x
  Note that downloading and building the dataset locally requires ~100GB disk
  space (but only ~60GB will be used permanently).
  """.format(_URLS_LIST_FILE))

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio':
                tfds.features.Audio(
                    file_format='wav', sample_rate=_SAMPLE_RATE),
            'label':
                tfds.features.ClassLabel(names=LABELS),
            'speaker_id':
                tf.string
        }),
        supervised_keys=('audio', 'label'),
        homepage=_HOMEPAGE,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    urls_list = dl_manager.download({'urls_list': _URLS_LIST_FILE})
    archive_urls = []
    with tf.io.gfile.GFile(urls_list['urls_list']) as f:
      for line in f:
        archive_url = line.strip().replace('"', '').replace('\'', '')
        archive_path = os.path.join(dl_manager.manual_dir, archive_url)
        if not tf.io.gfile.exists(archive_path):
          raise AssertionError(
              'VoxForge requires manual download. Path {} is missing'.format(
                  archive_path))
        archive_urls.append(archive_path)

    archives_and_speaker_ids = []
    for archive_url in archive_urls:
      _, archive_name = os.path.split(archive_url)
      speaker_id = archive_name.split('-')[0]
      archives_and_speaker_ids.append((archive_url, speaker_id))

    split_probs = [('train', 0.7), ('validation', 0.1), ('test', 0.2)]
    splits = _get_inter_splits_by_group(archives_and_speaker_ids, split_probs,
                                        0)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'file_names': splits['train'],
                'dl_manager': dl_manager
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'file_names': splits['validation'],
                'dl_manager': dl_manager
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'file_names': splits['test'],
                'dl_manager': dl_manager
            },
        ),
    ]

  def _build_pcollection(self, pipeline, file_names, dl_manager):
    """Build Pcollection of examples."""
    beam = tfds.core.lazy_imports.apache_beam
    return (pipeline
            | beam.Create(file_names)
            | beam.FlatMap(_generate_examples, dl_manager=dl_manager))


def _generate_examples(fname, dl_manager):
  """Yields examples."""
  folder, archive_name = os.path.split(fname)
  speaker_id = archive_name.split('-')[0]
  label_idx = folder.index('/Trunk') - 2
  label = folder[label_idx:label_idx + 2]
  iter_archive = dl_manager.iter_archive(fname)
  for wav_path, wav_obj in iter_archive:
    if not wav_path.endswith('.wav'):
      continue
    _, wav_name = os.path.split(wav_path)
    key = '{}_{}_{}'.format(label, archive_name, wav_name[:-len('.wav')])
    samples, sample_rate = _wav_obj_to_samples(wav_obj)
    if sample_rate != _SAMPLE_RATE:
      raise ValueError(
          f'Data sample rate was {sample_rate}, but must be {_SAMPLE_RATE}')
    yield key, {'audio': samples, 'label': label, 'speaker_id': speaker_id}

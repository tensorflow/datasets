"""AccentDB dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import numpy as np
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@InProceedings{ahamad-anand-bhargava:2020:LREC,
  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},
  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},
  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},
  month          = {May},
  year           = {2020},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5353--5360},
  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}
}
"""

_DESCRIPTION = """
AccentDB is a multi-pairwise parallel corpus of structured and labelled 
accented speech. It contains speech samples from speakers of 4 non-native 
accents of English (8 speakers, 4 Indian languages); and also has the 
compilation of 4 native accents of English (4 countries, 13 speakers) and a 
metropolitan Indian accent (2 speakers).
"""

_LABELS = ['american', 'australian', 'bangla', 'british', 'indian', 'malayalam', 
'odiya', 'telugu', 'welsh']

def _compute_split_boundaries(split_ratio, n_samples):
  """Computes boundary indices for each of the splits in split_ratio.
  Args:
    split_ratio: List of (split_name, prob), e.g. [('train', 0.7), 
    ('val', 0.15), ('test', 0.15)]
    n_samples: Number of samples we want to split.
  Returns:
    The sample indices of boundaries between different splits. For the above
    example and n_samples=100, these will be
    [('train', 0, 60), ('dev', 60, 80), ('test', 80, 100)].
  """
  if len(split_ratio) > n_samples:
    raise ValueError('Not enough samples for the splits. There are {splits} '
                     'splits while there are only {samples} samples'.format(
                         splits=len(split_ratio), samples=n_samples))
  total_probs = sum(p for name, p in split_ratio)
  if abs(1 - total_probs) > 1E-8:
    raise ValueError('Probs should sum up to 1. probs={}'.format(split_ratio))
  split_boundaries = []
  sum_p = 0.0
  for name, p in split_ratio:
    prev = sum_p
    sum_p += p
    split_boundaries.append(
      (name, int(prev * n_samples), int(sum_p * n_samples)))

  # Guard against rounding errors.
  split_boundaries[-1] = (split_boundaries[-1][0], split_boundaries[-1][1],
                          n_samples)

  return split_boundaries


def _get_split_sets(samples, split_ratio, seed):
  """
  Split samples into train/dev/test in the ratio specified by split_ratio.
  Args:
    samples: Sequence of (file, label, speaker_id) tuples.
    split_ratio: List of (split_name, ratio), e.g. [('train', 0.7), 
    ('val', 0.15), ('test', 0.15)]
    seed: For reproducibility while shuffling the samples.
  Returns:
    Dictionary that looks like {split name -> set(samples)}.
  """
  rng = np.random.RandomState(seed)
  rng.shuffle(samples)

  split_boundaries = _compute_split_boundaries(split_ratio, len(samples))
  split_to_ids = collections.defaultdict(set)

  for split_name, i_start, i_end in split_boundaries:
    for i in range(i_start, i_end):
      split_to_ids[split_name].add(samples[i])

  return split_to_ids


class Accentdb(tfds.core.GeneratorBasedBuilder):
  """AccentDB dataset, comprising 9 accents (4 non-native Indian accents, 
  collected by the authors, and 5 accents generated from using an online TTS 
  system described in the paper). The dataset used here corresponds to release 
  titled accentDB_extended."""

  VERSION = tfds.core.Version('1.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Please download the file accentDB_extended.tar.gz from the link below and 
  place it under the directory ~/tensorflow_datasets/downloads/manual.
  Link: https://drive.google.com/file/d/1NO1NKQSpyq3DMLEwiqA-BHIqXli8vtIL/view
  """

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=44100),
            'label': tfds.features.ClassLabel(names=_LABELS),
            'speaker_id': tf.string
        }),
        supervised_keys=('audio', 'label'),
        homepage='https://accentdb.github.io/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    zip_path = os.path.join(dl_manager.manual_dir, 'accentDB_extended.tar.gz')
    if not tf.io.gfile.exists(zip_path): 
      raise AssertionError(
          'AccentDB requires manual download of the data. Please download '
          'the audio data and place it into: {}'.format(zip_path))

    extract_path = dl_manager.extract(zip_path)
    samples = []
    for accent in tf.io.gfile.listdir('{}/data'.format(extract_path)):
      for speaker in tf.io.gfile.listdir(
        '{}/data/{}'.format(extract_path, accent)):
        speaker_id = '{}_{}'.format(accent, speaker)
        for file in tf.io.gfile.listdir(
          '{}/data/{}/{}'.format(extract_path, accent, speaker)):
          fname = '{}/data/{}/{}/{}'.format(extract_path, accent, speaker, file)
          samples.append((fname, accent, speaker_id))

    split_ratio = [('train', 0.7), ('validation', 0.15), ('test', 0.15)]
    splits = _get_split_sets(samples, split_ratio, seed=1337)

    return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN,
              gen_kwargs={'split_set': splits['train']},
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.VALIDATION,
              gen_kwargs={'split_set': splits['validation']},
          ),
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={'split_set': splits['test']},
          ),
      ]

  def _generate_examples(self, split_set):
    """Yields examples."""
    for sample in split_set:
      fname, accent, speaker_id = sample
      key = fname.split('.')[-2]
      yield key, {'audio': fname, 'label': accent, 'speaker_id': speaker_id}


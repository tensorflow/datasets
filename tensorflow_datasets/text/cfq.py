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

"""CFQ (Compositional Freebase Question) dataset."""

import json
import os
import re
from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Keysers2020,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers and Nathanael Sch\"{a}rli and Nathan Scales and
          Hylke Buisman and Daniel Furrer and Sergii Kashubin and
          Nikola Momchev and Danila Sinopalnikov and Lukasz Stafiniak and
          Tibor Tihon and Dmitry Tsarkov and Xiao Wang and Marc van Zee and
          Olivier Bousquet},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
"""

_DESCRIPTION = """
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

A note about the validation set: Since it has the same distribution as the test
set and we are interested in measuring the compositional generalization of a
*model* with respect to an *unknown* test distribution we suggest that any
tuning should be done on a subset of the train set only (see section 5.1 of the
paper).

Example usage:

```
data = tfds.load('cfq/mcd1')
```
"""

_DATA_URL = 'https://storage.googleapis.com/cfq_dataset/cfq.tar.gz'

_RANDOM_SEEDS = [
    '4_0', '4_42', '4.5_0', '4.5_45', '5_50', '5_50', '5.5_0', '5.5_55', '6_0'
]


class CFQConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CFQ splits."""

  def __init__(self,
               *,
               name=None,
               directory=None,
               compound_divergence=None,
               random_seed=None,
               **kwargs):
    """BuilderConfig for CFQ.

    Can be constucted in two ways:
    1. With directory and name in which case these determine the split file.
    2. With compound_divergence (and optionally random_seed).

    Args:
      name: Unique name of the split.
      directory: Which subdirectory to read the split from.
      compound_divergence: The desired compound divergence.
      random_seed: The random seed. Can be either the specific random-seeds used
        to generate the split as string or an index in the range [1, 9].
      **kwargs: keyword arguments forwarded to super.
    """
    if compound_divergence is not None:
      if random_seed is None:
        random_seed_index = 1
        random_seed = _RANDOM_SEEDS[0]
      elif random_seed in range(0, 10):
        random_seed_index = random_seed
        random_seed = _RANDOM_SEEDS[random_seed - 1]
      elif random_seed in _RANDOM_SEEDS:
        random_seed_index = _RANDOM_SEEDS.index(random_seed)
      else:
        raise ValueError('Invalid random seed: %s' % random_seed)
      directory = 'splits/all_divergence_splits'
      split_name = 'divergence_split_s0.4_d%s_r%s' % (compound_divergence,
                                                      random_seed)
      name = 'cd%s_r%s' % (compound_divergence, random_seed_index)
    else:
      directory = 'splits'
      split_name = name
    super(CFQConfig, self).__init__(
        name=name, version=tfds.core.Version('1.2.0'), **kwargs)
    self.split_file = os.path.join(directory, split_name + '.json')


_QUESTION = 'question'
_QUERY = 'query'
_QUESTION_FIELD = 'questionPatternModEntities'
_QUERY_FIELD = 'sparqlPatternModEntities'


def _generate_compound_divergence_builder_configs():
  """Generate configs for different compound divergences and random seeds."""
  configs = []
  for compound_divergence in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1]:
    for random_seed in range(1, 10):
      configs.append(
          CFQConfig(
              compound_divergence=compound_divergence, random_seed=random_seed))
  return configs


class CFQ(tfds.core.GeneratorBasedBuilder):
  """CFQ task / splits."""

  BUILDER_CONFIGS = [
      CFQConfig(name='mcd1'),
      CFQConfig(name='mcd2'),
      CFQConfig(name='mcd3'),
      CFQConfig(name='question_complexity_split'),
      CFQConfig(name='question_pattern_split'),
      CFQConfig(name='query_complexity_split'),
      CFQConfig(name='query_pattern_split'),
      CFQConfig(name='random_split'),
  ] + _generate_compound_divergence_builder_configs()

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _QUESTION: tfds.features.Text(),
            _QUERY: tfds.features.Text(),
        }),
        supervised_keys=(_QUESTION, _QUERY),
        homepage='https://github.com/google-research/google-research/tree/master/cfq',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(data_dir, 'cfq')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'base_directory': data_dir,
                'splits_file': self.builder_config.split_file,
                'split_id': 'trainIdxs'
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'base_directory': data_dir,
                'splits_file': self.builder_config.split_file,
                'split_id': 'devIdxs'
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'base_directory': data_dir,
                'splits_file': self.builder_config.split_file,
                'split_id': 'testIdxs'
            })
    ]

  def _scrub_json(self, content):
    """Reduce JSON by filtering out only the fields of interest."""
    # Loading of json data with the standard Python library is very inefficient:
    # For the 4GB dataset file it requires more than 40GB of RAM and takes 3min.
    # There are more efficient libraries but in order to avoid additional
    # dependencies we use a simple (perhaps somewhat brittle) regexp to reduce
    # the content to only what is needed. This takes 1min to execute but
    # afterwards loading requires only 500MB or RAM and is done in 2s.
    regex = re.compile(
        r'("%s":\s*"[^"]*").*?("%s":\s*"[^"]*")' %
        (_QUESTION_FIELD, _QUERY_FIELD), re.DOTALL)
    return '[' + ','.join([
        '{' + m.group(1) + ',' + m.group(2) + '}'
        for m in regex.finditer(content)
    ]) + ']'

  def _generate_examples(self, base_directory, splits_file, split_id):
    """Yields examples."""
    samples_path = os.path.join(base_directory, 'dataset.json')
    splits_path = os.path.join(base_directory, splits_file)
    with tf.io.gfile.GFile(samples_path) as samples_file:
      with tf.io.gfile.GFile(splits_path) as splits_file:
        logging.info('Reading json from %s into memory...', samples_path)
        samples = json.loads(self._scrub_json(samples_file.read()))
        logging.info('%d samples loaded', len(samples))
        logging.info('Loaded json data from %s.', samples_path)
        splits = json.load(splits_file)
        for idx in splits[split_id]:
          sample = samples[idx]
          yield idx, {
              _QUESTION: sample[_QUESTION_FIELD],
              _QUERY: sample[_QUERY_FIELD]
          }

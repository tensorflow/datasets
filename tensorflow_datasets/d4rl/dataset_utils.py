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

"""Utils to generate builders for D4RL datasets."""
from typing import Any, Dict

import h5py
import numpy as np
import tensorflow as tf

gfile = tf.io.gfile


_DESCRIPTION = """
D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.
"""

_CITATION = """\
@misc{fu2020d4rl,
    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},
    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
    year={2020},
    eprint={2004.07219},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""


def description():
  return _DESCRIPTION


def citation():
  return _CITATION


def url():
  return 'https://sites.google.com/view/d4rl/home'


def generate_examples(file_path: str):
  """Provides a common generate_examples method for D4RL datasets."""
  dataset_dict = read_d4rl_dataset(file_path)
  if 'timeouts' not in dataset_dict:
    raise ValueError('Only datasets with explicit timeouts are supported.')

  done = [
      terminal or timeout
      for (terminal,
           timeout) in zip(dataset_dict['terminals'], dataset_dict['timeouts'])
  ]
  # is_first corresponds to the done flag delayed by one step.
  dataset_dict['is_first'] = [True] + done[:-1]
  dataset_dict['is_last'] = done

  # Get step metadata
  infos_dict = _get_nested_metadata(dataset_dict, 'infos')

  # Flatten reward
  dataset_dict['rewards'] = np.squeeze(dataset_dict['rewards'])

  episode_metadata = _get_nested_metadata(dataset_dict, 'metadata')
  dataset_dict = {
      'observation': dataset_dict['observations'],
      'action': dataset_dict['actions'],
      'reward': dataset_dict['rewards'],
      'discount': np.ones_like(dataset_dict['rewards']),
      'is_terminal': dataset_dict['terminals'],
      'is_first': dataset_dict['is_first'],
      'is_last': dataset_dict['is_last'],
  }
  if infos_dict:
    dataset_dict['infos'] = infos_dict
  num_steps = len(dataset_dict['is_first'])
  prev = 0
  counter = 0
  for pos in range(num_steps):
    if dataset_dict['is_first'][pos] and pos > prev:
      yield counter, _get_episode(dataset_dict, episode_metadata, prev, pos)
      prev = pos
      counter += 1
  if prev < num_steps:
    yield counter, _get_episode(dataset_dict, episode_metadata, prev, num_steps)


def _get_nested_metadata(dataset: Dict[str, Any],
                         prefix: str) -> Dict[str, Any]:
  """Generate a metadata dictionary using flattened metadata keys.

  Args:
    dataset: dictionary containing the dataset keys and values. Keys are
      flatened.
    prefix: common prefix of the metadata fields.

  Returns:
    Nested dictionary with the episode metadata.

  If the dataset contains:
  {
    'metadata/v1/v2': 1,
    'metadata/v3': 2,
  }
  and prefix='metadata', it returns:
  {
    'v1':{
      'v2': 1,
    }
    'v3': 2,
  }
  It assumes that the flattened metadata keys are well-formed.
  """
  episode_metadata = {}
  for k in dataset.keys():
    if f'{prefix}/' not in k:
      continue
    keys = k.split('/')[1:]
    nested_dict = episode_metadata
    leaf_value = dataset[k]
    for index, nested_key in enumerate(keys):
      if index == (len(keys) - 1):
        nested_dict[nested_key] = leaf_value
      else:
        if nested_key not in nested_dict:
          nested_dict[nested_key] = {}
        nested_dict = nested_dict[nested_key]

  return episode_metadata


def _get_episode(steps: Dict[str, Any], episode_metadata: Dict[str, Any],
                 begin: int, end: int) -> Dict[str, Any]:
  """Builds a full episode dict.

  Args:
      steps: a dict with all steps in a dataset
      episode_metadata: dict with the episode metadata
      begin: defines a starting position of an episode
      end: defines an ending position of an episode

  Returns:
     A dict with data specific to one episode, already broken into steps.
  """
  # It's an initial step if the episode is empty.
  episode = {}
  for k in [
      'is_first', 'is_last', 'observation', 'action', 'reward', 'discount'
  ]:
    episode[k] = steps[k][begin:end]
  # In some cases, the episode ends with terminals = timeouts = False. However,
  # We still want to signal that this is the last sep of an episode.
  episode['is_last'][-1] = True
  episode['is_terminal'] = [False] * (end - begin)
  if 'infos' in steps.keys():
    episode['infos'] = {}
    for k in steps['infos'].keys():
      episode['infos'][k] = steps['infos'][k][begin:end]

  if steps['is_terminal'][end - 1]:
    # If the step is terminal, then we propagate the information to a next
    # state. This matches the definition in RLDS. See types.py.
    episode['is_first'] = np.concatenate((episode['is_first'], [False]))
    # Observation, action and reward are dummy.
    episode['observation'] = np.concatenate(
        (episode['observation'], [np.zeros_like(steps['observation'][0])]))
    episode['action'] = np.concatenate(
        (episode['action'], [np.zeros_like(steps['action'][0])]))
    episode['reward'] = np.concatenate(
        (episode['reward'], [np.zeros_like(steps['reward'][0])]))
    episode['discount'][-1] = 0.0
    episode['discount'] = np.array(
        np.concatenate((episode['discount'], [0.0])), dtype=np.float32)
    episode['is_terminal'] = np.concatenate((episode['is_terminal'], [True]))
    episode['is_last'][-1] = False
    episode['is_last'] = np.concatenate((episode['is_last'], [True]))
    if 'infos' in steps.keys():
      for k in steps['infos'].keys():
        episode['infos'][k] = np.concatenate(
            (episode['infos'][k], [np.zeros_like(steps['infos'][k][0])]))
  full_episode = {'steps': episode}
  if episode_metadata:
    full_episode.update(episode_metadata)
  return full_episode


def _get_dataset_keys(h5file):
  """Gets the keys present in the D4RL dataset."""
  keys = []

  def visitor(name, item):
    if isinstance(item, h5py.Dataset):
      keys.append(name)

  h5file.visititems(visitor)
  return keys


def read_d4rl_dataset(file_path: str):
  """Reads a D4RL dataset and returns the dataset as a dictionary."""
  with gfile.GFile(file_path, 'rb') as f:
    with h5py.File(f, 'r') as dataset_file:
      dataset_dict = {}
      for k in _get_dataset_keys(dataset_file):
        try:
          # first try loading as an array
          dataset_dict[k] = dataset_file[k][:]
        except ValueError:  # try loading as a scalar
          dataset_dict[k] = dataset_file[k][()]

    return dataset_dict

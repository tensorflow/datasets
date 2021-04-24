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
from typing import Any, Dict, Iterable, List, Tuple, Union

import h5py
import numpy as np
from tensorflow.io import gfile


def generate_examples(file_path: str):
  """Provides a common generate_examples method for D4RL datasets."""
  with gfile.GFile(file_path, 'rb') as f:
    dataset_file = h5py.File(f, 'r')
    dataset_dict = {}
    for k in _get_dataset_keys(dataset_file):
      try:
        # first try loading as an array
        dataset_dict[k] = dataset_file[k][:]
      except ValueError as e:  # try loading as a scalar
        dataset_dict[k] = dataset_file[k][()]
    dataset_file.close()
  if 'timeouts' not in dataset_dict:
    raise ValueError('Only datasets with explicit timeouts are supported.')

  done = [
      terminal or timeout
      for (terminal,
           timeout) in zip(dataset_dict['terminals'], dataset_dict['timeouts'])
  ]
  # is_first corresponds to the done flag delayed by one step.
  dataset_dict['is_first'] = [True] + done[:-1]

  # TODO(sabela): Add extra keys for metadata (qpos, qval, goal) that is only
  # present in some datasets.
  dataset_dict = {
      'observation': dataset_dict['observations'],
      'action': dataset_dict['actions'],
      'reward': dataset_dict['rewards'],
      'discount': np.ones_like(dataset_dict['rewards']),
      'is_terminal': dataset_dict['terminals'],
      'is_first': dataset_dict['is_first'],
  }
  num_steps = len(dataset_dict['is_first'])
  prev = 0
  counter = 0
  for pos in range(num_steps):
    if dataset_dict['is_first'][pos] and pos > prev:
      yield counter, _get_episode(dataset_dict, prev, pos)
      prev = pos
      counter += 1
  if prev < num_steps:
    yield counter, _get_episode(dataset_dict, prev, num_steps)


def _get_episode(steps: Dict[str, Any], begin: int, end: int) -> Dict[str, Any]:
  """Builds a full episode dict.

  Args:
      steps: a dict with all steps in a dataset
      begin: defines a starting position of an episode
      end: defines an ending position of an episode

  Returns:
     A dict with data specific to one episode, already broken into steps.
  """
  # It's an initial step if the episode is empty.
  episode = {}
  episode['is_first'] = steps['is_first'][begin:end]
  episode['observation'] = steps['observation'][begin:end]
  episode['action'] = steps['action'][begin:end]
  episode['reward'] = steps['reward'][begin:end]
  episode['discount'] = steps['discount'][begin:end]
  episode['is_terminal'] = [False] * (end - begin)
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
  return {'steps': _unpack_steps(episode)}


def _get_nested_field(data: Union[Dict[str, Any], Tuple[Any], List[Any]],
                      index: int) -> Any:
  """Gets nested data and returns element at index respecting the shape.

  It assumes that the most leaf type is a list.

  If the input data is, for example:
  data = {
    'field_1': {
        'nested': [1,2,3],
    },
    'field_2': [4, 5, 6],
  }
  index = 1
  The output is:
  {
    'field_1':{
      'nested': 2,
    },
    'field_2': 5,
  }

  Args:
    data: data with nested shape, where the most inner type is a list.
    index: index in the list to construct the returned element.

  Returns:
    Element i of data respecting the nested shape.

  Raises:
    ValueError if the input data type is not dict, tuple, list or np.ndarray.
  """
  if isinstance(data, list) or isinstance(data, np.ndarray):
    return data[index]
  if isinstance(data, dict):
    return {k: _get_nested_field(data[k], index) for k in data}
  if isinstance(data, tuple):
    return (_get_nested_field(data[k], index) for k in data)
  raise ValueError(f'Data has to be list, dict or tuple and it is {type(data)}')


def _unpack_steps(steps: Dict[str, List[Any]]) -> Iterable[Dict[str, Any]]:
  """Gets a step represented as a dict[nested_list] and returns list[dict]."""
  length = len(steps['is_first'])
  for i in range(length):
    step = {}
    for k in steps:
      step[k] = _get_nested_field(steps[k], i)
    yield step


def _get_dataset_keys(h5file):
  """Gets the keys present in the D4RL dataset."""
  keys = []

  def visitor(name, item):
    if isinstance(item, h5py.Dataset):
      keys.append(name)

  h5file.visititems(visitor)
  return keys

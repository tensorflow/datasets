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

"""Utils to read envlogger data into a dataset that is compatible with RLDS."""

from typing import AbstractSet, Any, Callable, Dict, Generator, List, Sequence, Tuple, Union

import numpy as np
import tensorflow as tf


def get_episode_metadata(
    episode: Sequence[Any]) -> Dict[str, Any]:
  """Extracts the episode metadata and returns it as a dictionary.

  This is only used when the episode metadata is stored in the first step.

  Args:
    episode: sequence of steps (envlogger.StepData).

  Returns:
    Dictionary containing the episode metadata
  """

  first_step = episode[0]
  if not first_step.timestep.first():
    raise ValueError('The first step in this episode is not first')
  custom_data = first_step.custom_data
  return custom_data.get('episode_metadata', {}) if custom_data else {}


def get_step_metadata(
    step: Any,
    step_metadata_skip_list: AbstractSet[str] = frozenset()
) -> Dict[str, Any]:
  """Extracts the custom metadata from the step.

  Args:
    step: step data (envlogger.StepData).
    step_metadata_skip_list: Set of metadata keys to filter.

  Returns:
    Dictionary containing the step metadata.
  """
  if not isinstance(step.custom_data, dict):
    # We ignore step metadata if step.custom_data is not a dictionary
    return {}
  return {
      k: v
      for k, v in step.custom_data.items()
      if k != 'episode_metadata' and k not in step_metadata_skip_list
  }


def generate_episodes(
    tag_reader: Any,
    keep_episode_fn: Callable[[Dict[str, Any]], bool] = lambda x: True,
    step_metadata_skip_list: AbstractSet[str] = frozenset(),
    steps_to_ds=False) -> Generator[Dict[str, Any], None, None]:
  """Generates episodes by reading them from the tag_reader.

  Args:
    tag_reader: Envlogger reader (envlogger.Reader).
    keep_episode_fn: function that receives an episode and returns a boolean,
      acting as a filter (true if we want to keep this episodes, false if we
      want to skip it).
    step_metadata_skip_list: list of fields of the step's metadata that will not
      be included in the result.
    steps_to_ds: if True, the steps of each episode are returned as a nested
      dataset.

  Yields:
    A dictionary representing one episode.
  """
  for index, episode_metadata in enumerate(tag_reader.episode_metadata()):
    episode = tag_reader.episodes[index]
    if episode_metadata:
      episode_dict = episode_metadata
    else:
      episode_dict = get_episode_metadata(episode)
    if not keep_episode_fn(episode_dict):
      continue
    steps = _generate_steps(episode, step_metadata_skip_list)

    if steps_to_ds:
      steps = tf.data.Dataset.from_tensor_slices(steps)
    episode_dict['steps'] = steps
    yield episode_dict


def _generate_steps(
    episode: Sequence[Any],
    step_metadata_skip_list: AbstractSet[str]) -> Dict[str, Any]:
  """Constructs a dictionary of steps for the given episode.

  Args:
    episode: Sequence of steps (envlogger.StepData).
    step_metadata_skip_list: Set of metadata keys to filter.

  Returns:
    Nested dictionary with the steps of one episode.
  """
  step_metadata = _empty_nested_list(
      get_step_metadata(episode[0], step_metadata_skip_list))

  steps = {
      'observation':
          _empty_nested_list(episode[0].timestep.observation),
      'action':
          _empty_nested_list(episode[0].action),
      'reward': [],
      'discount': [],
      'is_terminal': [],
      'is_first': [],
      'is_last': [],
  }
  steps.update(step_metadata)

  prev_step = None
  for step in episode:
    if prev_step is not None:
      steps['is_first'].append(prev_step.timestep.first())
      steps['is_terminal'].append(False)
      steps['is_last'].append(prev_step.timestep.last())
      steps['observation'] = _append_nested(
          steps['observation'], prev_step.timestep.observation)
      steps['reward'].append(step.timestep.reward)
      steps['discount'].append(step.timestep.discount)
      steps['action'] = _append_nested(steps['action'], step.action)
      step_metadata = get_step_metadata(prev_step, step_metadata_skip_list)
      for k, v in step_metadata.items():
        steps[k] = _append_nested(steps[k], v)
    prev_step = step
  if prev_step is not None:
    # We append the observation of the final step (action and reward were
    # included in the previous step.
    # The terminal flag is inferred like in termination(), truncation()
    # from dm_env/_environment.py
    is_terminal = (
        prev_step.timestep.last() and prev_step.timestep.discount == 0.0)
    steps['is_first'].append(prev_step.timestep.first())
    steps['is_terminal'].append(is_terminal)
    steps['is_last'].append(True)
    steps['observation'] = _append_nested(
        steps['observation'], prev_step.timestep.observation)
    # Discount, action and reward are meaningless in the terminal step
    steps['reward'].append(np.zeros_like(prev_step.timestep.reward))
    steps['discount'].append(
        np.zeros_like(prev_step.timestep.discount))
    steps['action'] = _append_nested(
        steps['action'],
        tf.nest.map_structure(np.zeros_like, prev_step.action))
    step_metadata = get_step_metadata(prev_step, step_metadata_skip_list)
    for k, v in step_metadata.items():
      steps[k] = _append_nested(steps[k], v)
  return steps


def _append_nested(
    collection: Any, data: Union[np.ndarray, List[Any], Tuple[Any, ...],
                                 Dict[str, Any]]) -> Any:
  """Appends data to the more nested dimension of collection.

  Args:
    collection: collection constructed by appending elements like data to the
      most nested dimension. It is of type Union[np.ndarray, List[Any],
      Tuple[Any, ...], Dict[str, Any]] but using this causes type errors because
      it considers that we are trying to append to a dict or a tuple.
    data: data logged by DM Env Logger that can be a scalar, array, dict or
      tuple.

  Returns:
    Collection with data appended to the nested dimension.
  """
  if isinstance(data, dict):
    for k in collection:
      _append_nested(collection[k], data[k])
    return collection
  elif isinstance(data, tuple):
    return tuple(
        _append_nested(collection[index], value)
        for index, value in enumerate(data))
  else:
    collection.append(data)
    return collection


def _empty_nested_list(
    data: Union[np.ndarray, List[Any], Tuple[Any, ...], Dict[str, Any]]
) -> Union[List[Any], Tuple[Any, ...], Dict[str, Any]]:
  """Creates an element like data but with empty lists in the nested dimensions.

  Args:
    data: scalar, array, list, tuple or dictionary.

  Returns:
    item with the same shape of data but with empty lists in its nested
    dimensions.
  """
  if isinstance(data, dict):
    return {k: _empty_nested_list(data[k]) for k in data}
  elif isinstance(data, tuple):
    return tuple(_empty_nested_list(x) for x in data)
  else:
    return []

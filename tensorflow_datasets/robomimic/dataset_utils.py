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

"""Library functions for robomimic datasets."""

from typing import Any, Dict, List, Mapping

import numpy as np
import tensorflow as tf


def _concat_obs(base_obs, extra_obs):
  return np.append(base_obs, np.expand_dims(extra_obs, 0), axis=0)


def episode_metadata(mask: Mapping[str, List[str]],
                     episode_key: str) -> Dict[str, bool]:
  """Builds the metadata of an episode.

  Args:
    mask: A dict that maps flags to the list of episodes for which this
      flag is true.
    episode_key: The key of an episode.

  Returns:
    Dictionary that maps the flags to the value corresponding to the given
    episode.
  """
  metadata = {}
  for k in mask:
    metadata[k] = episode_key in mask[k]
  return metadata


def build_episode(steps: Mapping[str, Any]) -> Dict[str, Any]:
  """Builds a full episode dict.

  Args:
    steps: A dict with each key corresponding to an episode of that variable.

  Returns:
   A dict with data specific to one episode.
  """

  # This is the base episode length without the end step, that step will get
  # added manually.  `[:]` notation is necessary to extract data from the hdf5
  # object.
  ep_length = steps['actions'][:].shape[0]
  episode = {}
  episode['is_first'] = np.append(True, np.zeros(ep_length, dtype=bool))

  # The standard 'obs' needs to be extended with the last element from
  # 'next_obs' to reconstruct the full sequence.
  obs = tf.nest.map_structure(np.array, dict(steps['obs']))
  last_obs = tf.nest.map_structure(lambda el: el[-1], dict(steps['next_obs']))
  concat_obs = tf.nest.map_structure(_concat_obs, obs, last_obs)

  actions = steps['actions'][:]
  dones = steps['dones'][:]
  episode['observation'] = concat_obs
  episode['action'] = np.append(
      actions, np.expand_dims(np.zeros(actions[0].shape), 0), axis=0)
  episode['reward'] = np.append(steps['rewards'][:], 0)
  episode['discount'] = np.append(np.ones(ep_length), 0)
  # Offset `dones` by one as it corresponds to the `next_obs`:
  # "done signal, equal to 1 if playing the corresponding action in the state
  # should terminate the episode".  Since playing another action may not end the
  # episode, it is actually representing whether the following state is
  # the terminal state.
  episode['is_terminal'] = np.append(False, dones).astype(bool)
  episode['is_last'] = np.append(np.zeros(ep_length, dtype=bool), True)
  states = steps['states'][:]
  episode['states'] = np.append(
      states, np.expand_dims(np.zeros(states[0].shape), 0), axis=0)

  return episode

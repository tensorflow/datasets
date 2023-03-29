# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for rlds.experiments.robomimic_loader.py."""

import inspect
import os

from absl import flags
from absl.testing import absltest
from etils import epath
import h5py
import numpy as np
from tensorflow_datasets.robomimic import dataset_utils
import tree

FLAGS = flags.FLAGS


def _build_dataset(file_path):
  path = epath.Path(file_path)
  with path.open('rb') as f:
    with h5py.File(f, 'r') as dataset_file:
      data = dataset_file['data']
      for key in data:
        yield {'steps': dataset_utils.build_episode(data[key])}


class DatasetUtilsTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    basedir = epath.Path(inspect.getfile(inspect.getmodule(self))).parent
    self.dataset_dir = os.path.join(
        basedir, 'dummy_data', 'robomimic_test.hdf5'
    )

  def test_last_transition_corresponds_to_source_dataset(self):
    dataset = _build_dataset(self.dataset_dir)
    # Get the final observation of the first episode directly from the file.
    with h5py.File(self.dataset_dir, 'r') as ds_file:
      raw_last_obs = {}
      for key, item in ds_file['data']['demo_1']['next_obs'].items():
        raw_last_obs[key] = item[-1]

    # Get final observation of the first episode from the iterator.
    for el in dataset:
      ds_last_obs = {}
      for key, item in el['steps']['observation'].items():
        ds_last_obs[key] = item[-1]
      break

    # As these are dicts of arrays need to run comparison by hand or we will
    # have a complaint about truth value of an array.
    equality = np.array(
        tree.flatten(
            tree.map_structure(
                lambda a, b: (a == b).all(), ds_last_obs, raw_last_obs
            )
        )
    ).all()
    self.assertTrue(equality)

  def test_episode_boundaries_are_coherent(self):
    num_episodes = 0
    dataset = _build_dataset(self.dataset_dir)
    for episode in dataset:
      steps = episode['steps']
      num_steps = len(steps['is_first'])
      for i in range(num_steps):
        if i == 0:
          # Test first step:
          self.assertEqual(steps['is_first'][i], True)
          self.assertEqual(steps['is_last'][i], False)
          self.assertEqual(steps['is_terminal'][i], False)
          self.assertEqual(steps['discount'][i], 1.0)
        # Test middle steps:
        if i > 0 and i < num_steps - 1:
          self.assertEqual(steps['is_first'][i], False)
          self.assertEqual(steps['is_last'][i], False)
          self.assertEqual(steps['discount'][i], 1.0)
        # Test final steps:
        if i == num_steps - 1:
          self.assertEqual(steps['is_first'][i], False)
          self.assertEqual(steps['is_last'][i], True)
          self.assertEqual(steps['is_terminal'][i], True)
          self.assertEqual(steps['discount'][i], 0.0)

      num_episodes += 1
    # The number of episodes should be consistent with the total available.
    self.assertEqual(num_episodes, 2)

  def test_episode_metadata(self):
    mask = {'flag0': ['episode0'], 'flag1': ['episode1', 'episode2']}
    metadata = dataset_utils.episode_metadata(mask, 'episode1')
    expected_metadata = {'flag0': False, 'flag1': True}
    self.assertDictEqual(metadata, expected_metadata)


if __name__ == '__main__':
  absltest.main()

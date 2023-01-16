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

"""Test for delete_old_versions.py script."""

import pathlib

from typing import List

from tensorflow_datasets.scripts.cleanup import delete_old_versions


def test_split_full_names():
  """Test _split_full_names function."""
  full_names = [
      'my_dataset/1.2.0',
      'my_dataset/1.3.0',
      'my_other_dataset/config/2.0.0',
      'my_other_dataset/config/1.3.0',
      'my_other_dataset/other_config/1.3.0',
  ]
  assert delete_old_versions._split_full_names(full_names) == {
      'my_dataset': {
          '1.2.0': {},
          '1.3.0': {},
      },
      'my_other_dataset': {
          'config': {
              '2.0.0': {},
              '1.3.0': {},
          },
          'other_config': {
              '1.3.0': {},
          },
      },
  }


def test_delete_script(tmp_path: pathlib.PurePath):
  # Create paths
  for dataset_dir in [
      'extracted',  # DownloadManager directories should be preserved.
      'dataset/config/1.0.0',
      'my_dataset/other_dir',
      'my_dataset/1.0.0/other',
      'my_dataset/1.1.0',
      'my_dataset/1.2.0/diff',
      'my_dataset/1.2.0/other',
      'my_dataset/1.3.0',
      'my_other_dataset/config/1.2.0',
      'my_other_dataset/config/1.3.0',
      'my_other_dataset/other_config/1.2.0',
      'my_other_dataset/other_config/1.3.0',
      'my_other_dataset/yet_other_config',
      'my_other_dataset/config_deprecated/1.2.0',
      'old_dataset',
  ]:
    tmp_path.joinpath(dataset_dir).mkdir(parents=True)

  dirs_to_keep, dirs_to_delete = delete_old_versions._get_extra_dirs(
      data_dir=tmp_path,
      current_full_names=[
          'non_generated_dataset0/1.0.0',
          'non_generated_dataset1/config/1.0.0',
          'dataset/config/1.0.0',
          'my_dataset/1.2.0',
          'my_dataset/1.3.0',
          'my_other_dataset/config/1.3.0',
          'my_other_dataset/other_config/1.3.0',
          'another_dataset/config/1.2.0',
          'another_dataset/other_config/1.1.0',
      ],
  )
  assert dirs_to_keep == _norm_path(
      tmp_path,
      [
          'dataset/config/1.0.0',
          'my_dataset/1.2.0',
          'my_dataset/1.3.0',
          'my_other_dataset/config/1.3.0',
          'my_other_dataset/other_config/1.3.0',
      ],
  )
  assert dirs_to_delete == _norm_path(
      tmp_path,
      [
          'my_dataset/1.0.0',
          'my_dataset/1.1.0',
          'my_dataset/other_dir',
          'my_other_dataset/config/1.2.0',
          'my_other_dataset/config_deprecated',
          'my_other_dataset/other_config/1.2.0',
          'my_other_dataset/yet_other_config',
          'old_dataset',
      ],
  )


def _norm_path(root_path: pathlib.Path, paths: List[str]) -> List[pathlib.Path]:
  """Normalize paths (for windows compatibility)."""
  return [root_path / p for p in paths]

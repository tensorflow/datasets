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

"""Test for delete_old_versions.py script"""
from tensorflow_datasets.scripts.cleanup import delete_old_versions
import tensorflow_datasets.testing as tfds_test
import pathlib

def test_delete_script(tmp_path: pathlib.Path):
  for dataset_dir in [
    'dataset/config/1.0.0',
    'my_dataset/1.0.0',
    'my_dataset/1.2.0',
    'my_dataset/1.3.0',
    'my_other_dataset/config/1.2.0',
    'my_other_dataset/config/1.3.0',
    'my_other_dataset/other_config/1.2.0',
    'my_other_dataset/other_config/1.3.0',
    'old_dataset',
  ]:
    tmp_path.joinpath(dataset_dir).touch(exist_ok)

  dir_to_keep, dir_to_delete = delete_old_versions.get_datasets(
      data_dir=str(tmp_path),
      current_full_names=[
            'dataset/config/1.0.0',
            'my_dataset/1.3.0',
            'my_other_dataset/config/1.3.0',
            'my_other_dataset/other_config/1.3.0',
            'another_dataset/config/1.2.0'
            'another_dataset/other_config/1.1.0',
      ],
  )
  assert dir_to_keep == [
      'dataset/config/1.0.0',
      'my_dataset/1.3.0',
      'my_other_dataset/config/1.3.0',
      'my_other_dataset/other_config/1.3.0',
  ]
  assert dir_to_delete == [
      'my_dataset/1.0.0',
      'my_dataset/1.2.0',
      'my_other_dataset/config/1.2.0',
      'my_other_dataset/other_config/1.2.0',
      'old_dataset',
  ]

if __name__ == "__main__":
  tfds_test.test_main()

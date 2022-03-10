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

"""Tests for compute_split_info."""

from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.folder_dataset import compute_split_utils


def test_compute_split_info(tmp_path):
  builder = testing.DummyDataset(data_dir=tmp_path)
  builder.download_and_prepare()

  filename_template = naming.ShardedFileTemplate(
      dataset_name=builder.name,
      data_dir=builder.data_dir,
      filetype_suffix=builder.info.file_format.file_suffix)
  split_infos = compute_split_utils.compute_split_info(
      out_dir=tmp_path,
      filename_template=filename_template,
  )

  assert [s.to_proto() for s in split_infos
         ] == [s.to_proto() for s in builder.info.splits.values()]

  # Split info are correctly saved
  filename_template = filename_template.replace(
      data_dir=tmp_path, split='train')
  split_info = compute_split_utils._split_info_from_path(filename_template)
  assert builder.info.splits['train'].to_proto() == split_info.to_proto()

# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from etils import epath
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.scripts.cli import convert_format_utils


def test_shard_instructions_for_split():
  split_info = splits_lib.SplitInfo(
      name='train',
      shard_lengths=[1, 2, 3],
      num_bytes=1,
      filename_template=naming.ShardedFileTemplate(
          data_dir=epath.Path('/in'),
          dataset_name='ds',
          split='train',
          filetype_suffix='tfrecord',
      ),
  )
  in_file_adapter = file_adapters.TfRecordFileAdapter
  out_file_adapter = file_adapters.ArrayRecordFileAdapter
  actual = convert_format_utils._shard_instructions_for_split(
      split_info=split_info,
      out_file_format=file_adapters.FileFormat.ARRAY_RECORD,
      out_path=epath.Path('/out'),
      in_file_adapter=in_file_adapter,
      out_file_adapter=out_file_adapter,
  )
  assert actual == [
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00000-of-00003'),
          in_file_adapter=in_file_adapter,
          out_path=epath.Path('/out/ds-train.array_record-00000-of-00003'),
          out_file_adapter=out_file_adapter,
      ),
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00001-of-00003'),
          in_file_adapter=in_file_adapter,
          out_path=epath.Path('/out/ds-train.array_record-00001-of-00003'),
          out_file_adapter=out_file_adapter,
      ),
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00002-of-00003'),
          in_file_adapter=in_file_adapter,
          out_path=epath.Path('/out/ds-train.array_record-00002-of-00003'),
          out_file_adapter=out_file_adapter,
      ),
  ]

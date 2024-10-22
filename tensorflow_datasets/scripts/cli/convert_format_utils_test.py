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

import os

from etils import epath
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.scripts.cli import convert_format_utils


def _create_dataset_info(
    data_dir: epath.Path,
    name: str = 'a',
    version: str = '1.2.3',
    config_name: str = 'cfg1',
    file_format: file_adapters.FileFormat = file_adapters.FileFormat.TFRECORD,
    split_lengths: dict[str, int] | None = None,
) -> dataset_info_pb2.DatasetInfo:
  filename_template = naming.ShardedFileTemplate(
      data_dir=data_dir,
      dataset_name=name,
      split=None,  # will be set in _create_split_info
      filetype_suffix=file_format.value,
  )
  split_lengths = split_lengths or {}
  info = dataset_info_lib.DatasetInfo(
      builder=dataset_info_lib.DatasetIdentity(
          name=name,
          version=version,
          config_name=config_name,
          data_dir=data_dir,
          module_name='xyz',
      ),
      split_dict=splits_lib.SplitDict(
          split_infos=[
              _create_split_info(
                  name=split_name,
                  shard_lengths=[1] * split_length,
                  filename_template=filename_template,
              )
              for split_name, split_length in split_lengths.items()
          ]
      ),
  )
  info.set_file_format(file_format)
  data_dir.mkdir(parents=True, exist_ok=True)
  info.write_to_directory(data_dir)
  return info.as_proto


def _create_split_info(
    name: str,
    shard_lengths: list[int],
    filename_template: naming.ShardedFileTemplate,
) -> splits_lib.SplitInfo:
  return splits_lib.SplitInfo(
      name=name,
      shard_lengths=shard_lengths,
      num_bytes=1,
      filename_template=filename_template.replace(split=name),
  )


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
  convert_config = convert_format_utils.ConvertConfig(
      in_file_format=file_adapters.FileFormat.TFRECORD,
      out_file_format=file_adapters.FileFormat.ARRAY_RECORD,
  )
  actual = convert_format_utils._shard_instructions_for_split(
      split_info=split_info,
      out_path=epath.Path('/out'),
      convert_config=convert_config,
  )
  assert actual == [
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00000-of-00003'),
          out_path=epath.Path('/out/ds-train.array_record-00000-of-00003'),
          config=convert_config,
      ),
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00001-of-00003'),
          out_path=epath.Path('/out/ds-train.array_record-00001-of-00003'),
          config=convert_config,
      ),
      convert_format_utils.ShardInstruction(
          in_path=epath.Path('/in/ds-train.tfrecord-00002-of-00003'),
          out_path=epath.Path('/out/ds-train.array_record-00002-of-00003'),
          config=convert_config,
      ),
  ]




def test_create_out_dir():
  actual = convert_format_utils._create_out_dir(
      dataset_dir='/a/b/c/d',
      root_in_dir='/a/b',
      root_out_dir='/e',
  )
  assert os.fspath(actual) == '/e/c/d'


def test_create_from_to_dirs():
  references = [
      naming.DatasetReference(
          dataset_name='a', config='cfg1', version='1.0.0', data_dir='/data/in'
      ),
      naming.DatasetReference(
          dataset_name='a', config='cfg2', version='1.0.0', data_dir='/data/in'
      ),
      naming.DatasetReference(
          dataset_name='b', config='cfg1', version='1.0.0', data_dir='/data/in'
      ),
      naming.DatasetReference(
          dataset_name='c', version='1.0.0', data_dir='/data/in'
      ),
  ]
  actual = convert_format_utils._create_from_to_dirs(
      references, epath.Path('/data/in'), epath.Path('/out')
  )
  assert actual == {
      epath.Path('/data/in/a/cfg1/1.0.0'): epath.Path('/out/a/cfg1/1.0.0'),
      epath.Path('/data/in/a/cfg2/1.0.0'): epath.Path('/out/a/cfg2/1.0.0'),
      epath.Path('/data/in/b/cfg1/1.0.0'): epath.Path('/out/b/cfg1/1.0.0'),
      epath.Path('/data/in/c/1.0.0'): epath.Path('/out/c/1.0.0'),
  }


def test_create_from_to_dirs_same_folder():
  references = [
      naming.DatasetReference(
          dataset_name='a', config='cfg1', version='1.0.0', data_dir='/data/in'
      )
  ]
  actual = convert_format_utils._create_from_to_dirs(
      references, root_in_dir=epath.Path('/data/in'), out_path=None
  )
  expected_path = epath.Path('/data/in/a/cfg1/1.0.0')
  assert actual == {expected_path: expected_path}


def test_get_root_data_dir(tmpdir):
  leaf_data_dir = epath.Path(tmpdir) / 'a/cfg1/1.2.3'
  info = _create_dataset_info(data_dir=leaf_data_dir)
  actual = convert_format_utils._get_root_data_dir(
      in_dir=leaf_data_dir, info=info
  )
  assert os.fspath(tmpdir) == os.fspath(actual)


def test_record_source_dataset(tmpdir):
  tmpdir = epath.Path(tmpdir)
  in_root_data_dir = tmpdir / 'data'
  in_data_dir = in_root_data_dir / 'a/cfg1/1.2.3'
  out_data_dir = tmpdir / 'out'
  in_data_dir.mkdir(parents=True)
  out_data_dir.mkdir(parents=True)
  info = _create_dataset_info(in_data_dir)
  convert_format_utils.convert_metadata(
      in_dir=in_data_dir,
      out_path=out_data_dir,
      info=info,
      out_file_format=file_adapters.FileFormat.RIEGELI,
  )
  converted_info = dataset_info_lib.read_proto_from_builder_dir(out_data_dir)
  assert converted_info.name == info.name
  assert converted_info.version == info.version
  assert converted_info.config_name == info.config_name
  assert converted_info.module_name == info.module_name
  assert converted_info.file_format == file_adapters.FileFormat.RIEGELI.value
  assert len(converted_info.data_source_accesses) == 1
  data_source_access = converted_info.data_source_accesses[0]
  assert data_source_access.tfds_dataset.data_dir == os.fspath(in_root_data_dir)
  assert data_source_access.tfds_dataset.name == info.name
  assert data_source_access.tfds_dataset.version == info.version
  assert data_source_access.tfds_dataset.config == info.config_name


def test_convert_metadata_add_to_existing(tmpdir):
  in_data_dir = epath.Path(tmpdir) / 'a/cfg1/1.2.3'
  in_data_dir.mkdir(parents=True)
  info = _create_dataset_info(data_dir=in_data_dir, split_lengths={'train': 1})

  # Create a converted shard in the input directory.
  converted_shard = in_data_dir / 'a-train.riegeli-00000-of-00001'
  converted_shard.touch()

  convert_format_utils.convert_metadata(
      in_dir=in_data_dir,
      out_path=in_data_dir,
      info=info,
      out_file_format=file_adapters.FileFormat.RIEGELI,
  )
  converted_info = dataset_info_lib.read_proto_from_builder_dir(in_data_dir)
  assert converted_info.file_format == file_adapters.FileFormat.TFRECORD.value
  assert converted_info.alternative_file_formats == [
      file_adapters.FileFormat.RIEGELI.value
  ]


def test_convert_metadata_missing_shards(tmpdir):
  in_data_dir = epath.Path(tmpdir) / 'a/cfg1/1.2.3'
  in_data_dir.mkdir(parents=True)
  info = _create_dataset_info(
      in_data_dir, split_lengths={'train': 2, 'test': 1}
  )
  convert_format_utils.convert_metadata(
      in_dir=in_data_dir,
      out_path=in_data_dir,
      info=info,
      out_file_format=file_adapters.FileFormat.RIEGELI,
  )
  converted_info = dataset_info_lib.read_proto_from_builder_dir(in_data_dir)
  assert converted_info.file_format == file_adapters.FileFormat.TFRECORD.value
  # Make sure no alternative file format was added.
  assert not converted_info.alternative_file_formats

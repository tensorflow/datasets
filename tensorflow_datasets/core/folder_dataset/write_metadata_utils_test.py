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

"""Tests for write_metadata_lib."""

import pathlib

from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core.folder_dataset import write_metadata_utils

_PATH = epath.Path('/a/b')


@pytest.mark.parametrize(
    'file_format',
    [
        None,
    ],
)
def test_write_metadata(
    tmp_path: pathlib.Path,
    file_format,
):
  tmp_path = epath.Path(tmp_path)

  src_builder = testing.DummyDataset(
      data_dir=tmp_path / 'origin',
      file_format=file_format,
  )
  src_builder.download_and_prepare()

  dst_dir = tmp_path / 'copy'
  dst_dir.mkdir()

  # Copy all the tfrecord files, but not the dataset info
  for f in src_builder.data_path.iterdir():
    if naming.FilenameInfo.is_valid(f.name):
      f.copy(dst_dir / f.name)

  metadata_path = dst_dir / 'dataset_info.json'

  if file_format is None:
    split_infos = list(src_builder.info.splits.values())
  else:
    split_infos = None  # Auto-compute split infos

  assert not metadata_path.exists()
  write_metadata_utils.write_metadata(
      data_dir=dst_dir,
      features=src_builder.info.features,
      split_infos=split_infos,
      description='my test description.',
  )
  assert metadata_path.exists()

  # After metadata are written, builder can be restored from the directory
  builder = read_only_builder.builder_from_directory(dst_dir)
  assert builder.name == 'dummy_dataset'
  assert builder.version == '1.0.0'
  assert set(builder.info.splits) == {'train'}
  assert builder.info.splits['train'].num_examples == 3
  assert builder.info.description == 'my test description.'

  # Values are the same
  src_ds = src_builder.as_dataset(split='train')
  ds = builder.as_dataset(split='train')
  assert list(src_ds.as_numpy_iterator()) == list(ds.as_numpy_iterator())


@pytest.mark.parametrize(
    ['data_dir', 'filename_template', 'result'],
    [
        (
            _PATH,
            '{DATASET}',
            naming.ShardedFileTemplate(data_dir=_PATH, template='{DATASET}'),
        ),
        (
            _PATH,
            None,
            naming.ShardedFileTemplate(
                data_dir=_PATH,
                template='{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}',
            ),
        ),
        (
            _PATH,
            naming.ShardedFileTemplate(data_dir=epath.Path('/other')),
            naming.ShardedFileTemplate(
                data_dir=_PATH,
                template='{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}',
            ),
        ),
        (
            _PATH,
            naming.ShardedFileTemplate(
                data_dir=epath.Path('/other'), dataset_name='mnist'
            ),
            naming.ShardedFileTemplate(
                data_dir=_PATH,
                dataset_name='mnist',
                template='{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}',
            ),
        ),
    ],
)
def test_construct_filename_template(data_dir, filename_template, result):
  actual = write_metadata_utils._construct_filename_template(
      data_dir=data_dir, filename_template=filename_template
  )
  assert actual == result


@pytest.mark.parametrize(
    ['filename_template', 'file_infos', 'result'],
    [
        (
            naming.ShardedFileTemplate(data_dir=_PATH, template='{DATASET}'),
            [
                naming.FilenameInfo(
                    dataset_name='mnist', filetype_suffix='tfrecord'
                )
            ],
            naming.ShardedFileTemplate(
                data_dir=_PATH,
                template='{DATASET}',
                dataset_name='mnist',
                filetype_suffix='tfrecord',
            ),
        ),
        (
            naming.ShardedFileTemplate(
                data_dir=_PATH, template='{DATASET}', dataset_name='mnist'
            ),
            [naming.FilenameInfo(dataset_name='mnist')],
            naming.ShardedFileTemplate(
                data_dir=_PATH, template='{DATASET}', dataset_name='mnist'
            ),
        ),
        (
            naming.ShardedFileTemplate(data_dir=_PATH, template='{DATASET}'),
            [naming.FilenameInfo(filetype_suffix='tfrecord')],
            naming.ShardedFileTemplate(
                data_dir=_PATH, template='{DATASET}', filetype_suffix='tfrecord'
            ),
        ),
    ],
)
def test_enrich_filename_template(filename_template, file_infos, result):
  actual = write_metadata_utils._enrich_filename_template(
      filename_template=filename_template, file_infos=file_infos
  )
  assert actual == result


def test_enrich_filename_template_different_dataset_name():
  filename_template = naming.ShardedFileTemplate(
      data_dir=_PATH, template='{DATASET}', dataset_name='imagenet'
  )
  file_infos = [naming.FilenameInfo(dataset_name='mnist')]
  with pytest.raises(ValueError, match='Detected dataset name.+'):
    write_metadata_utils._enrich_filename_template(
        filename_template=filename_template, file_infos=file_infos
    )


def test_enrich_filename_template_different_filetype_suffix():
  filename_template = naming.ShardedFileTemplate(
      data_dir=_PATH, template='{DATASET}', filetype_suffix='tfrecord'
  )
  file_infos = [naming.FilenameInfo(filetype_suffix='riegeli')]
  with pytest.raises(ValueError, match='Detected filetype suffix.+'):
    write_metadata_utils._enrich_filename_template(
        filename_template=filename_template, file_infos=file_infos
    )

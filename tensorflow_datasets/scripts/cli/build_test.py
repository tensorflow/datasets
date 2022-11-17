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

"""Tests for tensorflow_datasets.scripts.cli.build."""

import contextlib
import os
import pathlib
from typing import Dict, Iterator, List, Optional
from unittest import mock

from etils import epath
import pytest

import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import download
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.scripts.cli import build as build_lib
from tensorflow_datasets.scripts.cli import main

type_utils = tfds.core.utils.type_utils

_DUMMY_DATASET_PATH = tfds.core.tfds_path() / 'testing/dummy_dataset'


class DummyDatasetNoGenerate(tfds.testing.DummyDataset):

  def _generate_examples(self):
    if True:  # pylint: disable=using-constant-test
      raise NotImplementedError('Should not be called')
    yield

  @utils.classproperty
  @classmethod
  def url_infos(cls) -> Optional[Dict[str, download.checksums.UrlInfo]]:
    return {
        'http://data.org/file1.zip':
            download.checksums.UrlInfo(
                size=42,
                checksum='d45899d9a6a0e48afb250aac7ee3dc50e73e263687f15761d754515cd8284e0a',
                filename='file1.zip'),
    }


@pytest.fixture(scope='function', autouse=True)
def mock_default_data_dir(tmp_path: pathlib.Path):
  """Changes the default `--data_dir` to tmp_path."""
  tmp_path = tmp_path / 'datasets'
  default_data_dir = os.environ.get('TFDS_DATA_DIR')
  try:
    os.environ['TFDS_DATA_DIR'] = os.fspath(tmp_path)
    yield tmp_path
  finally:
    if default_data_dir:
      os.environ['TFDS_DATA_DIR'] = default_data_dir
    else:
      del os.environ['TFDS_DATA_DIR']


@contextlib.contextmanager
def mock_cwd(path: epath.PathLike) -> Iterator[None]:
  """Mock the current directory."""
  path = pathlib.Path(path)
  assert path.exists() and path.is_dir()  # Check given path is valid cwd dir
  with mock.patch('os.getcwd', return_value=os.fspath(path)):
    yield


def _build(cmd_flags: str, mock_download_and_prepare: bool = True) -> List[str]:
  """Executes `tfds build {cmd_flags}` and returns the list of generated ds."""
  # Execute the command
  args = main._parse_flags(f'tfds build {cmd_flags}'.split())

  original_dl_and_prepare = tfds.core.DatasetBuilder.download_and_prepare

  # Unfortunately, `mock.Mock` removes `self` from `call_args`, so we have
  # to patch the function to record the generated_ds manually.
  # See:
  # https://stackoverflow.com/questions/64792295/how-to-get-self-instance-in-mock-mock-call-args
  generated_ds_names = []

  def _download_and_prepare(self, *args, **kwargs):
    # Remove version from generated name (as only last version can be generated)
    full_name = '/'.join(self.info.full_name.split('/')[:-1])
    generated_ds_names.append(full_name)
    if mock_download_and_prepare:
      return
    else:
      return original_dl_and_prepare(self, *args, **kwargs)

  with mock.patch(
      'tensorflow_datasets.core.DatasetBuilder.download_and_prepare',
      _download_and_prepare):
    main.main(args)
  return generated_ds_names


def test_build_single():
  assert _build('mnist') == ['mnist']
  assert _build('mnist:3.0.1') == ['mnist']
  # Keyword arguments also possible
  assert _build('--datasets mnist') == ['mnist']

  with pytest.raises(tfds.core.registered.DatasetNotFoundError):
    _build('unknown_dataset')

  with pytest.raises(AssertionError, match='cannot be loaded at version 1.0.0'):
    _build('mnist:1.0.0')  # Can only built the last version

  with pytest.raises(ValueError, match='not have config'):
    _build('mnist --config_idx 0')


def test_build_multiple():
  # Multiple datasets can be built in a single call
  assert _build('mnist imagenet2012 cifar10') == [
      'mnist',
      'imagenet2012',
      'cifar10',
  ]
  # Keyword arguments also possible
  assert _build('mnist --datasets imagenet2012 cifar10') == [
      'mnist',
      'imagenet2012',
      'cifar10',
  ]


def test_build_dataset_configs():
  # By default, all configs are build
  assert _build('trivia_qa') == [
      'trivia_qa/rc',
      'trivia_qa/rc.nocontext',
      'trivia_qa/unfiltered',
      'trivia_qa/unfiltered.nocontext',
  ]

  # If config is set, only the defined config is generated

  # --config_idx
  assert _build('trivia_qa --config_idx=0') == ['trivia_qa/rc']

  # --config
  assert _build('trivia_qa --config unfiltered.nocontext') == [
      'trivia_qa/unfiltered.nocontext',
  ]

  # --config Json
  config_json = '{"name":"my_config","description":"abcd"}'
  assert _build(f'imdb_reviews --config {config_json}') == [
      'imdb_reviews/my_config',
  ]

  # name/config
  assert _build('trivia_qa/unfiltered.nocontext') == [
      'trivia_qa/unfiltered.nocontext'
  ]

  with pytest.raises(ValueError, match='Config should only be defined once'):
    _build('trivia_qa/unfiltered.nocontext --config_idx=0')

  with pytest.raises(ValueError, match='greater than number of configs'):
    _build('trivia_qa --config_idx 100')


def test_exclude_datasets():
  # Exclude all datasets except 2
  all_ds = [b for b in tfds.list_builders() if b not in ('mnist', 'cifar10')]
  all_ds_str = ','.join(all_ds)

  assert _build(f'--exclude_datasets {all_ds_str}') == [
      'cifar10',
      'mnist',
  ]

  with pytest.raises(ValueError, match='--exclude_datasets can\'t be used'):
    _build('mnist --exclude_datasets cifar10')


def test_build_overwrite(mock_default_data_dir: pathlib.Path):  # pylint: disable=redefined-outer-name
  data_dir = mock_default_data_dir / 'mnist/3.0.1'
  data_dir.mkdir(parents=True)
  metadata_path = tfds.core.tfds_path(
      'testing/test_data/dataset_info/mnist/3.0.1')

  for f in metadata_path.iterdir():  # Copy metadata files.
    data_dir.joinpath(f.name).write_text(f.read_text())

  # By default, will skip generation if the data already exists
  assert _build('mnist') == ['mnist']  # Called, but no-op
  assert data_dir.exists()

  assert _build('mnist --overwrite') == ['mnist']
  assert not data_dir.exists()  # Previous data-dir has been removed


def test_max_examples_per_split_0(mock_default_data_dir: pathlib.Path):  # pylint: disable=redefined-outer-name
  assert _build(
      'dummy_dataset_no_generate --max_examples_per_split 0',
      mock_download_and_prepare=False,
  ) == ['dummy_dataset_no_generate']

  builder_path = mock_default_data_dir / 'dummy_dataset_no_generate/1.0.0'
  # Dataset has been generated
  assert builder_path.exists()
  # tf-records files have not been generated
  assert sorted(builder_path.iterdir()) == [
      builder_path / 'dataset_info.json',
      builder_path / 'features.json',
  ]


def test_build_files():
  # Make sure DummyDataset isn't registered by default
  with pytest.raises(tfds.core.registered.DatasetNotFoundError):
    _build('dummy_dataset')

  with pytest.raises(FileNotFoundError, match='Could not find .* script'):
    _build('')

  # cd .../datasets/dummy_dataset && tfds build
  with mock_cwd(_DUMMY_DATASET_PATH):
    assert _build('') == ['dummy_dataset']

  # cd .../datasets/dummy_dataset && tfds build dummy_dataset.py
  with mock_cwd(_DUMMY_DATASET_PATH):
    assert _build('dummy_dataset.py') == ['dummy_dataset']

  # cd .../datasets/ && tfds build dummy_dataset
  with mock_cwd(_DUMMY_DATASET_PATH.parent):
    assert _build('dummy_dataset') == ['dummy_dataset']

  # cd .../datasets/ && tfds build dummy_dataset --imports=xxx
  # --imports is passed. so do not load dataset from file
  with mock_cwd(_DUMMY_DATASET_PATH.parent):
    with pytest.raises(tfds.core.registered.DatasetNotFoundError):
      assert _build('dummy_dataset --imports=os')

  # cd .../datasets/ && tfds build dummy_dataset/dummy_dataset
  with mock_cwd(_DUMMY_DATASET_PATH.parent):
    assert _build('dummy_dataset/dummy_dataset') == ['dummy_dataset']


# Somehow only with tf-nightly, `dummy_dataset` is already imported by
# community/load_test.py (with `skip_registration()`). Thus import here have
# no-effects.
@pytest.mark.skip(reason='Conflict with `load_test.py`')
def test_build_import():
  # DummyDataset isn't registered by default
  with pytest.raises(tfds.core.registered.DatasetNotFoundError):
    _build('dummy_dataset')

  # --imports register the dataset
  ds_module = 'tensorflow_datasets.testing.dummy_dataset.dummy_dataset'
  assert _build(f'dummy_dataset --imports {ds_module}') == ['dummy_dataset']


def test_publish_data_dir(mock_fs: testing.MockFs):
  del mock_fs
  builder = testing.DummyMnist(data_dir='/tmp')
  actual = build_lib._publish_data_dir(
      publish_dir=epath.Path('/a/b'), builder=builder)
  assert actual == epath.Path('/a/b/dummy_mnist/3.0.1')
  assert build_lib._publish_data_dir(publish_dir=None, builder=builder) is None


def test_publish_data(mock_fs: testing.MockFs):
  builder = testing.DummyMnist(data_dir='/tmp')
  expected_from = epath.Path('/tmp') / 'dummy_mnist/3.0.1'
  filename = 'dataset_info.json'
  content = 'a'
  mock_fs.add_file(path=expected_from / filename, content=content)
  publish_data_dir = epath.Path('/a/b')
  build_lib._publish_data(publish_data_dir=publish_data_dir, builder=builder)
  assert mock_fs.read_file(publish_data_dir / filename) == content


def test_download_only():
  with mock.patch(
      'tensorflow_datasets.download.DownloadManager.download') as mock_download:
    assert not _build('dummy_dataset_no_generate --download_only')
    mock_download.assert_called_with({'file0': 'http://data.org/file1.zip'})

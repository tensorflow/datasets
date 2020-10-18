"""Tests for tensorflow_datasets.core.utils.gpath."""

import os
import pathlib
from pathlib import Path

import pytest
import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.core.utils.gpath import GcsPath


@pytest.fixture
def mocked_gfile_path(tmp_path: pathlib.Path):
  def _norm_path(path: str):
    return path.replace('gs://', os.fspath(tmp_path) + '/')

  def _rename(source, target, overwrite=False):
    if not overwrite:
      os.rename(source, target)
    else:
      os.replace(source, target)

  with testing.mock_tf(
      'tf.io.gfile',
      exists=lambda p: os.path.exists(_norm_path(p)),
      isdir=lambda p: os.path.isdir(_norm_path(p)),
      listdir=lambda p: os.listdir(_norm_path(p)),
      GFile=lambda p, *args, **kwargs: open(_norm_path(p), *args, **kwargs),
      rename=lambda p1, p2, **kwargs: _rename(_norm_path(p1), _norm_path(p2), **kwargs),
      mkdir=lambda p: os.mkdir(_norm_path(p)),
      makedirs=lambda p: os.makedirs(_norm_path(p)),
      glob=lambda p: Path(_norm_path(p)).parent.glob(Path(_norm_path(p)).stem)  # TODO: temporary function
  ):
    yield tmp_path


def test_representations(mocked_gfile_path: pathlib.Path):
  g_path = GcsPath('gs://bucket/dir')

  assert isinstance(g_path, GcsPath)
  assert isinstance(g_path.joinpath('file.py').parent, GcsPath)
  assert str(g_path) == 'gs://bucket/dir'
  assert os.fspath(g_path) == 'gs://bucket/dir'

  g_path = GcsPath('/gs/bucket/datasets/')
  assert str(g_path) == 'gs://bucket/datasets'
  assert repr(g_path).startswith('GcsPath')

  p = GcsPath(g_path, 'mnist', 'dataset.json')
  assert str(p) == 'gs://bucket/datasets/mnist/dataset.json'

  parts = [g_path, Path('mnist-100'), 'dataset.json']
  assert '/'.join(os.fspath(p)
                  for p in parts) == 'gs://bucket/datasets/mnist-100/dataset.json'

  with pytest.raises(ValueError, match='Invalid path'):
    GcsPath('/bucket/dir')


def test_gfs(mocked_gfile_path: pathlib.Path):
  # touch()
  touch_path = GcsPath('gs://touch.txt')
  assert not touch_path.exists()

  touch_path.touch()
  assert touch_path.exists()
  assert mocked_gfile_path.joinpath('touch.txt').exists()

  # mkdir()
  g_path = GcsPath('gs://bucket/dir')
  assert not g_path.exists()
  g_path.mkdir(parents=True)

  # exists()
  assert g_path.exists()
  assert mocked_gfile_path.joinpath('bucket/dir').exists()

  # is_dir()
  assert not mocked_gfile_path.joinpath('read_text_file.txt').is_dir()
  assert g_path.is_dir()


def test_open(mocked_gfile_path: pathlib.Path):

  files = ['foo.py', 'bar.py', 'foo_bar.py', 'dataset.json',
           'dataset_info.json', 'readme.md']
  dataset_path = GcsPath('gs://bucket/dataset')

  dataset_path.mkdir(parents=True)
  assert dataset_path.exists()

  # open()
  for file in files:
    with dataset_path.joinpath(file).open('w') as f:
      f.write(' ')

  # iterdir()
  assert len(list(mocked_gfile_path.joinpath('bucket/dataset').iterdir())) == 6


def test_read_write(mocked_gfile_path: pathlib.Path):
  # read_text()
  with tf.io.gfile.GFile('gs://text_file.txt', 'w') as f:
    f.write('abcd')
  assert mocked_gfile_path.joinpath('text_file.txt').read_text() == 'abcd'

  # read_bytes()
  with tf.io.gfile.GFile('gs://bytes_file.txt', 'wb') as f:
    f.write(b'abcd')
  assert mocked_gfile_path.joinpath('bytes_file.txt').read_bytes() == b'abcd'

  # write_text() write_bytes()
  GcsPath('gs://tfds_text.txt').write_text('tfds')
  GcsPath('gs://tfds_byte.txt').write_bytes(b'tfds')

  # read_text() and read_bytes()
  assert GcsPath('gs://text_file.txt').read_text() == 'abcd'
  assert GcsPath('gs://bytes_file.txt').read_bytes() == b'abcd'

  assert GcsPath('gs://tfds_text.txt').read_text() == 'tfds'
  assert GcsPath('gs://tfds_byte.txt').read_bytes() == b'tfds'

  assert mocked_gfile_path.joinpath('text_file1.txt').read_text() == 'abcd'
  assert mocked_gfile_path.joinpath('bytes_file1.txt').read_bytes() == b'foobar'


def test_mkdir(mocked_gfile_path: pathlib.Path):
  g_path = GcsPath('gs://bucket')
  assert not g_path.exists()

  g_path.mkdir()
  assert g_path.exists()

  with pytest.raises(FileExistsError, match='already exists'):
    g_path.mkdir()

  assert mocked_gfile_path.joinpath('bucket').exists()


def test_rename(mocked_gfile_path: pathlib.Path):
  src_path = GcsPath('gs://foo.py')
  src_path.write_text(' ')

  assert mocked_gfile_path.joinpath('foo.py').exists()

  src_path.rename('gs://bar.py')

  assert not mocked_gfile_path.joinpath('foo.py').exists()
  assert mocked_gfile_path.joinpath('bar.py').exists()

  file_name = lambda l: l.name
  assert sorted(list(map(file_name, mocked_gfile_path.iterdir()))) == ['bar.py']


def test_replace(mocked_gfile_path: pathlib.Path):

  file_path = GcsPath('gs://tfds.py')
  file_path.write_text('tfds')

  file_path.replace('gs://tfds-dataset.py')

  assert not mocked_gfile_path.joinpath('tfds.py').exists()
  assert mocked_gfile_path.joinpath('tfds-dataset.py').exists()
  assert mocked_gfile_path.joinpath('tfds-dataset.py').read_text() == 'tfds'

  mnist_path = GcsPath('gs://mnist.py')
  mnist_path.write_text('mnist')

  mnist_path.replace('gs://mnist-100.py')

  assert not mocked_gfile_path.joinpath('mnist.py').exists()
  assert mocked_gfile_path.joinpath('mnist-100.py').exists()
  assert mocked_gfile_path.joinpath('mnist-100.py').read_text() == 'mnist'

  assert len(list(mocked_gfile_path.iterdir())) == 2

  file_name = lambda l: l.name
  assert sorted(list(map(file_name, mocked_gfile_path.iterdir()))) == ['mnist-100.py',
                                                                       'tfds-dataset.py']

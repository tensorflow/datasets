from absl import app
import os
import inspect
import posixpath
import shutil
import tensorflow_datasets as tfds
from tensorflow_datasets.core import naming
from typing import Type

"""A refactoring script to aggregate datasets file from diferent directories

my_dataset/
    fake_data/
    __init__.py
    dataset.py
    dataset_test.py
    make_fake_data.py
    checksum.txt

To run this script
python3 -m tensorflow_datasets.scripts.refactoring.refactoring_dataset

New datasets will be generated in tensorflow_datasets/refactored_dataset

"""

NEW_TFDS_DIR = 'tensorflow_datasets/refactored_dataset'
URL_CHECKSUM_DIR = 'tensorflow_datasets/url_checksums'
FAKE_DATA_DIR = 'tensorflow_datasets/testing/test_data/fake_examples'
FAKE_DATA_SCRIPT_DIR = 'tensorflow_datasets/testing/fake_data_generation'

_INIT_FILE = """\
\"""{dataset_name} dataset.\"""
from tensorflow_datasets.{dataset_type}.{dataset_name}.{dataset_name} import {dataset_name_cls}
"""

class BuilderInfo:
  '''
  dataset_file: path
  dataset_name: str
  dataset_type: str
  dataset_path: path
  '''

  def __init__(self, dataset_file, dataset_name, dataset_type, dataset_path):
    self.dataset_file = dataset_file
    self.dataset_name = dataset_name
    self.dataset_type = dataset_type
    self.dataset_path = dataset_path


def create_dirs(dataset_path: str) -> None:
  """Creates a new `my_dataset` directory"""
  if not os.path.exists(dataset_path):
    os.makedirs(os.path.join(dataset_path, 'fake_data'))


def make_init_file(dataset_info, dest_path) -> None:
  """Creates a new __init__.py. file"""
  file_path = os.path.join(dest_path, '__init__.py')
  dataset_name_cls = naming.snake_to_camelcase(dataset_info.dataset_name)
  data = {'dataset_type': dataset_info.dataset_type,
          'dataset_name': dataset_info.dataset_name,
          'dataset_name_cls': dataset_name_cls}

  with open(file_path, 'w') as f:
    f.write(_INIT_FILE.format(**data))


def copy_checksum_file(dataset_info, dest_path) -> None:
  """Copy checksum.txt file"""
  src_checksum_path = f'{URL_CHECKSUM_DIR}/{dataset_info.dataset_name}.txt'
  if os.path.exists(src_checksum_path):
    shutil.copy(src_checksum_path,
                os.path.join(dest_path, f'{dataset_info.dataset_name}.txt'))


def copy_make_data_file(dataset_info, dest_path) -> None:
  """Copy fake data genneration script file"""
  src_fake_data_script_path = f'{FAKE_DATA_SCRIPT_DIR}/{dataset_info.dataset_name}.py'
  if os.path.exists(src_fake_data_script_path):
    shutil.copy(src_fake_data_script_path,
                os.path.join(dest_path, 'make_fake_data.py'))


def copy_fake_data_dir(dataset_info, dest_path) -> None:
  """Copy fake data directory"""
  src_fake_data_dir = os.path.join(FAKE_DATA_DIR, dataset_info.dataset_name)
  if os.path.exists(src_fake_data_dir):
    if os.path.exists(dest_path):
      shutil.rmtree(dest_path)
    shutil.copytree(src_fake_data_dir, os.path.join(dest_path, 'fake_data'))


def copy_dataset_file(dataset_info, dest_path) -> None:
  """Copy my_dataset.py file"""

  shutil.copy(dataset_info.dataset_file,
              os.path.join(dest_path, f'{dataset_info.dataset_name}.py'))


def copy_dataset_test_file(dataset_info, dest_path) -> None:
  """Copy my_dataset_test.py file"""
  src_dataset_test_path = f'{dataset_info.dataset_path}/{dataset_info.dataset_name}_test.py'
  if os.path.exists(src_dataset_test_path):
    shutil.copy(src_dataset_test_path,
                os.path.join(dest_path, f'{dataset_info.dataset_name}_test.py'))


def extract_info(builder_cls: Type[tfds.core.DatasetBuilder]) -> BuilderInfo:
  """Extract dataset name, filepath, type, path from the DatasetBuilder class."""
  dataset_file = os.path.relpath(inspect.getfile(builder_cls)) # i.e tensorflow_datasets/image/mnist.py
  dataset_name = builder_cls.name                              # name of the dataset i.e mnist
  dataset_type = dataset_file.split('/')[1]                    # type of the dataset i.e image
  dataset_path = posixpath.split(dataset_file)[0]              # i.e tensorflow_datasets/image
  return BuilderInfo(dataset_file, dataset_name, dataset_type, dataset_path)


def refactor_dataset(DATASET_LIST):
  """Refactoring all dataset into one folder"""
  for dataset in DATASET_LIST:
    builder_cls = tfds.builder_cls(dataset)
    dataset_info = extract_info(builder_cls)

    # Refactored dataset path
    refactor_dataset_path = os.path.join(NEW_TFDS_DIR,
                                         dataset_info.dataset_type,
                                         dataset_info.dataset_name)

    create_dirs(refactor_dataset_path)   # create dirs

    # Copy all files and folders
    copy_fake_data_dir(dataset_info, refactor_dataset_path)
    make_init_file(dataset_info, refactor_dataset_path)
    copy_dataset_file(dataset_info, refactor_dataset_path)
    copy_dataset_test_file(dataset_info, refactor_dataset_path)
    copy_make_data_file(dataset_info, refactor_dataset_path)
    copy_checksum_file(dataset_info, refactor_dataset_path)

    print('The refactored {} dataset generated at {}'.format(dataset_info.dataset_name, refactor_dataset_path))


def main(_):
  refactor_dataset(tfds.list_builders())


if __name__ == '__main__':
  app.run(main)

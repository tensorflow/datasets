r"""A refactoring script to aggregate datasets file from diferent directories

my_dataset/
    fake_data/
    __init__.py
    dataset.py
    dataset_test.py
    make_fake_data.py
    checksum.txt

Instructions:
To run this script:

```
python3 -m tensorflow_datasets.scripts.refactoring.refactoring_dataset
```

"""

from dataclasses import dataclass
import inspect
from pathlib import Path
import shutil
from typing import Type, List
from absl import app
import tensorflow_datasets as tfds
from tensorflow_datasets.core import naming


TFDS_DIR = 'tensorflow_datasets'
URL_CHECKSUM_DIR = 'tensorflow_datasets/url_checksums'
FAKE_DATA_DIR = 'tensorflow_datasets/testing/test_data/fake_examples'
FAKE_DATA_SCRIPT_DIR = 'tensorflow_datasets/testing/fake_data_generation'

_INIT_FILE = """\
\"""{dataset_name} dataset.\"""
from tensorflow_datasets.{dataset_type}.{dataset_name}.{dataset_name} import {dataset_name_cls}
"""

@dataclass
class BuilderInfo:
  '''Dataset metadata
  dataset_file: path to dataset file
  dataset_name: name of the dataset
  dataset_type: type of the dataset
  dataset_path: path to dataset type directory
  '''
  dataset_file: Path
  dataset_name: str
  dataset_type: str
  dataset_path: Path


def create_dirs(dataset_path: Path) -> None:
  """Creates a new `my_dataset` directory"""
  if not dataset_path.exists():
    Path.mkdir(dataset_path.joinpath('fake_data'), parents=True)


def make_init_file(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Creates a new __init__.py. file"""
  file_path = dest_path.joinpath('__init__.py')
  dataset_name_cls = naming.snake_to_camelcase(dataset_info.dataset_name)
  data = {'dataset_type': dataset_info.dataset_type,
          'dataset_name': dataset_info.dataset_name,
          'dataset_name_cls': dataset_name_cls}

  with file_path.open('w') as f:
    f.write(_INIT_FILE.format(**data))


def copy_checksum_file(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Copy checksum.txt file"""
  src_checksum_path = Path(f'{URL_CHECKSUM_DIR}/'
                           f'{dataset_info.dataset_name}.txt')
  if src_checksum_path.exists():
    shutil.copy(src_checksum_path,
                dest_path.joinpath(f'{dataset_info.dataset_name}.txt'))


def copy_make_data_file(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Copy fake data generation script file"""
  src_fake_data_script_path = Path(f'{FAKE_DATA_SCRIPT_DIR}/' \
                              f'{dataset_info.dataset_name}.py')
  if src_fake_data_script_path.exists():
    shutil.copy(src_fake_data_script_path,
                dest_path.joinpath('make_fake_data.py'))


def copy_fake_data_dir(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Copy fake data directory"""
  src_fake_data_dir = Path(FAKE_DATA_DIR).joinpath(dataset_info.dataset_name)
  dest_fake_data_dir = Path(dest_path).joinpath('fake_data')
  if src_fake_data_dir.exists():
    if dest_fake_data_dir.exists():
      shutil.rmtree(dest_fake_data_dir)
    shutil.copytree(src_fake_data_dir, dest_fake_data_dir)


def copy_dataset_file(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Copy my_dataset.py file"""
  shutil.copy(dataset_info.dataset_file,
              dest_path.joinpath(f'{dataset_info.dataset_name}.py'))


def copy_dataset_test_file(dataset_info: BuilderInfo, dest_path: Path) -> None:
  """Copy my_dataset_test.py file"""
  test_file = Path(Path(dataset_info.dataset_file).name).stem
  src_dataset_test_path = Path(f'{dataset_info.dataset_path}/'
                               f'{test_file}_test.py')
  if src_dataset_test_path.exists():
    shutil.copy(src_dataset_test_path,
                dest_path.joinpath(f'{dataset_info.dataset_name}_test.py'))


def extract_info(builder_cls: Type[tfds.core.DatasetBuilder]) -> BuilderInfo:
  """Extract dataset name, filepath, type, path from the DatasetBuilder class."""
  dataset_file = Path(inspect.getfile(builder_cls)).relative_to(Path.cwd())  # Path: tensorflow_datasets/image/mnist.py
  dataset_name = builder_cls.name          # Str: name of the dataset i.e mnist
  dataset_type = dataset_file.parts[1]     # Str: type of the dataset i.e image
  dataset_path = dataset_file.parents[0]   # Path: tensorflow_datasets/image
  return BuilderInfo(dataset_file, dataset_name, dataset_type, dataset_path)


def refactor_dataset(dataset_list: List) -> None:
  """Refactoring all dataset into one folder"""
  for dataset in dataset_list:
    builder_cls = tfds.builder_cls(dataset)
    dataset_info = extract_info(builder_cls)
    # Refactored dataset path
    refactor_dataset_path = Path(TFDS_DIR,
                                 dataset_info.dataset_type,
                                 dataset_info.dataset_name)

    create_dirs(refactor_dataset_path)  # create dirs

    # Copy all files and folders
    copy_fake_data_dir(dataset_info, refactor_dataset_path)
    make_init_file(dataset_info, refactor_dataset_path)
    copy_dataset_file(dataset_info, refactor_dataset_path)
    copy_dataset_test_file(dataset_info, refactor_dataset_path)
    copy_make_data_file(dataset_info, refactor_dataset_path)
    copy_checksum_file(dataset_info, refactor_dataset_path)
    print(f'The refactored {dataset_info.dataset_name} '
          f'dataset generated at {refactor_dataset_path}')


def main(_):
  refactor_dataset(tfds.list_builders())


if __name__ == '__main__':
  app.run(main)

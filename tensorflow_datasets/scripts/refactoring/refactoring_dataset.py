from absl import app
import os
import posixpath
import shutil
import tensorflow_datasets as tfds
from tensorflow_datasets.core import naming
from typing import Dict

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

TFDS_DIR = 'tensorflow_datasets'
NEW_TFDS_DIR = 'tensorflow_datasets/refactored_dataset'
URL_CHECKSUM_DIR = 'tensorflow_datasets/url_checksums'
FAKE_DATA_DIR = 'tensorflow_datasets/testing/test_data/fake_examples'
FAKE_DATA_SCRIPT_DIR = 'tensorflow_datasets/testing/fake_data_generation'

_INIT_FILE = """\
\"""{dataset_name} dataset.\"""
from tensorflow_datasets.{dataset_type}.{dataset_name}.{dataset_name} import {dataset_name_cls}
"""

DATASET_TYPE = ['audio',
                'image',
                'image_classification',
                'object_detection',
                'question_answering',
                'structured',
                'summarization',
                'text',
                'translate',
                'video']

audio_datasets = ['common_voice', 'crema_d', 'dementiabank', 'fuss', 'groove',
                  'librispeech', 'libritts', 'ljspeech', 'nsynth', 'savee',
                  'speech_commands', 'tedlium', 'vctk', 'voxceleb', 'voxforge']

DATASETS_NAMES = {
  'audio': ['tedlium', 'speech_commands'],    # will add full audio_datasets list
  'image': ['arc', 'abstract_reasoning'],
  'image_classification': ['binary_alpha_digits']
}


def create_dirs(dataset_path: str) -> None:
  """Creates a new `my_dataset` directory"""
  if not os.path.exists(dataset_path):
    os.makedirs(os.path.join(dataset_path, 'fake_data'))


def make_init_file(dataset_type, dataset_name, dataset_path) -> None:
  """Creates a new __init__.py. file"""
  file_path = os.path.join(dataset_path, '__init__.py')
  dataset_name_cls = naming.snake_to_camelcase(dataset_name)
  data = {'dataset_type': dataset_type,
          'dataset_name': dataset_name,
          'dataset_name_cls': dataset_name_cls}

  with open(file_path, 'w') as f:
    f.write(_INIT_FILE.format(**data))


def copy_checksum_file(src_checksum_path, dest_path) -> None:
  """Copy checksum.txt file"""
  if os.path.exists(src_checksum_path):
    shutil.copy(src_checksum_path,
                os.path.join(dest_path, posixpath.basename(src_checksum_path)))


def copy_make_data_file(src_fake_data_script_path, dest_path) -> None:
  """Copy fake data genneration script file"""
  if os.path.exists(src_fake_data_script_path):
    shutil.copy(src_fake_data_script_path,
                os.path.join(dest_path, 'make_fake_data.py'))


def copy_fake_data_dir(src_fake_data_dir, dest_path) -> None:
  """Copy fake data directory"""
  if os.path.exists(src_fake_data_dir):
    if os.path.exists(dest_path):
      shutil.rmtree(dest_path)
    shutil.copytree(src_fake_data_dir, os.path.join(dest_path, 'fake_data'))


def copy_dataset_file(src_dataset_path, dest_path) -> None:
  """Copy my_dataset.py file"""
  shutil.copy(src_dataset_path,
              os.path.join(dest_path, posixpath.basename(src_dataset_path)))


def copy_dataset_test_file(src_dataset_test_path, dest_path) -> None:
  """Copy my_dataset_test.py file"""
  shutil.copy(src_dataset_test_path,
              os.path.join(dest_path, posixpath.basename(src_dataset_test_path)))


def refactor_dataset(datasets: Dict[str, list]) -> None:
  """Refactor all the dataset"""
  for dataset_type, dataset_names in datasets.items():
    for dataset_name in dataset_names:
      # Dataset files path
      fake_data_dir = os.path.join(FAKE_DATA_DIR, dataset_name)
      fake_data_script_py = f'{FAKE_DATA_SCRIPT_DIR}/{dataset_name}.py'
      dataset_dir = os.path.join(TFDS_DIR, dataset_type)
      checksum_txt = f'{URL_CHECKSUM_DIR}/{dataset_name}.txt'
      dataset_py = f'{dataset_dir}/{dataset_name}.py'
      dataset_test_py = f'{dataset_dir}/{dataset_name}_test.py'

      # Newly creted dataset path
      refactor_dataset_path = os.path.join(NEW_TFDS_DIR, dataset_type, dataset_name)

      # Create dirs
      create_dirs(refactor_dataset_path)

      # Copy all files and folders
      copy_fake_data_dir(fake_data_dir, refactor_dataset_path)
      make_init_file(dataset_type, dataset_name, refactor_dataset_path)
      copy_dataset_file(dataset_py, refactor_dataset_path)
      copy_dataset_test_file(dataset_test_py, refactor_dataset_path)
      copy_make_data_file(fake_data_script_py, refactor_dataset_path)
      copy_checksum_file(checksum_txt, refactor_dataset_path)

      print('The refactored {} dataset generated at {}'.format(dataset_name, refactor_dataset_path))


def main(_):
  refactor_dataset(DATASETS_NAMES)


if __name__ == '__main__':
  app.run(main)

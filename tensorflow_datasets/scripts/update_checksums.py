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

"""Script to update all the checksums.tsv files with tabs instead of spaces"""

from absl import app
from typing import List
from pathlib import Path

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds

_DATASET_TYPES = list(['audio',
                        'image',
                        'image_classification',
                        'object_detection',
                        'question_answering',
                        'structured',
                        'summarization',
                        'text',
                        'translate',
                        'video'])

_ROOT_DIR = Path(__file__).parent.parent

_TXT_CHECKSUM_DIR = Path.joinpath(_ROOT_DIR, 'url_checksums')
_TXT_CHECKSUM_SUFFIX = '.txt'
_TSV_CHECKSUM_SUFFIX = '.tsv'


def get_tsv_checksums_paths() -> List[str]:
  """Returns the paths of all the .tsv checksum files of folder datasets"""
  paths = list()
  datasets_list = tfds.list_builders()
  for dataset in datasets_list:
    path = Path.joinpath(tfds.builder_cls(dataset).code_path.parent,
                        'checksums.tsv')
    if path.is_file():
      paths.append(path)
  return paths

def get_txt_checksums_paths() -> List[str]:
  """Returns the paths of all the .txt checksum files relative to the
  root directory"""

  #print(_TXT_CHECKSUM_DIR)
  paths = list([Path.joinpath(_TXT_CHECKSUM_DIR, path)
                for path in tf.io.gfile.listdir(_TXT_CHECKSUM_DIR)
                if path.endswith(_TXT_CHECKSUM_SUFFIX)])
  return paths


def rewrite_checksums(paths : List[str]) -> None:
  """Update all .txt checksum files to use tabs instead of spaces"""
  for path in paths:
    print(f'Processing file: {path}')
    #Read the checksum file
    with tf.io.gfile.GFile(path) as f:
      content = f.read().splitlines()

    #Checking whether file already has tabs or not
    if content == []:
      continue
    elif len(content[0].split('\t'))==3:
      continue
    else:
      content = [info.rsplit(' ', 2) for info in content]
      with tf.io.gfile.GFile(path, 'w') as f:
        for info in content:
          url, size, checksum = info
          f.write(f'{url}\t{size}\t{checksum}\n')


def update_checksums() -> None:
  paths = get_txt_checksums_paths()
  rewrite_checksums(paths)
  paths = get_tsv_checksums_paths()
  rewrite_checksums(paths)
  print('\n\nAll checksums files have been successfully updated!')

def main(_):
  update_checksums()

if __name__ == '__main__':
  app.run(main)

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

import os
from absl import app
from typing import List

import tensorflow.compat.v2 as tf

_DATASET_TYPES = list(['audio',
                        'image',
                        'image_claffication',
                        'onject_detection',
                        'question_answering',
                        'structured',
                        'summarization',
                        'text',
                        'translate',
                        'video'])

_ROOT_DIR = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))

_TXT_CHECKSUM_DIR = os.path.join(_ROOT_DIR, 'url_checksums')
_TXT_CHECKSUM_SUFFIX = '.txt'
_TSV_CHECKSUM_SUFFIX = '.tsv'


def get_tsv_checksums_paths() -> List[str]:
  """Returns the paths of all the .tsv checksum files of folder datasets"""
  paths = list()
  for dataset_type in _DATASET_TYPES:
    #Check whether the dataset type folder exists
    dataset_dir = os.path.join(_ROOT_DIR, dataset_type)
    if tf.io.gfile.isdir(dataset_dir):

      #Find the paths of all datasets in every type of dataset
      dataset_paths = [os.path.join(dataset_dir, dir)
                  for dir in tf.io.gfile.listdir(dataset_dir)
                  if tf.io.gfile.isdir(os.path.join(dataset_dir, dir)) and
                  dir!='_pycache_']

      #Getting the path of eack checksum file for every dataset
      for dataset_path in dataset_paths:
        checksum_path = os.path.join(dataset_path, 'checksums.tsv')
        if os.path.isfile(checksum_path):
          paths.append(checksum_path)
    else:
      continue
  return paths

def get_txt_checksums_paths() -> List[str]:
  """Returns the paths of all the .txt checksum files relative to the
  root directory"""

  #print(_TXT_CHECKSUM_DIR)
  paths = list([os.path.join(_TXT_CHECKSUM_DIR, path)
                for path in tf.io.gfile.listdir(_TXT_CHECKSUM_DIR)
                if path.endswith(_TXT_CHECKSUM_SUFFIX)])
  return paths


def rewrite_checksums(paths : List[str]) -> None:
  """Update all .txt checksum files to use tabs instead of spaces"""
  for path in paths:
    print('Processing file: {}'.format(path))
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
          f.write('{}    {}    {}\n'.format(url, size, checksum))


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

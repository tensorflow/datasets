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

r"""Update checksums to contain filename."""

import os
import pathlib
import requests
from absl import app
from typing import Dict
from concurrent import futures

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.download import checksums


TFDS_PATH = tfds.core.utils.tfds_path()


def _get_builder_checksum_path(name) -> pathlib.Path:
  """Get path of DatasetBuilder dataset."""
  # instead of glob can also use
  # tfds.builder_cls(name).__dict__.__module__.split('.')[1:-1] to get path
  path = (
    tf.io.gfile.glob(os.path.join(
      TFDS_PATH, '*', name, 'checksums.tsv'))
    or
    # since yesno dataset folder name is inconsistent with the
    # dataset.builder's dataset name (yes_no)
    tf.io.gfile.glob(os.path.join(
      TFDS_PATH, '*', name.replace('_', ''), 'checksums.tsv'))
  )
  path = path[0]
  if isinstance(path, str):
    path = pathlib.Path(path)
  return path

def _request_filename(url) -> (str, str):
  """Get filename of dataset at `url`."""
  filename  = ''
  try:
    response = requests.get(url, timeout=10)
    filename = tfds.core.download.downloader._get_filename(response)
    print(f'Success for {url}')
  except requests.exceptions.HTTPError as http_err:
    print(f'HTTP Error {http_err} for {url}.')
  except Exception as error:
    print(f'Error {error} for {url}.')
  return (url, filename)

def _update_url_infos(url_infos) -> Dict[str, checksums.UrlInfo]:
  """Get and update dataset filname in UrlInfo."""
  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    all_content = executor.map(_request_filename, url_infos)

  for content in all_content:
    url, filename = content
    url_infos[url].filename = filename
  return url_infos

def main(_):
  # Legacy datasets
  url_checksums_paths = checksums._checksum_paths().values()
  print(url_checksums_paths)
  for url_path in list(url_checksums_paths):
    if isinstance(url_path, str):
      url_path = pathlib.Path(url_path)
    url_infos = checksums.load_url_infos(url_path)  #load checksums
    url_infos = _update_url_infos(url_infos)        #update checkums to add filename
    checksums.save_url_infos(url_path, url_infos)   #save checksums

  # New datasets - tfds.core.DatasetBuilder
  for name in tfds.list_builders()[:20]:
      if not tfds.builder_cls(name).url_infos:
        url_infos = tfds.builder_cls(name).url_infos  #load checksums
        url_infos = _update_url_infos(url_infos)      #update checkums to add filename
        path = _get_builder_checksum_path(name)       #get checksums path
        checksums.save_url_infos(path, url_infos)     #save checksums


if __name__ == '__main__':
  app.run(main)

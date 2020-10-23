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
from typing import Dict, List
from concurrent import futures

import tensorflow_datasets as tfds
from tensorflow_datasets.core.download import checksums


TFDS_PATH = tfds.core.utils.tfds_write_path()


def _collect_path_to_update() -> List[tfds.core.utils.ReadWritePath]:
  """Collect checksums paths to update."""
  url_checksums_paths = list(checksums._checksum_paths().values())

  builder_checksums_path = []
  for name in tfds.list_builders():
    builder_cls = tfds.builder_cls(name)
    if builder_cls.url_infos != None:
      builder_checksums_path.append(builder_cls._checksums_path)
  return url_checksums_paths + builder_checksums_path

def _request_filename(url) -> (str, str):
  """Get filename of dataset at `url`."""
  filename  = ''
  try:
    response = requests.get(url, timeout=10)
    filename = tfds.core.download.downloader._get_filename(response)
    print(f'Success for {url}')
  except requests.exceptions.HTTPError as http_err:
    print(f'HTTP Error {http_err} for {url}.')
  return (url, filename)

def _update_url_infos(url_infos, filenames) -> Dict[str, checksums.UrlInfo]:
  """Get and update dataset filname in UrlInfo."""
  for url, filename in filenames:
    url_infos[url].filename = filename
  return url_infos


def main(_):
  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_filenames = {}
    cached_url_infos = {}
    # Collect legacy datasets as well as new datasets
    for url_path in _collect_path_to_update():
      url_infos = checksums.load_url_infos(url_path)
      cached_url_infos[url_path] = url_infos
      future_filenames[url_path] = executor.map(_request_filename, url_infos)
    for path, future_filename in future_filenames.items():
      old_url_infos = cached_url_infos[path]
      updated_url_infos = _update_url_infos(old_url_infos, future_filename)
      checksums.save_url_infos(path, updated_url_infos)


if __name__ == '__main__':
  app.run(main)

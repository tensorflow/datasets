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
import logging
import dataclasses
from absl import app
from typing import Dict, List
from concurrent import futures

import tensorflow_datasets as tfds
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums

TFDS_PATH = tfds.core.utils.tfds_write_path()


def _collect_path_to_url_infos() -> Dict[utils.ReadWritePath,
                                          Dict[str, checksums.UrlInfo]]:
  """Collect checksums paths to url_infos."""
  path_to_url_infos = {}

  url_checksums_paths = list(checksums._checksum_paths().values())

  builder_checksums_path = []
  for name in tfds.list_builders():
    builder_cls = tfds.builder_cls(name)
    if builder_cls.url_infos is not None:
      builder_checksums_path.append(builder_cls._checksums_path)

  for url_path in url_checksums_paths + builder_checksums_path:
    path_to_url_infos[url_path] = checksums.load_url_infos(url_path)
  return path_to_url_infos

def _request_filename(url) -> str:
  """Get filename of dataset at `url`."""
  filename  = ''
  try:
    response = requests.get(url, timeout=10)
    filename = tfds.core.download.downloader._get_filename(response)
    print(f'Success for {url}')
  except requests.exceptions.HTTPError as http_err:
    print(f'HTTP Error {http_err} for {url}.')
  return filename

def _update_url_infos(url_infos, urls_to_filename) -> Dict[str, checksums.UrlInfo]:
  """Get and update dataset filname in UrlInfo."""
  for url, url_info in url_infos.items():
    new_filename = urls_to_filename[url].result()
    old_filename = url_info.filename
    if old_filename and old_filename != new_filename:
      logging.warning(f"Filename for {url} already exist. "
                      f"Updating {old_filename} to {new_filename}")
    url_info = dataclasses.replace(url_info, filename=new_filename)
    url_infos.update({url: url_info})
  return url_infos

def main(_):
  path_to_url_infos = _collect_path_to_url_infos()

  # Remove duplicate urls
  all_url_infos = {}
  for url_infos in path_to_url_infos.values():
    all_url_infos.update(url_infos)

  with futures.ThreadPoolExecutor(max_workers=100) as executor:
    urls_to_filename = {
      url: executor.submit(_request_filename, url)
      for url in all_url_infos
    }
    for path, url_infos in path_to_url_infos.items():
      url_infos = _update_url_infos(url_infos, urls_to_filename)
      checksums.save_url_infos(path, url_infos)


if __name__ == '__main__':
  app.run(main)

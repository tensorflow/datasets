# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.download.checksums."""

import hashlib
import pathlib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums


def test_checksums(tmp_path: pathlib.Path):
  path = tmp_path / 'checksums.tsv'
  url_infos = {
      'http://abc.org/data':
          checksums.UrlInfo(
              checksum='abcd',
              size=1234,
              filename='a.zip',
          ),
      'http://edf.org/data':
          checksums.UrlInfo(
              checksum='abcd',
              size=1234,
              filename='b.zip',
          ),
  }

  checksums.save_url_infos(path, url_infos)
  loaded_url_infos = checksums.load_url_infos(path)
  assert loaded_url_infos == url_infos


def test_compute_url_info():
  filepath = utils.tfds_path() / 'testing/test_data/6pixels.png'

  expected_url_info = checksums.UrlInfo(
      checksum='04f38ebed34d3b027d2683193766155912fba647158c583c3bdb4597ad8af34c',
      size=utils.Size(102),
      filename='6pixels.png',
  )
  url_info = checksums.compute_url_info(filepath, checksum_cls=hashlib.sha256)
  assert url_info == expected_url_info
  assert url_info.filename == expected_url_info.filename

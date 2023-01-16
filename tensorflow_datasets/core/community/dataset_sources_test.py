# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.community.dataset_sources."""

import os

from tensorflow_datasets.core import github_api
from tensorflow_datasets.core.community import dataset_sources


def test_dataset_source():
  uri = 'github://owner/repo/tree/master/.../audio/gtzan/gtzan.py'
  src = dataset_sources.DatasetSource.from_json(uri)
  assert isinstance(src.root_path, github_api.GithubPath)
  assert (
      os.fspath(src.root_path)
      == 'github://owner/repo/tree/master/.../audio/gtzan'
  )
  assert src.filenames == ['gtzan.py']
  src_json = src.to_json()
  assert uri == src_json
  assert src == dataset_sources.DatasetSource.from_json(src_json)


def test_dataset_source_multifiles():
  json_input = {
      'root_path': 'github://owner/repo/tree/master/.../audio/gtzan',
      'filenames': ['checksums.tsv', 'gtzan.py'],
  }
  src = dataset_sources.DatasetSource.from_json(json_input)
  assert isinstance(src.root_path, github_api.GithubPath)
  assert (
      os.fspath(src.root_path)
      == 'github://owner/repo/tree/master/.../audio/gtzan'
  )
  assert src.filenames == ['checksums.tsv', 'gtzan.py']
  src_json = src.to_json()
  assert json_input == src_json
  assert src == dataset_sources.DatasetSource.from_json(src_json)

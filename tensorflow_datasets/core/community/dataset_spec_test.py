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

"""Tests for tensorflow_datasets.core.community.dataset_specs."""

from tensorflow_datasets.core import github_api
from tensorflow_datasets.core.community import dataset_spec


def test_import_export_json_source():
  p = github_api.GithubPath('/tensorflow/graphics/tree/path/to/datasets')
  source = dataset_spec.GithubSource(p)

  source_uri = source.to_uri()
  assert source_uri == 'github://tensorflow/graphics/tree/path/to/datasets'

  reconstructed_source = dataset_spec.DatasetSource.from_uri(source_uri)
  assert isinstance(reconstructed_source, dataset_spec.GithubSource)
  assert source_uri == reconstructed_source.to_uri()


def test_import_export_json_spec():
  p = github_api.GithubPath('/tensorflow/graphics/tree/path/to/datasets')
  spec = dataset_spec.DatasetSpec(
      name='mnist',
      namespace='tensorflow_graphics',
      source=dataset_spec.GithubSource(p),
  )
  assert spec.cannonical_name == 'tensorflow_graphics/mnist'

  json_spec = spec.to_json()
  assert json_spec == {
      'name': 'mnist',
      'namespace': 'tensorflow_graphics',
      'source': 'github://tensorflow/graphics/tree/path/to/datasets',
  }

  reconstructed_spec = dataset_spec.DatasetSpec.from_json(json_spec)
  assert isinstance(reconstructed_spec.source, dataset_spec.GithubSource)
  assert json_spec == reconstructed_spec.to_json()

# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from unittest import mock

import datasets as hf_datasets
import numpy as np
import pytest
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder
from tensorflow_datasets.core.utils.lazy_imports_utils import huggingface_hub

PIL_Image = lazy_imports_lib.lazy_imports.PIL_Image


class DummyHuggingfaceBuilder(hf_datasets.GeneratorBasedBuilder):

  def _info(self):
    return hf_datasets.DatasetInfo(
        description='description',
        citation='citation',
        license='test-license',
        features=None,
        version='1.0.0',
    )

  def _split_generators(self, dl_manager):
    return [hf_datasets.SplitGenerator(name='train.clean')]

  def _generate_examples(self):
    for i in range(2):
      yield i, {
          'number': i,
          'text': f'{i}',
          'image': PIL_Image.new(mode='L', size=(4, 4)),
      }

  def download_and_prepare(self, *args, **kwargs):
    # Disable downloads from GCS
    kwargs['try_from_hf_gcs'] = False
    super().download_and_prepare(*args, **kwargs)


@pytest.fixture(name='load_dataset_builder')
def mock_load_dataset_builder(tmp_path):
  hf_builder = DummyHuggingfaceBuilder(cache_dir=tmp_path / 'data')
  hf_builder.download_and_prepare = mock.Mock(
      wraps=hf_builder.download_and_prepare
  )
  with mock.patch.object(
      hf_datasets, 'load_dataset_builder', return_value=hf_builder
  ) as load_dataset_builder:
    yield load_dataset_builder


@pytest.fixture(name='login_to_hf')
def mock_login_to_hf():
  with mock.patch.object(
      huggingface_dataset_builder, 'login_to_hf'
  ) as login_to_hf:
    yield login_to_hf


@pytest.fixture(autouse=True)
def mock_hub_dataset_info():
  fake_dataset_info = huggingface_hub.hf_api.DatasetInfo(
      id='foo/bar',
      citation='citation from the hub',
      private=False,
      downloads=123,
      likes=456,
      tags=[],
  )
  with mock.patch.object(
      huggingface_hub, 'dataset_info', return_value=fake_dataset_info
  ) as dataset_info:
    yield dataset_info


@pytest.fixture(name='builder')
def mock_huggingface_dataset_builder(
    tmp_path, load_dataset_builder, login_to_hf
):
  builder = huggingface_dataset_builder.HuggingfaceDatasetBuilder(
      file_format='array_record',
      hf_repo_id='foo/bar',
      hf_config='config',
      ignore_verifications=True,
      data_dir=tmp_path / 'data',
      hf_hub_token='SECRET_TOKEN',
      hf_num_proc=100,
      other_arg='this is another arg',
  )
  load_dataset_builder.assert_called_once_with(
      'foo/bar', 'config', other_arg='this is another arg'
  )
  login_to_hf.assert_called_once_with('SECRET_TOKEN')
  assert builder.info.description == 'description'
  assert builder.info.citation == 'citation from the hub'
  assert builder.info.redistribution_info.license == 'test-license'
  yield builder


def test_download_and_prepare(builder):
  builder.download_and_prepare()
  ds = builder.as_data_source()
  expected_image = PIL_Image.new(mode='RGB', size=(4, 4))
  # Split names are sanitized, eg train.clean -> train_clean
  for element, expected in zip(
      ds['train_clean'],
      [
          {'number': 0, 'text': b'0', 'image': expected_image},
          {'number': 1, 'text': b'1', 'image': expected_image},
      ],
  ):
    for feature in ['number', 'text', 'image']:
      assert np.array_equal(element[feature], expected[feature])
  assert len(ds['train_clean']) == 2


def test_all_parameters_are_passed_down_to_hf(builder):
  builder._hf_builder.download_and_prepare.assert_called_once_with(
      verification_mode='no_checks', num_proc=100
  )


def test_hf_features(builder):
  assert builder._hf_features() == {
      'number': hf_datasets.Value('int64'),
      'text': hf_datasets.Value('string'),
      'image': hf_datasets.Image(),
  }

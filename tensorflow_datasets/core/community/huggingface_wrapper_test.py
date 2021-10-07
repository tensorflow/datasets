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

"""Tests for tensorflow_datasets.core.community.huggingface_wrapper."""

import pathlib

import tensorflow as tf
from tensorflow_datasets.core.community import huggingface_wrapper as hg_wrapper


def test_make_scalar_feature():
  assert hg_wrapper._make_scalar_feature('string') == tf.string
  assert hg_wrapper._make_scalar_feature('bool') == tf.bool
  assert hg_wrapper._make_scalar_feature('double') == tf.float64
  assert hg_wrapper._make_scalar_feature('int32') == tf.int32


def test_mock_gfile(tmp_path: pathlib.Path):
  with hg_wrapper.mock_builtin_to_use_gfile():
    with open(tmp_path / 'test.txt', 'w') as f:
      f.write('hello!\n')


def test_mock_import(tmp_path: pathlib.Path):
  with hg_wrapper.mock_huggingface_import():
    from tensorflow_datasets.testing.huggingface import dummy_dataset  # pylint: disable=g-import-not-at-top

  builder = dummy_dataset.HFDataset(data_dir=tmp_path)
  builder.download_and_prepare()
  assert builder.info.splits['train'].num_examples == 10
  assert builder.info.splits['validation'].num_examples == 5
  # TFDS re-order the config so the default one is the first one, as HF
  # explicitly define the default config through `DEFAULT_CONFIG_NAME`
  assert builder.BUILDER_CONFIGS[0].name == 'config2'

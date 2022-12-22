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

"""Test import."""

import sys
from unittest import mock

from absl import logging
import tensorflow_datasets as tfds


def test_import_tfds_without_loading_tf():
  with mock.patch.object(logging, 'log_first_n') as log_first_n:
    assert 'tensorflow' not in sys.modules

    with tfds.testing.tmp_dir() as data_dir:
      tfds.testing.DummyMnist(data_dir=data_dir).download_and_prepare()
      tfds.load('dummy_mnist', split='train', data_dir=data_dir)

    # No warning concerning TensorFlow DTypes was dispatched while loading
    assert not log_first_n.called

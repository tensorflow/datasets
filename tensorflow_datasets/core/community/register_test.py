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

"""Tests for tensorflow_datasets.core.community.register."""

import pathlib
import textwrap

from tensorflow_datasets.core.community import dataset_spec
from tensorflow_datasets.core.community import register


# pylint: disable=redefined-outer-name


def test_available_register(tmp_path: pathlib.Path):
  # Create a dummy register
  register_path = tmp_path / 'register.jsonl'
  register_path.write_text(
      textwrap.dedent(
          """\
          {"name": "mnist", "namespace": "nlp", "source": "github://user/nlp/tree/datasets/mnist"}
          {"name": "robotnet", "namespace": "nlp", "source": "github://user/nlp/tree/datasets/robotnet"}
          {"name": "cifar", "namespace": "tensorflow_graphics", "source": "github://tensorflow/graphics/tree/datasets/cifar"}
          """
      )
  )
  dummy_register = register.DatasetSpecRegister(str(register_path))

  assert dummy_register.is_available()
  assert dummy_register.dataset_specs == {
      'nlp/mnist': dataset_spec.DatasetSpec(
          name='mnist',
          namespace='nlp',
          source=dataset_spec.GithubSource.from_uri(
              'github://user/nlp/tree/datasets/mnist'
          ),
      ),
      'nlp/robotnet': dataset_spec.DatasetSpec(
          name='robotnet',
          namespace='nlp',
          source=dataset_spec.GithubSource.from_uri(
              'github://user/nlp/tree/datasets/robotnet'
          ),
      ),
      'tensorflow_graphics/cifar': dataset_spec.DatasetSpec(
          name='cifar',
          namespace='tensorflow_graphics',
          source=dataset_spec.GithubSource.from_uri(
              'github://tensorflow/graphics/tree/datasets/cifar'
          ),
      ),
  }


def test_unavailable_register(tmp_path: pathlib.Path):
  # Create a dummy register pointing to an unavailable file.
  register_path = tmp_path / 'register.jsonl'
  dummy_register = register.DatasetSpecRegister(str(register_path))
  assert not dummy_register.is_available()

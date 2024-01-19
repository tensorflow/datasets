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

"""Tests for conllu_dataset_builder_utils."""

from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib


def test_get_universal_morphology_config():
  lang_1 = "it"
  lang_2 = "de"
  config_1 = conllu_lib.get_universal_morphology_config(
      language=lang_1,
      features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES,
      name=f"test_{lang_1}",
  )
  config_2 = conllu_lib.get_universal_morphology_config(
      language=lang_2,
      features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES,
      name=f"test_{lang_2}",
      description="Config 2 description.",
  )

  assert config_1.name == f"test_{lang_1}"
  assert config_2.name == f"test_{lang_2}"

  assert config_1.language == lang_1
  assert config_2.language == lang_2

  assert config_1.features == config_2.features

  assert config_1.description is None
  assert config_2.description != config_1.description

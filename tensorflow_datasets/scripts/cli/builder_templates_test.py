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

"""Tests for builder_templates."""
import pathlib
import pytest

from tensorflow_datasets.scripts.cli import builder_templates
from tensorflow_datasets.scripts.cli import cli_utils as utils

NAME = "my_dataset"
PATH_DIR = pathlib.Path.cwd() / "tensorflow_datasets/image/my_dataset"
TFDS_API = "tensorflow_datasets"
TODO = f"{NAME}"

testdata = [
    (builder_templates.STANDARD, "tfds.core.GeneratorBasedBuilder"),
    (builder_templates.CONLL, "tfds.dataset_builders.ConllDatasetBuilder"),
    (builder_templates.CONLLU, "tfds.dataset_builders.ConllUDatasetBuilder"),
]


@pytest.mark.parametrize("ds_format,ds_builder", testdata)
def test_valid_builder_templates(ds_format, ds_builder):
  dataset_info = utils.DatasetInfo(
      name=NAME, in_tfds=True, path=PATH_DIR, data_format=ds_format
  )
  template = builder_templates.create_builder_template(dataset_info)
  assert isinstance(template, str)
  assert ds_builder in template


def test_create_inexistent_builder_template():
  nonexistent_data_format = "nonexistent_data_format"
  nonexistent_dataset_info = utils.DatasetInfo(
      name=NAME,
      in_tfds=True,
      path=PATH_DIR,
      data_format=nonexistent_data_format,
  )

  error_msg = (
      f"Required format {nonexistent_data_format} isn't associated with a"
      " format-specific builder in TFDS."
  )
  with pytest.raises(ValueError, match=error_msg):
    builder_templates.create_builder_template(nonexistent_dataset_info)

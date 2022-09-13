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

"""Utility functions for TFDS CLI."""

import dataclasses
import itertools
import pathlib
from tensorflow_datasets.core import naming


@dataclasses.dataclass
class DatasetInfo:
  """Structure for common string used for formatting.

  Attributes:
    name: Dataset name (`my_dataset`)
    cls_name: Class name (`MyDataset`)
    path: Root directory in which the dataset is added
    in_tfds: Whether the dataset is added in tensorflow_datasets/ or externally
    tfds_api: The Dataset API to import
    todo: Field to fill (`TODO(my_dataset)`)
    ds_import: Dataset import (`tensorflow_datasets.image.my_dataset`)
    data_format: Optional format of the input data used to generate
      format-specific dataset builders.
  """
  name: str
  in_tfds: bool
  path: pathlib.Path
  cls_name: str = dataclasses.field(init=False)
  tfds_api: str = dataclasses.field(init=False)
  todo: str = dataclasses.field(init=False)
  ds_import: str = dataclasses.field(init=False)
  data_format: str

  def __post_init__(self):
    self.cls_name = naming.snake_to_camelcase(self.name)
    self.tfds_api = ('tensorflow_datasets.public_api'
                     if self.in_tfds else 'tensorflow_datasets')
    self.todo = f'TODO({self.name})'

    if self.in_tfds:
      # `/path/to/tensorflow_datasets/image/my_dataset`
      # ->`tensorflow_datasets.image.my_dataset`
      import_parts = itertools.dropwhile(lambda p: p != 'tensorflow_datasets',
                                         self.path.parts)
      ds_import = '.'.join(import_parts)
    else:
      # For external datasets, it's difficult to correctly infer the full
      # `from my_module.path.datasets.my_dataset import MyDataset`.
      # Could try to auto-infer the absolute import path from the `setup.py`.
      # Instead uses relative import for now: `from . import my_dataset`
      ds_import = '.'
    self.ds_import = ds_import

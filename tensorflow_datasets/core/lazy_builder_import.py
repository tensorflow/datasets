# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Class to lazy load DatasetBuilder classes from legacy locations.

This module is only intended to be used until all TFDS `DatasetsBuilder`s are
defined under the "datasets/" directory and the legacy locations have been
deprecated (ie: a new major release).
"""
from typing import Text

from absl import logging
from tensorflow_datasets.core import registered


class LazyBuilderImport:
  """Lazy load DatasetBuilder from given name from legacy locations."""

  def __init__(self, dataset_name: Text):
    object.__setattr__(self, "_dataset_name", dataset_name)
    object.__setattr__(self, "_dataset_cls", None)

  def _get_builder_cls(self):
    cls = object.__getattribute__(self, "_dataset_cls")
    if not cls:
      builder_name = object.__getattribute__(self, "_dataset_name")
      logging.warning(
          (
              "DEPRECATED! Do not use a DatasetBuilder class directly, but"
              " call `tfds.builder_cls('%s')`."
          ),
          builder_name,
      )
      cls = registered.imported_builder_cls(builder_name)
      object.__setattr__(self, "_dataset_cls", cls)
    return cls

  def __getattribute__(self, attr_name):
    cls = object.__getattribute__(self, "_get_builder_cls")()
    return getattr(cls, attr_name)

  def __call__(self, *args, **kwargs):
    cls = object.__getattribute__(self, "_get_builder_cls")()
    return cls(*args, **kwargs)

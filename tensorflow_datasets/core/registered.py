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

"""Access registered datasets."""

import abc
import collections
import contextlib
import inspect
from typing import Iterator

from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import py_utils

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

# Datasets that are under active development and which we can't therefore load.
# <str snake_cased_name, in development DatasetBuilder subclass>
_IN_DEVELOPMENT_REGISTRY = {}

# Keep track of Dict[str (module name), List[DatasetBuilder]]
# This is directly accessed by `tfds.community.builder_cls_from_module` when
# importing community packages.
_MODULE_TO_DATASETS = collections.defaultdict(list)



_skip_registration = False


@contextlib.contextmanager
def skip_registration() -> Iterator[None]:
  """Context manager within which dataset builders are not registered."""
  global _skip_registration
  try:
    _skip_registration = True
    yield
  finally:
    _skip_registration = False


class RegisteredDataset(abc.ABCMeta):
  """Subclasses will be registered and given a `name` property."""

  def __new__(cls, cls_name, bases, class_dict):
    name = naming.camelcase_to_snakecase(cls_name)
    class_dict["name"] = name
    builder_cls = super(RegisteredDataset, cls).__new__(  # pylint: disable=too-many-function-args,redefined-outer-name
        cls, cls_name, bases, class_dict)

    if py_utils.is_notebook():  # On Colab/Jupyter, we allow overwriting
      pass
    elif name in _DATASET_REGISTRY:
      raise ValueError("Dataset with name %s already registered." % name)
    elif name in _IN_DEVELOPMENT_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as in development." % name)
    elif name in _ABSTRACT_DATASET_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as abstract." % name)

    is_abstract = inspect.isabstract(builder_cls)

    # Capture all concrete datasets, including when skip registration is True.
    # This ensure that `builder_cls_from_module` can load the datasets
    # even when the module has been imported inside a `skip_registration`
    # context.
    if not is_abstract:
      _MODULE_TO_DATASETS[builder_cls.__module__].append(builder_cls)

    if _skip_registration:
      pass  # Skip dataset registration within the contextmanager
    elif is_abstract:
      _ABSTRACT_DATASET_REGISTRY[name] = builder_cls
    elif class_dict.get("IN_DEVELOPMENT"):
      _IN_DEVELOPMENT_REGISTRY[name] = builder_cls
    else:
      _DATASET_REGISTRY[name] = builder_cls
    return builder_cls

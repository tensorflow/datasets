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
import textwrap
from typing import ClassVar, Iterator, List, Type

from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import py_utils

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

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


class DatasetNotFoundError(ValueError):
  """The requested Dataset was not found."""

  def __init__(self, name, is_abstract=False):
    self.is_abstract = is_abstract
    if is_abstract:
      error_string = (
          f'Dataset {name} is an abstract class so cannot be created. '
          'Please make sure to instantiate all abstract methods.\n'
      )
    else:
      all_datasets_str = '\n\t- '.join([''] + list_registered_datasets())
      error_string = (
          f'Dataset {name} not found. Available datasets:{all_datasets_str}\n'
      )
    error_string += textwrap.dedent(
        """
        Check that:
            - if dataset was added recently, it may only be available
              in `tfds-nightly`
            - the dataset name is spelled correctly
            - dataset class defines all base class abstract methods
            - the module defining the dataset class is imported
        """
    )
    ValueError.__init__(self, error_string)


class RegisteredDataset(abc.ABC):
  """Subclasses will be registered and given a `name` property."""

  # Name of the dataset, automatically filled.
  name: ClassVar[str]


  def __init_subclass__(cls, skip_registration=False, **kwargs):  # pylint: disable=redefined-outer-name
    super().__init_subclass__(**kwargs)

    # Set the name if the dataset does not define it.
    # Use __dict__ rather than getattr so subclasses are not affected.
    if not cls.__dict__.get('name'):
      cls.name = naming.camelcase_to_snakecase(cls.__name__)

    is_abstract = inspect.isabstract(cls)

    # Capture all concrete datasets, including when skip registration is True.
    # This ensure that `builder_cls_from_module` can load the datasets
    # even when the module has been imported inside a `skip_registration`
    # context.
    if not is_abstract:
      _MODULE_TO_DATASETS[cls.__module__].append(cls)

    # Skip dataset registration within contextmanager, or if skip_registration
    # is passed as meta argument.
    if skip_registration or _skip_registration:
      return

    # Check for name collisions
    if py_utils.is_notebook():  # On Colab/Jupyter, we allow overwriting
      pass
    elif cls.name in _DATASET_REGISTRY:
      raise ValueError(f'Dataset with name {cls.name} already registered.')
    elif cls.name in _ABSTRACT_DATASET_REGISTRY:
      raise ValueError(
          f'Dataset with name {cls.name} already registered as abstract.'
      )

    # Add the dataset to the registers
    if is_abstract:
      _ABSTRACT_DATASET_REGISTRY[cls.name] = cls
    else:
      _DATASET_REGISTRY[cls.name] = cls


def list_registered_datasets() -> List[str]:
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  return sorted(list(_DATASET_REGISTRY))


def registered_dataset_cls(name: str) -> Type[RegisteredDataset]:
  """Returns the Registered dataset class."""
  if name in _ABSTRACT_DATASET_REGISTRY:
    raise DatasetNotFoundError(name, is_abstract=True)
  if name not in _DATASET_REGISTRY:
    raise DatasetNotFoundError(name)
  return _DATASET_REGISTRY[name]  # pytype: disable=bad-return-type

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

"""Access registered datasets."""

import abc
import collections
import contextlib
import functools
import importlib
import inspect
import os.path
from typing import ClassVar, Dict, Iterator, List, Type, Text, Tuple

from etils import epath
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import visibility
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import resource_utils

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

# Keep track of Dict[str (module name), List[DatasetBuilder]]
# This is directly accessed by `tfds.community.builder_cls_from_module` when
# importing community packages.
_MODULE_TO_DATASETS = collections.defaultdict(list)

# Internal registry containing:
# <str registered_name, DatasetCollectionBuilder subclass>
_DATASET_COLLECTION_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetCollectionBuilder subclass>
_ABSTRACT_DATASET_COLLECTION_REGISTRY = {}

# Keep track of Dict[str (module name), List[DatasetCollectionBuilder]]
_MODULE_TO_DATASET_COLLECTIONS = collections.defaultdict(list)


class DatasetNotFoundError(ValueError):
  """Exception raised when the dataset cannot be found."""


class DatasetCollectionNotFoundError(ValueError):
  """Exception raised when the dataset collection cannot be found."""


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


# The implementation of this class follows closely RegisteredDataset.
class RegisteredDatasetCollection(abc.ABC):
  """Subclasses will be registered and given a `name` property."""

  # Name of the dataset_collection, automatically filled.
  name: ClassVar[str]

  def __init_subclass__(cls, skip_registration=False, **kwargs):  # pylint: disable=redefined-outer-name
    super().__init_subclass__(**kwargs)

    # Set the name if the dataset_collection does not define it.
    # Use __dict__ rather than getattr so subclasses are not affected.
    if not cls.__dict__.get('name'):
      cls.name = naming.camelcase_to_snakecase(cls.__name__)

    is_abstract = inspect.isabstract(cls)

    # Capture all concrete dataset_collections, including when skip registration
    # is True. This ensures that `builder_cls_from_module` can load the
    # dataset_collections even when the module has been imported inside a
    # `skip_registration` context.
    if not is_abstract:
      _MODULE_TO_DATASET_COLLECTIONS[cls.__module__].append(cls)

    # Skip dataset_collection registration within contextmanager, or if
    # skip_registration is passed as meta argument.
    if skip_registration or _skip_registration:
      return

    # Check for name collisions
    if py_utils.is_notebook():  # On Colab/Jupyter, we allow overwriting
      pass
    elif cls.name in _DATASET_COLLECTION_REGISTRY:
      raise ValueError(
          f'DatasetCollection with name {cls.name} already registered.')
    elif cls.name in _ABSTRACT_DATASET_COLLECTION_REGISTRY:
      raise ValueError(
          f'DatasetCollection with name {cls.name} already registered as abstract.'
      )

    # Add the dataset_collection to the registers
    if is_abstract:
      _ABSTRACT_DATASET_COLLECTION_REGISTRY[cls.name] = cls
    else:
      _DATASET_COLLECTION_REGISTRY[cls.name] = cls


def list_imported_dataset_collections() -> List[str]:
  """Returns the string names of all `tfds.core.DatasetCollection`s."""
  all_dataset_collections = [
      dataset_collection_name for dataset_collection_name,
      dataset_collection_cls in _DATASET_COLLECTION_REGISTRY.items()
  ]
  return sorted(all_dataset_collections)


def is_dataset_collection(name: str) -> bool:
  return name in _DATASET_COLLECTION_REGISTRY


def imported_dataset_collection_cls(
    name: str) -> Type[RegisteredDatasetCollection]:
  """Returns the Registered dataset class."""
  if name in _ABSTRACT_DATASET_COLLECTION_REGISTRY:
    raise AssertionError(f'DatasetCollection {name} is an abstract class.')

  if not is_dataset_collection(name):
    raise DatasetCollectionNotFoundError(f'DatasetCollection {name} not found.')

  dataset_collection_cls = _DATASET_COLLECTION_REGISTRY[name]

  return dataset_collection_cls  # pytype: disable=bad-return-type


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
    # This ensures that `builder_cls_from_module` can load the datasets
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
          f'Dataset with name {cls.name} already registered as abstract.')

    # Add the dataset to the registers
    if is_abstract:
      _ABSTRACT_DATASET_REGISTRY[cls.name] = cls
    else:
      _DATASET_REGISTRY[cls.name] = cls


def _is_builder_available(builder_cls: Type[RegisteredDataset]) -> bool:
  """Returns `True` is the builder is available."""
  return visibility.DatasetType.TFDS_PUBLIC.is_available()


def list_imported_builders() -> List[str]:
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  all_builders = [
      builder_name for builder_name, builder_cls in _DATASET_REGISTRY.items()
      if _is_builder_available(builder_cls)
  ] + list(_get_existing_dataset_packages(constants.DATASETS_TFDS_SRC_DIR))
  return sorted(all_builders)


@functools.lru_cache(maxsize=None)
def _get_existing_dataset_packages(
    datasets_dir: Text) -> Dict[Text, Tuple[epath.Path, Text]]:
  """Returns existing datasets.

  Args:
    datasets_dir: directory path, relative to tensorflow_datasets srcs root,
      where are defined the dataset packages. This directory must only contain
      valid dataset packages.

  Returns:
    {ds_name: (pkg_path, builder_module)}.
    For example: {'mnist': ('/lib/tensorflow_datasets/datasets/mnist',
                            'tensorflow_datasets.datasets.mnist.builder')}
  """
  datasets = {}
  try:
    datasets_dir_path = resource_utils.tfds_path(datasets_dir)
  except OSError:
    # Raised when datasets_dir does not exist, for example in tests when data
    # does not contain the directory (when running with bazel).
    return datasets
  if not datasets_dir_path.exists():
    return datasets
  ds_dir_pkg = '.'.join(['tensorflow_datasets'] +
                        datasets_dir.split(os.path.sep))
  for child in datasets_dir_path.iterdir():
    # Except for `__init__.py`, all children of datasets/ directory are packages
    # of datasets.
    # There are no exceptions, so no needs to check child is a directory and
    # contains a `builder.py` module.
    if child.name != '__init__.py':
      pkg_path = epath.Path(datasets_dir_path) / child.name
      builder_module = f'{ds_dir_pkg}.{child.name}.{child.name}_dataset_builder'
      datasets[child.name] = (pkg_path, builder_module)
  return datasets


def imported_builder_cls(name: str) -> Type[RegisteredDataset]:
  """Returns the Registered dataset class."""
  existing_ds_pkgs = _get_existing_dataset_packages(
      constants.DATASETS_TFDS_SRC_DIR)
  if name in existing_ds_pkgs:
    pkg_dir_path, builder_module = existing_ds_pkgs[name]
    cls = importlib.import_module(builder_module).Builder
    cls.pkg_dir_path = pkg_dir_path
    return cls

  if name in _ABSTRACT_DATASET_REGISTRY:
    # Will raise TypeError: Can't instantiate abstract class X with abstract
    # methods y, before __init__ even get called
    _ABSTRACT_DATASET_REGISTRY[name]()  # pytype: disable=not-callable
    # Alternatively, could manually extract the list of non-implemented
    # abstract methods.
    raise AssertionError(f'Dataset {name} is an abstract class.')

  if name not in _DATASET_REGISTRY:
    raise DatasetNotFoundError(f'Dataset {name} not found.')

  builder_cls = _DATASET_REGISTRY[name]
  if not _is_builder_available(builder_cls):
    available_types = visibility.get_availables()
    msg = f'Dataset {name} is not available. Only: {available_types}'
    raise PermissionError(msg)
  return builder_cls  # pytype: disable=bad-return-type

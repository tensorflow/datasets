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

"""Access registered datasets."""

import abc
import collections
from collections.abc import Iterator
import contextlib
import functools
import importlib
import inspect
import os.path
import time
from typing import ClassVar, Type

from absl import logging
from etils import epath
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import visibility
import tensorflow_datasets.core.logging as _tfds_logging
from tensorflow_datasets.core.logging import call_metadata as _call_metadata
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import resource_utils

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

# Keep track of dict[str (module name), list[DatasetBuilder]]
# This is directly accessed by `tfds.community.builder_cls_from_module` when
# importing community packages.
_MODULE_TO_DATASETS = collections.defaultdict(list)

# Internal registry containing:
# <str registered_name, DatasetCollectionBuilder subclass>
_DATASET_COLLECTION_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetCollectionBuilder subclass>
_ABSTRACT_DATASET_COLLECTION_REGISTRY = {}

# Keep track of dict[str (module name), list[DatasetCollectionBuilder]]
_MODULE_TO_DATASET_COLLECTIONS = collections.defaultdict(list)

# eg for dataset "foo": "tensorflow_datasets.datasets.foo.foo_dataset_builder".
_BUILDER_MODULE_SUFFIX = '_dataset_builder'


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


@functools.cache
def _import_legacy_builders() -> None:
  """Imports legacy builders."""
  modules_to_import = [
      'audio',
      'graphs',
      'image',
      'image_classification',
      'object_detection',
      'nearest_neighbors',
      'question_answering',
      'd4rl',
      'ranking',
      'recommendation',
      'rl_unplugged',
      'rlds.datasets',
      'robotics',
      'robomimic',
      'structured',
      'summarization',
      'text',
      'text_simplification',
      'time_series',
      'translate',
      'video',
      'vision_language',
  ]

  before_dataset_imports = time.time()
  metadata = _call_metadata.CallMetadata()
  metadata.start_time_micros = int(before_dataset_imports * 1e6)
  try:
    # For builds that don't include all dataset builders, we don't want to fail
    # on import errors of dataset builders.
    try:
      for module in modules_to_import:
        importlib.import_module(f'tensorflow_datasets.{module}')
    except (ImportError, ModuleNotFoundError):
      pass

  except Exception as exception:  # pylint: disable=broad-except
    metadata.mark_error()
    logging.exception(exception)
  finally:
    import_time_ms_dataset_builders = int(
        (time.time() - before_dataset_imports) * 1000
    )
    metadata.mark_end()
    _tfds_logging.tfds_import(
        metadata=metadata,
        import_time_ms_tensorflow=0,
        import_time_ms_dataset_builders=import_time_ms_dataset_builders,
    )


@functools.cache
def _import_dataset_collections() -> None:
  """Imports dataset collections."""
  try:
    importlib.import_module('tensorflow_datasets.dataset_collections')
  except (ImportError, ModuleNotFoundError):
    pass


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
          f'DatasetCollection with name {cls.name} already registered.'
      )
    elif cls.name in _ABSTRACT_DATASET_COLLECTION_REGISTRY:
      raise ValueError(
          f'DatasetCollection with name {cls.name} already registered as'
          ' abstract.'
      )

    # Add the dataset_collection to the registers
    if is_abstract:
      _ABSTRACT_DATASET_COLLECTION_REGISTRY[cls.name] = cls
    else:
      _DATASET_COLLECTION_REGISTRY[cls.name] = cls


def list_imported_dataset_collections() -> list[str]:
  """Returns the string names of all `tfds.core.DatasetCollection`s."""
  _import_dataset_collections()
  all_dataset_collections = list(_DATASET_COLLECTION_REGISTRY.keys())
  return sorted(all_dataset_collections)


def is_dataset_collection(name: str) -> bool:
  _import_dataset_collections()
  return name in _DATASET_COLLECTION_REGISTRY


def imported_dataset_collection_cls(
    name: str,
) -> Type[RegisteredDatasetCollection]:
  """Returns the Registered dataset class."""
  _import_dataset_collections()

  if name in _ABSTRACT_DATASET_COLLECTION_REGISTRY:
    raise AssertionError(f'DatasetCollection {name} is an abstract class.')

  if not is_dataset_collection(name):
    raise DatasetCollectionNotFoundError(f'DatasetCollection {name} not found.')

  dataset_collection_cls = _DATASET_COLLECTION_REGISTRY[name]

  return dataset_collection_cls  # pytype: disable=bad-return-type


class RegisteredDataset(abc.ABC):
  """Subclasses will be registered and given a `name` property."""

  # Name of the dataset, automatically filled if not already set.
  name: ClassVar[str]


  def __init_subclass__(cls, skip_registration=False, **kwargs):  # pylint: disable=redefined-outer-name
    super().__init_subclass__(**kwargs)

    # Set the name if the dataset does not define it.
    # Use __dict__ rather than getattr so subclasses are not affected.
    if not cls.__dict__.get('name'):
      if cls.__name__ == 'Builder':
        # Config-based builders should be defined with a class named "Builder".
        # In such a case, the builder name is extracted from the module if it
        # follows conventions:
        module_name = cls.__module__.rsplit('.', 1)[-1]
        if module_name.endswith(_BUILDER_MODULE_SUFFIX):
          cls.name = module_name[: -len(_BUILDER_MODULE_SUFFIX)]
        elif '.' in cls.__module__:  # Extract dataset name from package name.
          cls.name = cls.__module__.rsplit('.', 2)[-2]
        else:
          raise AssertionError(
              'When using `Builder` as class name, the dataset builder name is '
              'inferred from module name if named "*_dataset_builder" or from '
              f'package name, but there is no package in "{cls.__module__}".'
          )
      else:  # Legacy builders.
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
          f'Dataset with name {cls.name} already registered as abstract.'
      )

    # Add the dataset to the registers
    if is_abstract:
      _ABSTRACT_DATASET_REGISTRY[cls.name] = cls
    else:
      _DATASET_REGISTRY[cls.name] = cls


def _is_builder_available(builder_cls: Type[RegisteredDataset]) -> bool:
  """Returns `True` is the builder is available."""
  return visibility.DatasetType.TFDS_PUBLIC.is_available()


def list_imported_builders() -> list[str]:
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  _import_legacy_builders()
  all_builders = [
      builder_name
      for builder_name, builder_cls in _DATASET_REGISTRY.items()
      if _is_builder_available(builder_cls)
  ] + list(_get_existing_dataset_packages(constants.DATASETS_TFDS_SRC_DIR))
  return sorted(all_builders)


@functools.lru_cache(maxsize=None)
def _get_existing_dataset_packages(
    datasets_dir: str,
) -> dict[str, tuple[epath.Path, str]]:
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
  datasets_dir_path = resource_utils.tfds_path(datasets_dir)
  if not datasets_dir_path.exists():
    return datasets
  ds_dir_pkg = '.'.join(
      ['tensorflow_datasets'] + datasets_dir.split(os.path.sep)
  )
  for child in datasets_dir_path.iterdir():
    # Except for a few exceptions, all children of datasets/ directory are
    # packages of datasets, no needs to check child is a directory and contains
    # a `builder.py` module.
    exceptions = [
        '__init__.py',
    ]
    if child.name not in exceptions:
      pkg_path = epath.Path(datasets_dir_path) / child.name
      builder_module = (
          f'{ds_dir_pkg}.{child.name}.{child.name}{_BUILDER_MODULE_SUFFIX}'
      )
      datasets[child.name] = (pkg_path, builder_module)
  return datasets


def imported_builder_cls(name: str) -> Type[RegisteredDataset]:
  """Returns the Registered dataset class."""
  existing_ds_pkgs = _get_existing_dataset_packages(
      constants.DATASETS_TFDS_SRC_DIR
  )
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
    # Dataset not found in the registry, try to import legacy builders.
    # Dataset builders are imported lazily to avoid slowing down the startup
    # of the binary.
    _import_legacy_builders()
    if name not in _DATASET_REGISTRY:
      raise DatasetNotFoundError(f'Dataset {name} not found.')

  builder_cls = _DATASET_REGISTRY[name]
  if not _is_builder_available(builder_cls):
    available_types = visibility.get_availables()
    msg = f'Dataset {name} is not available. Only: {available_types}'
    raise PermissionError(msg)
  return builder_cls  # pytype: disable=bad-return-type

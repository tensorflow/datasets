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

"""TFDS logging module."""
import atexit
import threading
from typing import Callable, Dict, List, Optional, Tuple, TypeVar

from absl import flags
from tensorflow_datasets.core.logging import base_logger
from tensorflow_datasets.core.logging import call_metadata
from tensorflow_datasets.core.logging import logging_logger

import wrapt


_T = TypeVar("_T")

_registered_loggers: Optional[List[base_logger.Logger]] = None

_import_operations: List[Tuple[call_metadata.CallMetadata, int, int]] = []
_import_operations_lock = threading.Lock()

_thread_ids_running_builder_init = set()


def _check_init_registered_loggers() -> None:
  """Initializes the registered loggers if they are not set yet."""
  global _registered_loggers
  if _registered_loggers is None:
    _registered_loggers = [
        logging_logger.LoggingLogger(),
    ]


def _log_import_operation():
  """Log import operations (most of time maximum one), if any."""
  with _import_operations_lock:
    for metadata, import_time_tf, import_time_builders in _import_operations:
      for logger in _registered_loggers:
        logger.tfds_import(
            metadata=metadata,
            import_time_ms_tensorflow=import_time_tf,
            import_time_ms_dataset_builders=import_time_builders,
        )
    _import_operations.clear()


@atexit.register
def _at_exit():
  """Log import operation if needed, calls `process_ends` on loggers."""
  if _registered_loggers is None:
    _check_init_registered_loggers()
  _log_import_operation()
  for logger in _get_registered_loggers():
    logger.process_ends()


def _get_registered_loggers() -> List[base_logger.Logger]:
  _check_init_registered_loggers()
  _log_import_operation()
  return _registered_loggers


def register(logger: base_logger.Logger) -> None:
  """Register an additional logger within TFDS.

  Registered loggers are called on TFDS events, synchronously, from the same
  thread the call was made, in sequence, and in registration order. Exceptions
  are *NOT* caught.

  Args:
    logger: the logger to register.
  """
  _check_init_registered_loggers()
  _registered_loggers.append(logger)


def tfds_import(*, metadata: call_metadata.CallMetadata,
                import_time_ms_tensorflow: int,
                import_time_ms_dataset_builders: int):
  """Call `tfds_import` on registered loggers.

  Given the number of operations which can be done at import time should be
  limited, here the registered loggers calls are deferred and done either:
   - on the following call to one of the logging method; or
   - at exit time.

  Args:
    metadata: metadata associated to import operation.
    import_time_ms_tensorflow: time (ms) it took to import TF.
    import_time_ms_dataset_builders: time (ms) it took to import DatasetBuilder
      modules.
  """
  with _import_operations_lock:
    _import_operations.append(
        (metadata, import_time_ms_tensorflow, import_time_ms_dataset_builders))


def builder_init() -> Callable[[_T], _T]:
  """"Decorator to call `builder_init` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, dsbuilder, args, kwargs):
    metadata = call_metadata.CallMetadata()
    first_builder_init_in_stack = (
        metadata.thread_id not in _thread_ids_running_builder_init)
    if first_builder_init_in_stack:
      _thread_ids_running_builder_init.add(metadata.thread_id)
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      if first_builder_init_in_stack:
        metadata.mark_end()
        _thread_ids_running_builder_init.remove(metadata.thread_id)
        data_dir = kwargs.get("data_dir")
        config = kwargs.get("config")
        if config is not None:
          config = str(config)
        version = kwargs.get("version")
        if version is not None:
          version = str(version)
        for logger in _get_registered_loggers():
          logger.builder_init(
              metadata=metadata,
              name=dsbuilder.name,
              data_dir=data_dir,
              config=config,
              version=version)

  return decorator


def _get_name_config_version_datadir(dsbuilder):
  """Returns (builder_name, config, version, data_dir).

  Args:
    dsbuilder: the builder instance to get info for.
  """
  config_name = dsbuilder.builder_config.name if dsbuilder.builder_config else ""
  data_path = dsbuilder.data_dir
  return dsbuilder.name, config_name, str(dsbuilder.version), data_path


def builder_info() -> Callable[[_T], _T]:
  """"Decorator to call `builder_info` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, dsbuilder, args, kwargs):
    dsbuilder = args[0]  # Because property decorator applied first.
    name, config_name, version, data_path = (
        _get_name_config_version_datadir(dsbuilder))
    metadata = call_metadata.CallMetadata()
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.builder_info(
            metadata=metadata,
            name=name,
            config_name=config_name,
            version=version,
            data_path=data_path,
        )

  return decorator


def as_dataset() -> Callable[[_T], _T]:
  """Decorator to call `as_dataset` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, dsbuilder, args, kwargs):
    name, config_name, version, data_path = (
        _get_name_config_version_datadir(dsbuilder))
    metadata = call_metadata.CallMetadata()
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.as_dataset(
            metadata=metadata,
            name=name,
            config_name=config_name,
            version=version,
            data_path=data_path,
            split=args and args[0] or kwargs.get("split"),
            batch_size=kwargs.get("batch_size"),
            shuffle_files=kwargs.get("shuffle_files"),
            read_config=kwargs.get("read_config"),
            as_supervised=kwargs.get("as_supervised"),
            decoders=kwargs.get("decoders"),
        )

  return decorator


def list_builders() -> Callable[[_T], _T]:
  """Decorator to call `list_builders` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, unused_none_instance, args, kwargs):
    metadata = call_metadata.CallMetadata()
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.list_builders(
            metadata=metadata,
            with_community_datasets=kwargs.get("with_community_datasets"))

  return decorator


def load() -> Callable[[_T], _T]:
  """Decorator to call `load` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, unused_none_instance, args, kwargs):
    metadata = call_metadata.CallMetadata()
    name = args[0] if args else kwargs["name"]
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.load(
            metadata=metadata,
            name=name,
            split=kwargs.get("split"),
            data_dir=kwargs.get("data_dir"),
            batch_size=kwargs.get("batch_size"),
            shuffle_files=kwargs.get("shuffle_files"),
            download=kwargs.get("download"),
            as_supervised=kwargs.get("as_supervised"),
            decoders=kwargs.get("decoders"),
            read_config=kwargs.get("read_config"),
            with_info=kwargs.get("with_info"),
            try_gcs=kwargs.get("try_gcs"),
        )

  return decorator


def builder() -> Callable[[_T], _T]:
  """Decorator to call `builder` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, unused_none_instance, args, kwargs):
    metadata = call_metadata.CallMetadata()
    name = args[0] if args else kwargs["name"]
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.builder(
            metadata=metadata,
            name=name,
            try_gcs=kwargs.get("try_gcs"),
        )

  return decorator

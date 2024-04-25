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

"""TFDS logging module."""

import abc
import atexit
import collections
import functools
import threading
from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar

from absl import flags
from tensorflow_datasets.core.logging import base_logger
from tensorflow_datasets.core.logging import call_metadata
from tensorflow_datasets.core.logging import logging_logger
import wrapt

_T = TypeVar("_T")
_Decorator = Callable[[_T], _T]
_LoggerMethod = Callable[..., None]


_registered_loggers: Optional[List[base_logger.Logger]] = None

_import_operations: List[Tuple[call_metadata.CallMetadata, int, int]] = []
_import_operations_lock = threading.Lock()

_thread_id_to_builder_init_count = collections.Counter()


def _init_registered_loggers() -> List[base_logger.Logger]:
  """Initializes the registered loggers if they are not set yet."""
  global _registered_loggers
  if _registered_loggers is None:
    _registered_loggers = [
        logging_logger.LoggingLogger(),
    ]
  return _registered_loggers


def _log_import_operation():
  """Log import operations (most of time maximum one), if any."""
  with _import_operations_lock:
    for metadata, import_time_tf, import_time_builders in _import_operations:
      for logger in _init_registered_loggers():
        logger.tfds_import(
            metadata=metadata,
            import_time_ms_tensorflow=import_time_tf,
            import_time_ms_dataset_builders=import_time_builders,
        )
    _import_operations.clear()


def _get_registered_loggers() -> List[base_logger.Logger]:
  _log_import_operation()
  return _init_registered_loggers()


@atexit.register
def _at_exit():
  """Log import operation if needed, calls `process_ends` on loggers."""
  # Do not try to populate loggers when nothing was called.
  if _registered_loggers is None:
    return
  for logger in _get_registered_loggers():
    logger.process_ends()


class _FunctionDecorator(abc.ABC):
  """Base class for a TFDS function decorator.

  When a decorated function is called, the method with the same name as this
  class is called on the registered loggers.
  """

  def _start_call(self) -> call_metadata.CallMetadata:
    """Initializes call metadata."""
    return call_metadata.CallMetadata()

  def _fill_logger_method_kwargs(
      self,
      logger_method: _LoggerMethod,
      metadata: call_metadata.CallMetadata,
      instance: Any,
      args: Any,
      kwargs: Any,
  ) -> _LoggerMethod:
    """Fills kwargs for the corresponding logger method.

    Args:
      logger_method: logger method with the same name as this class.
      metadata: call metadata.
      instance: the object to which the wrapped function was bound when it was
        called.
      args: args captured during the function call.
      kwargs: kwargs captured during the function call.

    Returns:
      partial logger method with filled kwargs.
    """
    del instance, args, kwargs
    return functools.partial(logger_method, metadata=metadata)

  @abc.abstractmethod
  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    """Calls the logger method with appropriate `args` and `kwargs`.

    Child classes need to implement how `args` and `kwargs` are passed from the
    function to the corresponding logger method.

    Args:
      logger_method: logger method with the same name as this class.
      args: args captured during the function call.
      kwargs: kwargs captured during the function call.
    """
    pass

  def _finish_call(
      self,
      metadata: call_metadata.CallMetadata,
      instance: Any,
      args: Any,
      kwargs: Any,
  ):
    """Completes wrapped function call.

    Metadata marks the end and the corresponding method is called on the
    registered loggers.

    Args:
      metadata: call metadata.
      instance: the object to which the wrapped function was bound when it was
        called.
      args: args captured during the function call.
      kwargs: kwargs captured during the function call.
    """
    metadata.mark_end()
    for logger in _get_registered_loggers():
      method_name = self.__class__.__name__
      logger_method = getattr(logger, method_name)
      logger_method = self._fill_logger_method_kwargs(
          logger_method, metadata, instance, args, kwargs
      )
      self._call_logger_method(logger_method, args, kwargs)

  @wrapt.decorator
  def __call__(self, function, instance, args, kwargs):
    """Decorator to call the corresponding method on registered loggers."""
    metadata = self._start_call()
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      self._finish_call(metadata, instance, args, kwargs)


class _DsbuilderMethodDecorator(_FunctionDecorator):
  """Base class for a dataset builder method decorator."""

  # Flag. If `True` then the wrapped dsbuilder method is a property.
  IS_PROPERTY: bool = False

  @staticmethod
  def _get_info(dsbuilder: Any) -> Tuple[str, str, str, str]:
    """Gets information about the builder.

    Args:
      dsbuilder: the builder instance to which the wrapped function was bound
        when it was called.

    Returns:
      builder_name: name of the builder.
      config: name of the builder config.
      version: version of the builder.
      data_path: path to the builder data directory.
    """
    config_name = (
        dsbuilder.builder_config.name if dsbuilder.builder_config else ""
    )
    data_path = dsbuilder.data_dir
    return dsbuilder.name, config_name, str(dsbuilder.version), data_path

  def _fill_logger_method_kwargs(
      self,
      logger_method: _LoggerMethod,
      metadata: call_metadata.CallMetadata,
      instance: Any,
      args: Any,
      kwargs: Any,
  ) -> _LoggerMethod:
    """Fills kwargs for the corresponding logger method.

    Args:
      logger_method: logger method with the same name as this class.
      metadata: call metadata.
      instance: the object to which the wrapped function was bound when it was
        called.
      args: args captured during the function call.
      kwargs: kwargs captured during the function call.

    Returns:
      partial logger method with filled kwargs.
    """
    del kwargs
    if self.IS_PROPERTY:
      dsbuilder = args[0]  # Because property decorator applied first.
    else:
      dsbuilder = instance
    name, config_name, version, data_path = self._get_info(dsbuilder)

    return functools.partial(
        logger_method,
        metadata=metadata,
        name=name,
        config_name=config_name,
        version=version,
        data_path=data_path,
    )




def register(logger: base_logger.Logger) -> None:
  """Register an additional logger within TFDS.

  Registered loggers are called on TFDS events, synchronously, from the same
  thread the call was made, in sequence, and in registration order. Exceptions
  are *NOT* caught.

  Args:
    logger: the logger to register.
  """
  _init_registered_loggers().append(logger)


def tfds_import(
    *,
    metadata: call_metadata.CallMetadata,
    import_time_ms_tensorflow: int,
    import_time_ms_dataset_builders: int,
):
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
        (metadata, import_time_ms_tensorflow, import_time_ms_dataset_builders)
    )


def builder_init(is_read_only_builder: bool = False) -> _Decorator:
  """Decorator to call `builder_init` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, dsbuilder, args, kwargs):
    metadata = call_metadata.CallMetadata()
    _thread_id_to_builder_init_count[metadata.thread_id] += 1
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      if _thread_id_to_builder_init_count[metadata.thread_id] == 1:
        metadata.mark_end()
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
              version=version,
              is_read_only_builder=is_read_only_builder,
          )
      _thread_id_to_builder_init_count[metadata.thread_id] -= 1

  return decorator


class builder_info(_DsbuilderMethodDecorator):  # pylint: disable=invalid-name
  """Decorator to call `builder_info` method on registered loggers."""

  IS_PROPERTY = True

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    del args, kwargs
    logger_method()


class as_dataset(_DsbuilderMethodDecorator):  # pylint: disable=invalid-name
  """Decorator to call `as_dataset` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        split=args and args[0] or kwargs.get("split"),
        batch_size=kwargs.get("batch_size"),
        shuffle_files=kwargs.get("shuffle_files"),
        read_config=kwargs.get("read_config"),
        as_supervised=kwargs.get("as_supervised"),
        decoders=kwargs.get("decoders"),
    )


class download_and_prepare(_DsbuilderMethodDecorator):  # pylint: disable=invalid-name
  """Decorator to call `download_and_prepare` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    del args
    logger_method(
        download_dir=kwargs.get("download_dir"),
        download_config=kwargs.get("download_config"),
        file_format=kwargs.get("file_format"),
    )


def as_numpy(function: _Decorator) -> _Decorator:
  """Decorator to call `as_numpy` method on registered loggers."""

  # Here we use `functools.wraps` as `wrapt.decorator` is not serializable.
  # https://github.com/GrahamDumpleton/wrapt/issues/158.
  @functools.wraps(function)
  def decorator(*args, **kwargs):
    dataset = args[0] if args else kwargs["dataset"]
    metadata = call_metadata.CallMetadata()
    try:
      return function(*args, **kwargs)
    except Exception:
      metadata.mark_error()
      raise
    finally:
      metadata.mark_end()
      for logger in _get_registered_loggers():
        logger.as_numpy(metadata=metadata, dataset=dataset)

  return decorator


class list_builders(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `list_builders` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    del args
    logger_method(with_community_datasets=kwargs.get("with_community_datasets"))


class load_from_ml_catalog(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `load_from_ml_catalog` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        name=args[0] if args else kwargs["name"],
        split=kwargs.get("split"),
        decoders=kwargs.get("decoders"),
        read_config=kwargs.get("read_config"),
        shuffle=kwargs.get("shuffle"),
    )


class load(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `load` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        name=args[0] if args else kwargs["name"],
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


class builder(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `builder` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        name=args[0] if args else kwargs["name"],
        try_gcs=kwargs.get("try_gcs"),
    )


class dataset_collection(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `dataset_collection` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        name=args[0] if args else kwargs["name"],
        loader_kwargs=kwargs.get("loader_kwargs"),
    )


class data_source(_FunctionDecorator):  # pylint: disable=invalid-name
  """Decorator to call `data_source` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        name=args[0] if args else kwargs["name"],
        split=kwargs.get("split"),
        data_dir=kwargs.get("data_dir"),
        download=kwargs.get("download"),
        decoders=kwargs.get("decoders"),
        try_gcs=kwargs.get("try_gcs"),
    )


class as_data_source(_DsbuilderMethodDecorator):  # pylint: disable=invalid-name
  """Decorator to call `as_data_source` method on registered loggers."""

  def _call_logger_method(
      self,
      logger_method: _LoggerMethod,
      args: Any,
      kwargs: Any,
  ):
    logger_method(
        split=args and args[0] or kwargs.get("split"),
        decoders=kwargs.get("decoders"),
    )



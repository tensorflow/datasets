# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
from typing import Callable, TypeVar, List, Optional

from absl import flags
from tensorflow_datasets.core.logging import base_logger
from tensorflow_datasets.core.logging import logging_logger

import wrapt


_T = TypeVar('_T')

_registered_loggers: Optional[List[base_logger.Logger]] = None


def _check_init_registered_loggers() -> None:
  """Initializes the registered loggers if they are not set yet."""
  global _registered_loggers
  if _registered_loggers is None:
    _registered_loggers = [
        logging_logger.LoggingLogger(),
    ]


def _get_registered_loggers() -> List[base_logger.Logger]:
  _check_init_registered_loggers()
  return _registered_loggers


def register(logger: base_logger.Logger) -> None:
  """Register an additional logger within TFDS.

  Registered loggers are called on TFDS events, synchronously, from the same
  thread the call was made, in sequence, and in registration order. Exceptions
  are *NOT* caught.

  Args:
    logger: the logger to register.
  """
  global _registered_loggers
  _check_init_registered_loggers()
  _registered_loggers.append(logger)


def as_dataset() -> Callable[[_T], _T]:
  """Decorator to call `as_dataset` method on registered loggers."""

  @wrapt.decorator
  def decorator(function, builder, args, kwargs):
    config_name = builder.builder_config.name if builder.builder_config else ''
    data_path = builder.data_dir

    for logger in _get_registered_loggers():
      logger.as_dataset(
          dataset_name=builder.name,
          config_name=config_name,
          version=str(builder.version),
          data_path=data_path,
          split=args and args[0] or kwargs.get('split', 'all'),
          batch_size=kwargs.get('batch_size'),
          shuffle_files=kwargs.get('shuffle_files', False),
          read_config=kwargs.get('read_config', None),
          as_supervised=kwargs.get('as_supervised', False),
          decoders=kwargs.get('decoders', None))

    return function(*args, **kwargs)

  return decorator

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

"""This module defines the methods a logger implementation should define."""

from typing import Dict, Optional, Union

from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.core.utils import read_config as tfds_read_config


class Logger:
  """Defines interface any TFDS logger must implement.

  Registered loggers methods are called on TFDS events, synchronously, from the
  same thread the call was made, in sequence, and in registration order.
  Exceptions are *NOT* caught.
  """

  def as_dataset(self, *, dataset_name: str, config_name: Optional[str],
                 version: str, data_path: str,
                 split: Union[str, tfrecords_reader.ReadInstruction],
                 batch_size: Optional[int], shuffle_files: bool,
                 read_config: tfds_read_config.ReadConfig, as_supervised: bool,
                 decoders: Dict[str, str]):
    """Callback called when user calls `dataset_builder.as_dataset`.

    Callback is also triggered by `tfds.load`, which calls `as_dataset`.
    The logger MUST NOT mutate passed objects (decoders, read_config, ...).

    Args:
      dataset_name: the name of the dataset. E.g.: "mnist".
      config_name: the name of the config or None.
      version: the dataset version. E.g.: "1.2.3".
      data_path: The path to directory of the dataset loaded. E.g.:
        "/home/alice/.tensorflow_datasets/mnist/1.2.3".
      split: name of the split requested by user. 'all' for all splits.
      batch_size: See DatasetBuilder.as_dataset docstring.
      shuffle_files: -
      read_config: -
      as_supervised: -
      decoders: flatten dict of decoders dict given to `as_dataset`, with the
        values being `{module_name}.{class_name}` instad of a
    """
    raise NotImplementedError

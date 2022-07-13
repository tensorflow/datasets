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

"""A logger logging using absl.logging module."""

from typing import Optional, Union

from absl import logging
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.logging import base_logger
from tensorflow_datasets.core.logging import call_metadata
from tensorflow_datasets.core.utils import read_config as tfds_read_config
from tensorflow_datasets.core.utils import type_utils

TreeDict = type_utils.TreeDict


class LoggingLogger(base_logger.Logger):
  """A logger that is based on the absl logging module."""

  def as_dataset(
      self,
      *,
      metadata: call_metadata.CallMetadata,
      name: str,
      config_name: Optional[str],
      version: str,
      data_path: str,
      split: Union[str, splits_lib.ReadInstruction],
      batch_size: Optional[int],
      shuffle_files: bool,
      read_config: tfds_read_config.ReadConfig,
      as_supervised: bool,
      decoders: Optional[TreeDict[decode.partial_decode.DecoderArg]],
  ):
    logging.info("Constructing tf.data.Dataset %s for split %s, from %s", name,
                 str(split), data_path)

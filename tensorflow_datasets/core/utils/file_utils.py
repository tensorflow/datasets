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

"""Library of helper functions to handle dealing with files."""

import os
import pathlib
from typing import List, Optional

from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import generic_path
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import read_config
from tensorflow_datasets.core.utils import type_utils

PathLike = type_utils.PathLike
ListOrElem = type_utils.ListOrElem
ReadWritePath = type_utils.ReadWritePath

_registered_data_dir = set()


def add_data_dir(data_dir):
  """Registers a new default `data_dir` to search for datasets.

  When a `tfds.core.DatasetBuilder` is created with `data_dir=None`, TFDS
  will look in all registered `data_dir` (including the default one) to
  load existing datasets.

  * An error is raised if a dataset can be loaded from more than 1 registered
    data_dir.
  * This only affects reading datasets. Generation always uses the
    `data_dir` kwargs when specified or `tfds.core.constant.DATA_DIR` otherwise.

  Args:
    data_dir: New data_dir to register.
  """
  # Remove trailing / to avoid same directory being included twice in the set
  # with and without a final slash.
  data_dir = data_dir.rstrip('/')
  _registered_data_dir.add(data_dir)


def list_data_dirs(
    given_data_dir: Optional[ListOrElem[PathLike]] = None,) -> List[PathLike]:
  """Return the list of all `data_dir` to look-up.

  Args:
    given_data_dir: If a `data_dir` is provided, only the explicitly given
      `data_dir` will be returned, otherwise the list of all registered data_dir
      is returned

  Returns:
    The list of all data_dirs to look-up.
  """
  # If the data dir is explicitly given, no need to search everywhere.
  if given_data_dir:
    if isinstance(given_data_dir, list):
      return given_data_dir
    else:
      return [given_data_dir]
  else:
    all_data_dirs = _registered_data_dir | {constants.DATA_DIR}
    return sorted(os.path.expanduser(d) for d in all_data_dirs)


def get_default_data_dir(given_data_dir: Optional[str] = None,) -> str:
  """Returns the default data_dir."""
  if given_data_dir:
    return os.path.expanduser(given_data_dir)
  else:
    return os.path.expanduser(constants.DATA_DIR)

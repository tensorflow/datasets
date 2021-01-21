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

"""Cache utils.

The cache (default to `~/.cache/tensorflow_datasets/`) is used for:

* The community dataset index list (cached in
  `<cache_dir>/community-datasets-list.jsonl` from
  `gs://tfds-data/community-datasets-list.jsonl`)
* The installed dataset packages (downloaded from github and installed in
  `<cache_dir>/modules/tfds_community/`).

"""

import os
import sys

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import type_utils


def _default_cache_dir() -> type_utils.ReadWritePath:
  """Returns the default cache directory."""
  if 'TFDS_CACHE_DIR' in os.environ:
    path = os.environ['TFDS_CACHE_DIR']
  elif 'XDG_CACHE_HOME' in os.environ:
    path = os.path.join(os.environ['XDG_CACHE_HOME'], 'tensorflow_datasets')
  else:
    path = os.path.join('~', '.cache', 'tensorflow_datasets')
  return utils.as_path(path).expanduser()


@utils.memoize()
def cache_path() -> type_utils.ReadWritePath:
  """Returns the path to the TFDS cache."""
  path = _default_cache_dir()
  path.mkdir(parents=True, exist_ok=True)
  return path


@utils.memoize()
def module_path() -> type_utils.ReadWritePath:
  """Returns the path to the cached TFDS dynamically installed modules.

  Calling this function will update `sys.path` so modules installed in this
  directory can be imported.

  Returns:
    module_path: The path to the dynamically installed modules.
  """
  path = cache_path() / 'modules/'
  path.mkdir(parents=True, exist_ok=True)
  # Add the `~/.cache/tensorflow_datasets/modules/` to `sys.path`
  sys.path.append(os.fspath(path))
  return path

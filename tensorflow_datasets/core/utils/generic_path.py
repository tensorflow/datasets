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

"""Pathlib-like generic abstraction."""

import os
import pathlib

from tensorflow_datasets.core.utils import gpath
from tensorflow_datasets.core.utils import resource_utils
from tensorflow_datasets.core.utils import type_utils

PathLike = type_utils.PathLike
ReadOnlyPath = type_utils.ReadOnlyPath
ReadWritePath = type_utils.ReadWritePath


# Could eventually expose some `tfds.core.register_path_cls` API to unlock
# additional file system supports (e.g. `s3path.S3Path('s3://bucket/data')`)
_PATHLIKE_CLS = (
    gpath.GPath,
    resource_utils.ResourcePath,
    pathlib.Path,
)


def as_path(path: PathLike) -> ReadWritePath:
  """Create a generic `pathlib.Path`-like abstraction.

  This function

  Args:
    path: Pathlike object.

  Returns:
    path: The `pathlib.Path`-like abstraction.
  """
  if isinstance(path, str):
    if os.name == 'nt' and not path.startswith('gs://'):
      # On windows, all path are `pathlib.WindowsPath`, as `gpath.GPath` is
      # `PosixPurePath`
      return pathlib.Path(path)
    else:
      return gpath.GPath(path)  # On linux, or for `gs://`, uses `GPath`
  elif isinstance(path, _PATHLIKE_CLS):
    return path  # Forward resource path, gpath,... as-is
  elif isinstance(path, os.PathLike):  # Other `os.fspath` compatible objects
    return pathlib.Path(path)
  else:
    raise TypeError(f'Invalid path type: {path!r}')

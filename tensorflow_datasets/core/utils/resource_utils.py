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

"""Utils to handle resources."""

from etils import epath

to_write_path = epath.to_write_path


def tfds_path(*relative_path: epath.PathLike) -> epath.Path:
  """Path to `tensorflow_datasets/` root dir.

  The following examples are equivalent:

  ```py
  path = tfds.core.tfds_path() / 'path/to/data.txt'
  path = tfds.core.tfds_path('path/to/data.txt')
  path = tfds.core.tfds_path('path', 'to', 'data.txt')
  ```

  Note: Even if `/` is used, those examples are compatible with Windows, as
  pathlib will automatically normalize the paths.

  Args:
    *relative_path: Relative path, eventually to concatenate.

  Returns:
    path: The root TFDS path.
  """
  return epath.resource_path('tensorflow_datasets').joinpath(*relative_path)


def tfds_write_path(*relative_path: epath.PathLike) -> epath.Path:
  """Path to `tensorflow_datasets/` root dir (read-write).

  Contrary to `tfds.core.tfds_path`, path returned here support write
  operations. Used in scripts to update the TFDS repository.

  Args:
    *relative_path: Relative path, eventually to concatenate.

  Returns:
    path: The root TFDS path.
  """
  return epath.to_write_path(tfds_path(*relative_path))

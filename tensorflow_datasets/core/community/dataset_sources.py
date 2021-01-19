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

"""Utils to download locally dataset code source stored remotelly."""

from tensorflow_datasets.core import utils


def download_from_uri(uri: str, dst: utils.ReadWritePath) -> str:
  """Download the remote dataset code locally to the dst path.

  Args:
    uri: Source of the dataset. Can be:
        * A local/GCS path (e.g. `gs://bucket/datasets/my_dataset/`)
        * A github source
    dst: Empty directory on which copying the source

  Returns:
    The module mame of the package.
  """
  if uri.startswith('github://'):
    raise NotImplementedError('Github sources not supported yet')

  path = utils.as_path(uri)
  if not path.exists():
    raise ValueError(f'Unsuported source: {uri}')

  # Download the main file
  python_module = path / f'{path.name}.py'
  python_module.copy(dst / python_module.name)

  # TODO(tfds): Should also support download on the extra files (e.g. label.txt,
  # util module,...)

  # Add the `__init__` file
  (dst / '__init__.py').write_text('')
  return python_module.stem

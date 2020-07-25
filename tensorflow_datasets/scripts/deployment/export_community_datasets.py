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

"""Script which parse registered repositories and save datasets found."""

import itertools
import json
import pathlib
from typing import List

from absl import app
import tensorflow as tf

from tensorflow_datasets.core import community
from tensorflow_datasets.core import github_api
import toml


def _is_dataset_path(ds_path: github_api.GithubPath) -> bool:
  """Returns True if the given path correspond to a dataset.

  Currently a simple heuristic is used. This function checks the path has the
  following structure:

  ```
  <ds_name>/
      <ds_name>.py
  ```

  Args:
    ds_path: Path of the dataset module

  Returns:
    True if the path match the expected file structure
  """
  return ds_path.is_dir() and (ds_path / f'{ds_path.name}.py').exists()


def _list_namespace_ds_specs(
    namespace: str,
    path: str,
) -> List[community.DatasetSpec]:
  """Returns the dataset names found in a specific directory.

  The directory should have the following structure:

  ```
  <path>/
      <dataset0>/
      <dataset1>/
      ...
  ```

  Additional files or folders which are not detected as datasets will be
  ignored (e.g. `__init__.py`).

  Args:
    namespace: Namespace of the datasets
    path: The directory path containing the datasets.

  Returns:
    ds_specs: The dataset specs found in the directory (sorted for determinism).

  Raises:
    FileNotFoundError: If the path cannot be reached.
  """
  path = github_api.GithubPath(path)
  if not path.exists():
    # Should be fault-tolerant in the future
    raise FileNotFoundError(f'Could not find datasets at {path}')
  all_specs = [
      community.DatasetSpec(  # pylint: disable=g-complex-comprehension
          name=ds_path.name,
          namespace=namespace,
          source=community.GithubSource(ds_path),
      ) for ds_path in path.iterdir() if _is_dataset_path(ds_path)
  ]
  return sorted(all_specs, key=lambda spec: spec.cannonical_name)


def _find_community_ds_specs(
    config_path: pathlib.Path,
) -> List[community.DatasetSpec]:
  """Find all namepaces/dataset from the config.

  Config should contain the instructions in the following format:

  ```
  [Namespace]
  <namespace0> = '<owner0>/<github_repo0>/tree/<path/to/dataset/dir>'
  <namespace1> = '<owner1>/<github_repo1>/tree/<path/to/dataset/dir>'
  ```

  Args:
    config_path: Path to the config file containing lookup instructions.

  Returns:
    ds_specs: list of all found datasets.
  """
  config = toml.load(config_path)
  all_specs = itertools.chain.from_iterable(
      _list_namespace_ds_specs(namespace, path)
      for namespace, path in config['Namespaces'].items()
  )
  return sorted(all_specs, key=lambda spec: spec.cannonical_name)


def _save_community_ds_specs(
    file_path: str, ds_specs: List[community.DatasetSpec]
) -> None:
  """Save all loaded datasets.

  Saved file will have the following `.tsv` format:

  ```
  namespace0 dataset0 /path/to/dataset0/
  namespace0 dataset1 /path/to/dataset1/
  ...
  ```

  Args:
    file_path: `.jsonl` destination to which save the dataset
    ds_specs: Dataset paths to save
  """
  # TODO(tfds): Replace GFile by a pathlib-like abstraction for GCS.
  with tf.io.gfile.GFile(file_path, 'w') as f:
    for spec in ds_specs:
      f.write(json.dumps(spec.to_json()))
      f.write('\n')


def export_community_datasets(in_path: pathlib.Path, out_path: str) -> None:
  """Exports community datasets.

  Args:
    in_path: Config path containing the namespaces and dataset lookup
      instructions.
    out_path: File containing all detected datasets. Detected dataset will
      be saved to this file. Previous content is erased.
  """
  ds_specs = _find_community_ds_specs(in_path)
  _save_community_ds_specs(out_path, ds_specs)


def main(_):
  config_path = pathlib.Path(community.community_config_path())
  exported_path = community.COMMUNITY_EXPORTED_PATH
  export_community_datasets(in_path=config_path, out_path=exported_path)


if __name__ == '__main__':
  app.run(main)

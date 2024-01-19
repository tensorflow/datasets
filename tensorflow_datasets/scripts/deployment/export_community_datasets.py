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

r"""Script which parse registered repositories and save datasets found.

"""

import json
from typing import List

from absl import app
import tensorflow_datasets as tfds
from tensorflow_datasets.core.community import config as config_lib
import tqdm

# Community datasets namespaces and code location from where the datasets
# package index will be constructed.
_IN_PATH = tfds.core.tfds_path('community-datasets.toml')
# Community datasets package indexes which will be updated.
_OUT_PATH = tfds.core.utils.gcs_utils.GCS_COMMUNITY_INDEX_PATH

DatasetSource = tfds.core.community.dataset_sources.DatasetSource
DatasetPackage = tfds.core.community.register_package.DatasetPackage


def main(_):
  export_community_datasets(in_path=_IN_PATH, out_path=_OUT_PATH)  # pytype: disable=wrong-arg-types


def export_community_datasets(
    in_path: tfds.core.Path,
    out_path: tfds.core.Path,
) -> None:
  """Exports community datasets.

  Args:
    in_path: Config path containing the namespaces and dataset lookup
      instructions.
    out_path: File containing all detected datasets. Detected dataset will be
      saved to this file. Previous content is erased.
  """
  ds_packages = _find_community_ds_packages(in_path)
  _save_community_ds_packages(out_path, ds_packages)


def _find_community_ds_packages(
    config_path: tfds.core.Path,
) -> List[DatasetPackage]:
  """Find all namepaces/dataset from the config.

  Config should contain the instructions in the following format:

  ```
  [namespace0]
  paths = 'github://<owner0>/<github_repo0>/tree/<path/to/dataset/dir>'
  [namespace1]
  paths = 'gs://<bucket>/<datasets>/'
  ```

  Args:
    config_path: Path to the config file containing lookup instructions.

  Returns:
    ds_packages: list of all found datasets.
  """
  namespace_registry = config_lib.NamespaceRegistry(config_path)

  all_packages = []
  for namespace, config in tqdm.tqdm(
      namespace_registry.config_per_namespace.items()
  ):
    tqdm.tqdm.write(f'Searching datasets for {namespace}: {config}')
    for src_code_path in config.paths:
      for (
          pkg
      ) in tfds.core.community.register_package.list_ds_packages_for_namespace(
          namespace=namespace, path=tfds.core.Path(src_code_path)
      ):
        tqdm.tqdm.write(str(pkg.name))
        all_packages.append(pkg)

  return sorted(all_packages, key=lambda package: package.name)


def _save_community_ds_packages(
    file_path: tfds.core.Path, ds_packages: List[DatasetPackage]
) -> None:
  """Save all loaded datasets in the package index.

  Saved file will have the following `.jsonl` format:

  ```jsonl
  {'name': 'namespace0:dataset0', 'source': 'github://...'}
  {'name': 'namespace0:dataset0', 'source': 'github://...'}
  ...
  ```

  Args:
    file_path: `.jsonl` destination to which save the dataset
    ds_packages: Dataset paths to save
  """
  pkg_json = [json.dumps(pkg.to_json()) for pkg in ds_packages]
  file_path.write_text('\n'.join(pkg_json) + '\n')


if __name__ == '__main__':
  app.run(main)

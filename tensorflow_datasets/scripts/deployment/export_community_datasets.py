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

r"""Script which parse registered repositories and save datasets found.

"""

import itertools
import json
import pathlib
from typing import List, Optional

from absl import app
import tensorflow_datasets as tfds
import toml
import tqdm

# Community datasets namespaces and code location from where the datasets
# package index will be constructed.
_IN_PATH = tfds.core.tfds_path() / 'community-datasets.toml'
# Community datasets package indexes which will be updated.
_OUT_PATH = tfds.core.utils.gcs_utils.GCS_COMMUNITY_INDEX_PATH

DatasetSource = tfds.core.community.dataset_sources.DatasetSource
DatasetPackage = tfds.core.community.register_package.DatasetPackage


def main(_):
  export_community_datasets(in_path=_IN_PATH, out_path=_OUT_PATH)


def export_community_datasets(
    in_path: tfds.typing.ReadOnlyPath,
    out_path: tfds.typing.ReadWritePath,
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
    config_path: pathlib.Path,) -> List[DatasetPackage]:
  """Find all namepaces/dataset from the config.

  Config should contain the instructions in the following format:

  ```
  [Namespace]
  <namespace0> = 'github://<owner0>/<github_repo0>/tree/<path/to/dataset/dir>'
  <namespace1> = 'gs://<bucket>/<datasets>/'
  ```

  Args:
    config_path: Path to the config file containing lookup instructions.

  Returns:
    ds_packages: list of all found datasets.
  """
  config = toml.load(config_path)
  all_packages = itertools.chain.from_iterable(
      _list_ds_packages_for_namespace(namespace, tfds.core.as_path(
          src_code_path))
      for namespace, src_code_path in tqdm.tqdm(config['Namespaces'].items()))
  return sorted(all_packages, key=lambda package: package.name)


def _save_community_ds_packages(file_path: tfds.typing.ReadWritePath,
                                ds_packages: List[DatasetPackage]) -> None:
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


def _list_ds_packages_for_namespace(
    namespace: str,
    path: tfds.typing.ReadOnlyPath,
) -> List[DatasetPackage]:
  """Returns the dataset names found in a specific directory.

  The directory should have the following structure:

  ```
  <path>/
      <dataset0>/
          <dataset0>.py
      <dataset1>/
          <dataset1>.py
      ...
  ```

  Additional files or folders which are not detected as datasets will be
  ignored (e.g. `__init__.py`).

  Args:
    namespace: Namespace of the datasets
    path: The directory path containing the datasets.

  Returns:
    ds_packages: The dataset packages found in the directory (sorted for
      determinism).

  Raises:
    FileNotFoundError: If the path cannot be reached.
  """
  tqdm.tqdm.write(f'Searching datasets for {namespace}: {path}')
  if not path.exists():
    # Should be fault-tolerant in the future
    raise FileNotFoundError(f'Could not find datasets at {path}')

  all_packages = []
  for ds_path in tqdm.tqdm(sorted(path.iterdir())):
    source = _get_dataset_source(ds_path)
    if source:
      pkg = DatasetPackage(
          name=tfds.core.utils.DatasetName(
              namespace=namespace,
              name=ds_path.name,
          ),
          source=source,
      )
      tqdm.tqdm.write(str(pkg.name))
      all_packages.append(pkg)

  return all_packages


def _get_dataset_source(
    ds_path: tfds.typing.ReadOnlyPath,) -> Optional[DatasetSource]:
  """Returns True if the given path correspond to a dataset.

  Currently a simple heuristic is used. This function checks the path has the
  following structure:

  ```
  <ds_name>/
      <ds_name>.py
  ```

  If so, all `.py`, `.txt`, `.tsv` files will be added to the package.

  Args:
    ds_path: Path of the dataset module

  Returns:
    True if the path match the expected file structure
  """
  filter_list = {'__init__.py'}
  suffixes_list = ('.txt', '.tsv', '.py')

  if not ds_path.is_dir():
    return None
  all_filenames = set(f.name for f in ds_path.iterdir())
  # The dataset package is composed of all `.py` present in the dataset folder.
  if f'{ds_path.name}.py' in all_filenames:
    return DatasetSource(
        root_path=ds_path,
        filenames=sorted([
            fname for fname in all_filenames
            if fname.endswith(suffixes_list) and fname not in filter_list
        ]),
    )
  return None


if __name__ == '__main__':
  app.run(main)

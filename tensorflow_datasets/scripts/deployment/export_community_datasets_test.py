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

"""Tests for tensorflow_datasets.scripts.deployment.export_community_datasets."""

import pathlib
import string
import textwrap
from typing import Dict, List

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.deployment import export_community_datasets
import toml


def _write_dataset_files(
    root_path: pathlib.Path,
    namespace: str,
    ds_files: Dict[str, List[str]],
) -> str:
  """Write the repo content containing the datasets."""
  repo_path = root_path / namespace
  # Create all datasets
  for ds_name, files in ds_files.items():
    ds_path = repo_path / ds_name
    ds_path.mkdir(parents=True)  # Create the containing dir
    for fname in files:
      (ds_path / fname).touch()  # Create the file

  # Additional noisy files should be ignored
  (repo_path / '__init__.py').touch()
  return str(repo_path)


def test_export_community_datasets(tmp_path):
  # Create the community dataset repositories
  tfg_path = _write_dataset_files(
      tmp_path,
      namespace='tensorflow_graphics',
      ds_files={
          'cifar': ['cifar.py', '__init__.py', 'empty_dir'],
          'empty_dir': [],
      },
  )
  nlp_path = _write_dataset_files(
      tmp_path,
      namespace='nlp',
      ds_files={
          'mnist': ['mnist.py'],
          'robotnet': ['robotnet.py', 'checksums.tsv', 'label.txt'],
          'invalid_ds': ['name_do_not_match.py'],
      },
  )

  # Write a dummy `community-datasets.toml`
  in_path = tmp_path / 'config.toml'
  in_path.write_text(
      textwrap.dedent(
          f"""\
          [Namespaces]
          tensorflow_graphics = '{tfg_path}'
          nlp = '{nlp_path}'
          """
      )
  )

  # Load registered dataset and export the list.
  # We patch `GithubPath` with `pathlib.Path` as the two have the same API.
  out_path = tmp_path / 'out.jsonl'
  export_community_datasets.export_community_datasets(in_path, out_path)

  # Ensure datasets where correctly exported
  expected_output = textwrap.dedent(
      """\
      {"name": "nlp:mnist", "source": "${nlp_path}/mnist/mnist.py"}
      {"name": "nlp:robotnet", "source": {"root_path": "${nlp_path}/robotnet", "filenames": ["checksums.tsv", "label.txt", "robotnet.py"]}}
      {"name": "tensorflow_graphics:cifar", "source": "${tfg_path}/cifar/cifar.py"}
      """
  )
  expected_output = string.Template(expected_output).substitute(
      tfg_path=tfg_path,
      nlp_path=nlp_path,
  )
  assert out_path.read_text() == expected_output


def test_toml_valid():
  """Makes sure that reading the `.toml` file is valid."""
  config = toml.load(export_community_datasets._IN_PATH)
  _ = {
      namespace: tfds.core.Path(src_code_path)
      for namespace, src_code_path in config['Namespaces'].items()
  }

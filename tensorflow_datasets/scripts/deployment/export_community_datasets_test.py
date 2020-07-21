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

"""Tests for external datasets."""

import pathlib
import string
import textwrap
from typing import List

from unittest import mock

from tensorflow_datasets.core import github_api
from tensorflow_datasets.scripts.deployment import export_community_datasets


def _write_dataset_files(
    root_path: pathlib.Path, namespace: str, datasets: List[str]
) -> str:
  """Write the repo content containing the datasets."""
  repo_path = root_path / namespace
  # Create all datasets
  for ds_name in datasets:
    ds_path = repo_path / ds_name / f'{ds_name}.py'
    ds_path.parent.mkdir(parents=True)  # Create the containing dir
    ds_path.touch()  # Create the file

  # Additional noisy files should be ignored
  (repo_path / '__init__.py').touch()
  (repo_path / 'empty_dir').mkdir()
  return str(repo_path)


def test_export_community_datasets(tmp_path):

  # Create the community dataset repositories
  tfg_path = _write_dataset_files(
      tmp_path, namespace='tensorflow_graphics', datasets=['cifar']
  )
  nlp_path = _write_dataset_files(
      tmp_path, namespace='nlp', datasets=['mnist', 'robotnet']
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
  out_path = tmp_path / 'out.tsv'
  with mock.patch.object(github_api, 'GithubPath', pathlib.Path):
    export_community_datasets.export_community_datasets(in_path, str(out_path))

  # Ensure datasets where correctly exported
  expected_output = textwrap.dedent(
      """\
      {"name": "mnist", "namespace": "nlp", "source": "github://${nlp_path}/mnist"}
      {"name": "robotnet", "namespace": "nlp", "source": "github://${nlp_path}/robotnet"}
      {"name": "cifar", "namespace": "tensorflow_graphics", "source": "github://${tfg_path}/cifar"}
      """
  )
  expected_output = string.Template(expected_output).substitute(
      tfg_path=tfg_path.lstrip('/'),
      nlp_path=nlp_path.lstrip('/'),
  )
  assert out_path.read_text() == expected_output

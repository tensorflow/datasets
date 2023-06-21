# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""`tfds new` command."""

import argparse
import os
import pathlib
import subprocess
import textwrap
from typing import Optional

from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_metadata
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import resource_utils
from tensorflow_datasets.scripts.cli import builder_templates
from tensorflow_datasets.scripts.cli import cli_utils as utils


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `new` command."""
  new_parser = parsers.add_parser(
      'new', help='Creates a new dataset directory from the template.'
  )
  new_parser.add_argument(
      'dataset_name',  # Positional argument
      type=str,
      help='Name of the dataset to be created (in snake_case)',
  )
  new_parser.add_argument(
      '--data_format',  # Optional argument
      type=str,
      default=builder_templates.STANDARD,
      choices=[
          builder_templates.STANDARD,
          builder_templates.CONLL,
          builder_templates.CONLLU,
      ],
      help=(
          'Optional format of the input data, which is used to generate a '
          'format-specific template.'
      ),
  )
  new_parser.add_argument(
      '--dir',
      type=pathlib.Path,
      default=pathlib.Path.cwd(),
      help=(
          'Path where the dataset directory will be created. '
          'Defaults to current directory.'
      ),
  )
  new_parser.set_defaults(subparser_fn=_create_dataset_files)


def _create_dataset_files(args: argparse.Namespace) -> None:
  """Creates the dataset directory. Executed by `tfds new <name>`."""
  if not naming.is_valid_dataset_and_class_name(args.dataset_name):
    raise ValueError(
        'Invalid dataset name. It should be a valid Python class name.'
    )

  create_dataset_files(
      dataset_name=args.dataset_name,
      dataset_dir=args.dir,
      data_format=args.data_format,
  )


def create_dataset_files(
    dataset_name: str,
    dataset_dir: pathlib.Path,
    data_format: Optional[str] = None,
) -> None:
  """Creates the dataset files."""
  # Creates the root directory
  dataset_dir = dataset_dir.expanduser().resolve() / dataset_name
  dataset_dir.mkdir(parents=True)
  in_tfds = 'tensorflow_datasets' in dataset_dir.parts

  info = utils.DatasetInfo(
      name=dataset_name,
      in_tfds=in_tfds,
      path=dataset_dir,
      data_format=data_format,
  )

  _create_dataset_file(info)
  _create_dataset_test(info)
  _create_dataset_readme(info)
  _create_dataset_citations(info)
  _create_dataset_tags(info)
  _create_init(info)
  _create_dummy_data(info)
  _create_checksum(info)
  if in_tfds:
    _add_to_parent_init(info)

  print(
      'Dataset generated at {}\n'
      'You can start searching `{}` to complete the implementation.\n'
      'Please check '
      'https://www.tensorflow.org/datasets/add_dataset for additional details.'
      .format(info.path, info.todo)
  )


def _create_dataset_file(info: utils.DatasetInfo) -> None:
  """Create a new dataset from a template."""
  file_path = info.path / f'{info.name}_dataset_builder.py'

  content = builder_templates.create_builder_template(info)
  file_path.write_text(content)


def _create_dataset_test(info: utils.DatasetInfo) -> None:
  """Adds the `dummy_data/` directory."""
  file_path = info.path.joinpath(f'{info.name}_dataset_builder_test.py')

  content = textwrap.dedent(f'''\
      """{info.name} dataset."""

      from {info.ds_import} import {info.name}_dataset_builder
      import {info.tfds_api} as tfds

      class {info.cls_name}Test(tfds.testing.DatasetBuilderTestCase):
        """Tests for {info.name} dataset."""
        # {info.todo}:
        DATASET_CLASS = {info.name}_dataset_builder.Builder
        SPLITS = {{
            'train': 3,  # Number of fake train example
            'test': 1,  # Number of fake test example
        }}

        # If you are calling `download/download_and_extract` with a dict, like:
        #   dl_manager.download({{'some_key': 'http://a.org/out.txt', ...}})
        # then the tests needs to provide the fake output paths relative to the
        # fake data directory
        # DL_EXTRACT_RESULT = {{'some_key': 'output_file1.txt', ...}}


      if __name__ == '__main__':
        tfds.testing.test_main()
      ''')
  file_path.write_text(content)


def _create_dataset_readme(info: utils.DatasetInfo) -> None:
  """Adds the `README.md` file."""
  file_path = info.path / 'README.md'
  content = textwrap.dedent(f"""\
      {info.todo}: Markdown description of that will appear on the catalog page.
      Description is **formatted** as markdown.

      It should also contain any processing which has been applied (if any),
      (e.g. corrupted example skipped, images cropped,...):
      """)
  file_path.write_text(content)


def _create_dataset_citations(info: utils.DatasetInfo) -> None:
  """Adds the `CITATIONS.bib` file."""
  file_path = info.path / 'CITATIONS.bib'
  content = textwrap.dedent(f"""\
      // {info.todo}: BibTeX citation
      """)
  file_path.write_text(content)


def _create_dataset_tags(info: utils.DatasetInfo) -> None:
  """Adds the `TAGS.txt` file."""
  file_path = info.path / 'TAGS.txt'
  content = '// {info.todo}: remove tags which do not apply to dataset.\n' + (
      dataset_metadata.valid_tags_with_comments()
  )
  file_path.write_text(content)


def _create_init(info: utils.DatasetInfo) -> None:
  """Adds the `__init__.py` file."""
  file_path = info.path / '__init__.py'
  file_path.write_text('')


def _create_dummy_data(info: utils.DatasetInfo) -> None:
  """Adds the `dummy_data/` directory."""
  # Create a dummy file in the directory to force the directory creation in
  # version control system where empty directories aren't detected.
  file_path = info.path / 'dummy_data/TODO-add_fake_data_in_this_directory.txt'
  file_path.parent.mkdir()
  file_path.touch()


def _create_checksum(info: utils.DatasetInfo) -> None:
  """Adds the `checksums.tsv` file."""
  file_path = info.path / 'checksums.tsv'
  content = textwrap.dedent(f"""\
      # {info.todo}: If your dataset downloads files, then the checksums
      # will be automatically added here when running
      # `tfds build --register_checksums`.
      """)
  file_path.write_text(content)


def _add_to_parent_init(info: utils.DatasetInfo) -> None:
  """Add `import` dataset in the `<ds_type>/__init__.py` file."""
  if not info.in_tfds:
    # Could add global init, but would be tricky to foresee all use-cases
    raise NotImplementedError(
        'Adding __init__.py in non-tfds dir not supported.'
    )

  import_path = info.path.parent / '__init__.py'
  if not import_path.exists():
    return  # Should this be an error instead ?
  import_path.write_text(
      import_path.read_text()
      + f'from {info.ds_import} import {info.cls_name}\n'
  )

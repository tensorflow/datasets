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

"""`tfds new` command."""

import argparse
import itertools
import os
import pathlib
import subprocess
import textwrap
import dataclasses

from tensorflow_datasets.core import naming


@dataclasses.dataclass
class DatasetInfo:
  """Structure for common string used for formatting.

  Attributes:
    name: Dataset name (`my_dataset`)
    cls_name: Class name (`MyDataset`)
    path: Root directory in which the dataset is added
    in_tfds: Whether the dataset is added in tensorflow_datasets/ or externally
    tfds_api: The Dataset API to import
    todo: Field to fill (`TODO(my_dataset)`)
    ds_import: Dataset import (`tensorflow_datasets.image.my_dataset`)
  """
  name: str
  in_tfds: bool
  path: pathlib.Path
  cls_name: str = dataclasses.field(init=False)
  tfds_api: str = dataclasses.field(init=False)
  todo: str = dataclasses.field(init=False)
  ds_import: str = dataclasses.field(init=False)

  def __post_init__(self):
    self.cls_name = naming.snake_to_camelcase(self.name)
    self.tfds_api = ('tensorflow_datasets.public_api'
                     if self.in_tfds else 'tensorflow_datasets')
    self.todo = f'TODO({self.name})'

    if self.in_tfds:
      # `/path/to/tensorflow_datasets/image/my_dataset`
      # ->`tensorflow_datasets.image.my_dataset`
      import_parts = itertools.dropwhile(lambda p: p != 'tensorflow_datasets',
                                         self.path.parts)
      ds_import = '.'.join(import_parts)
    else:
      # For external datasets, it's difficult to correctly infer the full
      # `from my_module.path.datasets.my_dataset import MyDataset`.
      # Could try to auto-infer the absolute import path from the `setup.py`.
      # Instead uses relative import for now: `from . import my_dataset`
      ds_import = '.'
    self.ds_import = ds_import


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `new` command."""
  new_parser = parsers.add_parser(
      'new', help='Creates a new dataset directory from the template.')
  new_parser.add_argument(
      'dataset_name',  # Positional argument
      type=str,
      help='Name of the dataset to be created (in snake_case)',
  )
  new_parser.add_argument(
      '--dir',
      type=pathlib.Path,
      default=pathlib.Path.cwd(),
      help=('Path where the dataset directory will be created. '
            'Defaults to current directory.'))
  new_parser.set_defaults(subparser_fn=_create_dataset_files)


def _create_dataset_files(args: argparse.Namespace) -> None:
  """Creates the dataset directory. Executed by `tfds new <name>`."""
  if not naming.is_valid_dataset_and_class_name(args.dataset_name):
    raise ValueError(
        'Invalid dataset name. It should be a valid Python class name.')

  create_dataset_files(dataset_name=args.dataset_name, dataset_dir=args.dir)


def create_dataset_files(dataset_name: str, dataset_dir: pathlib.Path) -> None:
  """Creates the dataset files."""
  # Creates the root directory
  dataset_dir = dataset_dir.expanduser() / dataset_name
  dataset_dir.mkdir(parents=True)
  # TODO(py3.7): Should be `dir.expanduser().resolve()` but `.resolve()` fails
  # on some environments when the file doesn't exists.
  # https://stackoverflow.com/questions/55710900/pathlib-resolve-method-not-resolving-non-existant-files
  dataset_dir = dataset_dir.resolve()

  in_tfds = 'tensorflow_datasets' in dataset_dir.parts

  info = DatasetInfo(name=dataset_name, in_tfds=in_tfds, path=dataset_dir)

  _create_dataset_file(info)
  _create_dataset_test(info)
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
      .format(info.path, info.todo))


def _create_dataset_file(info: DatasetInfo) -> None:
  """Create a new dataset from a template."""
  file_path = info.path / f'{info.name}.py'

  content = textwrap.dedent(f'''\
      """{info.name} dataset."""

      import {info.tfds_api} as tfds

      # {info.todo}: Markdown description  that will appear on the catalog page.
      _DESCRIPTION = """
      Description is **formatted** as markdown.

      It should also contain any processing which has been applied (if any),
      (e.g. corrupted example skipped, images cropped,...):
      """

      # {info.todo}: BibTeX citation
      _CITATION = """
      """


      class {info.cls_name}(tfds.core.GeneratorBasedBuilder):
        """DatasetBuilder for {info.name} dataset."""

        VERSION = tfds.core.Version('1.0.0')
        RELEASE_NOTES = {{
            '1.0.0': 'Initial release.',
        }}

        def _info(self) -> tfds.core.DatasetInfo:
          """Returns the dataset metadata."""
          # {info.todo}: Specifies the tfds.core.DatasetInfo object
          return tfds.core.DatasetInfo(
              builder=self,
              description=_DESCRIPTION,
              features=tfds.features.FeaturesDict({{
                  # These are the features of your dataset like images, labels ...
                  'image': tfds.features.Image(shape=(None, None, 3)),
                  'label': tfds.features.ClassLabel(names=['no', 'yes']),
              }}),
              # If there's a common (input, target) tuple from the
              # features, specify them here. They'll be used if
              # `as_supervised=True` in `builder.as_dataset`.
              supervised_keys=('image', 'label'),  # Set to `None` to disable
              homepage='https://dataset-homepage/',
              citation=_CITATION,
          )

        def _split_generators(self, dl_manager: tfds.download.DownloadManager):
          """Returns SplitGenerators."""
          # {info.todo}: Downloads the data and defines the splits
          path = dl_manager.download_and_extract('https://todo-data-url')

          # {info.todo}: Returns the Dict[split names, Iterator[Key, Example]]
          return {{
              'train': self._generate_examples(path / 'train_imgs'),
          }}

        def _generate_examples(self, path):
          """Yields examples."""
          # {info.todo}: Yields (key, example) tuples from the dataset
          for f in path.glob('*.jpeg'):
            yield 'key', {{
                'image': f,
                'label': 'yes',
            }}
      ''')
  file_path.write_text(content)


def _create_dataset_test(info: DatasetInfo) -> None:
  """Adds the `dummy_data/` directory."""
  file_path = info.path.joinpath(f'{info.name}_test.py')

  content = textwrap.dedent(f'''\
      """{info.name} dataset."""

      import {info.tfds_api} as tfds
      from {info.ds_import} import {info.name}


      class {info.cls_name}Test(tfds.testing.DatasetBuilderTestCase):
        """Tests for {info.name} dataset."""
        # {info.todo}:
        DATASET_CLASS = {info.name}.{info.cls_name}
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


def _create_init(info: DatasetInfo) -> None:
  """Adds the `__init__.py` file."""
  file_path = info.path / '__init__.py'
  if info.in_tfds:
    # from tensorflow_datasets.image.my_dataset.my_dataset import MyDataset
    ds_import = f'{info.ds_import}.{info.name}'
  else:
    # from .my_dataset import MyDataset
    ds_import = f'{info.ds_import}{info.name}'
  # Could also import the BuilderConfig if it exists.
  content = textwrap.dedent(f'''\
      """{info.name} dataset."""

      from {ds_import} import {info.cls_name}
      ''')
  file_path.write_text(content)


def _create_dummy_data(info: DatasetInfo) -> None:
  """Adds the `dummy_data/` directory."""
  # Create a dummy file in the directory to force the directory creation in
  # version control system where empty directories aren't detected.
  file_path = info.path / 'dummy_data/TODO-add_fake_data_in_this_directory.txt'
  file_path.parent.mkdir()
  file_path.touch()


def _create_checksum(info: DatasetInfo) -> None:
  """Adds the `checksums.tsv` file."""
  file_path = info.path / 'checksums.tsv'
  content = textwrap.dedent(f"""\
      # {info.todo}: If your dataset downloads files, then the checksums
      # will be automatically added here when running
      # `tfds build --register_checksums`.
      """)
  file_path.write_text(content)


def _add_to_parent_init(info: DatasetInfo) -> None:
  """Add `import` dataset in the `<ds_type>/__init__.py` file."""
  if not info.in_tfds:
    # Could add global init, but would be tricky to foresee all use-cases
    raise NotImplementedError(
        'Adding __init__.py in non-tfds dir not supported.')

  import_path = info.path.parent / '__init__.py'
  if not import_path.exists():
    return  # Should this be an error instead ?
  import_path.write_text(import_path.read_text() +
                         f'from {info.ds_import} import {info.cls_name}\n')

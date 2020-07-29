r"""tfds CLI `new` command

This command will generate files needed for adding a new dataset to tfds.

Usage:

```
tfds new my_dataset
```

```
my_dataset/
    fake_examples/
    __init__.py
    dataset.py
    dataset_test.py
    fake_data_generator.py
    checksum.txt
```

"""

import argparse
import dataclasses
import pathlib
import textwrap

from tensorflow_datasets.core import naming


@dataclasses.dataclass
class Data():
  dataset_name: str
  dataset_cls: str
  todo: str


def _create_dataset_file(root_dir: pathlib.Path, data: Data) -> None:
  """Create a new dataset from a template."""
  file_path = root_dir / f'{data.dataset_name}.py'
  context = textwrap.dedent(
      f"""\
      \"""{data.dataset_name} dataset.\"""

      import tensorflow_datasets as tfds

      # {data.todo}: BibTeX citation
      _CITATION = \"""
      \"""

      # {data.todo}:
      _DESCRIPTION = \"""
      \"""


      class {data.dataset_cls}(tfds.core.GeneratorBasedBuilder):
        \"""DatasetBuilder for {data.dataset_name} dataset.\"""

        # {data.todo}: Set up version.
        VERSION = tfds.core.Version('0.1.0')

        def _info(self):
          \"""Returns DatasetInfo of {data.dataset_cls} dataset.\"""
          # {data.todo}: Specifies the tfds.core.DatasetInfo object
          return tfds.core.DatasetInfo(
              builder=self,
              # This is the description that will appear on the datasets page.
              description=_DESCRIPTION,
              # tfds.features.FeatureConnectors
              features=tfds.features.FeaturesDict({{
                  # These are the features of your dataset like images, labels ...
              }}),
              # If there's a common (input, target) tuple from the features,
              # specify them here. They'll be used if as_supervised=True in
              # builder.as_dataset.
              supervised_keys=(),
              # Homepage of the dataset for documentation
              homepage='https://dataset-homepage/',
              citation=_CITATION,
          )

        def _split_generators(self, dl_manager):
          \"""Returns SplitGenerators.\"""
          # {data.todo}: Downloads the data and defines the splits
          # dl_manager is a tfds.download.DownloadManager that can be used to
          # download and extract URLs
          return [
              tfds.core.SplitGenerator(
                  name=tfds.Split.TRAIN,
                  # These kwargs will be passed to _generate_examples
                  gen_kwargs={{}},
              ),
          ]

        def _generate_examples(self):
          \"""Yields examples.\"""
          # {data.todo}: Yields (key, example) tuples from the dataset
          yield 'key', {{}}
      """
  )
  with file_path.open('w') as f:
    f.write(context)


def _add_the_init(root_dir: pathlib.Path, data: Data) -> None:
  """Creates a new __init__.py. file"""
  file_path = root_dir / '__init__.py'
  context = textwrap.dedent(
      f"""\
      \"""{data.dataset_name} dataset.\"""

      from {data.dataset_name} import {data.dataset_cls}

      __all__ = [
          "{data.dataset_cls}"
      ]
      """
  )
  with file_path.open('w') as f:
    f.write(context)


def _create_dataset_test_file(root_dir: pathlib.Path, data: Data) -> None:
  """Create the test file associated with the dataset."""
  file_path = root_dir / f'{data.dataset_name}_test.py'

  context = textwrap.dedent(
      f"""\
      \"""{data.dataset_name} dataset.\"""

      import tensorflow_datasets as tfds
      import {data.dataset_name}


      class {data.dataset_cls}Test(tfds.testing.DatasetBuilderTestCase):
        \"""Tests for {data.dataset_name} dataset.\"""
        # {data.todo}:
        DATASET_CLASS = {data.dataset_name}.{data.dataset_cls}
        SPLITS = {{
            "train": 3,  # Number of fake train example
            "test": 1,  # Number of fake test example
        }}

        # If you are calling `download/download_and_extract` with a dict, like:
        #   dl_manager.download({{'some_key': 'http://a.org/out.txt', ...}})
        # then the tests needs to provide the fake output paths relative to the
        # fake data directory
        # DL_EXTRACT_RESULT = {{'some_key': 'output_file1.txt', ...}}


      if __name__ == "__main__":
        tfds.testing.test_main()
      """
  )

  with file_path.open('w') as f:
    f.write(context)


def _create_fake_data(root_dir: pathlib.Path, data: Data) -> None:
  file_path = (root_dir / 'fake_examples'
               / 'TODO-add_fake_data_in_this_directory.txt')

  with file_path.open('w') as f:
    f.write(f'{data.todo}: Add fake data in this directory')


def _create_fake_data_gen_file(root_dir: pathlib.Path, data: Data) -> None:
  file_path = root_dir / 'fake_data_generator.py'

  context = textwrap.dedent(
      f"""\
      \"""{data.dataset_name} dataset.\"""

      from absl import app


      def main(_):
        # {data.todo}: Generate Fake Data
        pass


      if __name__ == "__main__":
        app.run(main)
      """
  )
  with file_path.open('w') as f:
    f.write(context)


def _create_checksum_file(root_dir: pathlib.Path, data: Data) -> None:
  file_path = root_dir / 'checksums.txt'

  context = textwrap.dedent(
      f"""\
      # {data.todo}: If your dataset downloads files, then the checksums will be
      # automatically added here when running the download_and_prepare script
      # with --register_checksums.
      """
  )
  with file_path.open('w') as f:
    f.write(context)


def _create_new_dataset(args: argparse.Namespace) -> None:
  ds_name = args.dataset_name
  root_dir = args.dst_dir.expanduser().resolve().joinpath(ds_name)
  root_dir.joinpath('fake_examples').mkdir(parents=True, exist_ok=True)

  data = Data(
      ds_name,
      naming.snake_to_camelcase(ds_name),
      f'TODO({ds_name})',
  )

  _create_dataset_file(root_dir, data)
  _add_the_init(root_dir, data)
  _create_dataset_test_file(root_dir, data)
  _create_fake_data(root_dir, data)
  _create_fake_data_gen_file(root_dir, data)
  _create_checksum_file(root_dir, data)

  print(
      'Dataset generated in {}\n'
      'You can start with searching TODO({}).\n'
      'Please check this '
      '`https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md`'
      'for details.'.format(root_dir, ds_name))


def add_parser(subparsers: argparse._SubParsersAction) -> None:  # pylint:disable = protected-access
  """Add subparser for `new` command"""
  new_ds_parser = subparsers.add_parser(
      'new', help='Generated new dataset files')

  new_ds_parser.add_argument(
      'dataset_name',
      type=str,
      action='store',
      default=None,
      help='Name of the dataset to be created'
  )

  new_ds_parser.add_argument(
      '--dst_dir',
      type=pathlib.Path,
      action='store',
      default=pathlib.Path.cwd(),
      help=('Create new dataset directory at the given location.'
            'Defaults to current directory.')
  )
  new_ds_parser.set_defaults(func=_create_new_dataset)

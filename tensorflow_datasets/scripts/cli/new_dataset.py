r"""tfds CLI `new` command

This command will generator files needed for adding a new dataset(s)
to tfds.

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
import pathlib
from typing import Dict

from tensorflow_datasets.core import naming


_HEADER = """\
\"""{dataset_name} dataset.\"""

"""

_DATASET_DEFAULT_IMPORTS = """\
import tensorflow_datasets as tfds

"""

_DATASET_TEST_DEFAULTS_IMPORTS = """\
import tensorflow_datasets as tfds
import {dataset_name}

"""

_CITATION = """\
# {TODO}: BibTeX citation
_CITATION = \"""
\"""\n
"""

_DESCRIPTION = """\
# {TODO}:
_DESCRIPTION = \"""
\"""\n
"""

_DATASET_DEFAULTS = """\

class {dataset_cls}(tfds.core.GeneratorBasedBuilder):
  \"""DatasetBuilder for {dataset_name} dataset.\"""

  # {TODO}: Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # {TODO}: Specifies the tfds.core.DatasetInfo object
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
    # {TODO}: Downloads the data and defines the splits
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
    # {TODO}: Yields (key, example) tuples from the dataset
    yield 'key', {{}}\n
"""

_DATASET_TEST_DEFAULTS = """\

class {dataset_cls}Test(tfds.testing.DatasetBuilderTestCase):
  # {TODO}:
  DATASET_CLASS = {dataset_name}.{dataset_cls}
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

_CHECKSUM_FILE = """\
# {TODO}: If your dataset downloads files, then the checksums will be
# automatically added here when running the download_and_prepare script
# with --register_checksums.
"""

_INIT_FILE = """\
from {dataset_name} import {dataset_cls}

__all__ = [
    "{dataset_cls}"
]
"""

_FAKE_DATA_GEN_FILE = """\
from absl import app

def main(_):
  # {TODO}: Generate Fake Data
  pass 

if __name__ == "__main__":
  app.run(main)
"""


def create_dataset_file(root_dir: pathlib.Path, data: Dict[str, str]) -> None:
  """Create a new dataset from a template."""
  file_path = root_dir.joinpath(f'{data["dataset_name"]}.py')
  context = (
      _HEADER + _DATASET_DEFAULT_IMPORTS + _CITATION + _DESCRIPTION +
      _DATASET_DEFAULTS)

  with file_path.open('w') as f:
    f.write(context.format(**data))


def add_the_init(root_dir: pathlib.Path, data: Dict[str, str]) -> None:
  """Creates a new __init__.py. file"""
  file_path = root_dir.joinpath('__init__.py')
  context = _HEADER + _INIT_FILE

  with file_path.open('w') as f:
    f.write(context.format(**data))


def create_dataset_test_file(
    root_dir: pathlib.Path,
    data: Dict[str, str]
) -> None:
  """Create the test file associated with the dataset."""
  file_path = root_dir.joinpath(f'{data["dataset_name"]}_test.py')
  context = _HEADER + _DATASET_TEST_DEFAULTS_IMPORTS + _DATASET_TEST_DEFAULTS

  with file_path.open('w') as f:
    f.write(context.format(**data))


def create_fake_data(root_dir: pathlib.Path, data: Dict[str, str]) -> None:
  file_path = root_dir.joinpath(
      'fake_examples', 'TODO-add_fake_data_in_this_directory.txt')

  with file_path.open('w') as f:
    f.write('{TODO}: Add fake data in this directory'.format(**data))


def create_fake_data_gen_file(
    root_dir: pathlib.Path,
    data: Dict[str, str]
) -> None:
  file_path = root_dir.joinpath('fake_data_generator.py')

  context = _HEADER + _FAKE_DATA_GEN_FILE
  with file_path.open('w') as f:
    f.write(context.format(**data))


def create_checksum_file(root_dir: pathlib.Path, data: Dict[str, str]) -> None:
  file_path = root_dir.joinpath('checksums.txt')

  with file_path.open('w') as f:
    f.write(_CHECKSUM_FILE.format(**data))


def create_new_datasets(args: argparse.Namespace) -> None:
  ds_name = args.dataset_name
  root_dir = args.dst_dir.expanduser().resolve().joinpath(ds_name)
  root_dir.joinpath('fake_examples').mkdir(parents=True, exist_ok=True)

  data = dict(
      dataset_name=ds_name,
      dataset_cls=naming.snake_to_camelcase(ds_name),
      TODO='TODO({})'.format(ds_name),
  )

  create_dataset_file(root_dir, data)
  add_the_init(root_dir, data)
  create_dataset_test_file(root_dir, data)
  create_fake_data(root_dir, data)
  create_fake_data_gen_file(root_dir, data)
  create_checksum_file(root_dir, data)

  print(
      'Dataset generated in {}\n'
      'You can start with searching TODO({}).\n'
      'Please check this '
      '`https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md`'
      'for details.'.format(root_dir, ds_name))


def add_new_dataset_parser(subparsers: argparse._SubParsersAction) -> None:  # pylint:disable = protected-access
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
  new_ds_parser.set_defaults(func=create_new_datasets)

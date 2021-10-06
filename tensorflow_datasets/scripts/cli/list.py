
"""`tfds list` command."""

import argparse

from tensorflow_datasets.core import load


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `list` command."""
  new_parser = parsers.add_parser('list', help='Lists all datasets')
  new_parser.set_defaults(subparser_fn=_list_datasets)


def _list_datasets(args: argparse.Namespace) -> None:
  """Creates the dataset directory. Executed by `tfds new <name>`."""
  list_datasets()


def list_datasets():
  datasets = load.list_builders(with_community_datasets=True)
  for dataset in datasets:
    print(dataset)

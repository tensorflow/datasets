
"""`tfds list` command."""

import argparse

from tensorflow_datasets.core import load


def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `list` command."""
  new_parser = parsers.add_parser('list', help='Lists all datasets')

  new_parser.add_argument(
    '--namespace',
    type=str,
    nargs='+',
    help='Namespace flag for displaying datasets from given namespace'
  )

  new_parser.add_argument(
    '--search',
    type=str,
    nargs='+',
    dest='search_query',
    help='Search flag to display all datasets containing the searched query'
  )
  new_parser.set_defaults(subparser_fn=_list_datasets)


def _list_datasets(args: argparse.Namespace) -> None:
  """Lists the datasets/namespaces. Executed by `tfds list <flags> <name>`."""
  list_datasets()


def list_datasets():
  datasets = load.list_builders(with_community_datasets=True)
  for dataset in datasets:
    print(dataset)

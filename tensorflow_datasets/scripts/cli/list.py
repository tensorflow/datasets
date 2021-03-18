
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
  if not args.namespace and not args.search_query:
    list_datasets()
  elif args.namespace:
    list_namespace_datasets(namespace: args.namespace)
  elif args.search_query:
    search_datasets(search_query: args.search_query)

def list_datasets():
  datasets = load.list_builders(with_community_datasets=True)
  for dataset in datasets:
    print(dataset)

def list_namespace_datasets(namespace: str) -> None:
  

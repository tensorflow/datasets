
"""`tfds list` command."""

import argparse

from tensorflow_datasets.core import community
from tensorflow_datasets.core import load
from tensorflow_datasets.core import visibility

def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `list` command."""
  new_parser = parsers.add_parser('list', help='Lists all datasets')

  new_parser.add_argument(
    '--namespace',
    type=str,
    nargs=1,
    help='Namespace flag for displaying datasets from given namespace'
  )

  new_parser.add_argument(
    '--search',
    type=str,
    nargs=1,
    dest='search_query',
    help='Search flag to display all datasets containing the searched query'
  )
  new_parser.set_defaults(subparser_fn=_list_datasets)


def _list_datasets(args: argparse.Namespace) -> None:
  """Lists the datasets/namespaces. Executed by `tfds list <flags> <name>`."""
  if not args.namespace and not args.search_query:
    list_datasets()
  elif args.namespace:
    list_namespace_datasets(namespace=args.namespace)
  elif args.search_query:
    search_datasets(search_query=args.search_query)

def list_datasets():
  datasets = load.list_builders(with_community_datasets=True)
  for dataset in datasets:
    print(dataset)

def list_namespace_datasets(namespace: str) -> None:
  datasets = list()
  dataset_found = False
  #Fetching all community datasets
  if visibility.DatasetType.COMMUNITY_PUBLIC.is_available():
    datasets = community.community_register.list_builders()

  print(f"Datasets associated with `{namespace[0]}` namespace:\n")
  #Getting all datasets for given namespace
  for dataset in datasets:
    if dataset.split(':')[0] == namespace[0]:
      print(dataset)
      if not dataset_found:
        dataset_found = True

  if not dataset_found:
    print("No datasets match given namespace.")

def search_datasets(search_query: str) -> None:
  datasets = load.list_builders()
  dataset_found = False
  #Search for matching datasets
  print(f"Datasets resembling `{search_query[0]}`:\n")
  for dataset in datasets:
    if search_query[0] in dataset:
      print(dataset)
      if not dataset_found:
        dataset_found = True

  if not dataset_found:
    print("No datasets match given query.")

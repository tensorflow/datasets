"""`tfds build` command."""

import argparse

def register_subparser(parsers: argparse._SubParsersAction) -> None:  # pylint: disable=protected-access
  """Add subparser for `build` command."""
  build_parser = parsers.add_parser(
      'build', help='Commands for downloading and preparing datasets.'
  )
  build_parser.add_argument(
      'datasets',  # Positional argument
      type=str,
      nargs='+',
      help='Name of the dataset(s) to be build',
  )
  build_parser.set_defaults(subparser_fn=_build_datasets)

def _build_datasets(args: argparse.Namespace) -> None:
  for ds in args.datasets:
    print(f'Building {ds}')

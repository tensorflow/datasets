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

r"""CLI for Tensorflow Datasets.

TFDS CLI to help creates and build datasets (e.g. `tfds new my_dataset`,
`tfds build`,...)

"""

import argparse
from typing import List

from absl import app
from absl.flags import argparse_flags

import tensorflow_datasets.public_api as tfds

# Import commands
from tensorflow_datasets.scripts.cli import build
from tensorflow_datasets.scripts.cli import new


def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Command lines flag parsing."""
  parser = argparse_flags.ArgumentParser(
      description='Tensorflow Datasets CLI tool',
  )
  parser.add_argument(
      '--version',
      action='version',
      version='TensorFlow Datasets: ' + tfds.__version__
  )
  parser.set_defaults(subparser_fn=lambda _: parser.print_help())
  # Register sub-commands
  subparser = parser.add_subparsers(title='command')
  build.register_subparser(subparser)
  new.register_subparser(subparser)
  return parser.parse_args(argv[1:])


def main(args: argparse.Namespace) -> None:
  # Launch the subcommand defined in the subparser (or default to print help)
  args.subparser_fn(args)


def launch_cli() -> None:
  """Parse arguments and launch the CLI main function."""
  app.run(main, flags_parser=_parse_flags)


if __name__ == '__main__':
  # Entry-points in `setup.py` launch the `launch_cli()` function directly, so
  # the code in `if __name__ == '__main__'` is never executed.
  launch_cli()

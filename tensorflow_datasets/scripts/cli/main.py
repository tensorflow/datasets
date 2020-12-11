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

See: https://www.tensorflow.org/datasets/cli

"""

import argparse
import logging as python_logging
import re
from typing import List

from absl import app
from absl import flags
from absl import logging
from absl.flags import argparse_flags

import tensorflow_datasets.public_api as tfds

# Import commands
from tensorflow_datasets.scripts.cli import build
from tensorflow_datasets.scripts.cli import new

FLAGS = flags.FLAGS


def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Command lines flag parsing."""
  # Normalize explicit boolean flags for absl.flags compatibility
  # See b/174043007 for context.
  argv = _normalize_flags(argv)

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


def _normalize_flags(argv: List[str]) -> List[str]:
  """Normalize explicit bolean flags for absl.flags compatibility."""
  bolean_flag_patern = re.compile(r'--[\w_]+=(true|false)')

  def _normalize_flag(arg: str) -> str:
    if not bolean_flag_patern.match(arg):
      return arg
    if arg.endswith('=true'):
      return arg[:-len('=true')]  # `--flag=true` -> `--flag`
    elif arg.endswith('=false'):
      # `--flag=false` -> `--noflag`
      return '--no' + arg[len('--'):-len('=false')]
    else:
      raise AssertionError(f'Unrecognized arg: {arg}')

  return [_normalize_flag(a) for a in argv]


def main(args: argparse.Namespace) -> None:

  # By default, ABSL won't display any `logging.info` unless the
  # user explicitly set `--logtostderr`.
  # For usability, we activate by default the python log information, but
  # not the C++ ones (which are too verbose).
  if (
      not FLAGS.logtostderr  # If user explicitly request logs, keep C++ logger
      and not FLAGS.alsologtostderr
  ):
    # Using cleaner, less verbose logger
    formatter = python_logging.Formatter(
        '{levelname}[{filename}]: {message}', style='{'
    )
    logging.use_python_logging(quiet=True)
    logging.set_verbosity(logging.INFO)
    logging.get_absl_handler().python_handler.setFormatter(formatter)

  # Launch the subcommand defined in the subparser (or default to print help)
  args.subparser_fn(args)


def launch_cli() -> None:
  """Parse arguments and launch the CLI main function."""
  app.run(main, flags_parser=_parse_flags)


if __name__ == '__main__':
  # Entry-points in `setup.py` launch the `launch_cli()` function directly, so
  # the code in `if __name__ == '__main__'` is never executed.
  launch_cli()

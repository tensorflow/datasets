# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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
from typing import List

from absl import app
from absl import flags
from absl import logging
from absl.flags import argparse_flags

import tensorflow_datasets.public_api as tfds

# Import commands
from tensorflow_datasets.scripts.cli import build
from tensorflow_datasets.scripts.cli import convert_format
from tensorflow_datasets.scripts.cli import croissant
from tensorflow_datasets.scripts.cli import new
from tensorflow_datasets.scripts.utils import flag_utils

FLAGS = flags.FLAGS


def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Command lines flag parsing."""
  argv = flag_utils.normalize_flags(argv)  # See b/174043007 for context.

  parser = argparse_flags.ArgumentParser(
      description='Tensorflow Datasets CLI tool',
      allow_abbrev=False,
  )
  parser.add_argument(
      '--version',
      action='version',
      version='TensorFlow Datasets: ' + tfds.__version__,
  )
  parser.add_argument(
      '--dry_run',
      action='store_true',
      help='If True, print the parsed arguments.',
  )
  parser.set_defaults(subparser_fn=lambda _: parser.print_help())
  # Register sub-commands
  subparser = parser.add_subparsers(title='command')
  build.register_subparser(subparser)
  new.register_subparser(subparser)
  convert_format.register_subparser(subparser)
  croissant.register_subparser(subparser)
  return parser.parse_args(argv[1:])


def main(args: argparse.Namespace) -> None:

  # From the CLI, all datasets are visible
  tfds.core.visibility.set_availables([
      tfds.core.visibility.DatasetType.TFDS_PUBLIC,
      tfds.core.visibility.DatasetType.COMMUNITY_PUBLIC,
  ])

  # By default, ABSL won't display any `logging.info` unless the
  # user explicitly set `--logtostderr`.
  # For usability, we activate by default the python log information, but
  # not the C++ ones (which are too verbose).
  # `logtostderr` may not be defined if `main()` is called directly without
  # `absl.run` (e.g. open source `pytest` tests)
  if not FLAGS.is_parsed() or (
      # If user explicitly request logs, keep C++ logger
      not FLAGS.logtostderr
      and not FLAGS.alsologtostderr
  ):
    # Using cleaner, less verbose logger
    formatter = python_logging.Formatter(
        '{levelname}[{filename}]: {message}', style='{'
    )
    logging.use_python_logging(quiet=True)
    logging.set_verbosity(logging.INFO)
    python_handler = logging.get_absl_handler().python_handler
    python_handler.setFormatter(formatter)
    # Replace `sys.stderr` by the TQDM file
    new_stream = tfds.core.utils.tqdm_utils.TqdmStream()
    python_handler.setStream(new_stream)

  if args.dry_run:
    print(args)
  else:
    # Launch the subcommand defined in the subparser (or default to print help)
    args.subparser_fn(args)


def launch_cli() -> None:
  """Parse arguments and launch the CLI main function."""
  app.run(main, flags_parser=_parse_flags)


if __name__ == '__main__':
  # Entry-points in `setup.py` launch the `launch_cli()` function directly, so
  # the code in `if __name__ == '__main__'` is never executed.
  launch_cli()

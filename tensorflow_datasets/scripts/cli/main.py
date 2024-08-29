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

import dataclasses
import logging as python_logging

from absl import app
from absl import flags
from absl import logging
from etils import eapp
import simple_parsing
import tensorflow_datasets.public_api as tfds

# Import commands
from tensorflow_datasets.scripts.cli import build
from tensorflow_datasets.scripts.cli import convert_format
from tensorflow_datasets.scripts.cli import croissant
from tensorflow_datasets.scripts.cli import new

FLAGS = flags.FLAGS


@dataclasses.dataclass(frozen=True, kw_only=True)
class CmdArgs:
  """TFDS CLI."""

  command: (
      build.CmdArgs | convert_format.CmdArgs | croissant.CmdArgs | new.CmdArgs
  ) = simple_parsing.subparsers(
      subcommands={
          'build': build.CmdArgs,
          'convert_format': convert_format.CmdArgs,
          'build_croissant': croissant.CmdArgs,
          'new': new.CmdArgs,
      },
      default=None,
  )
  # pyformat: disable
  version: bool = simple_parsing.field(
  # pyformat: enable
      action='version',
      version='TensorFlow Datasets: ' + tfds.__version__,
      help='Print version.',
  )


_parse_flags = eapp.make_flags_parser(
    CmdArgs,
    description='Tensorflow Datasets CLI tool',
    allow_abbrev=False,
)


def main(args: CmdArgs) -> None:

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

  # Launch the subcommand defined in the subparser (or default to print help)
  if args.command:
    args.command.execute()
  else:
    _parse_flags(['', '--help'])


def launch_cli() -> None:
  """Parse arguments and launch the CLI main function."""
  app.run(main, flags_parser=_parse_flags)


if __name__ == '__main__':
  # Entry-points in `setup.py` launch the `launch_cli()` function directly, so
  # the code in `if __name__ == '__main__'` is never executed.
  launch_cli()

# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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
import simple_parsing

import tensorflow_datasets.public_api as tfds

# Import commands
from tensorflow_datasets.scripts.cli import build
from tensorflow_datasets.scripts.cli import cli_utils
from tensorflow_datasets.scripts.cli import convert_format
from tensorflow_datasets.scripts.cli import croissant
from tensorflow_datasets.scripts.cli import new

FLAGS = flags.FLAGS


@dataclasses.dataclass(frozen=True, kw_only=True)
class _DummyCommand:
  """Dummy command to avoid `command is MISSING` error."""

  pass


version_field = simple_parsing.field(
    action='version',
    version='TensorFlow Datasets: ' + tfds.__version__,
    help='The version of the TensorFlow Datasets package.',
)


@dataclasses.dataclass(frozen=True, kw_only=True)
class Args(cli_utils.Args):
  """Tensorflow Datasets CLI tool."""

  version: str = version_field
  """The version of the TensorFlow Datasets package."""

  dry_run: bool = simple_parsing.flag(default=False)
  """If True, print the parsed arguments and exit."""

  command: build.Args | new.Args | convert_format.Args | croissant.CmdArgs = (
      simple_parsing.subparsers(
          {
              'build': build.Args,
              'new': new.Args,
              'convert_format': convert_format.Args,
              'build_croissant': croissant.CmdArgs,
          },
          default_factory=_DummyCommand,
      )
  )
  """The command to execute."""

  def execute(self) -> None:
    """Run the command."""
    if self.dry_run:
      print(self)
    # When no command is given, print the help message.
    elif isinstance(self.command, _DummyCommand):
      _parse_flags(['', '--help'])
    else:
      self.command.execute()


_parse_flags = cli_utils.make_flags_parser(
    Args, description='Tensorflow Datasets CLI tool'
)


def main(args: Args) -> None:

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

  args.execute()


def launch_cli() -> None:
  """Parse arguments and launch the CLI main function."""
  app.run(main, flags_parser=_parse_flags)


if __name__ == '__main__':
  # Entry-points in `setup.py` launch the `launch_cli()` function directly, so
  # the code in `if __name__ == '__main__'` is never executed.
  launch_cli()

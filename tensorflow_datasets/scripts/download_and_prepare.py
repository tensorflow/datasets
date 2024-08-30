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

r"""Wrapper around `tfds build`."""

import dataclasses
from typing import List

from absl import app
from absl import logging
import simple_parsing
from tensorflow_datasets.scripts.cli import main as main_cli


@dataclasses.dataclass(frozen=True, kw_only=True)
class CmdArgs:
  """CLI arguments for downloading and preparing datasets.

  Attributes:
    module_import: `--imports` flag.
    dataset: singleton `--datasets` flag.
    builder_config_id: `--config_idx` flag.
  """

  module_import: str | None = None
  dataset: str | None = None
  builder_config_id: int | None = None


def _parse_flags(argv: List[str]) -> main_cli.CmdArgs:
  """Command lines flag parsing."""
  parser = simple_parsing.ArgumentParser()
  parser.add_arguments(CmdArgs, dest='args')
  namespace, build_argv = parser.parse_known_args(argv[1:])
  args = namespace.args

  # Construct CLI arguments for build command
  build_argv = [argv[0], 'build'] + build_argv
  if args.module_import:
    build_argv += ['--imports', args.module_import]
  if args.dataset:
    build_argv += ['--datasets', args.dataset]
  if args.builder_config_id is not None:
    build_argv += ['--config_idx', args.builder_config_id]
  return main_cli._parse_flags(build_argv)  # pylint: disable=protected-access


_display_warning = True


def main(args: main_cli.CmdArgs) -> None:
  if _display_warning:
    logging.warning(
        '***`tfds build` should be used instead of `download_and_prepare`.***'
    )
  main_cli.main(args)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)

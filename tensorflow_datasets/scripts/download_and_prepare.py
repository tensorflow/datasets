# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

import argparse
from typing import List

from absl import app
from absl import flags
from absl import logging

from tensorflow_datasets.scripts.cli import main as main_cli

module_import = flags.DEFINE_string('module_import', None, '`--imports` flag.')
dataset = flags.DEFINE_string('dataset', None, 'singleton `--datasets` flag.')

builder_config_id = flags.DEFINE_integer(
    'builder_config_id', None, '`--config_idx` flag'
)



def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Command lines flag parsing."""
  return main_cli._parse_flags([argv[0], 'build'] + argv[1:])  # pylint: disable=protected-access


_display_warning = True


def main(args: argparse.Namespace) -> None:
  if _display_warning:
    logging.warning(
        '***`tfds build` should be used instead of `download_and_prepare`.***'
    )
  if module_import.value:
    args.imports = module_import.value
  if dataset.value:
    args.datasets = [dataset.value]
  if builder_config_id.value is not None:
    args.config_idx = builder_config_id.value
  main_cli.main(args)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)

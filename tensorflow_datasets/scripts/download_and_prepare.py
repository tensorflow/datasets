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

r"""Wrapper around `tfds build`."""

from absl import app
from absl import flags
from tensorflow_datasets.scripts.cli import main as main_cli


def _parse_flags(argv: list[str]) -> main_cli.Args:
  """Command lines flag parsing."""
  return main_cli._parse_flags([argv[0], 'build'] + argv[1:])  # pylint: disable=protected-access


def main(args: main_cli.Args) -> None:
  from absl import logging
  logging.warning(
      '***`tfds build` should be used instead of `download_and_prepare`.***'
  )
  main_cli.main(args)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)

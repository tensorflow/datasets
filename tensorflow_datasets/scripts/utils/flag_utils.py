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

"""Utility for handling flags."""

import re
from typing import List


def normalize_flags(argv: List[str]) -> List[str]:
  """Returns normalized explicit bolean flags for `absl.flags` compatibility.

  Note: Boolean flags in `absl.flags` can be specified with --bool, --nobool,
  as well as --bool=true/false (though not recommended); in `argparse_flags`,
  it only allows --bool, --nobool.

  Args:
    argv: Arguments for `main()`.
  """
  bolean_flag_patern = re.compile(r'--[\w_]+=(true|false)')

  def _normalize_flag(arg: str) -> str:
    if not bolean_flag_patern.match(arg):
      return arg
    if arg.endswith('=true'):
      return arg[: -len('=true')]  # `--flag=true` -> `--flag`
    elif arg.endswith('=false'):
      # `--flag=false` -> `--noflag`
      return '--no' + arg[len('--') : -len('=false')]
    else:
      raise AssertionError(f'Unrecognized arg: {arg}')

  return [_normalize_flag(a) for a in argv]

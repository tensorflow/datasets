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

"""Utils to manage bools in TFDS."""

from typing import Union


def parse_bool(value: Union[bool, int, str]) -> bool:
  """Parses boolean value from strings/integers in datasets."""
  if not isinstance(value, str):
    return bool(value)
  normalized_string = value.strip().lower()
  if normalized_string in ('false', '0'):
    return False
  if normalized_string in ('true', '1'):
    return True
  raise Exception(f'Cannot convert "{value}" to bool')

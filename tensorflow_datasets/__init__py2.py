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

# pylint: disable=line-too-long
"""Python 2 imports."""
# pylint: enable=line-too-long

import typing
from typing import Any


# We expose a dummy API to avoid breaking Python 2 and 3 libraries which are
# using pytype.
if typing.TYPE_CHECKING:
  as_numpy = Any
  core = Any
  builder = Any
  builder_cls = Any
  decode = Any
  disable_progress_bar = Any
  download = Any
  features = Any
  GenerateMode = Any
  ImageFolder = Any
  is_dataset_on_gcs = Any
  list_builders = Any
  load = Any
  ReadConfig = Any
  Split = Any
  show_examples = Any
  show_statistics = Any
  testing = Any
  TranslateFolder = Any
  units = Any
  visualization = Any
  __version__ = Any

__all__ = []

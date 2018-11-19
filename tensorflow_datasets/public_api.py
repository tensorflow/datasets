# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Public API of tfds, without the registered dataset."""

# pylint: disable=unused-import

from tensorflow_datasets import core
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_format_adapter as file_adapter
from tensorflow_datasets.core import units
from tensorflow_datasets.core.download import GenerateMode
from tensorflow_datasets.core.registered import builder
from tensorflow_datasets.core.registered import list_builders
from tensorflow_datasets.core.registered import load
from tensorflow_datasets.core.splits import percent
from tensorflow_datasets.core.splits import Split

__all__ = [
    "core",
    "download",
    "features",
    "file_adapter",
    "units",
    "GenerateMode",
    "builder",
    "list_builders",
    "load",
    "percent",
    "Split",
]

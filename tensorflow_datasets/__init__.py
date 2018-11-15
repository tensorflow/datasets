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

"""`tensorflow_datasets` package.

`tensorflow_datasets` (`tfds`) defines a collection of datasets ready-to-use
with TensorFlow.

Each dataset is defined as a `tfds.core.DatasetBuilder`.
"""

# Imports for registration
from tensorflow_datasets import image
from tensorflow_datasets import video


# Public API to create and generate a dataset
from tensorflow_datasets.public_api import *  # pylint: disable=wildcard-import

# __all__ for import * as well as documentation
from tensorflow_datasets import public_api  # pylint: disable=g-bad-import-order
__all__ = public_api.__all__

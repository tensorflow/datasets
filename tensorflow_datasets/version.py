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

"""Version info (development version).

All users importing TFDS from `tfds-nightly` or synced to head will see
the `-nightly` suffix.

This file is replaced by `version_stable.py` for stable releases
(`tensorflow-datasets`) on PyPI.
"""

# We follow Semantic Versioning (https://semver.org/spec/v2.0.0.html)
_MAJOR_VERSION = '4'
_MINOR_VERSION = '7'
_PATCH_VERSION = '0'

__version__ = '.'.join([
    _MAJOR_VERSION,
    _MINOR_VERSION,
    _PATCH_VERSION,
]) + '+nightly'

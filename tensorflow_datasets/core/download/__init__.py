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

"""Public API of the download manager."""

from tensorflow_datasets.core.download.checksums_file import load as load_checksums
from tensorflow_datasets.core.download.download_manager import DownloadManager
from tensorflow_datasets.core.download.util import GenerateMode
from tensorflow_datasets.core.proto.download_generated_pb2 import ExtractInfo
from tensorflow_datasets.core.proto.download_generated_pb2 import UrlInfo

__all__ = [
    "DownloadManager",
    "ExtractInfo",
    "GenerateMode",
    "UrlInfo",
    "load_checksums",
]

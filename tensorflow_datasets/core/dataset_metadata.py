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

"""Logic related to reading datasets metadata from config files."""

import dataclasses
import functools
from typing import Dict, List, Text

from etils import epath
from tensorflow_datasets.core import utils

CITATIONS_FILENAME = "CITATIONS.bib"
DESCRIPTIONS_FILENAME = "README.md"
TAGS_FILENAME = "TAGS.txt"

_METADATA_FILES = [
    CITATIONS_FILENAME,
    DESCRIPTIONS_FILENAME,
    TAGS_FILENAME,
]


@dataclasses.dataclass(frozen=True)
class DatasetMetadata:
  """Contains Dataset metadata read from configs."""
  description: Text
  citation: Text
  tags: List[Text]


@functools.lru_cache(maxsize=256)
def load(pkg_path: epath.Path) -> DatasetMetadata:
  """Returns dataset metadata loaded from files in pkg."""
  raw_metadata = _read_files(pkg_path)
  tags = [t for t in raw_metadata.get(TAGS_FILENAME, "").split("\n") if t]
  return DatasetMetadata(
      description=raw_metadata[DESCRIPTIONS_FILENAME],
      citation=raw_metadata[CITATIONS_FILENAME],
      tags=tags,
  )


def _read_files(path: epath.Path) -> Dict[Text, Text]:
  """Reads all metadata files content.

  Args:
    path: path to package where metadata files are.

  Returns:
    dict {path: content}, where path is relative to the dataset src directory.
    e.g. {'README.md': '...', 'CITATIONS.cff': '...'}
  """
  name2path = {}
  for inode in path.iterdir():
    if inode.name in _METADATA_FILES:
      name2path[inode.name] = path.joinpath(inode.name)
  return utils.tree.parallel_map(lambda f: f.read_text("utf-8"), name2path)

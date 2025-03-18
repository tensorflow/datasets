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

"""Logic related to reading datasets metadata from config files."""

from __future__ import annotations

import dataclasses
import functools

from etils import epath
from etils import epy
from tensorflow_datasets.core import constants

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from etils import etree
  from tensorflow_datasets.core.utils import resource_utils
  # pylint: enable=g-import-not-at-top


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

  description: str
  citation: str
  tags: list[str]


def _get_tags(tags_txt: str) -> list[str]:
  """Returns list of tags from raw tags file content."""
  tags = []
  for line in tags_txt.split("\n"):
    tag = line.split("#", 1)[0].strip()
    if tag:
      tags.append(tag)
  return tags


def _get_valid_tags_text() -> str:
  """Returns the valid_tags.txt content."""
  path = resource_utils.tfds_path() / "core/valid_tags.txt"
  return path.read_text("utf-8")


def valid_tags() -> list[str]:
  """Returns a list of valid tags."""
  return _get_tags(_get_valid_tags_text())


def valid_tags_with_comments() -> str:
  """Returns valid tags (one per line) with comments."""
  return "\n".join([
      line
      for line in _get_valid_tags_text().split("\n")
      if not line.startswith("#")
  ])


@functools.lru_cache(maxsize=256)
def load(pkg_path: epath.Path) -> DatasetMetadata:
  """Returns dataset metadata loaded from files in pkg."""
  raw_metadata = _read_files(pkg_path)
  tags = _get_tags(raw_metadata.get(TAGS_FILENAME, ""))
  return DatasetMetadata(
      description=raw_metadata.get(DESCRIPTIONS_FILENAME, None),
      citation=raw_metadata.get(CITATIONS_FILENAME, None),
      tags=tags,
  )


def _read_files(path: epath.Path) -> dict[str, str]:
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
  return etree.parallel_map(lambda f: f.read_text(encoding="utf-8"), name2path)

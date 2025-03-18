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

"""Methods to retrieve and store size/checksums associated to URLs."""

from collections.abc import Iterable
import dataclasses
import hashlib
import io
from typing import Any

from absl import logging
from etils import epath
from tensorflow_datasets.core import utils

_CUSTOM_CHECKSUM_DIRS = []
_CHECKSUM_SUFFIX = '.txt'


@utils.memoize(maxsize=1)
def _default_checksum_dirs() -> list[epath.Path]:
  return [
      utils.tfds_path() / 'url_checksums',
  ]


def sha256(str_: str) -> str:
  return hashlib.sha256(str_.encode()).hexdigest()


@dataclasses.dataclass(eq=True)
class UrlInfo:
  """Small wrapper around the url metadata (checksum, size).

  Attributes:
    size: Download size of the file
    checksum: Checksum of the file
    filename: Name of the file
  """

  size: utils.Size
  checksum: str
  # We exclude the filename from `__eq__` for backward compatibility
  # Two checksums are equals even if filename is unknown or different.
  filename: str | None = dataclasses.field(compare=False)

  def asdict(self) -> dict[str, Any]:
    """Returns the dict representation of the dataclass."""
    return dataclasses.asdict(self)


def compute_url_info(
    path: epath.PathLike,
    checksum_cls=hashlib.sha256,
) -> UrlInfo:
  """Locally compute size, checksums of the given file."""
  path = epath.Path(path)

  checksum = checksum_cls()
  size = 0
  with path.open('rb') as f:
    while True:
      block = f.read(io.DEFAULT_BUFFER_SIZE)
      size += len(block)
      if not block:
        break
      checksum.update(block)

  return UrlInfo(
      checksum=checksum.hexdigest(),  # base64 digest would have been better.
      size=utils.Size(size),
      filename=path.name,
  )


def add_checksums_dir(checksums_dir: str) -> None:
  """Registers a new checksums dir.

  This function allow external datasets not present in the tfds repository to
  define their own checksums_dir containing the dataset downloads checksums.

  Note: When redistributing your dataset, you should distribute the checksums
  files with it and set `add_checksums_dir` when the user is importing your
  `my_dataset.py`.

  ```
  # Set-up the folder containing the 'my_dataset.txt' checksums.
  checksum_dir = os.path.join(os.path.dirname(__file__), 'checksums/')
  checksum_dir = os.path.normpath(checksum_dir)

  # Add the checksum dir (will be executed when the user import your dataset)
  tfds.download.add_checksums_dir(checksum_dir)

  class MyDataset(tfds.core.DatasetBuilder):
    ...
  ```

  Args:
    checksums_dir: `str`, checksums dir to add to the registry
  """
  logging.warning(
      '`tfds.core.add_checksums_dir` is deprecated. Refactor dataset in '
      'self-contained folders (`my_dataset/` folder containing '
      'my_dataset.py, my_dataset_test.py, dummy_data/, checksums.tsv). '
      'The checksum file will be automatically detected. More info at: '
      'https://www.tensorflow.org/datasets/add_dataset'
  )
  if (
      checksums_dir in _CUSTOM_CHECKSUM_DIRS
      or checksums_dir in _default_checksum_dirs()
  ):  # Avoid duplicates
    return
  _CUSTOM_CHECKSUM_DIRS.append(checksums_dir)


@utils.memoize()
def _checksum_paths() -> dict[str, epath.Path]:
  """Returns dict {'dataset_name': 'path/to/checksums/file'}."""
  dataset2path = {}
  for dir_path in _CUSTOM_CHECKSUM_DIRS + _default_checksum_dirs():
    if isinstance(dir_path, str):
      dir_path = epath.Path(dir_path)
    if not dir_path.exists():
      pass
    for file_path in dir_path.iterdir():
      if not file_path.name.endswith(_CHECKSUM_SUFFIX):
        continue
      dataset_name = file_path.name[: -len(_CHECKSUM_SUFFIX)]
      dataset2path[dataset_name] = file_path
  return dataset2path


def _parse_url_infos(checksums_file: Iterable[str]) -> dict[str, UrlInfo]:
  """Returns {URL: (size, checksum)}s stored within given file."""
  url_infos = {}
  for line in checksums_file:
    line = line.strip()  # Remove the trailing '\r' on Windows OS.
    if not line or line.startswith('#'):
      continue
    values = line.split('\t')
    if len(values) == 1:  # not enough values to unpack (legacy files)
      # URL might have spaces inside, but size and checksum will not.
      values = line.rsplit(' ', 2)
    if len(values) == 4:
      url, size, checksum, filename = values
    elif len(values) == 3:
      url, size, checksum = values
      filename = None
    else:
      raise AssertionError(f'Error parsing checksums: {values}')
    url_infos[url] = UrlInfo(
        size=utils.Size(size),
        checksum=checksum,
        filename=filename,
    )
  return url_infos


@utils.memoize()
def get_all_url_infos() -> dict[str, UrlInfo]:
  """Returns dict associating URL to UrlInfo."""
  url_infos = {}
  for path in _checksum_paths().values():
    dataset_url_infos = load_url_infos(path)
    for url, url_info in dataset_url_infos.items():
      if url_infos.get(url, url_info) != url_info:
        raise AssertionError(
            'URL {} is registered with 2+ distinct size/checksum tuples. '
            '{} vs {}'.format(url, url_info, url_infos[url])
        )
    url_infos.update(dataset_url_infos)
  return url_infos


def load_url_infos(path: epath.PathLike) -> dict[str, UrlInfo]:
  """Loads the checksums."""
  return _parse_url_infos(epath.Path(path).read_text().splitlines())


def save_url_infos(
    path: epath.Path,
    url_infos: dict[str, UrlInfo],
) -> None:
  """Store given checksums and sizes for specific dataset.

  Content of file is never disgarded, only updated. This is to ensure that if
  process is killed right after first download finishes, checksums registered
  during previous runs aren't lost.

  It is the responsibility of the caller not to call function multiple times in
  parallel for a given dataset.

  Only original file content is updated. This means the entire set of new sizes
  and checksums must be given at every call.

  Args:
    path: Path to the resources.
    url_infos: dict, {url: (size_in_bytes, checksum)}.
  """
  original_data = load_url_infos(path) if path.exists() else {}
  new_data = original_data.copy()
  new_data.update(url_infos)
  # Compare filenames separately, as filename field is eq=False
  if original_data == new_data and _filenames_equal(original_data, new_data):
    return
  lines = [
      f'{url}\t{int(url_info.size)}\t{url_info.checksum}\t'
      f'{url_info.filename or ""}\n'
      for url, url_info in sorted(new_data.items())
  ]
  path.parent.mkdir(parents=True, exist_ok=True)
  path.write_text(''.join(lines), encoding='UTF-8')


def _filenames_equal(
    left: dict[str, UrlInfo],
    right: dict[str, UrlInfo],
) -> bool:
  """Compare filenames."""
  return all(
      l.filename == r.filename for _, (l, r) in utils.zip_dict(left, right)
  )


def validate_checksums_path(checksums_path: epath.PathLike):
  """Validates the checksums path.

  This function creates the file if it doesn't exist, and writes to it to make
  sure the user has write access before downloading any files.

  Args:
    checksums_path: Path to the checksums file.
  """
  checksums_path = epath.Path(checksums_path)
  if not checksums_path.exists():
    checksums_path.touch()
  else:
    checksums_path.write_text(checksums_path.read_text())

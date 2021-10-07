# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Github pathlib-like util."""

import enum
import functools
import os
import pathlib
import posixpath
from typing import Iterator, List, Optional, Tuple

import requests
from tensorflow_datasets.core import utils

JsonValue = utils.JsonValue

_URI_PREFIX = 'github://'


class _PathType(enum.Enum):
  """Path type (See: https://developer.github.com/v3/git/trees/#tree-object).

  Attributes:
    FILE: File
    DIRECTORY: Directory
    SUBMODULE: Git submodule
      (https://git-scm.com/book/en/v2/Git-Tools-Submodules)
  """
  FILE = enum.auto()
  DIRECTORY = enum.auto()
  SUBMODULE = enum.auto()


class _PathMetadata:
  """Class storing the Github metadata for a file/directory.

  Note:

  * _PathMetadata are cached, so two path pointing to the same file will
    only launch one query.
  * Attributes are dynamically fetched from the github API only when
    requested to avoid unecessary queries.
  * Directory also cache entries for the childs to reduce the
    number of queries. For instance, `[f for f in p.iterdir() if f.is_file()]`
    only use a single query in `iterdir()`, rather than one per `is_file()`.

  Attributes:
    repo: e.g. `tensorflow/datasets`
    branch: e.g. `master`
    subpath: e.g. `core/__init__.py`
  """

  @staticmethod
  @functools.lru_cache(maxsize=None)
  def from_cache(path: str) -> '_PathMetadata':
    """Factory which cache metadata (to avoid querying API multiple times)."""
    return _PathMetadata(path, private=True)

  def __init__(self, path: str, *, private=False):
    if not private:
      raise AssertionError(
          'Metadata should be created using `_PathMetadata.from_cache`')
    repo, branch, subpath = _parse_github_path(path)  # pytype: disable=name-error

    # Read-only attributes
    self._path: str = path
    self.repo: str = repo  # e.g. `tensorflow/datasets`
    self.branch: str = branch  # e.g. `master`
    self.subpath: str = subpath  # e.g 'core/__init__.py'

    # Dynamically loaded properties
    self._exists: Optional[bool] = None
    self._type: Optional[_PathType] = None  # FILE, DIRECTORY, SUBMODULE
    self._childs: Optional[List[str]] = None  # ['README.md', 'docs',...]

  @property
  def type(self) -> _PathType:
    """Type of the path (file, dir, submodule)."""
    if not self._type:
      self._init_and_cache_dynamic_properties()
    return self._type

  def listdir(self) -> List[str]:
    """Returns the filenames in the directory (e.g. `['.gitignore', 'src']`)."""
    if self.type != _PathType.DIRECTORY:
      raise NotADirectoryError(f'{self._path} is not a directory.')
    # self.type could have been computed by the parent dir, so
    # `_init_and_cache_dynamic_properties` may not have been called yet.
    if self._childs is None:
      self._init_and_cache_dynamic_properties()
    return self._childs

  def exists(self) -> bool:
    """Returns True if the file/dir exists."""
    if self._exists is not None:
      return self._exists
    elif self._type:  # If type has been set, the file/dir exists
      return True
    else:
      try:
        self._init_and_cache_dynamic_properties()
        self._exists = True
      except FileNotFoundError:
        self._exists = False
      return self._exists

  def _init_and_cache_dynamic_properties(self) -> None:
    """Query github to get the file/directory content.

    See doc at: https://developer.github.com/v3/repos/contents/

    Note:

     * After this function is called, `_type` and `_childs` (for directories)
       are guarantee to be initialized.
     * For directory, it will create a new `_PathMetadata` entry per
       child (to cache the filetype).

    """
    # e.g. 'https://api.github.com/repos/tensorflow/datasets/contents/docs'
    url = (f'https://api.github.com/repos/{self.repo}/contents/{self.subpath}'
           f'?ref={self.branch}')
    query_content = self._query_github(url)
    if isinstance(query_content, list):  # Directory
      self._init_directory(query_content)
    elif isinstance(query_content, dict):  # File
      self._init_file(query_content)
    else:
      raise AssertionError(f'Unknown content: {query_content}')

  def _init_directory(self, query_content: JsonValue) -> None:
    """Set the dynamic fields (called if `self` is a directory)."""
    self._type = _PathType.DIRECTORY
    self._childs = [f['name'] for f in query_content]

    # Create or update the child metadata type
    for f in query_content:
      metadata = _PathMetadata.from_cache(f"{self._path}/{f['name']}")
      metadata._set_type_from_str(f['type'])  # pylint: disable=protected-access

  def _init_file(self, query_content: JsonValue) -> None:
    """Set the dynamic fields (called if `self` is a file)."""
    # We do not cache the file content as this might grow to big.
    self._set_type_from_str(query_content['type'])

  def _set_type_from_str(self, value: str) -> None:
    """Sets or validates the file type.

    This is called in `_init_and_cache_dynamic_properties` either by `self` or
    the parent directory.

    If the type is already set, this function make sure the new type match.

    Args:
      value: The github type string (see:
        https://developer.github.com/v3/repos/contents/ for available values)
    """
    str_to_type = {
        'file': _PathType.FILE,
        'dir': _PathType.DIRECTORY,
    }
    if value not in str_to_type:
      raise ValueError(f'Unsuported file type: {value} for {self._path}')
    new_type = str_to_type[value]
    if self._type and self._type is not new_type:
      raise AssertionError(
          f'Cannot overwrite type {self._type} with {new_type} for {self._path}'
      )
    self._type = new_type

  def _query_github(self, url: str) -> JsonValue:
    """Launches a github API query and returns the result."""
    # Get the secret API token to avoid the 60 calls/hour limit
    # To get the current quota or test the token:
    # curl -H "Authorization: token ${GITHUB_TOKEN}" https://api.github.com/rate_limit  # pylint: disable=line-too-long
    token = os.environ.get('GITHUB_TOKEN')
    headers = {}
    if token:
      headers['Authorization'] = f'token {token}'
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
      raise FileNotFoundError(
          f'Request failed for {self._path}:\n'
          f' Request: {url}\n'
          f' Error: {resp.status_code}\n'
          f' Reason: {resp.content}',)
    return resp.json()

  def __repr__(self) -> str:
    return f'{type(self).__name__}({self._path})'


@utils.register_pathlike_cls(_URI_PREFIX)
class GithubPath(pathlib.PurePosixPath):
  """`pathlib.Path` like object for manipulating Github paths.

  Example:

  ```
  path = GithubPath.from_repo('tensorflow/datasets')
  path = path / 'docs' / 'catalog'
  assert path.is_dir()
  datasets = [
      p.name for p in path.iterdir() if p.match('*.md')
  ]

  path = GithubPath('github://tensorflow/datasets/tree/master/docs/README.md')
  assert path.subpath == 'docs/README.md'
  assert path.repo == 'tensorflow/datasets'
  assert path.branch == 'master'
  ```

  """

  def __new__(cls, *parts: utils.PathLike) -> 'GithubPath':
    full_path = '/'.join(os.fspath(p) for p in parts)
    _parse_github_path(full_path)  # Validate path
    return super().__new__(cls, full_path.replace(_URI_PREFIX, '/github/', 1))

  @utils.memoized_property
  def _path_str(self) -> str:
    return posixpath.join(_URI_PREFIX, *self.parts[2:])

  def __fspath__(self) -> str:
    return self._path_str

  def __str__(self) -> str:  # pylint: disable=invalid-str-returned
    return self._path_str

  @classmethod
  def from_repo(cls, repo: str, branch: str = 'master') -> 'GithubPath':
    """Factory to creates a GithubPath from a repo name.

    Args:
      repo: Repo name (e.g. `tensorflow/datasets`)
      branch: Branch name (e.g. `master`, 'v1.2.0', '0d240e8b85c'). Default to
        master.

    Returns:
      github_path: The repository root dir at head
    """
    return cls(f'github://{repo}/tree/{branch}')

  @utils.memoized_property
  def _metadata(self) -> _PathMetadata:
    """Returns the path metadata."""
    # The metadata object manage the cache and will dynamically query Github
    # API as needed.
    return _PathMetadata.from_cache(os.fspath(self))

  @property
  def subpath(self) -> str:
    """The inner path (e.g. `core/__init__.py`)."""
    return self._metadata.subpath

  @property
  def repo(self) -> str:
    """The repository identifier (e.g. `tensorflow/datasets`)."""
    return self._metadata.repo

  @property
  def branch(self) -> str:
    """The branch (e.g. `master`, `v2`, `43bbad116df`,...)."""
    return self._metadata.branch

  def as_raw_url(self) -> str:
    """Returns the raw content url (https://raw.githubusercontent.com)."""
    return ('https://raw.githubusercontent.com/'
            f'{self.repo}/{self.branch}/{self.subpath}')

  def iterdir(self) -> Iterator['GithubPath']:
    """Yields the sub-paths."""
    for filename in self._metadata.listdir():
      yield self / filename

  def is_dir(self) -> bool:
    """Returns True if the path is a directory or submodule."""
    return self._metadata.type in (_PathType.DIRECTORY, _PathType.SUBMODULE)

  def is_file(self) -> bool:
    """Returns True if the path is a file."""
    return self._metadata.type is _PathType.FILE

  def exists(self) -> bool:
    """Returns True if the path exists."""
    return self._metadata.exists()

  def read_bytes(self) -> bytes:
    """Returns the file content as bytes."""
    # As the content is fetched during the Github API calls, we could cache it
    # and return it directly here, rather than using an additional query.
    # However this might have significant memory impact if many `GithubPath`
    # are used, so would require some additional cleanup (weakref ?).
    # Using raw_url doesn't count in the API calls quota and should works with
    # arbitrary sized files.
    url = self.as_raw_url()
    resp = requests.get(url)
    if resp.status_code != 200:
      raise FileNotFoundError(f'Request failed for {url}\n'
                              f' Error: {resp.status_code}\n'
                              f' Reason: {resp.content}')
    return resp.content

  def read_text(self, encoding: Optional[str] = None) -> str:
    """Returns the file content as string."""
    return self.read_bytes().decode(encoding=encoding or 'utf-8')

  def copy(
      self,
      dst: utils.PathLike,
      overwrite: bool = False,
  ) -> utils.ReadWritePath:
    """Copy the current file to the given destination.

    Args:
      dst: Target file. It can be any PathLike compatible path (e.g. `gs://...`)
      overwrite: Whether the file should be overwritten or not

    Returns:
      The new created file.

    Raises:
      FileExistsError: If `overwrite` is false and destination exists.
    """
    dst = utils.as_path(dst)
    if not overwrite and dst.exists():
      raise FileExistsError(f'Cannot copy {self}. Destination {dst} exists.')
    # Otherwise, copy src to dst
    dst.write_bytes(self.read_bytes())
    return dst


def _parse_github_path(path: str) -> Tuple[str, str, str]:
  """Parse the absolute github path.

  Args:
    path: The full github path.

  Returns:
    repo: The repository identifiant.
    branch: Repository branch.
    subpath: The inner path.

  Raises:
    ValueError: If the path is invalid
  """
  err_msg = (f'Invalid github path: {path}. Expected format: '
             '`github://<owner>/<name>/tree/<branch>[/<path>]`.')

  if not path.startswith(_URI_PREFIX):
    raise ValueError(err_msg)
  if path.endswith('/'):
    raise ValueError(err_msg + ' Trailing `/` not supported.')
  parts = path[len(_URI_PREFIX):].split('/')
  if len(parts) < 4:
    raise ValueError(err_msg)

  # 'tensorflow', 'datasets', 'tree', 'master', ...
  owner, repo, tree, branch, *subpath = parts
  if tree != 'tree':
    raise ValueError(err_msg + '. `/blob/` isn\'t accepted. Only `/tree/`.')

  return f'{owner}/{repo}', branch, '/'.join(subpath)

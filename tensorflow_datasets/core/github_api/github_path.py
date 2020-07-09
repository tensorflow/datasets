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

"""Github pathlib-like util."""

import enum
import functools
import os
import pathlib
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

import requests

# TODO(pytype): Should be recursive
Json = Union[str, int, bool, float, List[Any], Dict[str, Any]]


class _PathType(enum.Enum):
  """Path type (See: https://developer.github.com/v3/git/trees/#tree-object).

  Attributes:
    FILE: File
    DIRECTORY: Directory
    COMMIT: Git submodule (https://git-scm.com/book/en/v2/Git-Tools-Submodules)
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
    # In the future, the cache might contains the full file content, this might
    # grow big. We should add a cleanup mechanism (use weakref ?).
    return _PathMetadata(path, private=True)

  def __init__(self, path: str, *, private=False):
    if not private:
      raise AssertionError(
          'Metadata should be created using `_PathMetadata.from_cache`'
      )
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
      self._init_and_cache_content()
    return self._type

  def _set_type_from_str(self, value: str) -> None:
    """Sets or validates the file type.

    This is called in `_init_and_cache_content` either by `self` or the parent
    directory.

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

  def listdir(self) -> List[str]:
    """Returns the filenames in the directory (e.g. `['.gitignore', 'src']`)."""
    if self.type != _PathType.DIRECTORY:
      raise NotADirectoryError(f'{self._path} is not a directory.')
    # self.type could have been computed by the parent dir, so
    # `_init_and_cache_content` may not have been called yet.
    if self._childs is None:
      self._init_and_cache_content()
    return self._childs

  def exists(self) -> bool:
    """Returns True if the file/dir exists."""
    if self._exists is not None:
      return self._exists
    elif self._type:  # If type has been set, the file/dir exists
      return True
    else:
      try:
        self._init_and_cache_content()
        self._exists = True
      except FileNotFoundError:
        self._exists = False
      return self._exists

  def _init_and_cache_content(self) -> None:
    """Query github to get the file/directory content.

    See doc at: https://developer.github.com/v3/repos/contents/

    Note:

     * After this function is called, `_type` and `_childs` (for directories)
       are guarantee to be initialized.
     * For directory, it will create a new `_PathMetadata` entry per
       child (to cache the filetype).

    """
    # e.g. 'https://api.github.com/repos/tensorflow/datasets/contents/docs'
    url = (
        f'https://api.github.com/repos/{self.repo}/contents/{self.subpath}'
        f'?ref={self.branch}'
    )
    data = self._query_github(url)
    if isinstance(data, list):  # Directory
      self._init_directory(data)
    elif isinstance(data, dict):  # File
      self._init_file(data)
    else:
      raise AssertionError(f'Unknown content: {data}')

  def _init_directory(self, data: Json) -> None:
    """Set the dynamic fields."""
    self._type = _PathType.DIRECTORY
    self._childs = [f['name'] for f in data]

    # Create or update the child metadata type
    for f in data:
      metadata = _PathMetadata.from_cache(f"{self._path}/{f['name']}")
      metadata._set_type_from_str(f['type'])  # pylint: disable=protected-access

  def _init_file(self, data: Json) -> None:
    self._set_type_from_str(data['type'])

  def _query_github(self, url: str) -> Json:
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
          f' Reason: {resp.content}',
      )
    return resp.json()

  def __repr__(self) -> str:
    return f'{type(self).__name__}({self._path})'


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

  path = GithubPath('/tensorflow/datasets/tree/master/docs/README.md')
  assert path.subpath == 'docs/README.md'
  assert path.repo == 'tensorflow/datasets'
  assert path.branch == 'master'
  ```

  """
  _metadata: _PathMetadata  # Additional file metadata

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
    return cls(f'/{repo}/tree/{branch}')

  def _init(self, *args, **kwargs):
    """Constructor."""
    # Currently, the best way for subclassing `pathlib` objects is to
    # overload `_init` (see: https://bugs.python.org/issue41109)
    # Future Python version may have a cleaner Path extension system:
    # https://discuss.python.org/t/make-pathlib-extensible/3428/24
    super()._init(*args, **kwargs)  # pytype: disable=attribute-error
    # The metadata object manage the cache and will dynamically query Github
    # API as needed.
    self._metadata = _PathMetadata.from_cache(str(self))

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
    return (
        'https://raw.githubusercontent.com/'
        f'{self.repo}/{self.branch}/{self.subpath}'
    )

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
  if path.endswith('/'):
    raise ValueError(
        f'Invalid github path: {path}. Trailing `/` not supported.'
    )
  parts = pathlib.PurePosixPath(path).parts
  if len(parts) < 5:
    raise ValueError(
        f'Invalid github path: {path}. Expected format: '
        '`/<owner>/<name>/tree/<branch>[/<path>]`.'
    )

  # '/', 'tensorflow', 'datasets', 'tree', 'master', ...
  root, owner, repo, tree, branch, *subpath = parts
  if root != '/' or tree != 'tree':
    raise ValueError(
        f'Invalid github path: {path}. Expected format: '
        '`/<owner>/<name>/tree/<branch>[/<path>]`. Note that `/blob/` isn\'t '
        'accepted. Only `/tree/`.'
    )

  return f'{owner}/{repo}', branch, '/'.join(subpath)

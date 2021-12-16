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

import dataclasses
import functools
import os
import pathlib
import posixpath
from typing import Iterator, Mapping, MutableMapping, Optional, Set, Tuple

import requests
from tensorflow_datasets.core import utils

JsonValue = utils.JsonValue

_URI_PREFIX = 'github://'


def _get_token():
  # Get the secret API token to avoid the 60 calls/hour limit
  # To get the current quota or test the token:
  # curl -H "Authorization: token ${GITHUB_TOKEN}" https://api.github.com/rate_limit  # pylint: disable=line-too-long
  return os.environ.get('GITHUB_TOKEN')


def get_content(url: str) -> bytes:
  resp = requests.get(url)
  if resp.status_code != 200:
    raise FileNotFoundError(f'Request failed for {url}\n'
                            f' Error: {resp.status_code}\n'
                            f' Reason: {resp.content}')
  return resp.content


class GithubApi:
  """Class to issue calls to the Github API."""

  def __init__(self, token: Optional[str] = None):
    self._token = token or _get_token()

  def query(self, url: str) -> JsonValue:
    """Launches a Github API query and returns the result."""
    headers = {}
    if self._token:
      headers['Authorization'] = f'token {self._token}'
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
      raise FileNotFoundError(
          f'Request failed:\n'
          f' Request: {url}\n'
          f' Error: {resp.status_code}\n'
          f' Reason: {resp.content}',)
    return resp.json()

  def query_tree(self, repo: str, branch: str) -> JsonValue:
    """Queries a repository tree.

    See https://docs.github.com/en/rest/reference/git#trees

    Args:
      repo: the repository
      branch: the branch for which to get the tree

    Returns:
      JSON dict with the tree.
    """
    url = f'https://api.github.com/repos/{repo}/git/trees/{branch}?recursive=1'
    return self.query(url)


def _correct_folder(folder: str) -> str:
  """Ensures the folder follows a standard.

  Pathlib.parent in the root folder results in '.', whereas in other places
  we should use '' for the root folder. This function makes sure the root
  folder is always empty string.

  Args:
    folder: the folder to be corrected.

  Returns:
    The corrected folder.
  """
  if folder == '.':
    return ''
  return folder


def _get_parent_folder(path: pathlib.PurePosixPath) -> str:
  return _correct_folder(os.fspath(path.parent))


@dataclasses.dataclass(frozen=True)
class _GithubElement:
  """Representation of an element in a Github tree (a file or folder).

  Attributes:
    parent_folder: the folder in which this element resides.
    name: the name of this element, e.g. the file name or the folder name.
    is_folder: whether this element is a folder or not.
  """
  parent_folder: str
  name: str
  is_folder: bool

  @classmethod
  def from_path(cls, path: pathlib.PurePosixPath,
                is_folder: bool) -> '_GithubElement':
    parent_folder = _get_parent_folder(path)
    name = path.name
    return cls(parent_folder=parent_folder, name=name, is_folder=is_folder)


@dataclasses.dataclass(frozen=True)
class _GithubTree:
  """A Github tree of a repository."""
  files_per_folder: Mapping[str, Set[_GithubElement]]

  def is_folder(self, path: str) -> bool:
    return _correct_folder(path) in self.files_per_folder

  def is_file(self, path: pathlib.PurePosixPath) -> bool:
    parent_folder = _get_parent_folder(path)
    files = self.files_per_folder.get(parent_folder)
    if not files:
      return False
    file = _GithubElement(
        parent_folder=parent_folder, name=path.name, is_folder=False)
    return file in files

  @classmethod
  def from_json(cls, value) -> '_GithubTree':
    """Parses a GithubTree from the given JSON."""
    if not isinstance(value, dict) or 'tree' not in value:
      raise ValueError(f'Github API response not supported: {value}')

    files_per_folder: MutableMapping[str, Set[str]] = {}
    for element in value['tree']:
      github_element = _GithubElement.from_path(
          path=pathlib.PurePosixPath(element['path']),
          is_folder=(element['type'] == 'tree'))
      if element['type'] in {'blob', 'tree'}:
        files_per_folder.setdefault(github_element.parent_folder, set())
        files_per_folder[github_element.parent_folder].add(github_element)
    return _GithubTree(files_per_folder=files_per_folder)

  @staticmethod
  @functools.lru_cache(maxsize=None)
  def from_cache(repo: str, branch: str) -> '_GithubTree':
    """Factory which caches the entire Github tree."""
    tree_json = GithubApi().query_tree(repo, branch)
    # If the tree is truncated, then we'll need a more sophisticated method to
    # retrieve the whole tree. Since this is currently not supported, it raises
    # an exception.
    assert not tree_json.get('truncated', False)
    return _GithubTree.from_json(tree_json)


@dataclasses.dataclass(frozen=True, eq=True)
class _PathMetadata:
  """Github metadata of a file or directory."""
  path: str
  repo: str  # e.g. `tensorflow/datasets`
  branch: str  # e.g. `master`
  subpath: str  # e.g 'core/__init__.py'

  @classmethod
  def from_path(cls, path: str) -> '_PathMetadata':
    repo, branch, subpath = _parse_github_path(path)
    return cls(path=path, repo=repo, branch=branch, subpath=subpath)


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
    _parse_github_path(full_path)
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
    return _PathMetadata.from_path(os.fspath(self))

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

  @property
  def github_tree(self) -> _GithubTree:
    return _GithubTree.from_cache(self.repo, self.branch)

  def as_raw_url(self) -> str:
    """Returns the raw content url (https://raw.githubusercontent.com)."""
    return ('https://raw.githubusercontent.com/'
            f'{self.repo}/{self.branch}/{self.subpath}')

  def as_human_friendly_url(self) -> str:
    """Returns the human friendly url."""
    return f'https://github.com/{self.repo}/blob/{self.branch}/{self.subpath}'

  def iterdir(self) -> Iterator['GithubPath']:
    """Yields the sub-paths."""
    if not self.is_dir():
      raise NotADirectoryError(f'{self.subpath} is not a directory.')
    for filename in self.github_tree.files_per_folder[self.subpath]:
      yield self / filename.name

  def is_dir(self) -> bool:
    """Returns True if the path is a directory or submodule."""
    return self.github_tree.is_folder(self.subpath)

  def is_file(self) -> bool:
    """Returns True if the path is a file."""
    return self.github_tree.is_file(pathlib.PurePosixPath(self.subpath))

  def exists(self) -> bool:
    """Returns True if the path exists."""
    return self.is_dir() or self.is_file()

  def read_bytes(self) -> bytes:
    """Returns the file content as bytes."""
    # As the content is fetched during the Github API calls, we could cache it
    # and return it directly here, rather than using an additional query.
    # However this might have significant memory impact if many `GithubPath`
    # are used, so would require some additional cleanup (weakref ?).
    # Using raw_url doesn't count in the API calls quota and should works with
    # arbitrary sized files.
    url = self.as_raw_url()
    return get_content(url)

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

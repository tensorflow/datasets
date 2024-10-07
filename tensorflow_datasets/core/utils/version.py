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

"""Version utils."""

from __future__ import annotations

import dataclasses
import enum
import re
from typing import List, Tuple, Union

from etils import epath

_VERSION_TMPL = r"^(?P<major>{v})" r"\.(?P<minor>{v})" r"\.(?P<patch>{v})$"
_NO_LEADING_ZEROS = r"\d|[1-9]\d*"
_VERSION_WILDCARD_REG = re.compile(
    _VERSION_TMPL.format(v=_NO_LEADING_ZEROS + r"|\*")
)
_VERSION_RESOLVED_REG = re.compile(_VERSION_TMPL.format(v=_NO_LEADING_ZEROS))


class DatasetVariantBlockedError(ValueError):
  """Exception raised when a blocked version and/or config is requested."""


# A dictionary of blocked versions or configs.
# The key is a version or config string, the value is a short sentence
# explaining why that version or config should not be used (or None).
BlockedWithMsg = dict[str, str | None]


@dataclasses.dataclass(frozen=True)
class IsBlocked:
  """Class to store information about a version or config being blocked.

  Also contains an optional message explaining why the version or config is
  blocked.
  """

  result: bool = False
  blocked_msg: str | None = None

  def __bool__(self) -> bool:
    return self.result


@dataclasses.dataclass(frozen=True)
class BlockedVersions:
  """Holds information on versions and configs that should not be used.

  Note that only complete versions can be blocked: wilcards in versions are not
  supported.

  versions: A dictionary of bad versions for which all configs should be
    blocked.
  configs: A mapping from versions to a dictionary of configs that should not be
    used for that version.
  """

  versions: BlockedWithMsg = dataclasses.field(default_factory=dict)
  configs: dict[str, BlockedWithMsg] = dataclasses.field(default_factory=dict)

  def is_blocked(
      self, version: str | Version, config: str | None = None
  ) -> IsBlocked:
    """Checks whether a version or config is blocked.

    Args:
      version: The version to check.
      config: The config to check. If None, the version is checked.

    Returns:
      An IsBlocked object. If IsBlocked.result is True, IsBlocked.blocked_msg
      contains the message explaining why the version or config is blocked, if
      it exists, or a default message otherwise.
    """
    if isinstance(version, Version):
      version = str(version)
    if version in self.versions:
      blocked_msg = self.versions[version] or f"Version {version} is blocked."
      return IsBlocked(True, blocked_msg)
    if config is not None and version in self.configs:
      if config in self.configs[version]:
        blocked_msg = (
            self.configs[version][config]
            or f"Config {config} for version {version} is blocked."
        )
        return IsBlocked(True, blocked_msg)
    return IsBlocked(False)


class Experiment(enum.Enum):
  """Experiments which can be enabled/disabled on a per version basis.

  Experiments are designed to gradually apply changes to datasets while
  maintaining backward compatibility with previous versions. All experiments
  should eventually be deleted, once used by all versions of all datasets.

  Eg:
  class Experiment(enum.Enum):
    EXP_A = enum.auto()  # Short description of experiment.

  class MyBuilder(...):
    VERSION = tfds.core.Version('1.2.3', experiments={
        tfds.core.Experiment.EXP_A: True,
        })
  """

  # A Dummy experiment, which should NOT be used, except for testing.
  DUMMY = 1


class Version:
  """Dataset version MAJOR.MINOR.PATCH."""

  _DEFAULT_EXPERIMENTS = {
      Experiment.DUMMY: False,
  }

  def __init__(
      self,
      version: Union[Version, str],
      experiments=None,
      tfds_version_to_prepare=None,
  ):
    """Version init.

    Args:
      version: string. Eg: "1.2.3".
      experiments: dict of experiments. See Experiment.
      tfds_version_to_prepare: string, defaults to None. If set, indicates that
        current version of TFDS cannot be used to `download_and_prepare` the
        dataset, but that TFDS at version {tfds_version_to_prepare} should be
        used instead.
    """
    if isinstance(version, Version):
      version_str = str(version)
      experiments = experiments or version._experiments
      tfds_version_to_prepare = (
          tfds_version_to_prepare or version.tfds_version_to_prepare
      )
    else:
      version_str = version
    self._experiments = self._DEFAULT_EXPERIMENTS.copy()
    self.tfds_version_to_prepare = tfds_version_to_prepare
    if experiments:
      if isinstance(experiments, str):
        raise ValueError(
            f"Invalid Version('{version}', '{experiments}'). Description is "
            "deprecated. RELEASE_NOTES should be used instead."
        )
      self._experiments.update(experiments)
    self.major, self.minor, self.patch = _str_to_version(version_str)

  def implements(self, experiment):
    """Returns True if version implements given experiment."""
    return self._experiments[experiment]

  def __str__(self):
    return "{}.{}.{}".format(*self.tuple)

  def __repr__(self) -> str:
    return f"{type(self).__name__}('{str(self)}')"

  @property
  def tuple(self):
    return self.major, self.minor, self.patch

  def _validate_operand(self, other):
    if isinstance(other, str):
      return Version(other)
    elif isinstance(other, Version):
      return other
    raise AssertionError(
        "{} (type {}) cannot be compared to version.".format(other, type(other))
    )

  def __eq__(self, other):
    if other is None:
      return False
    other = self._validate_operand(other)
    return self.tuple == other.tuple

  def __lt__(self, other):
    other = self._validate_operand(other)
    return self.tuple < other.tuple

  def __le__(self, other):
    other = self._validate_operand(other)
    return self.tuple <= other.tuple

  def __gt__(self, other):
    other = self._validate_operand(other)
    return self.tuple > other.tuple

  def __ge__(self, other):
    other = self._validate_operand(other)
    return self.tuple >= other.tuple

  def __hash__(self) -> int:
    return hash(self.tuple)

  def match(self, other_version) -> bool:
    """Returns True if other_version matches.

    Args:
      other_version: string, of the form "x[.y[.x]]" where {x,y,z} can be a
        number or a wildcard.
    """
    major, minor, patch = _str_to_version(other_version, allow_wildcard=True)
    return (
        major in [self.major, "*"]
        and minor in [self.minor, "*"]
        and patch in [self.patch, "*"]
    )

  @classmethod
  def is_valid(cls, version: Version | str | None) -> bool:
    """Returns True if the version can be parsed."""
    if isinstance(version, Version):
      return True
    elif version is None:
      return False
    try:
      return cls(version) and True
    except ValueError:  # Invalid version (ex: incomplete data dir)
      return False


def _str_to_version(
    version_str: str, allow_wildcard=False
) -> Tuple[Union[int, str], Union[int, str], Union[int, str]]:
  """Return the tuple (major, minor, patch) version extracted from the str."""
  if not isinstance(version_str, str):
    raise TypeError(
        "Can only convert strings to versions. "
        f"Got: {type(version_str)} with value {version_str}."
    )
  reg = _VERSION_WILDCARD_REG if allow_wildcard else _VERSION_RESOLVED_REG
  res = reg.match(version_str)
  if not res:
    msg = "Invalid version '{}'. Format should be x.y.z".format(version_str)
    if allow_wildcard:
      msg += " with {x,y,z} being digits or wildcard."
    else:
      msg += " with {x,y,z} being numbers without leading zeros."
    raise ValueError(msg)
  return tuple(
      v if v == "*" else int(v)  # pylint:disable=g-complex-comprehension
      for v in [res.group("major"), res.group("minor"), res.group("patch")]
  )


def list_all_versions(root_dir: epath.PathLike) -> List[Version]:
  """Lists all dataset versions present on disk, sorted."""
  root_dir = epath.Path(root_dir)
  versions = []
  try:
    for path in root_dir.iterdir():
      if Version.is_valid(path.name) and path.is_dir():
        versions.append(Version(path.name))
  except OSError:
    return versions
  return sorted(versions)

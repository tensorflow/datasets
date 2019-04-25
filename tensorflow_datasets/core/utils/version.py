# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Version utils.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import re

_VERSION_TMPL = (
    r"^(?P<major>{v})"
    r"\.(?P<minor>{v})"
    r"\.(?P<patch>{v})$")
_VERSION_WILDCARD_REG = re.compile(_VERSION_TMPL.format(v=r"\d+|\*"))
_VERSION_RESOLVED_REG = re.compile(_VERSION_TMPL.format(v=r"\d+"))


class Version(collections.namedtuple("Version", ["major", "minor", "patch"])):
  """Dataset version MAJOR.MINOR.PATCH."""

  LATEST = "latest"

  def __new__(cls, *args, **kwargs):
    if len(args) == 1:
      if kwargs:
        raise ValueError(
            "Only one of version str or major/minor/patch can be set")
      version_str = args[0]
      if isinstance(version_str, cls):
        return version_str
      elif version_str == cls.LATEST:
        return version_str
      return super(Version, cls).__new__(cls, *_str_to_version(version_str))
    elif not args and not kwargs:
      return super(Version, cls).__new__(cls, 0, 0, 0)
    else:
      return super(Version, cls).__new__(cls, *args, **kwargs)

  def __str__(self):
    return "{}.{}.{}".format(self.major, self.minor, self.patch)

  def match(self, other_version):
    """Returns True if other_version matches.

    Args:
      other_version: string, of the form "x[.y[.x]]" where {x,y,z} can be a
        number or a wildcard.
    """
    major, minor, patch = _str_to_version(other_version, allow_wildcard=True)
    return (major in [self.major, "*"] and minor in [self.minor, "*"]
            and patch in [self.patch, "*"])


def _str_to_version(version_str, allow_wildcard=False):
  """Return the tuple (major, minor, patch) version extracted from the str."""
  reg = _VERSION_WILDCARD_REG if allow_wildcard else _VERSION_RESOLVED_REG
  res = reg.match(version_str)
  if not res:
    msg = "Invalid version '{}'. Format should be x.y.z".format(version_str)
    if allow_wildcard:
      msg += " with {x,y,z} being digits or wildcard."
    else:
      msg += " with {x,y,z} being digits."
    raise ValueError(msg)
  return tuple(
      v if v == "*" else int(v)
      for v in [res.group("major"), res.group("minor"), res.group("patch")])

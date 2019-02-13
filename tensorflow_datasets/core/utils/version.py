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


def _str_to_version(version_str):
  """Return the tuple (major, minor, patch) version extracted from the str."""
  version_ids = version_str.split(".")
  if len(version_ids) != 3 or "-" in version_str:
    raise ValueError(
        "Could not convert the {} to version. Format should be x.y.z".format(
            version_str))
  try:
    version_ids = tuple(int(v) for v in version_ids)
  except ValueError:
    raise ValueError(
        "Could not convert the {} to version. Format should be x.y.z".format(
            version_str))
  return version_ids

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

"""Utilities for file names."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re

_first_cap_re = re.compile("(.)([A-Z][a-z0-9]+)")
_all_cap_re = re.compile("([a-z0-9])([A-Z])")


def camelcase_to_snakecase(name):
  """Convert camel-case string to snake-case."""
  s1 = _first_cap_re.sub(r"\1_\2", name)
  return _all_cap_re.sub(r"\1_\2", s1).lower()


def snake_to_camelcase(name):
  """Convert snake-case string to camel-case string."""
  return "".join(n.capitalize() for n in name.split("_"))


def filename_prefix_for_name(name):
  if os.path.basename(name) != name:
    raise ValueError("Should be a dataset name, not a path: %s" % name)
  return camelcase_to_snakecase(name)


def filename_prefix_for_split(name, split):
  if os.path.basename(name) != name:
    raise ValueError("Should be a dataset name, not a path: %s" % name)
  return "%s-%s" % (filename_prefix_for_name(name), split)


def sharded_filenames(filename_prefix, num_shards):
  """Sharded filenames given prefix and number of shards."""
  shard_suffix = "%05d-of-%05d"
  return [
      "%s-%s" % (filename_prefix, shard_suffix % (i, num_shards))
      for i in range(num_shards)
  ]


def filepattern_for_dataset_split(dataset_name, split, data_dir,
                                  filetype_suffix=None):
  prefix = filename_prefix_for_split(dataset_name, split)
  if filetype_suffix:
    prefix += ".%s" % filetype_suffix
  filepath = os.path.join(data_dir, prefix)
  return "%s*" % filepath


def filepaths_for_dataset_split(dataset_name, split, num_shards, data_dir,
                                filetype_suffix=None):
  prefix = filename_prefix_for_split(dataset_name, split)
  if filetype_suffix:
    prefix += ".%s" % filetype_suffix
  filenames = sharded_filenames(prefix, num_shards)
  filepaths = [os.path.join(data_dir, fname) for fname in filenames]
  return filepaths

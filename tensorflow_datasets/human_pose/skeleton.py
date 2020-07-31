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

# Lint as: python3
"""Utils for human skeleton annotations."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets.core import utils


class Skeleton():
  """Class for aiding in data manipulation/augmentation and visualizations.

  Each skeleton is defined by a number of links, where each link is a
  `(child, parent)` pair. Each joint must exist as a child, and each parent
  must be a joint or `None` (i.e. you may not have a non-None parent which
  does not exists as a child)

  By convention we use strings for joints. Any joint prefixed by "l_" or "r_"
  is interpretted as being a left or right joint respectively. This can be used
  for data augmentation. See `Skeleton.flip_left_right`.

  Joints are indexed by the location they appear in `links` as a child
  (provided in constructor), i.e. if entry index 1 of `links` is
  `('l_knee', 'l_hip')`, then associated arrays are assumed to have the relevant
  quantity about the left knee in index 1. This is helpful for plotting.
  """
  def __init__(self, links, name=None):
    """Create skeleton from the provided links.

    Each link in a tuple of `(child, parent)`, where parent may be `None`.

    e.g.
    ```python
    Skeleton((
      ('l_ankle', 'l_knee'),
      ('l_knee', 'l_hip'),
      ('l_hip', None)
    ))
    ```
    would represent a disconnected left leg. The left knee would be associated
    with index `1`.

    Every `parent` should exists as a `child`

    Args:
      `links`: iterable of `(child, parent)` iterables. Joints are indexed
        by their position in `links` as the child.
    """
    self._links = tuple(tuple(link) for link in links)  # make immutable
    if any(link[0] is None for link in self._links):
      raise ValueError("link children cannot be `None`.")
    self._num_joints = len(self._links)
    self._indices = {k[0]: i for i, k in enumerate(self._links)}
    for _, parent in self._links:
      if parent is not None and parent not in self._indices:
        raise ValueError(
            "Every non-None parent must be present as a child "
            "(possibly with `None` parent), '%s' is missing" % parent)
    self._name = name

  def __repr__(self):
    return "<Skeleton: %s>" % (
        self.num_joints if self._name is None else self._name)

  @property
  def num_joints(self):
    return self._num_joints

  @utils.memoized_property
  def flip_left_right_indices(self):
    indices = []
    for i, (child, _) in enumerate(self._links):
      if child.startsiwth("l_"):
        indices.append(self.index("r_%s" % child[2:]))
      else:
        indices.append(i)
    return tuple(indices)

  def index(self, key):
    return self._indices[key]

  @property
  def links(self):
    return self._links

  def parent(self, child):
    """Get parent joint of the given child joint."""
    return self._links[self.index(child)][1]

  @property
  def joints(self):
    """Get a tuple of joint keys in index order."""
    return tuple(l[0] for l in self._links)

  def parent_index(self, child_index):
    """Get parent index of the given child index."""
    joint = self._links[child_index][1]
    return None if joint is None else self.index(joint)

  @utils.memoized_property
  def parent_indices(self):
    return tuple(self.parent_index(i) for i in range(self.num_joints))

  def subset_indices(self, joint_subset):
    return tuple(self.index(j) for j in joint_subset)


def conversion_indices(src_skeleton, target_skeleton):
  return [src_skeleton.index(j) for j in target_skeleton.joints]


# common joint names
thorax = 'thorax'
r_hip = 'r_hip'
r_knee = 'r_knee'
r_ankle = 'r_ankle'
r_ball = 'r_ball'
r_toes = 'r_toes'
l_hip = 'l_hip'
l_knee = 'l_knee'
l_ankle = 'l_ankle'
l_ball = 'l_ball'
l_toes = 'l_toes'
neck = 'neck'
head_center = 'head-center'
head_back = 'head-back'
l_shoulder = 'l_shoulder'
l_elbow = 'l_elbow'
l_wrist = 'l_wrist'
l_thumb = 'l_thumb'
l_little = 'l_little'
r_shoulder = 'r_shoulder'
r_elbow = 'r_elbow'
r_wrist = 'r_wrist'
r_thumb = 'r_thumb'
r_little = 'r_little'
pelvis = 'pelvis'

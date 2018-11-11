# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Splits related API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

from six.moves import zip  # pylint: disable=redefined-builtin

__all__ = [
    "Split",
    "SplitDict",
    "SplitGenerator",
]


# TODO(epot): Replate the str by custom objects
class Split(object):
  """`Enum` for dataset splits.

  Datasets are typically split into different subsets to be used at various
  stages of training and evaluation.

  * `TRAIN`: the training data.
  * `VALIDATION`: the validation data. If present, this is typically used as
    evaluation data while iterating on a model (e.g. changing hyperparameters,
    model architecture, etc.).
  * `TEST`: the testing data. This is the data to report metrics on. Typically
    you do not want to use this during model iteration as you may overfit to it.
  """
  TRAIN = "train"
  VALIDATION = "validation"
  TEST = "test"


# TODO(afrozm): Replace by the proto object.
# Could also add the number of sample here such as the user can do
# num_train_sample = builder.info.splits[tfds.Split.TRAIN].num_sample
SplitInfo = collections.namedtuple("SplitInfo", ["name", "num_shards"])


class SplitDict(dict):
  """Split info object."""

  def __getitem__(self, key):
    return super(SplitDict, self).__getitem__(str(key))

  def __setitem__(self, key, value):
    raise ValueError("Cannot add elem. Use .add() instead.")

  def add(self, split_info):
    """Add the split info."""
    if split_info.name in self:
      raise ValueError("Split {} already present".format(split_info.name))
    super(SplitDict, self).__setitem__(str(split_info.name), split_info)

  # TODO(afrozm): Replace by proto
  def from_json_data(self, split_data):
    """Restore the splits info from the written metadata file."""
    self.clear()
    for s in split_data:
      self.add(SplitInfo(name=s["name"], num_shards=s["num_shards"]))

  def to_json_data(self):
    """Export the metadata for json export."""
    return [
        {"name": str(s.name), "num_shards": s.num_shards}
        for s in self.values()
    ]


class SplitGenerator(object):
  """Defines the split info for the generator.

  This should be used as returned value of
  `GeneratorBasedDatasetBuilder._split_generators`.
  See `GeneratorBasedDatasetBuilder._split_generators` for more info and example
  of usage.

  Args:
    name (str/list[str]): Name of the Split for which the generator will create
      the samples. If a list is given, the generator samples will be distributed
      among the splits proportionally to the num_shards
    num_shards (int/list[int]): Number of shards between which the generated
      samples will be written. If name is a list, then num_shards should be a
      list with the same number of element.
    gen_kwargs (dict): Kwargs to forward to the ._generate_samples() of the
      generator builder

  """

  def __init__(self, name, num_shards=1, gen_kwargs=None):
    self.gen_kwargs = gen_kwargs or {}

    if isinstance(name, list):
      split_zip = zip(name, num_shards)
    else:
      split_zip = [(name, num_shards)]
    self.split_info_list = [
        SplitInfo(name=n, num_shards=k) for n, k in split_zip
    ]

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

"""Script to call download_and_prepare on DatasetBuilder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pdb

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import download_manager
from tensorflow_datasets.core import registered

# pylint: disable=unused-import,g-bad-import-order
# TODO(rsepassi): Determine importing policy for tensorflow_datasets
from tensorflow_datasets.image import cifar
from tensorflow_datasets.image import mnist
# pylint: enable=unused-import,g-bad-import-order

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("builder", None, "Registered name of DatasetBuilder")
flags.DEFINE_string("data_dir", None, "Directory for data")
flags.DEFINE_string("download_dir", None, "Directory for downloads")
flags.DEFINE_boolean("debug", False,
                     "If True, will drop into debugger after generation")

STATS_STR = """
Stats
Dataset: {name}
Split: {split}
Count: {count}
Per-feature stats:
  {per_feature_stats}
"""

FEATURE_STATS_STR = """\
{name}: {dtype} {shape}
    {stats}\
"""


def main(_):
  dm = download_manager.DownloadManager(FLAGS.download_dir)
  builder = registered.builder(FLAGS.builder)(
      data_dir=FLAGS.data_dir, download_manager=dm)
  builder.download_and_prepare()

  # TODO(rsepassi): Get splits from info
  splits = [dataset_builder.Split.TRAIN, dataset_builder.Split.TEST]
  for split in splits:
    compute_stats(builder, split)


def compute_stats(builder, split):
  """Print statistics for this split."""
  dataset = builder.as_dataset(split=split)
  if FLAGS.debug:
    iterator = tf.contrib.eager.Iterator(dataset)
    pdb.set_trace()
    del iterator
    return

  first_example = None
  count = 0
  per_feature_stats = {}
  for example in dataset:
    count += 1
    if first_example is None:
      first_example = example
      for k in example:
        per_feature_stats[k] = {
            "min": np.inf,
            "max": -np.inf,
        }

    # TODO(rsepassi): Check feature names, types, shapes stay constant and match
    # DatasetInfo.

    for k in example:
      fmin = np.min(example[k].numpy())
      if fmin < per_feature_stats[k]["min"]:
        per_feature_stats[k]["min"] = fmin
      fmax = np.max(example[k].numpy())
      if fmax > per_feature_stats[k]["max"]:
        per_feature_stats[k]["max"] = fmax

  per_feature_stats_str = "\n  ".join([
      FEATURE_STATS_STR.format(
          name=k,
          dtype=repr(first_example[k].dtype),
          shape=first_example[k].shape,
          stats=v) for k, v in per_feature_stats.items()
  ])
  print(
      STATS_STR.format(
          name=builder.name,
          split=split,
          count=count,
          per_feature_stats=per_feature_stats_str))


if __name__ == "__main__":
  flags.mark_flags_as_required(["builder", "data_dir"])
  tf.enable_eager_execution()
  tf.app.run()

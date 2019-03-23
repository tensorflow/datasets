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

r"""Generate shapenet-like files with random data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import json
import random

import numpy as np
import tensorflow as tf

from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.volume import modelnet
from tensorflow_datasets.volume.shapenet.iccv2017 import load_class_names
from tensorflow_datasets.volume.shapenet.iccv2017 import NUM_PART_CLASSES
from tensorflow_datasets.volume.shapenet import iccv2017_test
from tensorflow_datasets.volume.utils import off
from tensorflow_datasets.core.utils import py_utils


fake_examples_dir = os.path.join(
    py_utils.tfds_dir(), "testing", "test_data", "fake_examples")


def make_iccv2017_part_data():
  base_dir = os.path.join(
    fake_examples_dir, "shapenet_part2017",
    "shapenetcore_partanno_segmentation_benchmark_v0_normal")
  test_utils.remake_dir(base_dir)
  split_dir = os.path.join(base_dir, "train_test_split")
  tf.io.gfile.makedirs(split_dir)
  _, class_ids = load_class_names()
  j = 0
  for split, num_examples in iccv2017_test.splits.items():
    if split == "validation":
      split = "val"
    paths = []

    for _ in range(num_examples):
      class_id = random.sample(class_ids, 1)[0]
      filename = 'example%d.txt' % j
      j += 1

      subdir = os.path.join(base_dir, class_id)
      if not tf.io.gfile.isdir(subdir):
        tf.io.gfile.makedirs(subdir)
      path = os.path.join(subdir, filename)
      n_points = np.random.randint(10) + 2
      points = np.random.normal(size=n_points*3).reshape((n_points, 3))
      normals = np.random.normal(size=n_points*3).reshape((n_points, 3))
      normals /= np.linalg.norm(normals, axis=-1, keepdims=True)
      point_labels = np.random.randint(NUM_PART_CLASSES, size=n_points)
      data = np.empty((n_points, 7), dtype=np.float32)
      data[:, :3] = points.astype(np.float32)
      data[:, 3:6] = normals.astype(np.float32)
      data[:, 6] = point_labels.astype(np.float32)
      with tf.io.gfile.GFile(path, "wb") as fp:
        np.savetxt(fp, data)
      paths.append(os.path.join("shape_data", class_id, filename[:-4]))

    with tf.io.gfile.GFile(
           os.path.join(split_dir, "shuffled_%s_file_list.json" % split),
           "wb") as fp:
      json.dump(paths, fp)


def main(_):
  make_iccv2017_part_data()



if __name__ == "__main__":
  main(None)

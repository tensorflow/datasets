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

r"""Generate modelnet-like files with random data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import random

import numpy as np
import tensorflow as tf

from tensorflow_datasets.testing import test_utils

from tensorflow_datasets.volume.modelnet.modelnet import load_class_names
from tensorflow_datasets.volume.modelnet.modelnet import ModelnetSampledConfig
from tensorflow_datasets.volume.modelnet import modelnet_test
from tensorflow_datasets.volume.utils import off
from tensorflow_datasets.core.utils import py_utils
import tarfile


fake_examples_dir = os.path.join(
      py_utils.tfds_dir(), "testing", "test_data", "fake_examples")


def add_off(
        data_dir, archive, split, class_name, example_index, num_vertices=10,
        num_faces=4, min_verts=3, max_verts=5):
  path = os.path.join(
    class_name, split, "%s_%04d.off" % (class_name, example_index + 1))
  vertices = np.random.normal(size=(num_vertices*3)).reshape((num_vertices, 3))
  face_lengths = np.random.randint(min_verts, max_verts, size=num_faces)
  face_values = np.random.randint(num_vertices, size=np.sum(face_lengths))
  offobj = off.OffObject(vertices, face_values, face_lengths)
  tmp_path = os.path.join(data_dir, "tmp.off")
  with tf.io.gfile.GFile(tmp_path, "wb") as fp:
    offobj.to_file(fp)
  archive.add(tmp_path, path)
  tf.io.gfile.remove(tmp_path)


def make_base_data(data_dir, num_classes):
  path = os.path.join(
    data_dir, modelnet_test.base_dl_extract_result(num_classes))
  class_names = load_class_names(num_classes)
  with tarfile.open(path, "w:gz") as archive:
    for (split, n) in (
        ('train', modelnet_test.num_train_examples),
        ('test', modelnet_test.num_test_examples)):
      for _ in range(n):
        class_name = random.sample(class_names, 1)[0]
        example_index = np.random.randint(9998)
        add_off(data_dir, archive, split, class_name, example_index)


def save_sampled_data(base_dir, num_points, class_name, example):
  folder = os.path.join(base_dir, class_name)
  if not tf.io.gfile.isdir(folder):
    tf.io.gfile.makedirs(folder)
  path = os.path.join(folder, "%s.txt" % example)
  positions = np.random.normal(size=(num_points*3)).reshape((num_points, 3))
  normals = np.random.normal(size=(num_points*3)).reshape((num_points, 3))
  normals /= np.linalg.norm(normals, axis=-1, keepdims=True)
  data = np.concatenate((positions, normals), axis=-1)
  with tf.io.gfile.GFile(path, "wb") as fp:
    np.savetxt(fp, data, delimiter=",")


def make_sampled_data():
  base_dir = os.path.join(
    fake_examples_dir, "modelnet_sampled", "modelnet40_normal_resampled")
  test_utils.remake_dir(base_dir)
  config = ModelnetSampledConfig(10)

  num_points = config.num_points
  all_examples = []
  # 10 class names are a subset of the 40
  class_names = load_class_names(10)
  for _ in range(
        modelnet_test.num_train_examples + modelnet_test.num_test_examples):
      class_name = random.sample(class_names, 1)[0]
      example_index = np.random.randint(0, 9998)
      example = "%s_%04d" % (class_name, example_index+1)
      all_examples.append(example)
      save_sampled_data(base_dir, num_points, class_name, example)
  for num_classes in (10, 40):
    random.shuffle(all_examples)
    train_examples = all_examples[:modelnet_test.num_train_examples]
    test_examples = all_examples[modelnet_test.num_train_examples:]
    for split_examples, split in (
        (train_examples, "train"), (test_examples, "test")):
      path = os.path.join(
        base_dir, "modelnet%d_%s.txt" % (num_classes, split))
      with tf.io.gfile.GFile(path, "wb") as fp:
        fp.write("".join((("%s\n" % example) for example in split_examples)))


def main(_):
  for num_classes in (10, 40):
    base_dir = os.path.join(fake_examples_dir, 'modelnet%d' % num_classes)
    test_utils.remake_dir(base_dir)
    make_base_data(base_dir, num_classes)
  aligned_dir = os.path.join(fake_examples_dir, 'modelnet_aligned40')
  test_utils.remake_dir(aligned_dir)
  make_base_data(aligned_dir, 40)
  make_sampled_data()



if __name__ == "__main__":
  main(None)

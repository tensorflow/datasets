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

r"""Generate shapenet_r2n2-like files, smaller and with random data.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.image import shapenet_r2n2 as sn
import tensorflow_datasets.core.features.run_length_encoded_feature.rle.binvox as bv
import tensorflow_datasets.core.features.run_length_encoded_feature.rle.np_impl as np_impl

flags.DEFINE_string("compression", "zip", "compression to use for images")
FLAGS = flags.FLAGS

sn.RENDERINGS_PER_EXAMPLE = 3
sn._TRAIN_FRAC = 0.5
CAT_IDS = sn.cat_ids()[:2]
N_EXAMPLES = 2


def examples_dir():
  return os.path.join(
      py_utils.tfds_dir(), "testing", "test_data", "fake_examples",
      "shapenet_r2n2")


def make_images(num_examples):
  # monocolored images that are good for compression
  shape = (num_examples, sn.RENDERINGS_PER_EXAMPLE, 1, 1, 3)
  vals = np.random.randint(256, size=np.prod(shape)).reshape(shape)
  return np.tile(vals, (1, 1) + sn.IMAGE_SHAPE[:-1] + (1,)).astype(np.uint8)


def make_labels(num_examples):
  shape = (num_examples,) + sn.VOXEL_SHAPE
  return (np.random.random(size=(np.prod(shape))) > 0.1).reshape(shape)

def write_images(root_dir, cat_id, example_ids):
  from PIL import Image
  images = make_images(len(example_ids))
  meta_shape = (sn.RENDERINGS_PER_EXAMPLE, 5)
  for example_id, example_images in zip(example_ids, images):
    base_dir = os.path.join(
        root_dir, "ShapeNetRendering", cat_id, example_id, "rendering")
    tf.io.gfile.makedirs(base_dir)
    for i, im in enumerate(example_images):
      path = os.path.join(base_dir, "%02d.png" % i)
      with tf.io.gfile.GFile(path, "wb") as fp:
        Image.fromarray(im).save(fp, compression=FLAGS.compression)
    rendering_data = np.random.random(size=meta_shape).reshape(meta_shape)
    path = os.path.join(base_dir, "rendering_metadata.txt")
    with tf.io.gfile.GFile(path, "wb") as fp:
      np.savetxt(fp, rendering_data)


def write_labels(root_dir, cat_id, example_ids):
  voxels = make_labels(len(example_ids))
  for example_id, vox in zip(example_ids, voxels):
    base_dir = os.path.join(root_dir, "ShapeNetVox32", cat_id, example_id)
    tf.io.gfile.makedirs(base_dir)
    path = os.path.join(base_dir, "model.binvox")
    with tf.io.gfile.GFile(path, "wb") as fp:
      rle = np_impl.dense_to_rle(
          vox.astype(np.uint8).flatten(), dtype=np.uint8)
      bv.write_binvox(fp, rle, sn.VOXEL_SHAPE)


def main(_):
  root_dir = examples_dir()
  test_utils.remake_dir(root_dir)
  for cat_id in CAT_IDS:
    example_ids = ["random_%s_%d" % (cat_id, i) for i in range(N_EXAMPLES)]
    write_images(root_dir, cat_id, example_ids)
    write_labels(root_dir, cat_id, example_ids)


if __name__ == "__main__":
  app.run(main)

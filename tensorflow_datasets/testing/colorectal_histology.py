r"""Generate ColorectalHistology-like files with random data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags
import numpy as np
import tensorflow as tf

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.image.colorectal_histology import _CLASS_NAMES
from tensorflow_datasets.image.colorectal_histology import _class_subdir
from tensorflow_datasets.image.colorectal_histology import _TILES_SUBDIR
from tensorflow_datasets.image.colorectal_histology import _LARGE_SUBDIR
from tensorflow_datasets.image.colorectal_histology import _TILES_SIZE
from tensorflow_datasets.image.colorectal_histology import _LARGE_SIZE

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
# --compression=raw may be more portable, but results in massive files (>100mb)
flags.DEFINE_string(
    "compression", "tiff_lzw", "Used by PIL to compress fake images")
FLAGS = flags.FLAGS

num_classes = len(_CLASS_NAMES)
class_index = {c: i for i, c in enumerate(_CLASS_NAMES)}


def examples_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples")


def histology_dir(large=False):
  folder = os.path.join(examples_dir(), "colorectal_histology")
  if large:
    folder = "%s_large" % folder
  return folder


def make_images(num_images, size):
    # random values compress badly
    return np.zeros((num_images, size, size, 3), dtype=np.uint8)


def write_image(filename, data):
  tfds.core.lazy_imports.PIL_Image.fromarray(data).save(
    filename, compression=FLAGS.compression)


def main(_):
  base_dir = os.path.join(histology_dir(False), _TILES_SUBDIR)
  for ci, class_name in enumerate(_CLASS_NAMES):
    subdir = os.path.join(base_dir, _class_subdir(ci, class_name))
    tf.io.gfile.makedirs(subdir)

    for i, image_data in enumerate(make_images(2, _TILES_SIZE)):
      fn = "image%d.tif" % i
      write_image(os.path.join(subdir, fn), image_data)

  base_dir = os.path.join(histology_dir(True), _LARGE_SUBDIR)
  tf.io.gfile.makedirs(base_dir)
  write_image(
      os.path.join(base_dir, "large_image.tif"), make_images(1, _LARGE_SIZE)[0])


if __name__ == "__main__":
  app.run(main)

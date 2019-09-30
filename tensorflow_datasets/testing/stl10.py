from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags
import numpy as np

import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils

NUMBER_IMAGES_PER_BATCH = 2
HEIGHT, WIDTH = (96,96)
NUMBER_BATCHES = 5
NUMBER_LABELS = 11

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def stl10_output_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
                      "stl10", "stl-10-batches-bin")


def dump(output_dir, fname, images, labels):
  path = os.path.join(output_dir, fname)
  print("Writing %s..." % path)
  with open(path, "wb") as out_file:
    for image, labels in zip(images, labels):
      out_file.write(labels.tobytes())
      out_file.write(image.tobytes())


def generate_stl10_batch(batch_name):
  images = np.random.randint(
      256, size=(NUMBER_IMAGES_PER_BATCH, HEIGHT * WIDTH * 3), dtype=np.uint8)
  labels = np.random.randint(1,
      high=NUMBER_LABELS, size=(NUMBER_IMAGES_PER_BATCH), dtype=np.uint8)
  dump(stl10_output_dir(), batch_name, images, labels)



def _generate_stl10_data():
  output_dir = stl10_output_dir()
  test_utils.remake_dir(output_dir)
  for batch_number in range(1, NUMBER_BATCHES + 1):
    generate_stl10_batch("data_batch_%s.bin" % batch_number)
  generate_stl10_batch("test_batch.bin")
  label_names = tfds.builder("stl10").info.features["label"].names
  print(label_names)
  with open(os.path.join(output_dir, "batches.meta.txt"), "w") as f:
    f.write("\n".join(label_names))


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_stl10_data()


if __name__ == "__main__":
  app.run(main)

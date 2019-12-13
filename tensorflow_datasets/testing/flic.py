"""Generates FLIC like files with random data for testing."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import scipy.io

from absl import app
from absl import flags

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
  "Path to tensorflow_datasets directory")

FLAGS = flags.FLAGS

def _output_dir(data):
  """Returns output directory."""
  dname = "FLIC" if data == "small" else "FLIC-full"
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
    "flic", dname)

def _generate_image(data, fdir, fname):
  dirname = os.path.join(_output_dir(data), fdir)
  if not os.path.exists(dirname):
    os.makedirs(dirname)
  tf.io.gfile.copy(
      fake_data_utils.get_random_jpeg(480, 720),
      os.path.join(dirname, fname),
      overwrite=True)

def _generate_mat(data, train_fname, test_fname):
  dirname = os.path.join(_output_dir(data), "examples.mat")
  data = {
    "examples": np.array([
      np.array([
        np.array([1, 2, 3], dtype=np.uint16),
        "example_movie",
        np.array([np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])]),
        train_fname,
        np.array([1.0, 2.0, 3.0]),
        1.0,
        np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32),
        True,
        False,
      ]),
      np.array([
        np.array([1, 2, 3], dtype=np.uint16),
        "example_movie",
        np.array([np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])]),
        test_fname,
        np.array([1.0, 2.0, 3.0]),
        1.0,
        np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32),
        False,
        True,
      ]),
    ]),
  }
  
  scipy.io.savemat(dirname, data)

def main(argv):
  _generate_image("small", "images", "example_movie00000001.jpg")
  _generate_image("small", "images", "example_movie00000002.jpg")
  _generate_mat("small", "example_movie00000001.jpg", "example_movie00000002.jpg")

  _generate_image("full", "images", "example_movie00000003.jpg")
  _generate_image("full", "images", "example_movie00000004.jpg")
  _generate_mat("full", "example_movie00000003.jpg", "example_movie00000004.jpg")

if __name__ == "__main__":
  app.run(main)
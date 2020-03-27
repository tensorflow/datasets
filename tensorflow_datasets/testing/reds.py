"""Generate fake data for REDS dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import zipfile

from absl import app
from absl import flags
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")

FLAGS = flags.FLAGS

_IMAGE_HEIGHT = 720
_IMAGE_WIDTH = 1280


def _output_dir():
  """Return the path to the output directory of the fake data."""
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
                      "reds")


def _zip_images(out_path, zip_path):
  """Create a zip file containing fake images.

  Args:
    out_path: (`str`) The output path of the zip file.
    zip_path: (`str`) Additional path inside the zip file.
  """
  image = fake_data_utils.get_random_png(height=_IMAGE_HEIGHT,
                                         width=_IMAGE_WIDTH)

  with zipfile.ZipFile(out_path, "w") as myzip:
    myzip.write(image, os.path.join(zip_path, "000", "00000000.png"))
    myzip.write(image, os.path.join(zip_path, "000", "00000001.png"))
    myzip.write(image, os.path.join(zip_path, "001", "00000000.png"))
    myzip.write(image, os.path.join(zip_path, "001", "00000001.png"))


def main(argv):
  del argv

  filenames = ["train_blur.zip", "val_blur.zip", "test_blur.zip"]
  out_paths = [os.path.join(_output_dir(), fname) for fname in filenames]
  zip_paths = ["train/train_blur", "val/val_blur", "test/test_blur"]

  for out_path, zip_path in zip(out_paths, zip_paths):
    _zip_images(out_path, zip_path)


if __name__ == "__main__":
  app.run(main)

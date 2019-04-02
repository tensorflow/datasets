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

r"""Generate sun397-like files, smaller and with random data.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import md5
import os
import random
import tarfile
import tempfile

from absl import app
from absl import flags

import numpy as np
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.image import sun
import tensorflow_datasets.public_api as tfds


flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

MIN_HEIGHT_WIDTH = 10
MAX_HEIGHT_WIDTH = 15


def _output_dir():
  return os.path.join(
      FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "sun397")


def _get_random_picture(height=None, width=None, channels=None):
  """Returns random picture as np.ndarray (int)."""
  height = height or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  width = width or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  channels = channels or random.randrange(1, 4)
  return np.random.randint(256, size=(height, width, channels), dtype=np.uint8)


def _generate_data():
  """Generate random data for testing the Sun397 dataset builder."""

  names_file = tfds.core.get_tfds_path(
      os.path.join("image", "sun397_labels.txt"))
  label_names = tfds.features.ClassLabel(names_file=names_file).names

  def _generate_image_to_tar(image_format, channels, tar):
    """Generate a random image and add it to the given tar file."""
    label = random.choice(label_names)
    image = _get_random_picture(channels=channels)
    # Regardless of the actual format, always write with .jpg extension.
    fobj = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    sun._encode_image(image, image_format, fobj=fobj)  # pylint: disable=protected-access
    filename = "SUN397/%s/sun_%s.jpg" % (label,
                                         md5.new(fobj.read()).hexdigest())
    fobj.seek(0)
    fobj.close()
    tar.add(fobj.name, arcname=filename)

  tar = tarfile.open(os.path.join(_output_dir(), "SUN397.tar.gz"), mode="w:gz")
  _generate_image_to_tar(image_format="JPEG", channels=1, tar=tar)
  _generate_image_to_tar(image_format="JPEG", channels=3, tar=tar)
  _generate_image_to_tar(image_format="GIF", channels=3, tar=tar)
  _generate_image_to_tar(image_format="BMP", channels=1, tar=tar)
  _generate_image_to_tar(image_format="BMP", channels=3, tar=tar)
  _generate_image_to_tar(image_format="PNG", channels=1, tar=tar)
  _generate_image_to_tar(image_format="PNG", channels=3, tar=tar)
  _generate_image_to_tar(image_format="PNG", channels=4, tar=tar)
  tar.close()


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_data()


if __name__ == "__main__":
  app.run(main)

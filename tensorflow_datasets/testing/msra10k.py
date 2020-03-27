# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

r"""
Generates MSRA 10K Like Dataset

"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags

import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.image import msra10k
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.testing import fake_data_utils
import matplotlib.pyplot as plt

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")

FLAGS = flags.FLAGS

NUM_IMAGES = 3
MIN_HEIGHT_WIDTH = 150
MAX_HEIGHT_WIDTH  = 350


def _output_dir():
  """Returns output directory."""
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
                      "msra10k", "msra10k_images")


def _generate_jpeg(height, width,image_idx):
  """Generates and saves jpeg picture."""
  jpeg = fake_data_utils.get_random_picture(height, width,channels=3)
  filepath = os.path.join(_output_dir())+"/"+str(image_idx)+".jpg"
  plt.imsave(filepath,jpeg)


def _generate_png(height, width,image_idx):
  """Generates and saves png picture."""
  png = fake_data_utils.get_random_picture(height, width)
  filepath = os.path.join(_output_dir())+"/"+str(image_idx)+'.png'
  plt.imsave(filepath,png)


def _generate_images():
  """Generates training images."""
  for i in range(NUM_IMAGES):
      height = np.random.randint(low=MIN_HEIGHT_WIDTH, high=MAX_HEIGHT_WIDTH)
      width = np.random.randint(low=MIN_HEIGHT_WIDTH, high=MAX_HEIGHT_WIDTH)
      jpeg = _generate_jpeg(height,width,i+1)
      png = _generate_png(height,width,i+1)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_images()


if __name__ == "__main__":
  app.run(main)

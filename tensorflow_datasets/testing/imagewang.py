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

r"""Generate testing images for Imagewang. 

Each image is a black 1 by 1 image.
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

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

_IMAGE_FILENAME = 'test_image.JPEG'
_LABEL_DIRNAME = 'label'

_SIZES = ["full-size", "320px", "160px"]
_SIZE_TO_DIRNAME = {
    "full-size": "imagewang",
    "320px": "imagewang-320",
    "160px": "imagewang-160"
}


def examples_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples")


def imagewang_dir(size, split):
  dir_name = _SIZE_TO_DIRNAME[size]
  return os.path.join(examples_dir(), 'imagewang', dir_name, split)


def imagewang_label_dir(size, split):
  return os.path.join(imagewang_dir(size, split), _LABEL_DIRNAME)


def make_image():
  return np.random.randint(256, size=(1 * 1), dtype=np.uint8)


def write_image_file(filename):
  with tf.io.gfile.GFile(filename, "wb") as f:
    f.write(b"1" * 16)  # header
    f.write(make_image().tobytes())


def main(_):
  for size in _SIZES:
    train_output_dir = imagewang_label_dir(size, split='train')
    val_output_dir = imagewang_label_dir(size, split='val')
    test_utils.remake_dir(os.path.join(train_output_dir))
    test_utils.remake_dir(os.path.join(val_output_dir))
    write_image_file(os.path.join(train_output_dir,  _IMAGE_FILENAME))
    write_image_file(os.path.join(val_output_dir, _IMAGE_FILENAME))


if __name__ == "__main__":
  app.run(main)

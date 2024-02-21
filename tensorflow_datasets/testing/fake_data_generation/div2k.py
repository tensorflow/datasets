# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Generates DIV2K like files with random data for testing."""

import os

from absl import app
from absl import flags

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string(
    "tfds_dir",
    os.fspath(utils.tfds_write_path()),
    "Path to tensorflow_datasets directory",
)

FLAGS = flags.FLAGS

DATA = {
    "DIV2K_train_HR": "0001.png",
    "DIV2K_train_LR_bicubic_X2": "0001x2.png",
    "DIV2K_train_LR_bicubic_X3": "0001x3.png",
    "DIV2K_train_LR_bicubic_X4": "0001x4.png",
    "DIV2K_train_LR_difficult": "0001x4d.png",
    "DIV2K_train_LR_mild": "0001x4m.png",
    "DIV2K_train_LR_unknown_X2": "0001x2.png",
    "DIV2K_train_LR_unknown_X3": "0001x3.png",
    "DIV2K_train_LR_unknown_X4": "0001x4.png",
    "DIV2K_train_LR_wild": "0001x4w.png",
    "DIV2K_train_LR_x8": "0001x8.png",
    "DIV2K_valid_HR": "0002.png",
    "DIV2K_valid_LR_bicubic_X2": "0002x2.png",
    "DIV2K_valid_LR_bicubic_X3": "0002x3.png",
    "DIV2K_valid_LR_bicubic_X4": "0002x4.png",
    "DIV2K_valid_LR_difficult": "0002x4d.png",
    "DIV2K_valid_LR_mild": "0002x4m.png",
    "DIV2K_valid_LR_unknown_X2": "0002x2.png",
    "DIV2K_valid_LR_unknown_X3": "0002x3.png",
    "DIV2K_valid_LR_unknown_X4": "0002x4.png",
    "DIV2K_valid_LR_wild": "0002x4w.png",
    "DIV2K_valid_LR_x8": "0002x8.png",
}


def _output_dir():
  """Returns output directory."""
  return os.path.join(
      FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "div2k"
  )


def _generate_image(fdir, fname):
  dirname = os.path.join(_output_dir(), fdir)
  if not os.path.exists(dirname):
    os.makedirs(dirname)
  tf.io.gfile.copy(
      fake_data_utils.get_random_png(1, 1),
      os.path.join(dirname, fname),
      overwrite=True,
  )


def main(argv):
  del argv
  for fdir, fname in DATA.items():
    _generate_image(fdir, fname)


if __name__ == "__main__":
  app.run(main)

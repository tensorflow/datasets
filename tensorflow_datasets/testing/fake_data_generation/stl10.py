# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Generate stl10 like files, smaller and with random data.

"""

import os

from absl import app
from absl import flags
import numpy as np

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils

HEIGHT, WIDTH = (96, 96)
NUMBER_LABELS = 10

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def stl_output_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
                      "stl10", "stl10_binary")


def dump(output_dir, fname, data):
  path = os.path.join(output_dir, fname)
  print("Writing %s..." % path)
  with open(path, "wb") as out_file:
    out_file.write(data.tobytes())


def _generate_stl10_data():
  """Generates .bin files for stl10."""
  output_dir = stl_output_dir()
  test_utils.remake_dir(output_dir)
  for fname in ["train_y.bin", "test_y.bin"]:
    labels = np.random.randint(
        NUMBER_LABELS, size=(1), dtype=np.uint8)
    dump(stl_output_dir(), fname, labels)

  for fname in ["train_X.bin", "test_X.bin", "unlabeled_X.bin"]:
    images = np.random.randint(
        256, size=(1, HEIGHT * WIDTH * 3), dtype=np.uint8)
    dump(stl_output_dir(), fname, images)
  label_names = [
      "airplane", "bird", "car", "cat", "deer", "dog", "horse", "monkey",
      "ship", "truck"
  ]
  with open(os.path.join(output_dir, "class_names.txt"), "w") as f:
    f.write("\n".join(label_names))


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate_stl10_data()


if __name__ == "__main__":
  app.run(main)

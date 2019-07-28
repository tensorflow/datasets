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

r"""Generate Fruits360-like files, smaller and with random data.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
from PIL import Image
from absl import app
from absl import flags

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.image.fruits360 import _CLASS_NAMES, _COMMIT_SHA
from tensorflow_datasets.testing import test_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(), "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def _generate():
  """Generates a fake dataset and writes it to the fake_examples directory."""
  commit_dir = 'Fruit-Images-Dataset-{}'.format(_COMMIT_SHA)
  output_dir = os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "fruits360", commit_dir)
  test_utils.remake_dir(output_dir)

  rs = np.random.RandomState(42)

  for split in ("Training", "Test"):
    for class_name in rs.choice(_CLASS_NAMES, 2, replace=False).tolist():
      class_directory = os.path.join(output_dir, split, class_name)
      test_utils.remake_dir(class_directory)

      for prefix in ('', 'r_', 'r2_'):
        img_index = rs.randint(0, 100)
        filename = '{prefix}{img_index}_100.jpg'.format(prefix=prefix, img_index=img_index)

        filepath = os.path.join(class_directory, filename)
        img = rs.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        Image.fromarray(img).save(filepath)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  _generate()


if __name__ == "__main__":
  app.run(main)

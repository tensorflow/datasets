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

r"""Generate FlyingChairs .ppm  and .flo files"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from random import shuffle

from absl import app
from absl import flags
import numpy as np

import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.image import FlyingChairs
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.testing.fake_data_utils import get_random_picture

HEIGHT, WIDTH, CHANNELS = (384, 512, 3)
NUMBER_TRAIN = 3
NUMBER_VALIDATION = 2

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def flying_chairs_output_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples",
                      "flying_chairs")


def _generate_flying_chairs_data(number, data_dir):
  """Writes two .PPM images and .FLO flow"""

  number = str(number).zfill(5)
  for fname in ["%s_img%s.ppm" % (number, i) for i in (1, 2)]:
    fake_im = get_random_picture(HEIGHT, WIDTH, CHANNELS)
    with open(os.path.join(data_dir, fname), 'wb') as f:
      tfds.core.lazy_imports.PIL_Image.fromarray(fake_im).save(f, 'ppm')

  fake_flo = get_random_picture(HEIGHT, WIDTH, 2)  # 2D planar flow
  with open(os.path.join(data_dir, "%s_flow.flo" % number), 'wb') as f:
    f.write('PIEH'.encode('utf-8'))
    np.array(fake_flo.shape, dtype=np.int32).tofile(f)  # write dims
    fake_flo = fake_flo.astype(np.float32)
    fake_flo.tofile(f)

def _generate_flying_chairs_fake_data():
  """Generates fake training and validation data"""

  output_dir = flying_chairs_output_dir()
  test_utils.remake_dir(output_dir)
  data_dir = os.path.join(flying_chairs_output_dir(),
                          "zip", "FlyingChairs_release", "data")
  test_utils.remake_dir(data_dir)

  # list with train and validation randomly sorted
  tags = [str(FlyingChairs.SPLIT_TAG_TRAIN)] * NUMBER_TRAIN \
         + [str(FlyingChairs.SPLIT_TAG_VALIDATION)] * NUMBER_VALIDATION
  shuffle(tags)

  for number in range(1, len(tags) + 1):
    _generate_flying_chairs_data(number, data_dir)

  # write split tags into split file
  with open(os.path.join(output_dir, "FlyingChairs_train_val.txt"), "w") as f:
    f.write("\n".join(tags))


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  _generate_flying_chairs_fake_data()


if __name__ == "__main__":
  app.run(main)

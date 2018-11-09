# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

r"""Generate cifar10 like files, smaller and with random data.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pickle

from absl import app
from absl import flags
import numpy as np

NUMBER_IMAGES_PER_BATCH = 2
HEIGHT, WIDTH = (32, 32)
NUMBER_BATCHES = 5
NUMBER_LABELS = 10

flags.DEFINE_string("output_dir", None,
                    "Path to directory where to generate data.")

FLAGS = flags.FLAGS


def dump(fname, **data):
  path = os.path.join(FLAGS.output_dir, fname)
  print("Writing %s..." % path)
  with open(path, "wb") as out_file:
    pickle.dump(data, out_file)


def generate_batch(batch_name):
  data = np.random.randint(
      256, size=(NUMBER_IMAGES_PER_BATCH, HEIGHT * WIDTH * 3), dtype=np.uint8)
  labels = np.random.randint(NUMBER_LABELS, size=(NUMBER_IMAGES_PER_BATCH),
                             dtype=np.uint8)
  dump(batch_name, data=data, labels=labels)


def generate_data():
  for batch_number in range(1, NUMBER_BATCHES+1):
    generate_batch("data_batch_%s" % batch_number)
  generate_batch("test_batch")
  label_names = ["label%s" % i for i in range(NUMBER_LABELS)]
  dump("batches.meta", labels_names=label_names)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")
  generate_data()


if __name__ == "__main__":
  app.run(main)

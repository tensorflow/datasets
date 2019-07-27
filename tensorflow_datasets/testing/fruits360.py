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

from absl import app
from absl import flags
import h5py
import numpy as np

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.image.fruits360 import _CLASS_NAMES

NUM_IMAGES = 95
OUTPUT_NAME = 'fruits360.h5'

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(), "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS


def _create_fake_samples():
    """Creates a set of fake examples.

    :return: tuple with fake images and fake labels
    """
    rs = np.random.RandomState(0)
    images = rs.randint(256, size=(NUM_IMAGES, 100, 100, 3)).astype(np.uint8)
    labels = np.arange(NUM_IMAGES).astype(np.int) % len(_CLASS_NAMES)
    return images, labels


def _generate():
    """Generates a fake dataset and writes it to the fake_examples directory."""
    output_dir = os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "fruits360")
    test_utils.remake_dir(output_dir)

    images, labels = _create_fake_samples()

    with h5py.File(os.path.join(output_dir, OUTPUT_NAME), 'w') as f:
        f.create_dataset("images", data=images)
        f.create_dataset("labels", data=labels)


def main(argv):
    if len(argv) > 1:
        raise app.UsageError("Too many command-line arguments.")
    _generate()


if __name__ == "__main__":
    app.run(main)

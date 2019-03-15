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

r"""Generate PatchCAMELYON-like files, smaller and with random data.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags
import numpy as np
import tensorflow_datasets as tfds

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import test_utils

flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

_PCAM_TRAIN_DATA_FILENAME = "camelyonpatch_train_x.h5"
_PCAM_TRAIN_LABELS_FILENAME = "camelyonpatch_train_y.h5"
_PCAM_VALID_DATA_FILENAME = "camelyonpatch_valid_x.h5"
_PCAM_VALID_LABELS_FILENAME = "camelyonpatch_valid_y.h5"
_PCAM_TEST_DATA_FILENAME = "camelyonpatch_test_x.h5"
_PCAM_TEST_LABELS_FILENAME = "camelyonpatch_test_y.h5"


def make_images(num_images):
    return np.random.randint(256, size=(num_images, 96, 96, 3), dtype=np.uint8)


def make_labels(num_labels):
    return np.random.randint(2, size=num_labels, dtype=np.uint8)


def write_image_file(filename, num_images):
    with tfds.core.lazy_imports.h5py.File(filename, "w") as f:
        f.create_dataset("x", data=make_images(num_images))


def write_label_file(filename, num_labels):
    with tfds.core.lazy_imports.h5py.File(filename, "w") as f:
        f.create_dataset("y", data=make_labels(num_labels))


def main(_):
    output_dir = os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples", "patch_camelyon")
    test_utils.remake_dir(output_dir)
    write_image_file(os.path.join(output_dir, _PCAM_TRAIN_DATA_FILENAME), 32)
    write_label_file(os.path.join(output_dir, _PCAM_TRAIN_LABELS_FILENAME), 32)
    write_image_file(os.path.join(output_dir, _PCAM_VALID_DATA_FILENAME), 4)
    write_label_file(os.path.join(output_dir, _PCAM_VALID_LABELS_FILENAME), 4)
    write_image_file(os.path.join(output_dir, _PCAM_TEST_DATA_FILENAME), 4)
    write_label_file(os.path.join(output_dir, _PCAM_TEST_LABELS_FILENAME), 4)


if __name__ == "__main__":
    app.run(main)

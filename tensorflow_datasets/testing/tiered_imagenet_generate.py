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

from absl import app
from absl import flags

import numpy as np
import os
import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils
import tensorflow_datasets.public_api as tfds
flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS
pickle = tfds.core.lazy_imports.pickle

_NUM_CATEGORIES_TRAIN = 5  # Original size in dataset is 20
_NUM_CATEGORIES_VAL = 2  # Original size in dataset is 6
_NUM_CATEGORIES_TEST = 2  # Original size in dataset is 8

_NUM_CLASSES_TRAIN = 10  # Original size in dataset is 351
_NUM_CLASSES_VAL = 3  # Original size in dataset is 97
_NUM_CLASSES_TEST = 4  # Original size in dataset is 160
_NUM_IMAGES_TRAIN = 20  # Original size in dataset is 448695
_NUM_IMAGES_VAL = 6  # Original size in dataset is 124261
_NUM_IMAGES_TEST = 10  # Original size in dataset is 206209
_PATH_DUMMY_DATA = "tensorflow_datasets/testing/test_data/fake_examples/tiered_imagenet"


def generate_train_data(path):
    """Generates dummy train, validation and test images file and corresponding labels file   .
    """
    if not tf.io.gfile.exists(path):
        tf.gfile.MakeDirs(path)
    # generate dummy train data
    train_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_TRAIN, 84, 84, 3), np.uint8)
    train_specific_labels = [str(i) for i in range(_NUM_CLASSES_TRAIN)]
    train_general_labels = [str(i) for i in range(_NUM_CATEGORIES_TRAIN)]
    train_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_TRAIN)]
    train_general_labels_str = [str(i) for i in range(_NUM_CATEGORIES_TRAIN)]
    train_images = {"images": train_images_data}
    train_labels = {"label_general": train_general_labels, "label_general_str": train_general_labels_str,
                    "label_specific": train_specific_labels, "label_specific_str": train_specific_labels_str}
    # save train images
    path_train = os.path.join(path, "train_images_png.pkl")
    with tf.io.gfile.GFile(path_train, "wb") as f:
        pickle.dump(train_images, f, pickle.HIGHEST_PROTOCOL)
    # save train labels
    path_train = os.path.join(path, "train_labels.pkl")
    with tf.io.gfile.GFile(path_train, "wb") as f:
        pickle.dump(train_labels, f, pickle.HIGHEST_PROTOCOL)


def generate_validation_data(path):
    """Generates dummy  validation  images file and corresponding labels file   .
    """
    # generate dummy validation data
    validation_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_VAL, 84, 84, 3), np.uint8)
    validation_specific_labels = [str(i) for i in range(_NUM_CLASSES_VAL)]
    validation_general_labels = [str(i) for i in range(_NUM_CATEGORIES_VAL)]
    validation_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_VAL)]
    validation_general_labels_str = [str(i)
                                     for i in range(_NUM_CATEGORIES_VAL)]
    val_images = {"images": validation_images_data}
    val_labels = {"label_general": validation_general_labels, "label_general_str": validation_general_labels_str,
                  "label_specific": validation_specific_labels, "label_specific_str": validation_specific_labels_str}

    # save validation images
    path_validation = os.path.join(path, "val_images_png.pkl")
    with tf.io.gfile.GFile(path_validation, "wb") as f:
        pickle.dump(val_images, f, pickle.HIGHEST_PROTOCOL)
    # save validation labels
    path_validation = os.path.join(path, "val_labels.pkl")
    with tf.io.gfile.GFile(path_validation, "wb") as f:
        pickle.dump(val_labels, f, pickle.HIGHEST_PROTOCOL)


def generate_test_data(path):
    """Generates dummy test images file and corresponding labels file   .
    """
    # generate dummy test data
    test_images_data = np.random.randint(
        0, 255, (_NUM_IMAGES_TEST, 84, 84, 3), np.uint8)
    test_specific_labels = [str(i) for i in range(_NUM_CLASSES_TEST)]
    test_general_labels = [str(i) for i in range(_NUM_CATEGORIES_TEST)]
    test_specific_labels_str = [str(i) for i in range(_NUM_CLASSES_TEST)]
    test_general_labels_str = [str(i) for i in range(_NUM_CATEGORIES_TEST)]
    test_images = {"images": test_images_data}
    test_labels = {"label_general": test_general_labels, "label_general_str": test_general_labels_str,
                   "label_specific": test_specific_labels, "label_specific_str": test_specific_labels_str}
    # save test images
    path_test = os.path.join(path, "test_images_png.pkl")
    with tf.io.gfile.GFile(path_test, "wb") as f:
        pickle.dump(test_images, f, pickle.HIGHEST_PROTOCOL)
    # save test labels
    path_test = os.path.join(path, "test_labels.pkl")
    with tf.io.gfile.GFile(path_test, "wb") as f:
        pickle.dump(test_labels, f, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    if not os.path.exists(_PATH_DUMMY_DATA):
        os.makedirs(_PATH_DUMMY_DATA)
    generate_train_data(_PATH_DUMMY_DATA)
    generate_test_data(_PATH_DUMMY_DATA)
    generate_validation_data(_PATH_DUMMY_DATA)

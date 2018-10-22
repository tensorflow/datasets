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

"""MNIST and Fashion MNIST."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import random

import numpy as np
import six.moves.urllib as urllib
import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.image import image_utils

# MNIST constants
_MNIST_URL = "http://yann.lecun.com/exdb/mnist/"
_MNIST_TRAIN_DATA_FILENAME = "train-images-idx3-ubyte.gz"
_MNIST_TRAIN_LABELS_FILENAME = "train-labels-idx1-ubyte.gz"
_MNIST_TEST_DATA_FILENAME = "t10k-images-idx3-ubyte.gz"
_MNIST_TEST_LABELS_FILENAME = "t10k-labels-idx1-ubyte.gz"
_MNIST_IMAGE_SIZE = 28
_TRAIN_EXAMPLES = 60000
_TEST_EXAMPLES = 10000

# URL for Fashion MNIST data.
_FASHION_MNIST_URL = ("http://fashion-mnist.s3-website.eu-central-1"
                      ".amazonaws.com/")


class MNIST(dataset_builder.GeneratorBasedDatasetBuilder):
  """MNIST."""
  URL = _MNIST_URL

  def _dataset_split_generators(self, dl_manager):

    # Download the full MNist Database
    filenames = {
        "train_data": _MNIST_TRAIN_DATA_FILENAME,
        "train_labels": _MNIST_TRAIN_LABELS_FILENAME,
        "test_data": _MNIST_TEST_DATA_FILENAME,
        "test_labels": _MNIST_TEST_LABELS_FILENAME,
    }
    mnist_files = dl_manager.download_and_extract({
        k: urllib.parse.urljoin(self.URL, v) for k, v in filenames.items()
    })

    # MNIST provides TRAIN and TEST splits, not a VALIDATION split, so we only
    # write the TRAIN and TEST splits to disk.
    train_gen = functools.partial(
        _generate_mnist_examples,
        nb_examples=_TRAIN_EXAMPLES,
        data_path=mnist_files["train_data"],
        label_path=mnist_files["train_labels"],
    )
    test_gen = functools.partial(
        _generate_mnist_examples,
        nb_examples=_TEST_EXAMPLES,
        data_path=mnist_files["test_data"],
        label_path=mnist_files["test_labels"],
    )
    train_splits = [
        self._split_files(split=dataset_builder.Split.TRAIN, num_shards=10)
    ]
    test_splits = [
        self._split_files(split=dataset_builder.Split.TEST, num_shards=1)
    ]
    return [
        dataset_builder.SplitGenerator(generator_fn=train_gen,
                                       split_files=train_splits),
        dataset_builder.SplitGenerator(generator_fn=test_gen,
                                       split_files=test_splits),
    ]

  @property
  def _file_format_adapter(self):
    example_spec = {
        "input/encoded": tf.FixedLenFeature(tuple(), tf.string),
        "target": tf.FixedLenFeature(tuple(), tf.int64),
    }
    return file_format_adapter.TFRecordExampleAdapter(example_spec)

  def _preprocess(self, record):
    record["input"] = image_utils.decode_png(
        record.pop("input/encoded"),
        [_MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1])
    return record


def _generate_mnist_examples(nb_examples, data_path, label_path):
  """Generate MNIST examples as dicts.

  Args:
    nb_examples (int): The number of example.
    data_path (str): Path to the data files
    label_path (str): Path to the labels

  Returns:
    Generator yielding:
      Feature dictionaries `dict<str feature_name, feature_value>` containing:
        * `image/encoded`: png-encoded image
        * `image/shape`: image shape
        * `image/format`: "png"
        * `target`: label
  """
  images = _extract_mnist_images(data_path, nb_examples)
  labels = _extract_mnist_labels(label_path, nb_examples)
  # Shuffle the data to make sure classes are well distributed.
  data = list(zip(images, labels))
  random.shuffle(data)

  return image_utils.image_classification_generator(data)


class FashionMNIST(MNIST):
  URL = _FASHION_MNIST_URL


def _extract_mnist_images(image_filepath, num_images):
  with tf.gfile.Open(image_filepath, "rb") as f:
    f.read(16)  # header
    buf = f.read(_MNIST_IMAGE_SIZE * _MNIST_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf, dtype=np.uint8).reshape(num_images, _MNIST_IMAGE_SIZE,
                                     _MNIST_IMAGE_SIZE, 1)
    return data


def _extract_mnist_labels(labels_filepath, num_labels):
  with tf.gfile.Open(labels_filepath, "rb") as f:
    f.read(8)  # header
    buf = f.read(num_labels)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels

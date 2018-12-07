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

import random

import numpy as np
import six.moves.urllib as urllib
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

# MNIST constants
_MNIST_URL = "http://yann.lecun.com/exdb/mnist/"
_MNIST_TRAIN_DATA_FILENAME = "train-images-idx3-ubyte.gz"
_MNIST_TRAIN_LABELS_FILENAME = "train-labels-idx1-ubyte.gz"
_MNIST_TEST_DATA_FILENAME = "t10k-images-idx3-ubyte.gz"
_MNIST_TEST_LABELS_FILENAME = "t10k-labels-idx1-ubyte.gz"
_MNIST_IMAGE_SIZE = 28
_MNIST_IMAGE_SHAPE = (_MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
_TRAIN_EXAMPLES = 60000
_TEST_EXAMPLES = 10000


class MNIST(tfds.core.GeneratorBasedBuilder):
  """MNIST."""
  URL = _MNIST_URL

  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description=("The MNIST database of handwritten digits."),
        version="1.0.0",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_MNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        urls=[self.URL],
        download_checksums=tfds.download.load_checksums(self.name),
        size_in_bytes=11.0 * tfds.units.MiB,
        citation="Y. Lecun and C. Cortes, \"The MNIST database of handwritten "
                 "digits,\" 1998.\n[Online]. Available: "
                 "http://yann.lecun.com/exdb/mnist/",
    )

  def _split_generators(self, dl_manager):

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
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(
                num_examples=_TRAIN_EXAMPLES,
                data_path=mnist_files["train_data"],
                label_path=mnist_files["train_labels"],
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(
                num_examples=_TEST_EXAMPLES,
                data_path=mnist_files["test_data"],
                label_path=mnist_files["test_labels"],
            )),
    ]

  def _generate_examples(self, num_examples, data_path, label_path):
    """Generate MNIST examples as dicts.

    Args:
      num_examples (int): The number of example.
      data_path (str): Path to the data files
      label_path (str): Path to the labels

    Yields:
      Generator yielding the next examples
    """
    images = _extract_mnist_images(data_path, num_examples)
    labels = _extract_mnist_labels(label_path, num_examples)
    # Shuffle the data to make sure classes are well distributed.
    data = list(zip(images, labels))
    random.shuffle(data)

    for image, label in data:
      yield self.info.features.encode_example({
          "image": image,
          "label": label,
      })


class FashionMNIST(MNIST):
  URL = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"

  # TODO(afrozm): Try to inherit from MNIST's _info and mutate things as needed.
  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description=("Fashion-MNIST is a dataset of Zalando's article images "
                     "consisting of a training set of 60,000 examples and a "
                     "test set of 10,000 examples. Each example is a 28x28 "
                     "grayscale image, associated with a label from 10 "
                     "classes."),
        version="1.0.0",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_MNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        urls=["https://github.com/zalandoresearch/fashion-mnist"],
        size_in_bytes=29.4 * tfds.units.MiB,
        citation="Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine"
                 " Learning Algorithms. Han Xiao, Kashif Rasul, Roland "
                 "Vollgraf. arXiv:1708.07747"
    )


def _extract_mnist_images(image_filepath, num_images):
  with tf.gfile.Open(image_filepath, "rb") as f:
    f.read(16)  # header
    buf = f.read(_MNIST_IMAGE_SIZE * _MNIST_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf,
        dtype=np.uint8,
    ).reshape(num_images, _MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
    return data


def _extract_mnist_labels(labels_filepath, num_labels):
  with tf.gfile.Open(labels_filepath, "rb") as f:
    f.read(8)  # header
    buf = f.read(num_labels)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels

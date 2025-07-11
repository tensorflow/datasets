# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""BinarizedMNIST."""

import numpy as np
from six.moves import urllib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.image_classification import mnist
import tensorflow_datasets.public_api as tfds

_URL = "http://www.cs.toronto.edu/~larocheh/public/datasets/binarized_mnist/"
_TRAIN_DATA_FILENAME = "binarized_mnist_train.amat"
_VALID_DATA_FILENAME = "binarized_mnist_valid.amat"
_TEST_DATA_FILENAME = "binarized_mnist_test.amat"


class Builder(tfds.core.GeneratorBasedBuilder):
  """A specific binarization of the MNIST dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial Release",
  }

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {"image": tfds.features.Image(shape=mnist.MNIST_IMAGE_SHAPE)}
        ),
        homepage="http://www.dmi.usherb.ca/~larocheh/mlpython/_modules/datasets/binarized_mnist.html",
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    filenames = {
        "train_data": _TRAIN_DATA_FILENAME,
        "validation_data": _VALID_DATA_FILENAME,
        "test_data": _TEST_DATA_FILENAME,
    }
    files = dl_manager.download(
        {k: urllib.parse.urljoin(_URL, v) for k, v in filenames.items()}
    )

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                data_path=files["train_data"],
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(
                data_path=files["validation_data"],
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                data_path=files["test_data"],
            ),
        ),
    ]

  def _generate_examples(self, data_path):
    """Generate Binarized MNIST examples as dicts.

    Args:
      data_path (str): Path to the data files

    Yields:
      Generator yielding the next examples
    """
    with tf.io.gfile.GFile(data_path, "rb") as f:
      images = (
          np.loadtxt(f, delimiter=" ")
          .astype(np.uint8)
          .reshape((-1,) + mnist.MNIST_IMAGE_SHAPE)
      )
    for index, image in enumerate(images):
      yield index, {"image": image}

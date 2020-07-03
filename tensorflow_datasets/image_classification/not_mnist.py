# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""notMNIST dataset.

notMNIST is a dataset curated by Yaroslav Bulatov by taking publicly
available fonts and extracting glyphs from them to create a dataset similar
to MNIST. The 28x28 pixel images comprise of 10 classes with letters A-J.
1 training example was discarded from the pool of 529115 training examples
because its PNG header was corrupted.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import mnist

_CITATION = """
@article{bulatov2011notmnist,
  title={Notmnist dataset},
  author={Bulatov, Yaroslav},
  journal={Google (Books/OCR), Tech. Rep.[Online]. 
    Available: http://yaroslavvb. blogspot. it/2011/09/notmnist-dataset. html},
  volume={2},
  year={2011}
}
"""

_DESCRIPTION = """
notMNIST is a dataset curated by Yaroslav Bulatov by taking publicly
available fonts and extracting glyphs from them to create a dataset similar
to MNIST. The 28x28 pixel images comprise of 10 classes with letters A-J.
1 training example was discarded from the pool of 529115 training examples
because its PNG header was corrupted.
"""

_TRAIN_DATA_URL = 'http://yaroslavvb.com/upload/notMNIST/notMNIST_large.tar.gz'
_TEST_DATA_URL = 'http://yaroslavvb.com/upload/notMNIST/notMNIST_small.tar.gz'

_TRAIN_DATA_DIR = 'notMNIST_large'
_TEST_DATA_DIR = 'notMNIST_small'

_IMAGE_SHAPE = 28
_ASCII_OFFSET = 65

_CORRUPTED_DIR = 'A'
_CORRUPTED_FILE = 'RnJlaWdodERpc3BCb29rLnR0Zg==.png'


class NotMnist(tfds.core.GeneratorBasedBuilder):
  """notMNIST dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    """Returns basic information about the dataset.

    Returns:
      tfds.core.DatasetInfo.
    """
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "name": tfds.features.Text(),
            "image": tfds.features.Image(shape=mnist.MNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(
                num_classes=mnist.MNIST_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage=
        "http://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Return the train, test split of notMNIST.

    Args:
      dl_manager: download manager object.

    Returns:
      train split, test split.
    """
    # Download the full notMNIST database
    urls = {
        "train_data": _TRAIN_DATA_URL,
        "test_data": _TEST_DATA_URL,
    }
    files = dl_manager.download_and_extract(urls)
    # notMNIST provides TRAIN and TEST splits, not a VALIDATION
    # split, so we only write the TRAIN and TEST splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                data_path=
                os.path.join(files["train_data"], _TRAIN_DATA_DIR),
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                data_path=os.path.join(files["test_data"], _TEST_DATA_DIR),
            )),
    ]

  def _generate_examples(self, data_path):
    """Generate the notMNIST data.

    Args:
        data_path: path to the location of extracted dataset.

    Returns:
        record with image along with its associated label.
    """
    for label in range(mnist.MNIST_NUM_CLASSES):
      label_char = chr(label + _ASCII_OFFSET)
      label_dir = os.path.join(data_path, label_char)
      images = list(tf.io.gfile.glob(label_dir + "*.png"))
      corrupted_image = os.path.join(
          data_path, _CORRUPTED_DIR, _CORRUPTED_FILE)
      # Discard the 1 training example with the corrupted PNG header
      if corrupted_image in images:
        images.remove(corrupted_image)
      for image in images:
        data = tf.io.gfile.GFile(image, "rb")
        record = {
            "name": label_char,
            "image": data,
            "label": label,
        }
        yield image, record

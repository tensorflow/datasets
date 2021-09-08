# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""MNIST, Fashion MNIST, KMNIST and EMNIST."""

import os
import numpy as np
from six.moves import urllib
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

# MNIST constants
# CVDF mirror of http://yann.lecun.com/exdb/mnist/
_MNIST_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"
_MNIST_TRAIN_DATA_FILENAME = "train-images-idx3-ubyte.gz"
_MNIST_TRAIN_LABELS_FILENAME = "train-labels-idx1-ubyte.gz"
_MNIST_TEST_DATA_FILENAME = "t10k-images-idx3-ubyte.gz"
_MNIST_TEST_LABELS_FILENAME = "t10k-labels-idx1-ubyte.gz"
_MNIST_IMAGE_SIZE = 28
MNIST_IMAGE_SHAPE = (_MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
MNIST_NUM_CLASSES = 10
_TRAIN_EXAMPLES = 60000
_TEST_EXAMPLES = 10000

_MNIST_CITATION = """\
@article{lecun2010mnist,
  title={MNIST handwritten digit database},
  author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
  journal={ATT Labs [Online]. Available: http://yann.lecun.com/exdb/mnist},
  volume={2},
  year={2010}
}
"""

_FASHION_MNIST_CITATION = """\
@article{DBLP:journals/corr/abs-1708-07747,
  author    = {Han Xiao and
               Kashif Rasul and
               Roland Vollgraf},
  title     = {Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning
               Algorithms},
  journal   = {CoRR},
  volume    = {abs/1708.07747},
  year      = {2017},
  url       = {http://arxiv.org/abs/1708.07747},
  archivePrefix = {arXiv},
  eprint    = {1708.07747},
  timestamp = {Mon, 13 Aug 2018 16:47:27 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1708-07747},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_K_MNIST_CITATION = """\
  @online{clanuwat2018deep,
  author       = {Tarin Clanuwat and Mikel Bober-Irizar and Asanobu Kitamoto and Alex Lamb and Kazuaki Yamamoto and David Ha},
  title        = {Deep Learning for Classical Japanese Literature},
  date         = {2018-12-03},
  year         = {2018},
  eprintclass  = {cs.CV},
  eprinttype   = {arXiv},
  eprint       = {cs.CV/1812.01718},
}
"""

_EMNIST_CITATION = """\
@article{cohen_afshar_tapson_schaik_2017,
    title={EMNIST: Extending MNIST to handwritten letters},
    DOI={10.1109/ijcnn.2017.7966217},
    journal={2017 International Joint Conference on Neural Networks (IJCNN)},
    author={Cohen, Gregory and Afshar, Saeed and Tapson, Jonathan and Schaik, Andre Van},
    year={2017}
}
"""


class MNIST(tfds.core.GeneratorBasedBuilder):
  """MNIST."""
  URL = _MNIST_URL

  VERSION = tfds.core.Version("3.0.1")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("The MNIST database of handwritten digits."),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=MNIST_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=MNIST_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage="http://yann.lecun.com/exdb/mnist/",
        citation=_MNIST_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download the full MNIST Database
    filenames = {
        "train_data": _MNIST_TRAIN_DATA_FILENAME,
        "train_labels": _MNIST_TRAIN_LABELS_FILENAME,
        "test_data": _MNIST_TEST_DATA_FILENAME,
        "test_labels": _MNIST_TEST_LABELS_FILENAME,
    }
    mnist_files = dl_manager.download_and_extract(
        {k: urllib.parse.urljoin(self.URL, v) for k, v in filenames.items()})

    # MNIST provides TRAIN and TEST splits, not a VALIDATION split, so we only
    # write the TRAIN and TEST splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                num_examples=_TRAIN_EXAMPLES,
                data_path=mnist_files["train_data"],
                label_path=mnist_files["train_labels"],
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
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
    data = list(zip(images, labels))

    # Using index as key since data is always loaded in same order.
    for index, (image, label) in enumerate(data):
      record = {"image": image, "label": label}
      yield index, record


class FashionMNIST(MNIST):
  URL = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"

  # TODO(afrozm): Try to inherit from MNIST's _info and mutate things as needed.
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Fashion-MNIST is a dataset of Zalando's article images "
                     "consisting of a training set of 60,000 examples and a "
                     "test set of 10,000 examples. Each example is a 28x28 "
                     "grayscale image, associated with a label from 10 "
                     "classes."),
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(shape=MNIST_IMAGE_SHAPE),
            "label":
                tfds.features.ClassLabel(names=[
                    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
                ]),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/zalandoresearch/fashion-mnist",
        citation=_FASHION_MNIST_CITATION,
    )


class KMNIST(MNIST):
  URL = "http://codh.rois.ac.jp/kmnist/dataset/kmnist/"

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Kuzushiji-MNIST is a drop-in replacement for the MNIST "
                     "dataset (28x28 grayscale, 70,000 images), provided in "
                     "the original MNIST format as well as a NumPy format. "
                     "Since MNIST restricts us to 10 classes, we chose one "
                     "character to represent each of the 10 rows of Hiragana "
                     "when creating Kuzushiji-MNIST."),
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(shape=MNIST_IMAGE_SHAPE),
            "label":
                tfds.features.ClassLabel(names=[
                    "o", "ki", "su", "tsu", "na", "ha", "ma", "ya", "re", "wo"
                ]),
        }),
        supervised_keys=("image", "label"),
        homepage="http://codh.rois.ac.jp/kmnist/index.html.en",
        citation=_K_MNIST_CITATION,
    )


class EMNISTConfig(tfds.core.BuilderConfig):
  """BuilderConfig for EMNIST CONFIG."""

  def __init__(self, *, class_number, train_examples, test_examples, **kwargs):
    """BuilderConfig for EMNIST class number.

    Args:
      class_number: There are six different splits provided in this dataset. And
        have different class numbers.
      train_examples: number of train examples
      test_examples: number of test examples
      **kwargs: keyword arguments forwarded to super.
    """
    super(EMNISTConfig, self).__init__(**kwargs)
    self.class_number = class_number
    self.train_examples = train_examples
    self.test_examples = test_examples


class EMNIST(MNIST):
  """Emnist dataset."""
  URL = "https://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/gzip.zip"
  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }
  BUILDER_CONFIGS = [
      EMNISTConfig(
          name="byclass",
          class_number=62,
          train_examples=697932,
          test_examples=116323,
          description="EMNIST ByClass",
      ),
      EMNISTConfig(
          name="bymerge",
          class_number=47,
          train_examples=697932,
          test_examples=116323,
          description="EMNIST ByMerge",
      ),
      EMNISTConfig(
          name="balanced",
          class_number=47,
          train_examples=112800,
          test_examples=18800,
          description="EMNIST Balanced",
      ),
      EMNISTConfig(
          name="letters",
          class_number=37,
          train_examples=88800,
          test_examples=14800,
          description="EMNIST Letters",
      ),
      EMNISTConfig(
          name="digits",
          class_number=10,
          train_examples=240000,
          test_examples=40000,
          description="EMNIST Digits",
      ),
      EMNISTConfig(
          name="mnist",
          class_number=10,
          train_examples=60000,
          test_examples=10000,
          description="EMNIST MNIST",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(
            "The EMNIST dataset is a set of handwritten character digits "
            "derived from the NIST Special Database 19 and converted to "
            "a 28x28 pixel image format and dataset structure that directly "
            "matches the MNIST dataset.\n\n"
            "Note: Like the original EMNIST data, images provided here are "
            "inverted horizontally and rotated 90 anti-clockwise. You can use "
            "`tf.transpose` within `ds.map` to convert the images to a "
            "human-friendlier format."),
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(shape=MNIST_IMAGE_SHAPE),
            "label":
                tfds.features.ClassLabel(
                    num_classes=self.builder_config.class_number),
        }),
        supervised_keys=("image", "label"),
        homepage=("https://www.nist.gov/itl/products-and-services/"
                  "emnist-dataset"),
        citation=_EMNIST_CITATION,
    )

  def _split_generators(self, dl_manager):
    filenames = {
        "train_data":
            "emnist-{}-train-images-idx3-ubyte.gz".format(
                self.builder_config.name),
        "train_labels":
            "emnist-{}-train-labels-idx1-ubyte.gz".format(
                self.builder_config.name),
        "test_data":
            "emnist-{}-test-images-idx3-ubyte.gz".format(
                self.builder_config.name),
        "test_labels":
            "emnist-{}-test-labels-idx1-ubyte.gz".format(
                self.builder_config.name),
    }

    dir_name = os.path.join(dl_manager.download_and_extract(self.URL), "gzip")
    extracted = dl_manager.extract(
        {k: os.path.join(dir_name, fname) for k, fname in filenames.items()})

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                num_examples=self.builder_config.train_examples,
                data_path=extracted["train_data"],
                label_path=extracted["train_labels"],
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                num_examples=self.builder_config.test_examples,
                data_path=extracted["test_data"],
                label_path=extracted["test_labels"],
            ))
    ]


def _extract_mnist_images(image_filepath, num_images):
  with tf.io.gfile.GFile(image_filepath, "rb") as f:
    f.read(16)  # header
    buf = f.read(_MNIST_IMAGE_SIZE * _MNIST_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf,
        dtype=np.uint8,
    ).reshape(num_images, _MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
    return data


def _extract_mnist_labels(labels_filepath, num_labels):
  with tf.io.gfile.GFile(labels_filepath, "rb") as f:
    f.read(8)  # header
    buf = f.read(num_labels)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels

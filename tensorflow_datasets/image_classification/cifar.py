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

"""CIFAR datasets."""

import collections
import os

import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

# Shared constants
_CIFAR_IMAGE_SIZE = 32
_CIFAR_IMAGE_SHAPE = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)


_CITATION = """\
@TECHREPORT{Krizhevsky09learningmultiple,
    author = {Alex Krizhevsky},
    title = {Learning multiple layers of features from tiny images},
    institution = {},
    year = {2009}
}
"""


class Cifar10(tfds.core.GeneratorBasedBuilder):
  """CIFAR-10."""

  VERSION = tfds.core.Version("3.0.2")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("The CIFAR-10 dataset consists of 60000 32x32 colour "
                     "images in 10 classes, with 6000 images per class. There "
                     "are 50000 training images and 10000 test images."),
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "image": tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.cs.toronto.edu/~kriz/cifar.html",
        citation=_CITATION,
    )

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url="https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz",
        train_files=[
            "data_batch_1.bin", "data_batch_2.bin", "data_batch_3.bin",
            "data_batch_4.bin", "data_batch_5.bin"
        ],
        test_files=["test_batch.bin"],
        prefix="cifar-10-batches-bin/",
        label_files=["batches.meta.txt"],
        label_keys=["label"],
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info

    cifar_path = os.path.join(cifar_path, cifar_info.prefix)

    # Load the label names
    for label_key, label_file in zip(cifar_info.label_keys,
                                     cifar_info.label_files):
      labels_path = os.path.join(cifar_path, label_file)
      with tf.io.gfile.GFile(labels_path) as label_f:
        label_names = [name for name in label_f.read().split("\n") if name]
      self.info.features[label_key].names = label_names

    # Define the splits
    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(cifar_path, f)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "split_prefix": "train_",
                "filepaths": gen_filenames(cifar_info.train_files)
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "split_prefix": "test_",
                "filepaths": gen_filenames(cifar_info.test_files)
            }),
    ]

  def _generate_examples(self, split_prefix, filepaths):
    """Generate CIFAR examples as dicts.

    Shared across CIFAR-{10, 100}. Uses self._cifar_info as
    configuration.

    Args:
      split_prefix (str): Prefix that identifies the split (e.g. "tr" or "te").
      filepaths (list[str]): The files to use to generate the data.

    Yields:
      The cifar examples, as defined in the dataset info features.
    """
    label_keys = self._cifar_info.label_keys
    index = 0  # Using index as key since data is always loaded in same order.
    for path in filepaths:
      for labels, np_image in _load_data(path, len(label_keys)):
        record = dict(zip(label_keys, labels))
        # Note: "id" is only provided for the user convenience. To shuffle the
        # dataset we use `index`, so that the sharding is compatible with
        # earlier versions.
        record["id"] = "{}{:05d}".format(split_prefix, index)
        record["image"] = np_image
        yield index, record
        index += 1


class Cifar100(Cifar10):
  """CIFAR-100 dataset."""

  VERSION = tfds.core.Version("3.0.2")

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url="https://www.cs.toronto.edu/~kriz/cifar-100-binary.tar.gz",
        train_files=["train.bin"],
        test_files=["test.bin"],
        prefix="cifar-100-binary/",
        label_files=["coarse_label_names.txt", "fine_label_names.txt"],
        label_keys=["coarse_label", "label"],
    )

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("This dataset is just like the CIFAR-10, except it has "
                     "100 classes containing 600 images each. There are 500 "
                     "training images and 100 testing images per class. The "
                     "100 classes in the CIFAR-100 are grouped into 20 "
                     "superclasses. Each image comes with a \"fine\" label "
                     "(the class to which it belongs) and a \"coarse\" label "
                     "(the superclass to which it belongs)."),
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(),
            "image": tfds.features.Image(shape=_CIFAR_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=100),
            "coarse_label": tfds.features.ClassLabel(num_classes=20),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.cs.toronto.edu/~kriz/cifar.html",
        citation=_CITATION,
    )


class CifarInfo(collections.namedtuple("_CifarInfo", [
    "name",
    "url",
    "prefix",
    "train_files",
    "test_files",
    "label_files",
    "label_keys",
])):
  """Contains the information necessary to generate a CIFAR dataset.

  Attributes:
    name (str): name of dataset.
    url (str): data URL.
    prefix (str): path prefix within the downloaded and extracted file to look
      for `train_files` and `test_files`.
    train_files (list<str>): name of training files within `prefix`.
    test_files (list<str>): name of test files within `prefix`.
    label_files (list<str>): names of the label files in the data.
    label_keys (list<str>): names of the label keys in the data.
  """


def _load_data(path, labels_number=1):
  """Yields (labels, np_image) tuples."""
  with tf.io.gfile.GFile(path, "rb") as f:
    data = f.read()
  offset = 0
  max_offset = len(data) - 1
  while offset < max_offset:
    labels = np.frombuffer(data, dtype=np.uint8, count=labels_number,
                           offset=offset).reshape((labels_number,))
    # 1 byte per label, 1024 * 3 = 3072 bytes for the image.
    offset += labels_number
    img = (np.frombuffer(data, dtype=np.uint8, count=3072, offset=offset)
           .reshape((3, _CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE))
           .transpose((1, 2, 0))
          )
    offset += 3072
    yield labels, img

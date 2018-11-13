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

"""CIFAR datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import random

import numpy as np
import six
from six.moves import cPickle
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# CIFAR-10 constants
_CIFAR10_URL = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
_CIFAR10_PREFIX = "cifar-10-batches-py/"
_CIFAR10_TRAIN_FILES = [
    "data_batch_1", "data_batch_2", "data_batch_3", "data_batch_4",
    "data_batch_5"
]
_CIFAR10_TEST_FILES = ["test_batch"]

# CIFAR-100 constants
_CIFAR100_URL = "https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz"
_CIFAR100_PREFIX = "cifar-100-python/"
_CIFAR100_TRAIN_FILES = ["train"]
_CIFAR100_TEST_FILES = ["test"]

# Shared constants
_CIFAR_IMAGE_SIZE = 32


# TODO(rsepassi): Add tests
class Cifar10(tfds.core.GeneratorBasedDatasetBuilder):
  """CIFAR-10."""

  SIZE = .162  # GB

  def _info(self):
    cifar_shape = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)
    return tfds.core.DatasetInfo(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=cifar_shape),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
    )

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url=_CIFAR10_URL,
        train_files=_CIFAR10_TRAIN_FILES,
        test_files=_CIFAR10_TEST_FILES,
        prefix=_CIFAR10_PREFIX,
        label_keys=["labels"],
    )

  def _split_generators(self, dl_manager):
    cifar_path = dl_manager.download_and_extract(self._cifar_info.url)
    cifar_info = self._cifar_info

    def gen_filenames(filenames):
      for f in filenames:
        yield os.path.join(cifar_path, self._cifar_info.prefix, f)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={"filepaths": gen_filenames(cifar_info.train_files)}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={"filepaths": gen_filenames(cifar_info.test_files)}),
    ]

  def _generate_samples(self, filepaths):
    """Generate CIFAR examples as dicts.

    Shared across CIFAR-{10, 100}. Uses self._cifar_info as
    configuration.

    Args:
      filepaths (list[str]): The files to use to generate the data.

    Yields:
      The cifar samples, as defined in the dataset info features.
    """
    images, labels = [], []
    for path in filepaths:
      with tf.gfile.Open(path, "rb") as f:
        if six.PY2:
          data = cPickle.load(f)
        else:
          data = cPickle.load(f, encoding="latin1")
      batch_images = data["data"]
      num_images = batch_images.shape[0]
      batch_images = batch_images.reshape(
          (num_images, 3, _CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE))
      # Get images into [height, width, channels] format
      images.extend([
          np.squeeze(batch_images[j]).transpose((1, 2, 0))
          for j in range(num_images)
      ])

      # Extract the list[dict[label_key, sample_label]]
      labels.extend([
          {k: data[k][j] for k in self._cifar_info.label_keys}
          for j in range(num_images)
      ])

    # Shuffle the data to make sure classes are well distributed.
    data = list(zip(images, labels))
    random.shuffle(data)

    for image, label in data:
      if len(label) == 1:
        label = label[self._cifar_info.label_keys[0]]
      yield self.info.features.encode_sample({
          "image": image,
          "label": label,
      })


class Cifar100(Cifar10):
  """CIFAR-100 dataset."""

  def __init__(self, use_coarse_labels=False, **kwargs):
    """Constructs Cifar-100 dataset.

    Args:
      use_coarse_labels (bool): whether to set the coarse labels or the fine
        labels as "label". Note that in either case, both features will be
        present in the features dictionary as "fine_label" and "coarse_label".
        Note also that this does NOT affect the data on disk and is only used in
        the `tf.data.Dataset` input pipeline.
      **kwargs: See DatasetBuilder.__init__.
    """
    self._use_coarse_labels = use_coarse_labels
    super(Cifar100, self).__init__(**kwargs)

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url=_CIFAR100_URL,
        train_files=_CIFAR100_TRAIN_FILES,
        test_files=_CIFAR100_TEST_FILES,
        prefix=_CIFAR100_PREFIX,
        label_keys=["fine_labels", "coarse_labels"],
    )

  def _info(self):
    cifar_shape = (_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3)
    label_to_use = "coarse_labels" if self._use_coarse_labels else "fine_labels"
    return tfds.core.DatasetInfo(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=cifar_shape),
            "label": tfds.features.OneOf(choice=label_to_use, feature_dict={
                "coarse_labels": tfds.features.ClassLabel(num_classes=20),
                "fine_labels": tfds.features.ClassLabel(num_classes=100),
            }),
        }),
        supervised_keys=("image", "label"),
    )


class CifarInfo(collections.namedtuple("_CifarInfo", [
    "name",
    "url",
    "prefix",
    "train_files",
    "test_files",
    "label_keys",
])):
  """Contains the information necessary to generate a CIFAR dataset.

  Args:
    name (str): name of dataset.
    url (str): data URL.
    prefix (str): path prefix within the downloaded and extracted file to look
      for `train_files` and `test_files`.
    train_files (list<str>): name of training files within `prefix`.
    test_files (list<str>): name of test files within `prefix`.
    label_keys (list<str>): names of the label keys in the data. If longer than
      1, provide `out_label_keys` to specify output names in feature
      dictionaries.  Otherwise will use "label".
  """

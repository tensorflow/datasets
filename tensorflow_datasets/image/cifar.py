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
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.image import image_utils

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
class Cifar10(dataset_builder.GeneratorBasedDatasetBuilder):
  """CIFAR-10."""

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url=_CIFAR10_URL,
        train_files=_CIFAR10_TRAIN_FILES,
        test_files=_CIFAR10_TEST_FILES,
        prefix=_CIFAR10_PREFIX,
        label_keys=["labels"],
        out_label_keys=None,
    )

  def _dataset_split_generators(self):
    train_gen = lambda: self._generate_cifar_examples(is_training=True)
    test_gen = lambda: self._generate_cifar_examples(is_training=False)
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
        [_CIFAR_IMAGE_SIZE, _CIFAR_IMAGE_SIZE, 3])
    return record

  def _generate_cifar_examples(self, is_training):
    """Generate CIFAR examples as dicts.

    Shared across CIFAR-{10, 100}. Uses self._cifar_info as
    configuration.

    Args:
      is_training (bool): Whether to generate train or test data.

    Yields:
      Feature dictionaries `dict<str feature_name, feature_value>` containing:
        * `image/encoded`: png-encoded image
        * `image/shape`: image shape
        * `image/format`: "png"
        * `target`: label

      If `len(self._cifar_info["label_keys"]) > 1`, then instead of `target` the
      feature dictionary will have all `label_keys` included with keys being
      `self._cifar_info["out_label_keys"]`.
    """
    download_manager = self._download_manager
    cifar_info = self._cifar_info
    downloaded, = download_manager.download([cifar_info.url])
    # TODO(epot): Combine the extractions
    extracted = download_manager.extract(
        downloaded, cifar_info.name + "tar", filetype="gz")
    extracted = download_manager.extract(
        extracted, cifar_info.name, filetype="tar")
    if is_training:
      data_files = cifar_info.train_files
    else:
      data_files = cifar_info.test_files

    label_keys = cifar_info.label_keys
    use_extra_labels = len(label_keys) > 1
    if use_extra_labels:
      assert len(label_keys) == 2

    images, labels = [], []
    extra_labels = []
    for filename in data_files:
      path = os.path.join(extracted, cifar_info.prefix, filename)
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
      batch_labels = data[label_keys[0]]
      labels.extend([batch_labels[j] for j in range(num_images)])
      if use_extra_labels:
        batch_extra_labels = data[label_keys[1]]
        extra_labels.extend([batch_extra_labels[j] for j in range(num_images)])

    # Shuffle the data to make sure classes are well distributed.
    data = [images, labels]
    if use_extra_labels:
      data.append(extra_labels)
    data = list(zip(*data))
    random.shuffle(data)
    if use_extra_labels:
      images, labels, extra_labels = list(zip(*data))
    else:
      images, labels = list(zip(*data))
      extra_labels = None

    example_gen = image_utils.image_classification_generator(
        zip(images, labels))
    for i, feature_dict in enumerate(example_gen):
      if extra_labels:
        feature_dict[cifar_info.out_label_keys[0]] = feature_dict.pop(
            "target")
        feature_dict[cifar_info.out_label_keys[1]] = extra_labels[i]
      yield feature_dict


class Cifar100(Cifar10):
  """CIFAR-100 dataset."""

  def __init__(self, use_coarse_labels=False, **kwargs):
    """Constructs Cifar-100 dataset.

    Args:
      use_coarse_labels (bool): whether to set the coarse labels or the fine
        labels as "target". Note that in either case, both features will be
        present in the features dictionary as "fine_label" and "coarse_label".
        Note also that this does NOT affect the data on disk and is only used in
        the `tf.data.Dataset` input pipeline.
      **kwargs: See DatasetBuilder.__init__.
    """
    super(Cifar100, self).__init__(**kwargs)
    self._use_coarse_labels = use_coarse_labels

  @property
  def _cifar_info(self):
    return CifarInfo(
        name=self.name,
        url=_CIFAR100_URL,
        train_files=_CIFAR100_TRAIN_FILES,
        test_files=_CIFAR100_TEST_FILES,
        prefix=_CIFAR100_PREFIX,
        label_keys=["fine_labels", "coarse_labels"],
        out_label_keys=["fine_label", "coarse_label"],
    )

  @property
  def _file_format_adapter(self):
    example_spec = {
        "input/encoded": tf.FixedLenFeature(tuple(), tf.string),
        "fine_label": tf.FixedLenFeature(tuple(), tf.int64),
        "coarse_label": tf.FixedLenFeature(tuple(), tf.int64),
    }
    return file_format_adapter.TFRecordExampleAdapter(example_spec)

  def _preprocess(self, record):
    record = super(Cifar100, self)._preprocess(record)
    target_key = "coarse_label" if self._use_coarse_labels else "fine_label"
    record["target"] = record[target_key]
    return record


class CifarInfo(collections.namedtuple("_CifarInfo", [
    "name",
    "url",
    "prefix",
    "train_files",
    "test_files",
    "label_keys",
    "out_label_keys",
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
      dictionaries.  Otherwise will use "target".
    out_label_keys (list<str>): if `label_keys` is longer than 1, these specify
      the names of those features in the generated feature dictionary.
  """
  pass

# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Functions to be reused by various imagenet derivatives."""
import os
import tarfile

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_LABELS_FNAME = 'datasets/imagenet2012/labels.txt'

# This file contains the validation labels, in the alphabetic order of
# corresponding image names (and not in the order they have been added to the
# tar file).
_VALIDATION_LABELS_FNAME = 'datasets/imagenet2012/validation_labels.txt'


def label_names_file():
  """Return path to label file."""
  return tfds.core.tfds_path(_LABELS_FNAME)


def get_validation_labels(val_path):
  """Returns labels for validation.

  Args:
    val_path: path to TAR file containing validation images. It is used to
      retrieve the name of pictures and associate them to labels.

  Returns:
    dict, mapping from image name (str) to label (str).
  """
  labels_path = tfds.core.tfds_path(_VALIDATION_LABELS_FNAME)
  with tf.io.gfile.GFile(os.fspath(labels_path)) as labels_f:
    # `splitlines` to remove trailing `\r` in Windows
    labels = labels_f.read().strip().splitlines()
  with tf.io.gfile.GFile(val_path, 'rb') as tar_f_obj:
    tar = tarfile.open(mode='r:', fileobj=tar_f_obj)
    images = sorted(tar.getnames())
  return dict(zip(images, labels))


def generate_examples_validation(archive, labels):
  for fname, fobj in archive:
    record = {
        'file_name': fname,
        'image': fobj,
        'label': labels[fname],
    }
    yield fname, record


def generate_examples_test(archive):
  for fname, fobj in archive:
    record = {
        'file_name': fname,
        'image': fobj,
        'label': -1,
    }
    yield fname, record

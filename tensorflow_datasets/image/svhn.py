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

"""Street View House Numbers (SVHN) Dataset, cropped version.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os  # TODO(b/120826984): Remove  # pylint: disable=unused-import

import numpy as np
import scipy.io
import six.moves.urllib as urllib
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

URL = "http://ufldl.stanford.edu/housenumbers/"


class SvhnCropped(tfds.core.GeneratorBasedBuilder):
  """Street View House Numbers (SVHN) Dataset, cropped version."""

  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description=(
            "The Street View House Numbers (SVHN) Dataset is an image digit "
            "recognition dataset of over 600,000 digit images coming from "
            "real world data. Images are cropped to 32x32."),
        version="1.0.0",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=(32, 32, 3)),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        urls=[URL],
        download_checksums=tfds.download.load_checksums(self.name),
        size_in_bytes=1.5 * tfds.units.GiB,
        citation=(
            "Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, "
            "Andrew Y. Ng, Reading Digits in Natural Images with Unsupervised "
            "Feature Learning, NIPS Workshop on Deep Learning and Unsupervised "
            "Feature Learning, 2011."),
    )

  def _split_generators(self, dl_manager):

    output_files = dl_manager.download({
        "train": urllib.parse.urljoin(URL, "train_32x32.mat"),
        "test": urllib.parse.urljoin(URL, "test_32x32.mat"),
        "extra": urllib.parse.urljoin(URL, "extra_32x32.mat"),
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(
                filepath=output_files["train"],
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(
                filepath=output_files["test"],
            )),
        tfds.core.SplitGenerator(
            name="extra",
            num_shards=10,
            gen_kwargs=dict(
                filepath=output_files["extra"],
            )),
    ]

  def _generate_examples(self, filepath):
    """Generate examples as dicts.

    Args:
      filepath: `str` path of the file to process.

    Yields:
      Generator yielding the next samples
    """
    with tf.gfile.Open(filepath, "rb") as f:
      data = scipy.io.loadmat(f)

    # Maybe should shuffle ?

    assert np.max(data["y"]) <= 10  # Sanity check
    assert np.min(data["y"]) > 0

    for image, label in zip(np.rollaxis(data["X"], -1), data["y"]):
      yield self.info.features.encode_example({
          "image": image,
          "label": label % 10,  # digit 0 is saved as 0 (instead of 10)
      })

# TODO(tfds): Add the SvhnFull dataset

# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Describable Textures Dataset (DTD)."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{cimpoi14describing,
Author    = {M. Cimpoi and S. Maji and I. Kokkinos and S. Mohamed and A. Vedaldi},
Title     = {Describing Textures in the Wild},
Booktitle = {Proceedings of the {IEEE} Conf. on Computer Vision and Pattern Recognition ({CVPR})},
Year      = {2014}}
"""
_DESCRIPTION = """\
The Describable Textures Dataset (DTD) is an evolving collection of textural
images in the wild, annotated with a series of human-centric attributes,
inspired by the perceptual properties of textures. This data is made available
to the computer vision community for research purposes.

The "label" of each example is its "key attribute" (see the official website).
The official release of the dataset defines a 10-fold cross-validation
partition. Our TRAIN/TEST/VALIDATION splits are those of the first fold.
"""
_URL = "https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html"
_DATA_URL = (
    "https://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1.tar.gz"
)


class Dtd(tfds.core.GeneratorBasedBuilder):
  """Describable Textures Dataset (DTD)."""

  VERSION = tfds.core.Version("3.0.1")

  def _info(self):
    names_file = tfds.core.tfds_path(
        os.path.join("image_classification", "dtd_key_attributes.txt")
    )
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "file_name": tfds.features.Text(),
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    # Note: The file extension is .tar.gz, but it is actually a .tar file.
    data_path = dl_manager.download_and_extract(_DATA_URL)

    # Note: DTD defines 10-fold CV partitions. Our TRAIN/TEST/VALIDATION are
    # those of the first fold.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(data_path=data_path, split_name="train1"),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(data_path=data_path, split_name="test1"),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(data_path=data_path, split_name="val1"),
        ),
    ]

  def _generate_examples(self, data_path, split_name):
    with tf.io.gfile.GFile(
        os.path.join(data_path, "dtd", "labels", split_name + ".txt"), "r"
    ) as split_file:
      for line in split_file:
        fname = line.strip()
        label = os.path.split(fname)[0]
        record = {
            "file_name": fname,
            "image": os.path.join(data_path, "dtd", "images", fname),
            "label": label,
        }
        yield fname, record

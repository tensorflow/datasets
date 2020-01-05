# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Dataset class for Food-101 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BASE_URL = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"

_DESCRIPTION = (
    "This dataset consists of 101 food categories, with 101'000 images. For "
    "each class, 250 manually reviewed test images are provided as well as 750"
    " training images. On purpose, the training images were not cleaned, and "
    "thus still contain some amount of noise. This comes mostly in the form of"
    " intense colors and sometimes wrong labels. All images were rescaled to "
    "have a maximum side length of 512 pixels.")

_LABELS_FNAME = "image/food-101_classes.txt"

_CITATION = """\
 @inproceedings{bossard14,
  title = {Food-101 -- Mining Discriminative Components with Random Forests},
  author = {Bossard, Lukas and Guillaumin, Matthieu and Van Gool, Luc},
  booktitle = {European Conference on Computer Vision},
  year = {2014}
}
"""


class Food101(tfds.core.GeneratorBasedBuilder):
  """Food-101 Images dataset."""

  VERSION = tfds.core.Version("2.0.0")

  def _info(self):
    """Define Dataset Info."""

    names_file = tfds.core.get_tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names_file=names_file),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.vision.ee.ethz.ch/datasets_extra/food-101/",
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    """Define Splits."""

    dl_path = dl_manager.download_and_extract(_BASE_URL)
    meta_path = os.path.join(dl_path, "food-101", "meta")
    image_dir_path = os.path.join(dl_path, "food-101", "images")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "json_file_path": os.path.join(meta_path, "train.json"),
                "image_dir_path": image_dir_path
            },
        ),

        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "json_file_path": os.path.join(meta_path, "test.json"),
                "image_dir_path": image_dir_path
            },
        ),
    ]

  def _generate_examples(self, json_file_path, image_dir_path):
    """Generate images and labels for splits."""
    with tf.io.gfile.GFile(json_file_path) as f:
      data = json.loads(f.read())
    for label, images in data.items():
      for image_name in images:
        image = os.path.join(image_dir_path, image_name + ".jpg")
        yield image_name, {
            "image": image,
            "label": label,
        }

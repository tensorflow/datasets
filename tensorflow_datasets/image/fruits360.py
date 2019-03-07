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

"""Fruits-360: A dataset of images containing fruits. About 700MB total.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{article,
author = {Mureșan, Horea and Oltean, Mihai},
year = {2018},
month = {06},
pages = {26-42},
title = {Fruit recognition from images using deep learning},
volume = {10},
journal = {Acta Universitatis Sapientiae, Informatica},
doi = {10.2478/ausi-2018-0002},
url = {https://github.com/Horea94/Fruit-Images-Dataset}
}
"""

_DOWNLOAD_URL = "https://github.com/Horea94/Fruit-Images-Dataset/archive/8c839e4d52ae0563d9e7d3986f34113e52a910a5.zip"

_IMAGE_SIZE = 100
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)
_CLASS_NAMES = ['Apple Braeburn', 'Apple Golden 1', 'Apple Golden 2', 'Apple Golden 3', 'Apple Granny Smith', 'Apple Red 1', 'Apple Red 2', 'Apple Red 3', 'Apple Red Delicious', 'Apple Red Yellow 1', 'Apple Red Yellow 2', 'Apricot', 'Avocado', 'Avocado ripe', 'Banana', 'Banana Lady Finger', 'Banana Red', 'Cactus fruit', 'Cantaloupe 1', 'Cantaloupe 2', 'Carambula', 'Cherry 1', 'Cherry 2', 'Cherry Rainier', 'Cherry Wax Black', 'Cherry Wax Red', 'Cherry Wax Yellow', 'Chestnut', 'Clementine', 'Cocos', 'Dates', 'Granadilla', 'Grape Blue', 'Grape Pink', 'Grape White', 'Grape White 2', 'Grape White 3', 'Grape White 4', 'Grapefruit Pink', 'Grapefruit White', 'Guava', 'Hazelnut', 'Huckleberry', 'Kaki', 'Kiwi', 'Kumquats', 'Lemon', 'Lemon Meyer', 'Limes', 'Lychee', 'Mandarine', 'Mango', 'Mangostan', 'Maracuja', 'Melon Piel de Sapo', 'Mulberry', 'Nectarine', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Peach 2', 'Peach Flat', 'Pear', 'Pear Abate', 'Pear Kaiser', 'Pear Monster', 'Pear Williams', 'Pepino', 'Physalis', 'Physalis with Husk', 'Pineapple', 'Pineapple Mini', 'Pitahaya Red', 'Plum', 'Plum 2', 'Plum 3', 'Pomegranate', 'Pomelo Sweetie', 'Quince', 'Rambutan', 'Raspberry', 'Redcurrant', 'Salak', 'Strawberry', 'Strawberry Wedge', 'Tamarillo', 'Tangelo', 'Tomato 1', 'Tomato 2', 'Tomato 3', 'Tomato 4', 'Tomato Cherry Red', 'Tomato Maroon', 'Walnut']


class Fruits360(tfds.core.GeneratorBasedBuilder):
  """Fruits-360 dataset."""

  VERSION = tfds.core.Version("0.0.2")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A large set of fruits on a white background.",
        features=tfds.features.FeaturesDict({
            "file_name": tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
            "label": tfds.features.ClassLabel(
                names=_CLASS_NAMES),
        }),
        supervised_keys=("image", "label"),
        urls=["https://github.com/Horea94/Fruit-Images-Dataset/"],
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    # For some reason the default extract method is NO_EXTRACT
    # so we specify it here. :/
    download_resource = tfds.download.Resource(
        url=_DOWNLOAD_URL,
        extract_method=tfds.download.ExtractMethod.ZIP)
    download_path = dl_manager.download_and_extract(download_resource)
    # The download manager extracts into a single folder
    # named after the file basename at the moment.
    sub = os.listdir(download_path)[0]
    real_root = os.path.join(download_path, sub)
    train_path = os.path.join(real_root, 'Training')
    test_path = os.path.join(real_root, 'Test')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs=dict(root_dir=train_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(root_dir=test_path),
        ),
    ]

  def _generate_examples(self, root_dir):
    """Generate fruits samples given a path.

    Args:
      root_dir: object that iterates over the zip.

    Yields:
      The image path and its label.
    """
    for class_name in _CLASS_NAMES:
      class_dir = os.path.join(root_dir, class_name)
      fns = os.listdir(class_dir)

      for fn in sorted(fns):
        image_fn = os.path.join(class_dir, fn)
        yield {
            "label": class_name,
            "file_name": image_fn,
        }

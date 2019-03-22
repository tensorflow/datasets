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


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
from collections import OrderedDict
import tensorflow_datasets.public_api as tfds

"""dataset_url: https://github.com/ebay/modanet"""

_CITATION = """\
@inproceedings{zheng/2018acmmm,
  author       = {Shuai Zheng and Fan Yang and M. Hadi Kiapour and Robinson Piramuthu},
  title        = {ModaNet: A Large-Scale Street Fashion Dataset with Polygon Annotations},
  booktitle    = {ACM Multimedia},
  year         = {2018},
}
"""

_DESCRIPTION = """\
ModaNet is a street fashion images dataset consisting of annotations related to RGB images. 
ModaNet provides multiple polygon annotations for each image. This dataset is described in a technical paper with the 
title ModaNet: A Large-Scale Street Fashion Dataset with Polygon Annotations. Each polygon is associated with a label 
from 13 meta fashion categories. The annotations are based on images in the PaperDoll image set, which has only a 
few hundred images annotated by the superpixel-based tool. The contribution of ModaNet is to provide new and extra 
polygon annotations for the images.
"""

# Path to images and category labels in data dir
_URL = "http://vision.is.tohoku.ac.jp/chictopia2/photos.lmdb.tar"

_IMAGE_WIDTH = 400
_IMAGE_HEIGHT = 600
_IMAGE_SHAPE = (_IMAGE_WIDTH, _IMAGE_HEIGHT, 3)

# Labels per category
_LABELS = OrderedDict({
    "1": "Bag",
    "2": "Belt",
    "3": "Boots",
    "4": "Footwear",
    "5": "Outer",
    "6": "Dress",
    "7": "Sunglasses",
    "8": "Pants",
    "9": "Top",
    "10": "Shorts",
    "11": "Skirt",
    "12": "Headwear",
    "13": "Scarf & Tie"
})


class ModaNet(tfds.core.GeneratorBasedBuilder):
    """Modanet: online street fashion dataset"""

    VERSION = tfds.core.Version('1.0.0')

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image": tfds.features.Image(),
                "label": tfds.features.Sequence(
                    tfds.features.ClassLabel(names=_LABELS.values())),
            }),
            supervised_keys=("image", "label"),
            urls=[_URL],
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        path = dl_manager.download_and_extract(_URL)

        # There is no predefined train/val/test split for this dataset.
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=100,
                gen_kwargs={
                    "images_dir_path": path
                }),
        ]

    def _generate_examples(self, images_dir_path):
        """Generate flower images and labels given the image directory path.

        Args:
          images_dir_path: path to the directory where the images are stored.

        Yields:
          The image path and its corresponding label.
        """
        parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
        walk_dir = os.path.join(images_dir_path, parent_dir)
        dirs = tf.io.gfile.listdir(walk_dir)

        for d in dirs:
            if tf.io.gfile.isdir(os.path.join(walk_dir, d)):
                for full_path, _, fname in tf.io.gfile.walk(os.path.join(walk_dir, d)):
                    for image_file in fname:
                        if image_file.endswith(".jpg"):
                            image_path = os.path.join(full_path, image_file)
                            yield {
                                "image": image_path,
                                "label": d.lower(),
                            }

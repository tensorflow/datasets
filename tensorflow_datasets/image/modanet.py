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

"""modanet:online streetfashion datasets"""

import re
from collections import OrderedDict
import tensorflow_datasets.public_api as tfds

"""dataset_url: https://github.com/ebay/modanet"""

_CITATION= """\
@inproceedings{zheng/2018acmmm,
  author       = {Shuai Zheng and Fan Yang and M. Hadi Kiapour and Robinson Piramuthu},
  title        = {ModaNet: A Large-Scale Street Fashion Dataset with Polygon Annotations},
  booktitle    = {ACM Multimedia},
  year         = {2018},
}
"""

_DESCRIPTION="""\
ModaNet is a street fashion images dataset consisting of annotations related to RGB images. 
ModaNet provides multiple polygon annotations for each image. This dataset is described in a technical paper with the 
title ModaNet: A Large-Scale Street Fashion Dataset with Polygon Annotations. Each polygon is associated with a label 
from 13 meta fashion categories. The annotations are based on images in the PaperDoll image set, which has only a 
few hundred images annotated by the superpixel-based tool. The contribution of ModaNet is to provide new and extra 
polygon annotations for the images.
"""

# Path to images and category labels in data dir
_TRAIN_URL = "http://vision.is.tohoku.ac.jp/chictopia2/photos.lmdb.tar"
_VALIDATION_URL = "https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip"

_IMAGE_WIDTH = 400
_IMAGE_HEIGHT = 600
_IMAGE_SHAPE = (_IMAGE_WIDTH, _IMAGE_HEIGHT, 3)

_NAME_RE = re.compile(r"^(humans|horses)/[\w-]*\.png$")

VERSION = tfds.core.Version('0.1.0')

# Labels per category
_LABELS = OrderedDict({
    "1": "bag",
    "2": "belt",
    "3": "boots",
    "4": "footwear",
    "5": "outer",
    "6": "dress",
    "7": "sunglasses",
    "8": "pants",
    "9": "top",
    "10": "shorts",
    "11": "skirt",
    "12": "headwear",
    "13": "scarf & tie"
})

class ModaNet(tfds.core.GeneratorBasedBuilder):
    """modanet: online street fashion dataset"""
    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "image_descrit\ption": tfds.features.Text(),  #
                "image": tfds.features.Image(),
                "label": tfds.features.Sequence(
                    tfds.features.ClassLabel(names=_LABELS.values())),
            }),
            supervised_keys=("image", "label"),
            urls=["https://github.com/ebay/modanet"],
            citation=_CITATION
        )

    def _split_generators(self, dl_manager):
        train_path, valid_path = dl_manager.download([_TRAIN_URL, _VALIDATION_URL])
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=10,
                gen_kwargs={
                    "archive": dl_manager.iter_archive(train_path)
                }),
            tfds.core.SplitGenerator(
                name=tfds.Split.VALIDATION,
                num_shards=10,
                gen_kwargs={
                    "archive": dl_manager.iter_archive(valid_path)
                }),
        ]

    def _generate_examples(self, archive):
        """Generate horses or humans images and labels given the directory path.

        Args:
          archive: object that iterates over the zip.

        Yields:
          The image path and its corresponding label.
        """

        for fname, fobj in archive:
            res = _NAME_RE.match(fname)
            if not res:  # if anything other than .png; skip
                continue
            label = res.group(1).lower()
            yield {
                "image": fobj,
                "label": label,
            }

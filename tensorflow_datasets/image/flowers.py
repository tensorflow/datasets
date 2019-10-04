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

"""Flowers dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }
"""

_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"

_NAME_RE = re.compile(
    r"^flower_photos[\\/](daisy|dandelion|roses|sunflowers|tulips)[\\/](\d|\w|_)+\.jpg$"
)


class TFFlowers(tfds.core.GeneratorBasedBuilder):
    """Flowers dataset."""

    VERSION = tfds.core.Version("1.0.0", experiments={tfds.core.Experiment.S3: False})
    SUPPORTED_VERSIONS = [
        tfds.core.Version(
            "3.0.0", "New split API (https://tensorflow.org/datasets/splits)"
        )
    ]

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description="A large set of images of flowers",
            features=tfds.features.FeaturesDict(
                {
                    "image": tfds.features.Image(),
                    "label": tfds.features.ClassLabel(
                        names=["dandelion", "daisy", "tulips", "sunflowers", "roses"]
                    ),
                }
            ),
            supervised_keys=("image", "label"),
            urls=[_URL],
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        path = dl_manager.download(_URL)
        path = os.path.join(path, tf.io.gfile.listdir(path)[0])
        # There is no predefined train/val/test split for this dataset.
        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                num_shards=20,
                gen_kwargs={"archive": dl_manager.iter_archive(path)},
            )
        ]

    def _generate_examples(self, archive):
        """Generate flower images and labels given the image directory path.

    Args:
      archive: C  omplete path where the image is stored.

    Yields:
      The image path and its corresponding label.
    """
        for fname, fobj in archive:
            res = _NAME_RE.match(fname)
            if not res:
                continue
            label = res.group(1).lower()
            record = {"image": fobj, "label": label}
            print("yield content is :", label, " fname is :", os.path.basename(fname))
            yield "%s/%s" % (label, os.path.basename(fname)), record

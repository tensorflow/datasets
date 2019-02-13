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

"""LSUN dataset.

Large scene understanding dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

LSUN_URL = "http://lsun.cs.princeton.edu/htbin/download.cgi?tag=latest&category=%s&set=%s"
LSUN_DATA_FILENAME = "lsun-%s-%s.zip"

_CITATION = """\
@article{journals/corr/YuZSSX15,
  added-at = {2018-08-13T00:00:00.000+0200},
  author = {Yu, Fisher and Zhang, Yinda and Song, Shuran and Seff, Ari and Xiao, Jianxiong},
  biburl = {https://www.bibsonomy.org/bibtex/2446d4ffb99a5d7d2ab6e5417a12e195f/dblp},
  ee = {http://arxiv.org/abs/1506.03365},
  interhash = {3e9306c4ce2ead125f3b2ab0e25adc85},
  intrahash = {446d4ffb99a5d7d2ab6e5417a12e195f},
  journal = {CoRR},
  keywords = {dblp},
  timestamp = {2018-08-14T15:08:59.000+0200},
  title = {LSUN: Construction of a Large-scale Image Dataset using Deep Learning with Humans in the Loop.},
  url = {http://dblp.uni-trier.de/db/journals/corr/corr1506.html#YuZSSX15},
  volume = {abs/1506.03365},
  year = 2015
}
"""


class Lsun(tfds.core.GeneratorBasedBuilder):
  """Lsun dataset."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name="classroom",
          description="Classroom images.",
          version="0.1.1",
      ),
      tfds.core.BuilderConfig(
          name="bedroom",
          description="Bedroom images.",
          version="0.1.1",
      )
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Large scale images showing different objects "
                     "from given categories like bedroom, tower etc."),
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(encoding_format="jpeg"),
        }),
        urls=["https://www.yf.io/p/lsun"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract({
        "train": LSUN_URL % (self.builder_config.name, "train"),
        "val": LSUN_URL % (self.builder_config.name, "val")
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=40,
            gen_kwargs={
                "extracted_dir": extracted_dirs["train"],
                "file_path": "%s_%s_lmdb" % (self.builder_config.name, "train")
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                "extracted_dir": extracted_dirs["val"],
                "file_path": "%s_%s_lmdb" % (self.builder_config.name, "val")
            }),
    ]

  def _generate_examples(self, extracted_dir, file_path):
    with tf.Graph().as_default():
      dataset = tf.contrib.data.LMDBDataset(
          os.path.join(extracted_dir, file_path, "data.mdb"))
      for _, jpeg_image in tfds.as_numpy(dataset):
        yield {"image": io.BytesIO(jpeg_image)}

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

"""Labeled faces in wild."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_URL = "http://vis-www.cs.umass.edu/lfw/lfw.tgz"

LFW_IMAGE_SHAPE = (250, 250, 3)

LFW_CITATION = """\
@TechReport{LFWTech,
    author = {Gary B. Huang and Manu Ramesh and Tamara Berg and Erik Learned-Miller},
    title = {Labeled Faces in the Wild: A Database for Studying Face Recognition in Unconstrained Environments},
    institution = {University of Massachusetts, Amherst},
    year = 2007,
    number = {07-49},
    month = {October}
}
"""


class LFW(tfds.core.GeneratorBasedBuilder):
  """LFW Class"""
  URL = "http://vis-www.cs.umass.edu/lfw/#resources"
  VERSION = tfds.core.Version("0.3.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Labeled Faces in the Wild:\
  A Database for Studying Face Recognition in Unconstrained Environments"),
        features=tfds.features.FeaturesDict({
            "image_name": tfds.features.Text(),
            "image": tfds.features.Image(shape=LFW_IMAGE_SHAPE),
            }),
        supervised_keys=("image_name", "image"),
        urls=[self.URL],
        citation=LFW_CITATION,
        )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)
    path = os.path.join(path, 'lfw')

    # There is no train/test split predefined
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=20,
            gen_kwargs={
                "data_path": path,}
            ),
        ]

  def _generate_examples(self, data_path):
    image_list = self.path_maker(data_path)

    for image in image_list:
      yield {
          "image_name":image[0],
          "image": image[1],
      }

  #This is a helper function for making lsit of all paths
  def path_maker(self, _path):
    path_list = []
    dir_list = tf.gfile.ListDirectory(_path)
    for _dir in dir_list:
      img_dir_path = os.path.join(_path, _dir)
      img_list = tf.gfile.ListDirectory(img_dir_path)
      for img in img_list:
        img_path = os.path.join(img_dir_path, img)
        path_list.append([_dir, img_path])
    return path_list

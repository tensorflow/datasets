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

"""CelebA dataset.

Large-scale CelebFaces Attributes (CelebA) Dataset

Deep Learning Face Attributes in the Wild
Ziwei Liu and Ping Luo and Xiaogang Wang and Xiaoou Tang
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

IMG_ALIGNED_DATA = ("https://drive.google.com/uc?export=download&"
                    "id=0B7EVK8r0v71pZjFTYXZWM3FlRnM")

EVAL_LIST = ("TODO")


class CelebA(tfds.core.GeneratorBasedDatasetBuilder):
  """CelebA dataset."""

  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description=("Large-scale CelebFaces Attributes, CelebA."
                     "Set of ~30k celebrities pictures. "
                     "These pictures are cropped."),
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(218, 178, 3), encoding_format="jpeg")
        }),
        urls=["http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html"],
        size_in_bytes=2 * tfds.units.GiB,
        citation="Ziwei Liu and Ping Luo and Xiaogang Wang and Xiaoou Tang "
        "Deep Learning Face Attributes in the Wild "
        "ICCV 2015")

  def _split_generators(self, dl_manager):
    files = dl_manager.download_and_extract(IMG_ALIGNED_DATA)
    img_list_path = dl_manager.download_and_extract(EVAL_LIST)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "file_id":
                    0,
                "filedir":
                    os.path.join(files, "img_align_celeba"),
                "img_list_path":
                    os.path.join(img_list_path, "list_eval_partition.txt")
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=4,
            gen_kwargs={
                "file_id":
                    1,
                "filedir":
                    os.path.join(files, "img_align_celeba"),
                "img_list_path":
                    os.path.join(img_list_path, "list_eval_partition.txt")
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=4,
            gen_kwargs={
                "file_id":
                    2,
                "filedir":
                    os.path.join(files, "img_align_celeba"),
                "img_list_path":
                    os.path.join(img_list_path, "list_eval_partition.txt")
            })
    ]

  def _generate_samples(self, filedir, img_list_path, file_id):
    with tf.gfile.Open(img_list_path) as f:
      files = [
          line.split()[0]
          for line in f.readlines()
          if int(line.split()[1]) == file_id
      ]
    for file_name in files:
      path = os.path.join(filedir, file_name)
      yield self.info.features.encode_sample({
          "image": path,
      })

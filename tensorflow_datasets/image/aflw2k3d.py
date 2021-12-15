# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""AFLW2000-3D Dataset."""

import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
AFLW2000-3D is a dataset of 2000 images that have been annotated with image-level
68-point 3D facial landmarks.
This dataset is typically used for evaluation of 3D facial landmark detection
models. The head poses are very diverse and often hard to be detected by a 
cnn-based face detector.
The 2D landmarks are skipped in this dataset, since some of the data are not
consistent to 21 points, as the original paper mentioned.
"""

_CITATION = """\
@article{DBLP:journals/corr/ZhuLLSL15,
  author    = {Xiangyu Zhu and
               Zhen Lei and
               Xiaoming Liu and
               Hailin Shi and
               Stan Z. Li},
  title     = {Face Alignment Across Large Poses: {A} 3D Solution},
  journal   = {CoRR},
  volume    = {abs/1511.07212},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.07212},
  archivePrefix = {arXiv},
  eprint    = {1511.07212},
  timestamp = {Mon, 13 Aug 2018 16:48:23 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/ZhuLLSL15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""


class Aflw2k3d(tfds.core.GeneratorBasedBuilder):
  """AFLW2000-3D dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(450, 450, 3), encoding_format="jpeg"),
            "landmarks_68_3d_xy_normalized":
                tfds.features.Tensor(shape=(68, 2), dtype=tf.float32),
            "landmarks_68_3d_z":
                tfds.features.Tensor(shape=(68, 1), dtype=tf.float32),
        }),
        homepage="http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    extracted_path = dl_manager.download_and_extract(
        "http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/Database/AFLW2000-3D.zip"
    )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "image_dir_path": os.path.join(extracted_path, "AFLW2000"),
            }),
    ]

  def _generate_examples(self, image_dir_path):
    image_files = tf.io.gfile.glob(
        pattern=os.path.join(image_dir_path, "image0*.jpg"))
    label_files = [s.replace("jpg", "mat") for s in image_files]

    for image_file, label_file in zip(image_files, label_files):
      with tf.io.gfile.GFile(label_file, "rb") as f:
        mat = tfds.core.lazy_imports.scipy.io.loadmat(f)
      landmarks_68_3d_xyz = mat["pt3d_68"].T.astype(np.float32)
      landmarks_68_3d_xy_normalized = landmarks_68_3d_xyz[..., 0:2] / 450.0
      landmarks_68_3d_z = landmarks_68_3d_xyz[..., 2:]
      yield os.path.basename(image_file), {
          "image": image_file,
          "landmarks_68_3d_xy_normalized": landmarks_68_3d_xy_normalized,
          "landmarks_68_3d_z": landmarks_68_3d_z,
      }

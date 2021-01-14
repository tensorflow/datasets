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

"""300W-LP Dataset."""

import os
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DATASET_URL = "https://drive.google.com/uc?export=download&id=0B7OEHD3T4eCkVGs0TkhUWFN6N1k"

_PROJECT_URL = "http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm"

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

_DESCRIPTION = """\
300W-LP Dataset is expanded from 300W, which standardises multiple alignment \
databases with 68 landmarks, including AFW, LFPW, HELEN, IBUG and XM2VTS. With \
300W, 300W-LP adopt the proposed face profiling to generate 61,225 samples \
across large poses (1,786 from IBUG, 5,207 from AFW, 16,556 from LFPW and \
37,676 from HELEN, XM2VTS is not used).

The dataset can be employed as the training set for the following computer \
vision tasks: face attribute recognition and landmark (or facial part) \
locaization.
"""


class The300wLp(tfds.core.GeneratorBasedBuilder):
  """300W-LP dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(450, 450, 3), encoding_format="jpeg"),
            "landmarks_origin":
                tfds.features.Tensor(shape=(68, 2), dtype=tf.float32),
            "landmarks_2d":
                tfds.features.Tensor(shape=(68, 2), dtype=tf.float32),
            "landmarks_3d":
                tfds.features.Tensor(shape=(68, 2), dtype=tf.float32),
            "roi":
                tfds.features.Tensor(shape=(4,), dtype=tf.float32),
            "illum_params":
                tfds.features.Tensor(shape=(10,), dtype=tf.float32),
            "color_params":
                tfds.features.Tensor(shape=(7,), dtype=tf.float32),
            "tex_params":
                tfds.features.Tensor(shape=(199,), dtype=tf.float32),
            "shape_params":
                tfds.features.Tensor(shape=(199,), dtype=tf.float32),
            "exp_params":
                tfds.features.Tensor(shape=(29,), dtype=tf.float32),
            "pose_params":
                tfds.features.Tensor(shape=(7,), dtype=tf.float32)
        }),
        homepage=_PROJECT_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract(_DATASET_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "image_dir_path": os.path.join(extracted_path, "300W_LP"),
            }),
    ]

  def _generate_examples(self, image_dir_path):
    """Yields examples."""
    image_files = tf.io.gfile.glob(
        pattern=os.path.join(image_dir_path, "[!Code]*[!_Flip]/[!_]*.jpg"))
    label_files = [s.replace("jpg", "mat") for s in image_files]
    landmark_files = [
        s.replace("300W_LP", "300W_LP/landmarks").replace(".jpg", "_pts.mat")
        for s in image_files
    ]
    for image_file, label_file, landmark_file in zip(image_files, label_files,
                                                     landmark_files):
      with tf.io.gfile.GFile(label_file, "rb") as f:
        mat = tfds.core.lazy_imports.scipy.io.loadmat(f)
      pt2d_origin = mat["pt2d"].T
      pt2d_origin = (pt2d_origin / 450.0).astype(np.float32)
      roi = mat["roi"].reshape(4).astype(np.float32)
      illum_params = mat["Illum_Para"].reshape([-1]).astype(np.float32)
      color_params = mat["Color_Para"].reshape([-1]).astype(np.float32)
      tex_params = mat["Tex_Para"].reshape([-1]).astype(np.float32)
      shape_params = mat["Shape_Para"].reshape([-1]).astype(np.float32)
      exp_params = mat["Exp_Para"].reshape([-1]).astype(np.float32)
      pose_params = mat["Pose_Para"].reshape([-1]).astype(np.float32)
      with tf.io.gfile.GFile(landmark_file, "rb") as f:
        ldm_mat = tfds.core.lazy_imports.scipy.io.loadmat(f)
        pt2d = (ldm_mat["pts_2d"] / 450.0).astype(np.float32)
        pt3d = (ldm_mat["pts_3d"] / 450.0).astype(np.float32)
      record = {
          "image": image_file,
          "landmarks_origin": pt2d_origin,
          "landmarks_2d": pt2d,
          "landmarks_3d": pt3d,
          "roi": roi,
          "illum_params": illum_params,
          "color_params": color_params,
          "tex_params": tex_params,
          "shape_params": shape_params,
          "exp_params": exp_params,
          "pose_params": pose_params
      }
      yield os.path.basename(image_file), record

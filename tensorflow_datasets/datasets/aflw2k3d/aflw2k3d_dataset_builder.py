# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """AFLW2000-3D dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(
                shape=(450, 450, 3), encoding_format="jpeg"
            ),
            "landmarks_68_3d_xy_normalized": tfds.features.Tensor(
                shape=(68, 2), dtype=np.float32
            ),
            "landmarks_68_3d_z": tfds.features.Tensor(
                shape=(68, 1), dtype=np.float32
            ),
        }),
        homepage=(
            "http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm"
        ),
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
            },
        ),
    ]

  def _generate_examples(self, image_dir_path):
    image_files = tf.io.gfile.glob(
        pattern=os.path.join(image_dir_path, "image0*.jpg")
    )
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

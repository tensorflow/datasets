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

"""NYU Depth V2 Dataset."""

import os

import numpy as np
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{Silberman:ECCV12,
  author    = {Nathan Silberman, Derek Hoiem, Pushmeet Kohli and Rob Fergus},
  title     = {Indoor Segmentation and Support Inference from RGBD Images},
  booktitle = {ECCV},
  year      = {2012}
}
@inproceedings{icra_2019_fastdepth,
  author    = {Wofk, Diana and Ma, Fangchang and Yang, Tien-Ju and Karaman, Sertac and Sze, Vivienne},
  title     = {FastDepth: Fast Monocular Depth Estimation on Embedded Systems},
  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2019}
}
"""

_DESCRIPTION = """\
The NYU-Depth V2 data set is comprised of video sequences from a variety of
indoor scenes as recorded by both the RGB and Depth cameras from the
Microsoft Kinect.
"""

_URL = 'http://datasets.lids.mit.edu/fastdepth/data/nyudepthv2.tar.gz'


class NyuDepthV2(tfds.core.GeneratorBasedBuilder):
  """NYU Depth V2 Dataset."""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(480, 640, 3)),
            'depth': tfds.features.Tensor(shape=(480, 640), dtype=tf.float16),
        }),
        supervised_keys=('image', 'depth'),
        homepage='https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    base_path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'root_dir': os.path.join(base_path, 'nyudepthv2', 'train')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'root_dir': os.path.join(base_path, 'nyudepthv2', 'val')
            },
        ),
    ]

  def _generate_examples(self, root_dir):
    """Yields examples."""
    h5py = tfds.core.lazy_imports.h5py
    for directory in tf.io.gfile.listdir(root_dir):
      for file_name in tf.io.gfile.listdir(os.path.join(root_dir, directory)):
        with h5py.File(os.path.join(root_dir, directory, file_name), 'r') as f:
          yield directory + '_' + file_name, {
              'image': np.transpose(f['rgb'], (1, 2, 0)),
              'depth': f['depth'][:].astype('float16')
          }

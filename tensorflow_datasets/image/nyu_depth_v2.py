# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
import tensorflow.compat.v2 as tf

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
Microsoft Kinect. It includes a labelled subset of frames with semantic and
instance annotations.
"""


class NyuDepthV2Config(tfds.core.BuilderConfig):

  def __init__(self, labeled=False, **kwargs):
    super().__init__(version='1.0.0', **kwargs)
    self.labeled = labeled


class NyuDepthV2(tfds.core.GeneratorBasedBuilder):
  """NYU Depth V2 Dataset."""

  VERSION = tfds.core.Version('0.0.1')

  BUILDER_CONFIGS = [
      NyuDepthV2Config(
          name='labeled',
          description=
          'Subset of frames labelled for semantic and instance segmentation.',
          labeled=True,
      ),
      NyuDepthV2Config(
          name='depth',
          description='Full dataset with rgb and depth images.',
          labeled=False,
      ),
  ]

  def _info(self):
    features = {
        'image': tfds.features.Image(shape=(480, 640, 3)),
        'depth': tfds.features.Tensor(shape=(480, 640), dtype=tf.float16),
    }
    if self.builder_config.labeled:
      features.update(
          {
              'depth':
                  tfds.features.Tensor(shape=(480, 640), dtype=tf.float32),
              'accelData':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
              'instances':
                  tfds.features.Tensor(shape=(480, 640), dtype=tf.uint8),
              'labels':
                  tfds.features.Tensor(shape=(480, 640), dtype=tf.uint16),
              'scene':
                  tf.string,
              'sceneType':
                  tf.string,
          }
      )
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        supervised_keys=(
            'image', 'labels' if self.builder_config.labeled else 'depth'
        ),
        homepage='https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    urls = {
        'fastdepth':
            'http://datasets.lids.mit.edu/fastdepth/data/nyudepthv2.tar.gz',
        'labeled':
            'http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat',
    }

    if self.builder_config.labeled:
      extracted = dl_manager.download_and_extract(urls['labeled'])
      return [
          tfds.core.SplitGenerator(
              name=tfds.Split.TRAIN, gen_kwargs={
                  'data_path': extracted,
              }
          )
      ]
    extracted = dl_manager.download_and_extract(urls['fastdepth'])
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'data_path': os.path.join(extracted, 'nyudepthv2', 'train')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'data_path': os.path.join(extracted, 'nyudepthv2', 'val')
            },
        ),
    ]

  def _generate_examples(self, data_path):
    """Yields examples."""
    h5py = tfds.core.lazy_imports.h5py
    if self.builder_config.labeled:
      with h5py.File(data_path, 'r') as f:
        for i in range(f['accelData'].shape[1]):
          yield i, {
              'accelData':
                  f['accelData'][:, i].astype('float32'),
              'depth':
                  np.transpose(f['depths'][i]).astype('float32'),
              'image':
                  np.transpose(f['images'][i]).astype('uint8'),
              'instances':
                  np.transpose(f['instances'][i]).astype('uint8'),
              'labels':
                  np.transpose(f['labels'][i]).astype('uint16'),
              'scene':
                  f[f['scenes'][0, i]][:, 0].tobytes().decode('ascii'),
              'sceneType':
                  f[f['sceneTypes'][0, i]][:, 0].tobytes().decode('ascii'),
          }
    else:
      for directory in tf.io.gfile.listdir(data_path):
        for file_name in tf.io.gfile.listdir(
            os.path.join(data_path, directory)
        ):
          with h5py.File(
              os.path.join(data_path, directory, file_name), 'r'
          ) as f:
            yield directory + '_' + file_name, {
                'image': np.transpose(f['rgb'], (1, 2, 0)),
                'depth': f['depth'][:].astype('float16')
            }

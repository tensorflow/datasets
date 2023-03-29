# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = 'http://datasets.lids.mit.edu/fastdepth/data/nyudepthv2.tar.gz'


class Builder(tfds.core.GeneratorBasedBuilder):
  """NYU Depth V2 Dataset."""

  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(480, 640, 3)),
            'depth': tfds.features.Tensor(shape=(480, 640), dtype=np.float16),
        }),
        supervised_keys=('image', 'depth'),
        homepage='https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html',
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
              'depth': f['depth'][:].astype('float16'),
          }

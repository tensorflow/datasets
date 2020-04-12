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

"""TODO(modelnet40): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import h5py
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# Constants
_URL = 'https://shapenet.cs.stanford.edu/media/modelnet40_ply_hdf5_2048.zip'

_CITATION = """
@inproceedings{qi2017pointnet,
  title={Pointnet: Deep learning on point sets for 3d classification and segmentation},
  author={Qi, Charles R and Su, Hao and Mo, Kaichun and Guibas, Leonidas J},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={652--660},
  year={2017}
}
"""

_DESCRIPTION = """
The dataset contains point clouds sampling CAD models from 40 different categories.
The files have been retrieved from https://modelnet.cs.princeton.edu
"""


class Modelnet40(tfds.core.GeneratorBasedBuilder):
  """ModelNet40."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    # TODO(modelnet40): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'points': tfds.features.Tensor(shape=(2048, 3), dtype=tf.float32),
            'label': tfds.features.Tensor(shape=(1,), dtype=tf.uint8),
        }),
        supervised_keys=('points', 'label'),
        homepage='https://modelnet.cs.princeton.edu',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extracted_path = dl_manager.download_and_extract(_URL)

    # Note: VALIDATION split was not provided
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                filename_list_path=os.path.join(
                    extracted_path,
                    'modelnet40_ply_hdf5_2048/train_files.txt'),)),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                filename_list_path=os.path.join(
                    extracted_path,
                    'modelnet40_ply_hdf5_2048/test_files.txt'),)),
    ]

  def _generate_examples(self, filename_list_path):
    """Yields examples."""

    ancestor_parth = os.path.dirname(os.path.dirname(filename_list_path))
    with tf.io.gfile.GFile(filename_list_path, 'r') as fid:
      filename_list = fid.readlines()
    filename_list = [line.rstrip()[5:] for line in filename_list]

    example_key = -1  #< as yield exists, need to pre-increment
    for filename in filename_list:
      h5path = os.path.join(ancestor_parth, filename)

      h5file = h5py.File(h5path, 'r')
      # TODO(atagliasacchi): 'GFile' object has no attribute 'encode' error
      # with tf.io.gfile.GFile(h5path, mode='rb') as binary_fid:
      #   h5file = h5py.File(binary_fid, 'r')

      points = h5file['data'][:]
      label = h5file['label'][:]
      # TODO(atagliasacchi): verify why squeeze is not necessary

      models_per_file = points.shape[0]
      for imodel in range(models_per_file):
        example_key += 1
        yield example_key, {
            'points': points[imodel, :, :],
            'label': label[imodel]
        }

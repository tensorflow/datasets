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

"""The Leeds Sports Pose Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{Johnson10,
   title = {Clustered Pose and Nonlinear Appearance Models for Human Pose Estimation},
   author = {Johnson, Sam and Everingham, Mark},
   year = {2010},
   booktitle = {Proceedings of the British Machine Vision Conference},
   note = {doi:10.5244/C.24.12}
}
"""

_DESCRIPTION = """\
  Leeds Sports Pose Dataset
  Sam Johnson and Mark Everingham
  http://sam.johnson.io/research/lsp.html

  This dataset contains 2000 images of mostly sports people
  gathered from Flickr. The images have been scaled such that the
  most prominent person is roughly 150 pixels in length. The file
  joints.mat contains 14 joint locations for each image along with
  a binary value specifying joint visibility.

  The ordering of the joints is as follows:

  Right ankle
  Right knee
  Right hip
  Left hip
  Left knee
  Left ankle
  Right wrist
  Right elbow
  Right shoulder
  Left shoulder
  Left elbow
  Left wrist
  Neck
  Head top

  This archive contains two folders:
  images - containing the original images
  visualized - containing the images with poses visualized
"""

_DOWNLOAD_URL = "http://sam.johnson.io/research/lsp_dataset.zip"

class LeedsSportsPose(tfds.core.GeneratorBasedBuilder):
  """This dataset contains: 
     images - folder containing the original images
     visualized - folder containing the images with poses visualized
     joints.mat - a MATLAB data file containing the joint annotations in a 
                  3x14x2000 matrix called 'joints' with x and y locations 
                  and a binary value indicating the visbility of each joint.
  """

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION, 
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "visualized_image": tfds.features.Image(),
            "x": tfds.features.Tensor(shape=(14,), dtype=tf.float64), 
            "y": tfds.features.Tensor(shape=(14,), dtype=tf.float64), 
            "binary_value_visbility": tfds.features.Tensor(shape=(14,), dtype=tf.float64), 
        }),
        supervised_keys=None,
        urls=["http://sam.johnson.io/research/lsp.html"], 
        citation=_CITATION, 
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    
    data_dirs = dl_manager.download_and_extract(_DOWNLOAD_URL) 
    
    return [
        tfds.core.SplitGenerator(
            name="train",
            num_shards=10,
            gen_kwargs={
                "path_to_dataset": data_dirs,  
            },
        )
    ] 

  def _generate_examples(self, path_to_dataset): 
    
    images_path = os.path.join(path_to_dataset, "images")
    visualized_path = os.path.join(path_to_dataset, "visualized")
    mat_file_path = os.path.join(path_to_dataset, "joints.mat") 
    
    images = sorted(tf.io.gfile.listdir(images_path))
    visualized_images = sorted(tf.io.gfile.listdir(visualized_path))
    mat = tfds.core.lazy_imports.scipy.io.loadmat(mat_file_path)['joints'] 
    
    for image, visualized_image in zip(images, visualized_images):
      assert image == visualized_image 
      
      index = int(image[-8:-4]) - 1
      joint = mat[:,:,index]
      yield{
          "image": os.path.join(images_path, image),
          "visualized_image": os.path.join(visualized_path, visualized_image),
          "x": joint[0], 
          "y": joint[1], 
          "binary_value_visbility": joint[2],   
      }
    
    

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

"""Caltech 10K Web Faces.

The dataset contains images of people collected from the web by typing common given names into  Google Image Search

Pruning Training Sets for Learning of Object Categories
Anelia Angelova, Yaser Abu-Mostafa, Pietro Perona
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf

import tensorflow_datasets.public_api as tfds

LANDMARK_HEADINGS = ("lefteye_x lefteye_y righteye_x righteye_y "
           "nose_x nose_y mouth_x mouth_y").split()
IMAGE_DATA = ("http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/Caltech_WebFaces.tar")
LANDMARK_DATA = ("http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/WebFaces_GroundThruth.txt")

_CITATION = """\
@article{Angelova05learningobjCategories,
  title={Pruning training sets for learning of object categories},
  author={ A. Angelova and Y. Abu-Mostafam and P. Perona },
  journal={Conference on Computer Vision and Pattern Recognition},
  year={2005},
}
"""
_DESCRIPTION = """\
The dataset contains images of people collected from the web by typing common given names into 
Google Image Search. The coordinates of the eyes, the nose and the center of the mouth for each 
frontal face are provided in a ground truth file. This information can be used to align and crop 
the human faces or as a ground truth for a face detection algorithm. The dataset has 10,524 human 
faces of various resolutions and in different settings, e.g. portrait images, groups of people, etc. 
Profile faces or very low resolution faces are not labeled.
""" 
class Caltech10K_WebFaces(tfds.core.GeneratorBasedBuilder):

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description='',
      features=tfds.features.FeaturesDict({
        "image": tfds.features.Image(encoding_format='jpeg'),
        "landmarks": {name: tf.int64 for name in LANDMARK_HEADINGS}
      }),
      urls=['http://www.vision.caltech.edu/Image_Datasets/Caltech_10K_WebFaces/'],
      citation=""
    )


  def _split_generator(self, dl_manager):
    extracted_dirs = dl_manager.download_and_extract({
      "images": IMAGE_DATA,
      "landmarks": LANDMARK_DATA
    })
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        num_shards=10,
        gen_kwargs={
          "file_id": 0,
          "extracted_dirs": extracted_dirs,
        }),
      tfds.core.SplitGenerator(
        name=tfds.Split.VALIDATION,
        num_shards=4,
        gen_kwargs={
          "file_id": 1,
          "extracted_dirs": extracted_dirs,
        }),
      tfds.core.SplitGenerator(
        name=tfds.Split.TEST,
        num_shards=4,
        gen_kwargs={
          "file_id": 2,
          "extracted_dirs": extracted_dirs,
        })
    ]


  def _process_caltech10k_config_file(self, file_path):
    with tf.io.gfile.GFile(file_path) as f:
      data_raw = f.read()
    lines = data_raw.split("\n")

    keys = [x.split()[0] for x in lines[:-1]]
    values = {}
    # Go over each line (skip the last one, as it is empty).
    for line in lines[0:-1]:
      row_values = line.strip().split()
      # Each row start with the 'file_name' and then space-separated values.
      values[row_values[0]] = [v for v in row_values[1:]]
    return keys, values

  def _generate_examples(self, extracted_dirs):
    filedir = os.path.join(extracted_dirs['images'],'images')
    landmarks_path = extracted_dirs["landmarks"]
    files = tf.io.gfile.listdir(filedir)
    

    landmarks = self._process_caltech10k_config_file(landmarks_path)

    for file_name in sorted(files):
      path = os.path.join(filedir, file_name)

      yield {
        "image": path,
        "landmarks":{
          k: v for k, v in zip(landmarks[0], landmarks[1][file_name])
        }
      }

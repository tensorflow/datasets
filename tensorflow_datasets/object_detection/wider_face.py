# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""WIDER FACE Dataset."""

from __future__ import annotations

import os
import re

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_PROJECT_URL = 'http://shuoyang1213.me/WIDERFACE/'

_WIDER_TRAIN_URL = (
    'https://drive.google.com/uc?export=download&'
    'id=15hGDLhsx8bLgLcIRD5DhYt5iBxnjNF1M'
)

_WIDER_VAL_URL = (
    'https://drive.google.com/uc?export=download&'
    'id=1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q'
)

_WIDER_TEST_URL = (
    'https://drive.google.com/uc?export=download&'
    'id=1HIfDbVEWKmsYKJZm4lchTBDLW5N7dY5T'
)

_WIDER_ANNOT_URL = (
    'https://drive.google.com/uc?export=download&'
    'id=1sAl2oml7hK6aZRdgRjqQJsjV5CEr7nl4'
)

_CITATION = """
@inproceedings{yang2016wider,
	Author = {Yang, Shuo and Luo, Ping and Loy, Chen Change and Tang, Xiaoou},
	Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
	Title = {WIDER FACE: A Face Detection Benchmark},
	Year = {2016}}
"""

_DESCRIPTION = """
WIDER FACE dataset is a face detection benchmark dataset, of which images are 
selected from the publicly available WIDER dataset. We choose 32,203 images and 
label 393,703 faces with a high degree of variability in scale, pose and 
occlusion as depicted in the sample images. WIDER FACE dataset is organized 
based on 61 event classes. For each event class, we randomly select 40%/10%/50% 
data as training, validation and testing sets. We adopt the same evaluation 
metric employed in the PASCAL VOC dataset. Similar to MALF and Caltech datasets,
we do not release bounding box ground truth for the test images. Users are 
required to submit final prediction files, which we shall proceed to evaluate.
"""


class WiderFace(tfds.core.GeneratorBasedBuilder):
  """WIDER FACE Dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    features = {
        'image': tfds.features.Image(encoding_format='jpeg'),
        'image/filename': tfds.features.Text(),
        'faces': tfds.features.Sequence({
            'bbox': tfds.features.BBoxFeature(),
            'blur': np.uint8,
            'expression': np.bool_,
            'illumination': np.bool_,
            'occlusion': np.uint8,
            'pose': np.bool_,
            'invalid': np.bool_,
        }),
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage=_PROJECT_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_dirs = dl_manager.download_and_extract({
        'wider_train': _WIDER_TRAIN_URL,
        'wider_val': _WIDER_VAL_URL,
        'wider_test': _WIDER_TEST_URL,
        'wider_annot': _WIDER_ANNOT_URL,
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'split': 'train', 'extracted_dirs': extracted_dirs},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'split': 'val', 'extracted_dirs': extracted_dirs},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'split': 'test', 'extracted_dirs': extracted_dirs},
        ),
    ]

  def _generate_examples(self, split, extracted_dirs):
    """Yields examples."""
    pattern_fname = re.compile(r'(.*.jpg)\n')
    pattern_annot = re.compile(
        r'(\d+) (\d+) (\d+) (\d+) (\d+) ' r'(\d+) (\d+) (\d+) (\d+) (\d+) \n'
    )
    annot_dir = 'wider_face_split'
    annot_fname = (
        'wider_face_test_filelist.txt'
        if split == 'test'
        else 'wider_face_' + split + '_bbx_gt.txt'
    )
    annot_file = os.path.join(annot_dir, annot_fname)
    image_dir = os.path.join(
        extracted_dirs['wider_' + split], 'WIDER_' + split, 'images'
    )
    annot_dir = extracted_dirs['wider_annot']
    annot_path = os.path.join(annot_dir, annot_file)
    with tf.io.gfile.GFile(annot_path, 'r') as f:
      while True:
        # First read the file name.
        line = f.readline()
        match = pattern_fname.match(line)
        if match is None:
          break
        fname = match.group(1)
        image_fullpath = os.path.join(image_dir, fname)
        faces = []
        if split != 'test':
          # Train and val contain also face information.
          with tf.io.gfile.GFile(image_fullpath, 'rb') as fp:
            image = tfds.core.lazy_imports.PIL_Image.open(fp)
            width, height = image.size

          # Read number of bounding boxes.
          nbbox = int(f.readline())
          if nbbox == 0:
            # Cases with 0 bounding boxes, still have one line with all zeros.
            # So we have to read it and discard it.
            f.readline()
          else:
            for _ in range(nbbox):
              line = f.readline()
              match = pattern_annot.match(line)
              if not match:
                raise ValueError('Cannot parse: %s' % image_fullpath)
              (
                  xmin,
                  ymin,
                  wbox,
                  hbox,
                  blur,
                  expression,
                  illumination,
                  invalid,
                  occlusion,
                  pose,
              ) = map(int, match.groups())
              ymax = np.clip(ymin + hbox, a_min=0, a_max=height)
              xmax = np.clip(xmin + wbox, a_min=0, a_max=width)
              ymin = np.clip(ymin, a_min=0, a_max=height)
              xmin = np.clip(xmin, a_min=0, a_max=width)
              faces.append({
                  'bbox': tfds.features.BBox(
                      ymin=ymin / height,
                      xmin=xmin / width,
                      ymax=ymax / height,
                      xmax=xmax / width,
                  ),
                  'blur': blur,
                  'expression': expression,
                  'illumination': illumination,
                  'occlusion': occlusion,
                  'pose': pose,
                  'invalid': invalid,
              })
        record = {
            'image': image_fullpath,
            'image/filename': fname,
            'faces': faces,
        }
        yield fname, record

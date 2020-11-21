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

"""Generate deeplesion like files, smaller and with random data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import zipfile

from absl import app
from absl import flags

import tensorflow as tf
import random
import tempfile
import numpy as np
from tensorflow_datasets.core import utils

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils


flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')
FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data',
                      'fake_examples', 'deeplesion')


MIN_HEIGHT_WIDTH = 10
MAX_HEIGHT_WIDTH = 15
CHANNELS_NB = 1


def get_random_picture(height=None, width=None, channels=CHANNELS_NB):
  """Returns random picture as np.ndarray (int)."""
  height = height or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  width = width or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  return np.random.randint(
      32768, size=(height, width, channels), dtype=np.uint16)


def get_random_png(height=None, width=None, channels=CHANNELS_NB):
  """Returns path to PNG picture."""
  # Big randomly generated pngs take large amounts of diskspace.
  # Instead, we resize a 4x4 random image to the png size.
  image = get_random_picture(4, 4, channels)
  image = tf.compat.v1.image.resize_nearest_neighbor(
      tf.expand_dims(image, 0), (height, width))[0]
  png = tf.image.encode_png(image)
  
  fobj = tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.PNG')
  fobj.write(png.numpy())
  fobj.close()
  return fobj.name


def _generate_data(num_zipfiles, num_images):
  """Generate images archive."""
  paths = []
  for i in range(1, num_zipfiles+1):
    paths.append(os.path.join(_output_dir(), 'zipfile{:02d}.zip'.format(i)))
  
  idx = 0
  for p in paths:
    idx += 1
    print('Following files will be zipped in {}:'.format(p)) 
    with zipfile.ZipFile(p, "w") as image_zip:
      # Generate images
      for i in range(0, num_images):
        png = get_random_png(512, 512)
        image_name = os.path.join("Images_png", "{:06d}_01_01".format(idx),
                              "{:03d}.png".format(i))
        image_zip.write(png, image_name, zipfile.ZIP_DEFLATED)
        print(image_name)
  
  print('All files zipped successfully!')        

  return paths
     

def _generate_csv():
# Generate annotations
  csv_dir = _output_dir()
  assert tf.io.gfile.exists(csv_dir), 'Oops, base_folder not exist'

  ann_file = os.path.join(csv_dir, 'fake_DL_info.csv')

  ann_info = \
    [['File_name','Patient_index','Study_index','Series_ID','Key_slice_index','Measurement_coordinates','Bounding_boxes','Lesion_diameters_Pixel_','Normalized_lesion_location','Coarse_lesion_type','Possibly_noisy','Slice_range','Spacing_mm_px_','Image_size','DICOM_windows','Patient_gender','Patient_age','Train_Val_Test'],
    ['000001_01_01_000.png',1,1,1,0,"233.537, 95.0204, 234.057, 106.977, 231.169, 101.605, 236.252, 101.143","226.169, 90.0204, 241.252, 111.977","11.9677, 5.10387","0.44666, 0.283794, 0.434454",3,0,"103, 115","0.488281, 0.488281, 5","512, 512","-175, 275",'F',62,1],
    ['000001_01_01_001.png',1,1,1,1,"224.826, 289.296, 224.016, 305.294, 222.396, 297.194, 228.978, 297.903","217.396, 284.296, 233.978, 310.294","16.019, 6.61971","0.431015, 0.485238, 0.340745",3,0,"8, 23","0.314453, 0.314453, 5","512, 512","-175, 275",'F',72,1],
    ['000001_01_01_002.png',1,1,1,2,"272.323, 320.763, 246.522, 263.371, 234.412, 305.494, 280.221, 288.118","229.412, 258.371, 285.221, 325.763","62.9245, 48.9929","0.492691, 0.503106, 0.351754",3,0,"8, 23","0.314453, 0.314453, 5","512, 512","-175, 275",'F',72,1],
    ['000001_01_01_003.png',1,1,1,3,"257.759, 157.618, 260.018, 133.524, 251.735, 145.571, 265.288, 146.841","246.735, 128.524, 270.288, 162.618","24.1998, 13.6123","0.498999, 0.278924, 0.452792",3,0,"58, 118","0.732422, 0.732422, 1","512, 512","-175, 275",'F',73,1],
    ['000001_01_01_004.png',1,1,1,4,"304.019, 230.585, 292.217, 211.789, 304.456, 218.783, 296.151, 223.998","287.217, 206.789, 309.456, 235.585","22.1937, 9.8065","0.572678, 0.42336, 0.445674",3,0,"11, 23","0.666016, 0.666016, 5","512, 512","-175, 275",'F',73,1],
    ['000002_01_01_000.png',2,1,1,0,"238.314, 261.228, 235.858, 268.594, 240.36, 265.729, 234.222, 262.865","229.222, 256.228, 245.36, 273.594","7.76388, 6.77335","0.437715, 0.573812, 0.609054",2,0,"156, 168","0.859375, 0.859375, 5","512, 512","-175, 275",'F',51,2],
    ['000002_01_01_001.png',2,1,1,1,"275.758, 191.194, 261.137, 190.799, 269.83, 185.662, 269.83, 195.541","256.137, 180.662, 280.758, 200.541","14.6261, 9.87891","0.508777, 0.438113, 0.66217",2,0,"170, 182","0.859375, 0.859375, 5","512, 512","-175, 275",'F',51,2],
    ['000002_01_01_002.png',2,1,1,2,"240.988, 215.969, 228.479, 219.186, 235.984, 223.475, 232.41, 212.395","223.479, 207.395, 245.988, 228.475","12.9166, 11.6422","0.43167, 0.47806, 0.702035",2,0,"44, 83","0.976562, 0.976562, 5","512, 512","-175, 275",'F',59,2],
    ['000002_01_01_003.png',2,1,1,3,"313.615, 261.093, 293.88, 259.183, 302.156, 253.135, 300.564, 269.051","288.88, 248.135, 318.615, 274.051","19.8278, 15.9952","0.596974, 0.57036, 0.60468",2,0,"44, 83","0.976562, 0.976562, 5","512, 512","-175, 275",'F',59,2],
    ['000002_01_01_004.png',2,1,1,4,"289.383, 205.23, 277.907, 202.448, 285.21, 198.623, 283.819, 209.055","272.907, 193.623, 294.383, 214.055","11.8077, 10.5244","0.536447, 0.458577, 0.661835",2,0,"44, 83","0.976562, 0.976562, 5","512, 512","-175, 275",'F',59,2],
    ['000003_01_01_000.png',3,1,1,0,"222.361, 259.958, 214.941, 273.809, 222.856, 269.851, 213.456, 264.41","208.456, 254.958, 227.856, 278.809","15.7138, 10.8607","0.395444, 0.586444, 0.612088",2,0,"44, 83","0.976562, 0.976562, 5","512, 512","-175, 275",'F',59,3],
    ['000003_01_01_001.png',3,1,1,1,"324.745, 261.451, 270.106, 260.369, 301.483, 249.008, 300.915, 277.68","265.106, 244.008, 329.745, 282.68","54.6491, 28.6773","0.560316, 0.501742, 0.690962",2,0,"35, 47","0.976562, 0.976562, 5","512, 512","-175, 275",'F',60,3],
    ['000003_01_01_002.png',3,1,1,2,"357.938, 289.428, 364.226, 314.912, 367.536, 300.35, 350.988, 305.976","345.988, 284.428, 372.536, 319.912","26.2489, 17.4787","0.69148, 0.624435, 0.616547",-1,0,"4, 28","0.488281, 0.488281, 2.5","512, 512","-175, 275",'F',19,3],
    ['000003_01_01_003.png',3,1,1,3,"357.938, 289.428, 364.226, 314.912, 367.536, 300.35, 350.988, 305.976","345.988, 284.428, 372.536, 319.912","26.2489, 17.4787","0.69148, 0.624435, 0.616547",-1,0,"4, 28","0.488281, 0.488281, 2.5","512, 512","-175, 275",'F',19,3],
    ['000003_01_01_004.png',3,1,1,4,"357.938, 289.428, 364.226, 314.912, 367.536, 300.35, 350.988, 305.976","345.988, 284.428, 372.536, 319.912","26.2489, 17.4787","0.69148, 0.624435, 0.616547",-1,0,"4, 28","0.488281, 0.488281, 2.5","512, 512","-175, 275",'F',19,3],
    ]


  with tf.io.gfile.GFile(ann_file,'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in ann_info:
      writer.writerow(line)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  dirs = _generate_data(3, 5)
  _generate_csv()


if __name__ == '__main__':
  app.run(main)

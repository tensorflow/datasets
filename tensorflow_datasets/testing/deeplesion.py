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

r"""Generate deeplesion like files, smaller and with random data.

"""

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
    [['File_name','Bounding_boxes', 'Image_size', 'Train_Val_Test'],
    ['000001_01_01_000.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '1'],
    ['000001_01_01_001.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '1'],
    ['000001_01_01_002.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '1'],
    ['000001_01_01_003.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '1'],
    ['000001_01_01_004.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '1'],
    ['000002_01_01_000.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '2'],
    ['000002_01_01_001.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '2'],
    ['000002_01_01_002.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '2'],
    ['000002_01_01_003.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '2'],
    ['000002_01_01_004.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '2'],
    ['000003_01_01_000.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '3'],
    ['000003_01_01_001.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '3'],
    ['000003_01_01_002.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '3'],
    ['000003_01_01_003.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '3'],
    ['000003_01_01_004.png','0.6757578125, 0.5555234375, 0.727609375, 0.624828125','512, 512', '3'],
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

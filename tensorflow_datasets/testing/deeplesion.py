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

from absl import app
from absl import flags

import tensorflow as tf

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils


flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')
FLAGS = flags.FLAGS


def _output_dir():
  return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data',
                      'fake_examples', 'deeplesion', 'Deeplesion-v0.1.0')


def _generate_data():
  """Generate images archive."""

  # Generate images
  images_dir = os.path.join(_output_dir(), 'Images_png')
  images_p1 = os.path.join(images_dir, '000001_01_01')
  images_p2 = os.path.join(images_dir, '000002_01_01')
  if not tf.io.gfile.exists(images_dir):
    tf.io.gfile.makedirs(images_dir)
  if not tf.io.gfile.exists(images_p1):
    tf.io.gfile.makedirs(images_p1)
  if not tf.io.gfile.exists(images_p2):
    tf.io.gfile.makedirs(images_p2)

  for i in range(5):
    image_name = '{:03d}.png'.format(i)
    tf.io.gfile.copy(fake_data_utils.get_random_png(),
                     os.path.join(images_p1, image_name),
                     overwrite=True)
  for i in range(5):
    image_name = '{:03d}.png'.format(i)
    tf.io.gfile.copy(fake_data_utils.get_random_png(),
                     os.path.join(images_p2, image_name),
                     overwrite=True)

def _generate_csv():
# Generate annotations
  csv_dir = _output_dir()
  assert tf.io.gfile.exists(csv_dir), 'Oops, base_folder not exist'

  train_file = os.path.join(csv_dir, 'train.csv')
  valid_file = os.path.join(csv_dir, 'valid.csv')
  
  train_info = \
    [['slice_uid','xmin','ymin','xmax','ymax','label'],
    ['000001_01_01_000.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000001_01_01_001.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000001_01_01_002.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000001_01_01_003.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000001_01_01_004.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],]
  valid_info = \
    [['slice_uid','xmin','ymin','xmax','ymax','label'],
    ['000002_01_01_000.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000002_01_01_001.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000002_01_01_002.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000002_01_01_003.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],
    ['000002_01_01_004.png','0.6757578125','0.5555234375','0.727609375','0.624828125','unknown'],]

  
  with tf.io.gfile.GFile(train_file,'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in train_info:
      writer.writerow(line)

  with tf.io.gfile.GFile(valid_file,'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in valid_info:
      writer.writerow(line)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  _generate_data()
  _generate_csv()


if __name__ == '__main__':
  app.run(main)

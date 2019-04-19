"""Fake Data Generator for Coil-100 Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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
  return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data', 'fake_examples',
                      'coil100')


def create_images(label):
  images_dir = _output_dir()
  if not tf.io.gfile.exists(images_dir):
    tf.io.gfile.makedirs(images_dir)
  for l in label:
    image_name = 'obj1_{}.png'.format(l)
    tf.io.gfile.copy(fake_data_utils.get_random_png(128, 128),
                     os.path.join(images_dir, image_name),
                     overwrite=True)

def main(argv):
  del argv
  label = [x for x in range(0, 25, 5)]
  create_images(label)


if __name__ == '__main__':
  app.run(main)

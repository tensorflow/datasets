r"""Generate fake data for iCoseg dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow.compat.v2 as tf

from absl import app
from absl import flags

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils

flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

FLAGS = flags.FLAGS


def _output_dir(type_of_data):
  if type_of_data == 'jpg':
    return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data', 'fake_examples',
                      'icoseg', 'dataset_public', 'images', 'test_img')
  else:
    return os.path.join(FLAGS.tfds_dir, 'testing', 'test_data', 'fake_examples',
                      'icoseg', 'dataset_public', 'ground_truth', 'test_img')

def _get_png(height, width):
  """Returns png picture."""
  image = fake_data_utils.get_random_picture(height, width)
  png = tf.image.encode_png(image)
  return png

def _get_jpeg(height, width):
  """Returns jpeg picture."""
  image = fake_data_utils.get_random_picture(height, width)
  jpeg = tf.image.encode_jpeg(image)
  return jpeg

def create_lbl(fname):
  jpg_out_path = _output_dir('jpg')
  png_out_path = _output_dir('png')
  if not os.path.exists(jpg_out_path):
    tf.io.gfile.makedirs(jpg_out_path)
  if not os.path.exists(png_out_path):
    tf.io.gfile.makedirs(png_out_path)
  img = _get_jpeg(height=4, width=4)
  img_lbl = _get_png(height=4, width=4)
  jpg_out_path = os.path.join(jpg_out_path, fname) + '.jpg'
  png_out_path = os.path.join(png_out_path, fname) + '.png'
  with tf.io.gfile.GFile(jpg_out_path, 'wb') as out_file:
    out_file.write(img.numpy())
  with tf.io.gfile.GFile(png_out_path, 'wb') as out_file:
    out_file.write(img_lbl.numpy())



def main(argv):
  del argv
  create_lbl('test_img')


if __name__ == '__main__':
  app.run(main)
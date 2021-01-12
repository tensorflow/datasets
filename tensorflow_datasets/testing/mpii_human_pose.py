from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags

import tensorflow as tf
import numpy as np
from tensorflow_datasets.core import lazy_imports
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.testing import fake_data_utils
import tarfile

from tensorflow_datasets.human_pose.mpii.mpii_human_pose_test import DL_EXTRACT_RESULT
from tensorflow_datasets.testing import test_utils
import shutil


flags.DEFINE_string('tfds_dir', py_utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

FLAGS = flags.FLAGS

def main(_):
  base_dir = os.path.join(
    FLAGS.tfds_dir, 'testing', 'test_data', 'fake_examples', 'mpii_human_pose')

  annot_dir = os.path.join(base_dir, "annot")

  annot_path = os.path.join(
    annot_dir,
    "mpii_human_pose_v1_u12_2",
    "mpii_human_pose_v1_u12_1.mat")

  images_subdir = os.path.join(base_dir, "images")
  test_utils.remake_dir(images_subdir)

  with tf.io.gfile.GFile(annot_path, "rb") as fp:
    data = lazy_imports.scipy_io.loadmat(fp)["RELEASE"] # pylint: disable=no-member

  names = data['annolist'][0][0]['image'][0]
  names = [name['name'][0][0][0] for name in names]

  for name in names:
    size = np.random.randint(100, 150, size=(2,))
    image_data = np.random.randint(0, 255)*np.ones(
      tuple(size) + (3,), dtype=np.uint8)
    image = lazy_imports.PIL_Image.fromarray(image_data) # pylint: disable=no-member
    image.save(os.path.join(images_subdir, name))

  shutil.make_archive(
    images_subdir, "gztar", root_dir=base_dir, base_dir="images")
  tf.io.gfile.rmtree(images_subdir)


if __name__ == '__main__':
  app.run(main)

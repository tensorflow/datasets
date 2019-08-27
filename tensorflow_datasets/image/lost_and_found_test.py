"""TODO(lost_and_found): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path, listdir, remove
import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.image import lost_and_found
from tensorflow_datasets.testing.cityscapes import generate_ids, create_zipfile


class LostAndFoundTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = lost_and_found.LostAndFound
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation', 'full']
  SPLITS = {
      "train": 4,  # Number of fake train example
      "test": 2,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
      'image_left': 'leftImg8bit.zip',
      'image_right': 'rightImg8bit.zip',
      'disparity_map': 'disparity.zip',
      'gt': 'gtCoarse.zip'}


if __name__ == "__main__":
  tf.compat.v1.enable_eager_execution()

  # create fake files
  testing.test_utils.remake_dir(
      'tensorflow_datasets/testing/test_data/fake_examples/lost_and_found')
  base_path = 'tensorflow_datasets/testing/test_data/fake_examples/lost_and_found/{}.zip'
  # generate image ids matching between zipfiles
  train_ids = [*generate_ids('01_Turmstr_17'), *generate_ids('02_Goethe_Str_6')]
  test_ids = list(generate_ids('03_Schlossallee_1'))
  splits = {'train': train_ids, 'test': test_ids}
  with tf.Graph().as_default():
    create_zipfile(
        base_path.format('leftImg8bit'), splits_with_ids=splits, suffixes=['leftImg8bit'])
    create_zipfile(
        base_path.format('gtCoarse'), splits_with_ids=splits,
        suffixes=['gtCoarse_instanceIds', 'gtCoarse_labelIds', 'gtCoarse_color'])
    create_zipfile(
        base_path.format('rightImg8bit'), splits_with_ids=splits, suffixes=['rightImg8bit'])
    create_zipfile(
        base_path.format('disparity'), splits_with_ids=splits, suffixes=['disparity'])

  testing.test_main()

  # remove fake files
  testing.test_utils.remake_dir(
      'tensorflow_datasets/testing/test_data/fake_examples/lost_and_found')

"""Script to generate fake 'Lost and Found' data."""
import tensorflow as tf

from tensorflow_datasets.testing.cityscapes import generate_ids, create_zipfile


if __name__ == '__main__':
  example_dir = ('tensorflow_datasets/testing/test_data/fake_examples/'
                 'lost_and_found')
  base_path = example_dir + '/{}.zip'
  # generate image ids matching between zipfiles
  train_ids = [*generate_ids('01_Turmstr_17'),
               *generate_ids('02_Goethe_Str_6')]
  test_ids = list(generate_ids('03_Schlossallee_1'))
  splits = {'train': train_ids, 'test': test_ids}
  with tf.Graph().as_default():
    create_zipfile(base_path.format('leftImg8bit'),
                   splits_with_ids=splits,
                   suffixes=['leftImg8bit'])
    create_zipfile(base_path.format('gtCoarse'),
                   splits_with_ids=splits,
                   suffixes=['gtCoarse_instanceIds',
                             'gtCoarse_labelIds',
                             'gtCoarse_color'])
    create_zipfile(base_path.format('rightImg8bit'),
                   splits_with_ids=splits,
                   suffixes=['rightImg8bit'])
    create_zipfile(base_path.format('disparity'),
                   splits_with_ids=splits,
                   suffixes=['disparity'])

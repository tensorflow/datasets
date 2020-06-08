# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Test for ImageFolder."""

import os
import mock

import tensorflow_datasets.public_api as tfds

_EXAMPLE_DIR = os.path.join(
    tfds.testing.test_utils.fake_examples_dir(), 'image_folder_data')

original_init = tfds.ImageFolder.__init__

def new_init(self, root_dir=None, **kwargs):
  assert root_dir is None
  del kwargs
  original_init(self, root_dir=_EXAMPLE_DIR)


class ImageFolderTest(tfds.testing.DatasetBuilderTestCase):
  """Test for ImageFolder."""

  DATASET_CLASS = tfds.ImageFolder
  SPLITS = {
      'train': 2,
      'test': 6,
  }
  EXAMPLE_DIR = _EXAMPLE_DIR
  MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = False

  @classmethod
  def setUpClass(cls): # pylint:disable = invalid-name
    super(ImageFolderTest, cls).setUpClass()
    cls.DATASET_CLASS.__init__ = new_init
    cls.DATASET_CLASS.download_and_prepare = mock.Mock(return_value=None)

  def test_registered(self):
    self.assertEqual('image_folder', self.builder.name)
    self.assertNotIn(self.builder.name, tfds.list_builders(),
                     'This dataset should not be registered.')

class ImageFolderFunctionTest(tfds.testing.TestCase):
  """Tests for ImageFolder functions"""

  def test_properties(self):
    images = [
        'root_dir/train/label1/img1.png',
        'root_dir/train/label2/img1.png',
        'root_dir/train/label2/img2.png',
        'root_dir/train/label3/img1.png',
        'root_dir/train/label3/img2.png',
        'root_dir/train/label3/img3.png',

        'root_dir/val/label1/img1.png',
        'root_dir/val/label2/img2.png',

        'root_dir/test/label1/img1.png',
        'root_dir/test/label2/img1.png',
        'root_dir/test/label4/img1.png',
    ]

    splits_info = {
        'train': 6,
        'val': 2,
        'test': 3,
    }

    labels = [
        'label1',
        'label2',
        'label3',
        'label4',
    ]

    split_label_img = {
        'train': {
            'label1': ['root_dir/train/label1/img1.png'],
            'label2': ['root_dir/train/label2/img1.png',
                       'root_dir/train/label2/img2.png'],
            'label3': ['root_dir/train/label3/img1.png',
                       'root_dir/train/label3/img2.png',
                       'root_dir/train/label3/img3.png'],
        },
        'val': {
            'label1': ['root_dir/val/label1/img1.png'],
            'label2': ['root_dir/val/label2/img2.png'],
        },
        'test': {
            'label1': ['root_dir/test/label1/img1.png'],
            'label2': ['root_dir/test/label2/img1.png'],
            'label4': ['root_dir/test/label4/img1.png'],
        }
    }


    split_img = tfds.core.custom_dataset.image_folder._get_split_label_images
    fs = tfds.testing.MockFs()
    with fs.mock():
      for file in images:
        fs.add_file(file)

      out1, out2 = split_img('root_dir')
      self.assertCountEqual(split_label_img, out1)
      self.assertCountEqual(labels, out2)

      builder = tfds.ImageFolder('root_dir')
      for split in builder.info.splits.keys():
        self.assertEqual(builder.info.splits[split].num_examples,
                         splits_info[split])

      self.assertEqual(builder.info.features['label'].names, labels)

if __name__ == '__main__':
  tfds.testing.test_main()

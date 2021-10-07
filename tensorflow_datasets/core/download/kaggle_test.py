# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for Kaggle API."""

import os

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core.download import kaggle


class KaggleTest(testing.TestCase):

  def test_competition_download(self):
    with testing.mock_kaggle_api():
      with testing.tmp_dir() as tmp_dir:
        out_path = kaggle.download_kaggle_data('digit-recognizer', tmp_dir)
        self.assertEqual(
            os.fspath(out_path), os.path.join(tmp_dir, 'digit-recognizer'))
        with tf.io.gfile.GFile(os.path.join(out_path, 'output.txt')) as f:
          self.assertEqual('digit-recognizer', f.read())

  def test_dataset_download(self):
    with testing.mock_kaggle_api():
      with testing.tmp_dir() as tmp_dir:
        out_path = kaggle.download_kaggle_data('user/dataset', tmp_dir)
        self.assertIsInstance(out_path, os.PathLike)
        self.assertEqual(
            os.fspath(out_path), os.path.join(tmp_dir, 'user_dataset'))
        with tf.io.gfile.GFile(os.path.join(out_path, 'output.txt')) as f:
          self.assertEqual('user/dataset', f.read())

  def test_competition_download_404(self):
    with testing.mock_kaggle_api(err_msg='404 - Not found'):
      with testing.tmp_dir() as tmp_dir:
        with self.assertRaisesRegex(ValueError,
                                    'Please ensure you have spelled the name'):
          kaggle.download_kaggle_data('digit-recognize', tmp_dir)

  def test_kaggle_type(self):
    self.assertEqual(
        kaggle._get_kaggle_type('digit-recognizer'), 'competitions')
    self.assertEqual(kaggle._get_kaggle_type('author/dataset'), 'datasets')


if __name__ == '__main__':
  testing.test_main()

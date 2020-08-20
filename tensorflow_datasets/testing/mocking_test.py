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

"""Tests for tensorflow_datasets.testing.mocking."""

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import load
from tensorflow_datasets.testing import mocking
from tensorflow_datasets.testing import test_case
from tensorflow_datasets.testing import test_utils

# Import for registration
# pylint: disable=g-bad-import-order,unused-import
from tensorflow_datasets.image_classification import imagenet
from tensorflow_datasets.image_classification import mnist
from tensorflow_datasets.text import lm1b
# pylint: enable=g-bad-import-order,unused-import

tf.enable_v2_behavior()


class MockingTest(test_case.TestCase):

  def test_mocking_imagenet(self):
    with mocking.mock_data():
      ds = load.load('imagenet2012', split='train')
      self.assertEqual(ds.element_spec, {
          'file_name': tf.TensorSpec(shape=(), dtype=tf.string),
          'image': tf.TensorSpec(shape=(None, None, 3), dtype=tf.uint8),
          'label': tf.TensorSpec(shape=(), dtype=tf.int64),
      })
      list(ds.take(3))  # Iteration should work

  def test_mocking_imagenet_decoders(self):
    with mocking.mock_data():
      ds, ds_info = load.load(
          'imagenet2012',
          split='train',
          decoders={'image': decode.SkipDecoding()},
          with_info=True,
      )
      self.assertEqual(ds.element_spec, {
          'file_name': tf.TensorSpec(shape=(), dtype=tf.string),
          'image': tf.TensorSpec(shape=(), dtype=tf.string),  # Encoded images
          'label': tf.TensorSpec(shape=(), dtype=tf.int64),
      })
      for ex in ds.take(10):
        # Image decoding should works
        image = ds_info.features['image'].decode_example(ex['image'])
        image.shape.assert_is_compatible_with((None, None, 3))
        self.assertEqual(image.dtype, tf.uint8)

  def test_mocking_lm1b(self):
    with mocking.mock_data():
      ds = load.load('lm1b/bytes', split='train')
      self.assertEqual(ds.element_spec, {
          'text': tf.TensorSpec(shape=(None,), dtype=tf.int64),
      })
      for ex in ds.take(10):
        self.assertEqual(ex['text'].dtype, tf.int64)
        ex['text'].shape.assert_is_compatible_with((None,))

  def test_custom_as_dataset(self):
    def _as_dataset(self, *args, **kwargs):  # pylint: disable=unused-argument
      return tf.data.Dataset.from_generator(
          lambda: ({  # pylint: disable=g-long-lambda
              'text': t,
          } for t in ['some sentence', 'some other sentence']),
          output_types=self.info.features.dtype,
          output_shapes=self.info.features.shape,
      )

    with mocking.mock_data(as_dataset_fn=_as_dataset):
      ds = load.load('lm1b', split='train')
      out = [ex['text'] for ex in dataset_utils.as_numpy(ds)]
      self.assertEqual(out, [b'some sentence', b'some other sentence'])

  def test_max_values(self):
    with mocking.mock_data(num_examples=50):
      ds = load.load('mnist', split='train')
      self.assertEqual(ds.element_spec, {
          'image': tf.TensorSpec(shape=(28, 28, 1), dtype=tf.uint8),
          'label': tf.TensorSpec(shape=(), dtype=tf.int64),
      })
      for ex in ds.take(50):
        self.assertLessEqual(tf.math.reduce_max(ex['label']).numpy(), 10)
      self.assertEqual(  # Test determinism
          [ex['label'].numpy() for ex in ds.take(5)],
          [1, 9, 2, 5, 3],
      )
      self.assertEqual(  # Iterating twice should yield the same samples
          [ex['label'].numpy() for ex in ds.take(5)],
          [1, 9, 2, 5, 3],
      )


if __name__ == '__main__':
  test_utils.test_main()

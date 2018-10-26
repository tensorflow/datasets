# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.features.image_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import features


class ImageFeatureTest(tf.test.TestCase):

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    specs = features.SpecDict({
        'img': features.Image(),
        'img_shaped': features.Image(shape=(32, 64, 3)),
    })

    img = np.random.randint(256, size=(128, 100, 1), dtype=np.uint8)
    img_shaped = np.random.randint(256, size=(32, 64, 3), dtype=np.uint8)

    decoded_sample = _encode_decode(specs, {
        'img': img,
        'img_shaped': img_shaped,
    })

    self.assertAllEqual(decoded_sample['img'], img)
    self.assertAllEqual(decoded_sample['img_shaped'], img_shaped)

    # 'img' shape can be dynamic
    img2 = np.random.randint(256, size=(64, 200, 1), dtype=np.uint8)
    decoded_sample = _encode_decode(specs, {
        'img': img2,
        'img_shaped': img_shaped,
    })
    self.assertAllEqual(decoded_sample['img'], img2)

    # 'img_shaped' shape should be static
    img_shaped2 = np.random.randint(256, size=(31, 64, 3), dtype=np.uint8)
    with self.assertRaises(ValueError) as err:
      _encode_decode(specs, {
          'img': img2,
          'img_shaped': img_shaped2,
      })
    self.assertIn('Shape (31, 64, 3) do not match', str(err.exception))

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_wrong_input(self):
    specs = features.SpecDict({
        'img': features.Image(),
    })

    # Correct shape/type should succeed
    _encode_decode(specs, {
        'img': np.random.randint(256, size=(128, 128, 1), dtype=np.uint8),
    })
    _encode_decode(specs, {
        'img': np.random.randint(256, size=(64, 64, 1), dtype=np.uint8),
    })

    # Invalid type
    with self.assertRaises(ValueError) as err:
      _encode_decode(specs, {
          'img': np.random.randint(256, size=(128, 128, 1), dtype=np.uint32),
      })
    self.assertIn('Image should be uint8', str(err.exception))

    # Invalid number of dimensions
    with self.assertRaises(ValueError) as err:
      _encode_decode(specs, {
          'img': np.random.randint(256, size=(128, 128), dtype=np.uint8),
      })
    self.assertIn('Shapes should have same length', str(err.exception))

    # Invalid number of channels
    with self.assertRaises(ValueError) as err:
      _encode_decode(specs, {
          'img': np.random.randint(256, size=(128, 128, 3), dtype=np.uint8),
      })
    self.assertIn('Shape (128, 128, 3) do not match', str(err.exception))


def _encode_decode(specs, sample):
  encoded_sample = specs.encode_sample(sample)
  return specs.decode_sample(encoded_sample)

if __name__ == '__main__':
  tf.test.main()

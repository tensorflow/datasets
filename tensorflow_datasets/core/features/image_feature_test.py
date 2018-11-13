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

import os

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import test_utils


class ImageFeatureTest(tf.test.TestCase):

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    features = features_lib.FeaturesDict({
        'img': features_lib.Image(),
        'img_shaped': features_lib.Image(shape=(32, 64, 3)),
        'img_file': features_lib.Image(),
    })

    img = np.random.randint(256, size=(128, 100, 3), dtype=np.uint8)
    img_shaped = np.random.randint(256, size=(32, 64, 3), dtype=np.uint8)

    img_file_path = os.path.join(os.path.dirname(__file__),
                                 '../test_data/6pixels.png')
    img_file_expected_content = [  # see tests_data/README.md
        [[0, 255, 0], [255, 0, 0], [255, 0, 255]],
        [[0, 0, 255], [255, 255, 0], [126, 127, 128]],
    ]

    decoded_sample = test_utils.features_encode_decode(features, {
        'img': img,
        'img_shaped': img_shaped,
        'img_file': img_file_path,
    })

    self.assertAllEqual(decoded_sample['img'], img)
    self.assertAllEqual(decoded_sample['img_shaped'], img_shaped)
    self.assertAllEqual(decoded_sample['img_file'], img_file_expected_content)

    # 'img' shape can be dynamic
    img2 = np.random.randint(256, size=(64, 200, 3), dtype=np.uint8)
    decoded_sample = test_utils.features_encode_decode(features, {
        'img': img2,
        'img_shaped': img_shaped,
        'img_file': img_file_path,
    })
    self.assertAllEqual(decoded_sample['img'], img2)

    # 'img_shaped' shape should be static
    img_shaped2 = np.random.randint(256, size=(31, 64, 3), dtype=np.uint8)
    with self.assertRaisesWithPredicateMatch(ValueError, 'are incompatible'):
      test_utils.features_encode_decode(features, {
          'img': img2,
          'img_shaped': img_shaped2,
          'img_file': img_file_path,
      })

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_wrong_input(self):
    features = features_lib.FeaturesDict({
        'img': features_lib.Image(),
    })

    # Correct shape/type should succeed
    test_utils.features_encode_decode(features, {
        'img': np.random.randint(256, size=(128, 128, 3), dtype=np.uint8),
    })
    test_utils.features_encode_decode(features, {
        'img': np.random.randint(256, size=(64, 64, 3), dtype=np.uint8),
    })

    # Invalid type
    with self.assertRaisesWithPredicateMatch(ValueError, 'should be uint8'):
      test_utils.features_encode_decode(features, {
          'img': np.random.randint(256, size=(128, 128, 3), dtype=np.uint32),
      })

    # Invalid number of dimensions
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             'must have the same rank'):
      test_utils.features_encode_decode(features, {
          'img': np.random.randint(256, size=(128, 128), dtype=np.uint8),
      })

    # Invalid number of channels
    with self.assertRaisesWithPredicateMatch(ValueError, 'are incompatible'):
      test_utils.features_encode_decode(features, {
          'img': np.random.randint(256, size=(128, 128, 1), dtype=np.uint8),
      })


if __name__ == '__main__':
  tf.test.main()

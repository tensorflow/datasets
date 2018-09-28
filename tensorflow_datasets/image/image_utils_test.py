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

"""Tests for tensorflow_datasets.image.image_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.image import image_utils


class ImageUtilsTest(tf.test.TestCase):

  def _random_image(self, shape):
    return np.random.randint(256, size=shape, dtype=np.uint8)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes
  def test_encode_decode(self):
    image_shape = [24, 24, 3]
    image = self._random_image(image_shape)
    image_dict = image_utils.encode_image_as_png_dict(image)
    self.assertEqual("png", image_dict["image/format"])
    self.assertEqual(image_shape, image_dict["image/shape"])
    decoded = image_utils.decode_png(image_dict["image/encoded"], image_shape)
    self.assertAllEqual(image, self.evaluate(decoded))

  def test_image_classification_generator(self):
    image_shape = [24, 24, 3]
    num_examples = 5
    images = [self._random_image(image_shape) for _ in range(num_examples)]
    labels = [np.random.randint(10) for _ in range(num_examples)]
    images_and_labels = zip(images, labels)
    feature_dict_gen = image_utils.image_classification_generator(
        images_and_labels)
    for i, feature_dict in enumerate(feature_dict_gen):
      self.assertEqual(4, len(feature_dict.keys()))
      self.assertEqual(labels[i], feature_dict["target"])
      self.assertEqual("png", feature_dict["input/format"])
      self.assertEqual(image_shape, feature_dict["input/shape"])
      decoded = image_utils.decode_png(feature_dict["input/encoded"],
                                       image_shape)
      self.assertAllEqual(images[i], self.evaluate(decoded))


if __name__ == "__main__":
  tf.test.main()

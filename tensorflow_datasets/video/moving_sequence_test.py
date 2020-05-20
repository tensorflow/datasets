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
"""Tests for moving_sequence."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf

from tensorflow_datasets import testing
import tensorflow_datasets.video.moving_sequence as ms

tf.enable_v2_behavior()


class MovingSequenceTest(tf.test.TestCase):

  @testing.run_in_graph_and_eager_modes()
  def test_images_as_moving_sequence(self):
    h, w = (28, 28)
    sequence_length = 8

    vh = 1 / (sequence_length)
    vw = 1 / (2*(sequence_length))
    image = tf.ones((28, 28, 1), dtype=tf.uint8)

    velocity = tf.constant([vh, vw], dtype=tf.float32)
    out_size = (h + sequence_length, w + sequence_length)
    start_position = tf.constant([0, 0], dtype=tf.float32)

    sequence = ms.image_as_moving_sequence(
        image, start_position=start_position, velocity=velocity,
        output_size=out_size, sequence_length=sequence_length)
    sequence = tf.cast(sequence.image_sequence, tf.float32)

    self.assertAllEqual(*self.evaluate([
        tf.reduce_sum(sequence, axis=(1, 2, 3)),
        tf.fill((sequence_length,),
                tf.reduce_sum(tf.cast(image, tf.float32)))
    ]))

    for i, full_image in enumerate(tf.unstack(sequence, axis=0)):
      j = i // 2
      subimage = full_image[i:i+h, j:j+w]
      n_true = tf.reduce_sum(subimage)
      # allow for pixel rounding errors in each dimension
      self.assertGreaterEqual(self.evaluate(n_true), (h-1)*(w-1))


if __name__ == '__main__':
  testing.test_main()

"""Tests for moving_sequence."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.video.moving_sequence as ms

test_utils.run_test_in_graph_and_eager_modes = tf.contrib.eager.run_test_in_graph_and_eager_modes


class MovingSequenceTest(tf.test.TestCase):
  @test_utils.run_test_in_graph_and_eager_modes()
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

    self.assertAllEqual(
        tf.reduce_sum(sequence, axis=(1, 2, 3)),
        tf.fill((sequence_length,), tf.reduce_sum(tf.cast(image, tf.float32))))

    for i, full_image in enumerate(tf.unstack(sequence, axis=0)):
      j = i // 2
      subimage = full_image[i:i+h, j:j+w]
      n_true = tf.reduce_sum(subimage)
      # allow for pixel rounding errors in each dimension
      self.assertAllEqual(n_true >= (h-1)*(w-1), True)

  def test_dynamic_shape_inputs(self):
    graph = tf.Graph()
    with graph.as_default():
      image_floats = tf.placeholder(
          shape=(None, None, 1), dtype=tf.float32)
      image = tf.cast(image_floats, tf.uint8)
      h, w = 64, 64
      sequence_length = 20
      sequence = ms.image_as_moving_sequence(
          image, output_size=(h, w),
          sequence_length=sequence_length).image_sequence

    with tf.Session(graph=graph) as sess:
      for ih, iw in ((31, 32), (37, 38)):
        image_vals = np.random.uniform(high=255, size=(ih, iw, 1))
        out = sess.run(sequence, feed_dict={image_floats: image_vals})
        self.assertAllEqual(out.shape, [sequence_length, h, w, 1])



if __name__ == '__main__':
  tf.test.main()

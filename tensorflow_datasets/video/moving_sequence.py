# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Provides `image_as_moving_sequence`."""

import collections

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def _create_moving_sequence(image, pad_lefts, total_padding):
  """Create a moving image sequence from the given image a left padding values.

  Args:
    image: [in_h, in_w, n_channels] uint8 array
    pad_lefts: [sequence_length, 2] int32 array of left padding values
    total_padding: tensor of padding values, (pad_h, pad_w)

  Returns:
    [sequence_length, out_h, out_w, n_channels] uint8 image sequence, where
      out_h = in_h + pad_h, out_w = in_w + out_w
  """

  with tf.name_scope("moving_sequence"):

    def get_padded_image(args):
      pad_left, = args
      pad_right = total_padding - pad_left
      padding = tf.stack([pad_left, pad_right], axis=-1)
      z = tf.zeros((1, 2), dtype=pad_left.dtype)
      padding = tf.concat([padding, z], axis=0)
      return tf.pad(image, padding)

    padded_images = tf.map_fn(
        get_padded_image,
        [pad_lefts],
        dtype=tf.uint8,
        infer_shape=False,
    )

  return padded_images


def _get_linear_trajectory(x0, velocity, t):
  """Construct a linear trajectory from x0.

  Args:
    x0: N-D float tensor.
    velocity: N-D float tensor
    t: [sequence_length]-length float tensor

  Returns:
    x: [sequence_length, ndims] float tensor.
  """
  x0 = tf.convert_to_tensor(x0)
  velocity = tf.convert_to_tensor(velocity)
  t = tf.convert_to_tensor(t)
  if x0.shape.ndims != 1:
    raise ValueError("x0 must be a rank 1 tensor")
  if velocity.shape.ndims != 1:
    raise ValueError("velocity must be a rank 1 tensor")
  if t.shape.ndims != 1:
    raise ValueError("t must be a rank 1 tensor")
  x0 = tf.expand_dims(x0, axis=0)
  velocity = tf.expand_dims(velocity, axis=0)
  dx = velocity * tf.expand_dims(t, axis=-1)
  linear_trajectories = x0 + dx
  rank2_error_msg = "linear_trajectories should be a rank 2 tensor"
  assert linear_trajectories.shape.ndims == 2, rank2_error_msg
  return linear_trajectories


def _bounce_to_bbox(points):
  """Bounce potentially unbounded points to [0, 1].

  Bouncing occurs by exact reflection, i.e. a pre-bound point at 1.1 is moved
  to 0.9, -0.2 -> 0.2. This theoretically can occur multiple times, e.g.
  2.3 -> -0.7 -> 0.3

  Implementation
  points <- points % 2
  return min(2 - points, points)

  Args:
    points: float array

  Returns:
    tensor with same shape/dtype but values in [0, 1].
  """
  points = points % 2
  return tf.math.minimum(2 - points, points)


def _get_random_unit_vector(ndims=2, dtype=tf.float32):
  x = tf.random.normal((ndims,), dtype=dtype)
  return x / tf.linalg.norm(x, axis=-1, keepdims=True)


MovingSequence = collections.namedtuple(
    "_MovingSequence",
    ["image_sequence", "trajectory", "start_position", "velocity"])


def image_as_moving_sequence(image,
                             sequence_length=20,
                             output_size=(64, 64),
                             velocity=0.1,
                             start_position=None):
  """Turn simple static images into sequences of the originals bouncing around.

  Adapted from Srivastava et al.
  http://www.cs.toronto.edu/~nitish/unsupervised_video/

  Example usage:
  ```python
  from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
  import tensorflow_datasets as tfds
  from tensorflow_datasets.video import moving_sequence
  tf.enable_v2_behavior()

  def animate(sequence):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    sequence = np.squeeze(sequence, axis=-1)

    fig = plt.figure()
    plt.axis("off")
    ims = [[plt.imshow(im, cmap="gray", animated=True)] for im in sequence]
    # don't remove `anim =` as linter may suggets
    # weird behaviour, plot will freeze on last frame
    anim = animation.ArtistAnimation(
        fig, ims, interval=50, blit=True, repeat_delay=100)

    plt.show()
    plt.close()


  tf.enable_v2_behavior()
  mnist_ds = tfds.load("mnist", split=tfds.Split.TRAIN, as_supervised=True,
                       shuffle_files=True)
  mnist_ds = mnist_ds.repeat().shuffle(1024)

  def map_fn(image, label):
    sequence = moving_sequence.image_as_moving_sequence(
        image, sequence_length=20)
    return sequence.image_sequence

  moving_mnist_ds = mnist_ds.map(map_fn).batch(2).map(
      lambda x: dict(image_sequence=tf.reduce_max(x, axis=0)))

  # # for comparison with test data provided by original authors
  # moving_mnist_ds = tfds.load("moving_mnist", split=tfds.Split.TEST)

  for seq in moving_mnist_ds:
    animate(seq["image_sequence"].numpy())
  ```

  Args:
    image: [in_h, in_w, n_channels] tensor defining the sub-image to be bouncing
      around.
    sequence_length: int, length of sequence.
    output_size: (out_h, out_w) size returned images.
    velocity: scalar speed or 2D velocity of image. If scalar, the 2D velocity
      is randomly generated with this magnitude. This is the normalized distance
      moved each time step by the sub-image, where normalization occurs over the
      feasible distance the sub-image can move e.g if the input image is [10 x
      10] and the output image is [60 x 60], a speed of 0.1 means the sub-image
      moves (60 - 10) * 0.1 = 5 pixels per time step.
    start_position: 2D float32 normalized initial position of each image in [0,
      1]. Randomized uniformly if not given.

  Returns:
    `MovingSequence` namedtuple containing:
        `image_sequence`:
          [sequence_length, out_h, out_w, n_channels] image at each time step.
          padded values are all zero. Same dtype as input image.
        `trajectory`: [sequence_length, 2] float32 in [0, 1]
          2D normalized coordinates of the image at every time step.
        `start_position`: 2D float32 initial position in [0, 1].
          2D normalized initial position of image. Same as input if provided,
          otherwise the randomly value generated.
        `velocity`: 2D float32 normalized velocity. Same as input velocity
          if provided as a 2D tensor, otherwise the random velocity generated.
  """
  ndims = 2
  image = tf.convert_to_tensor(image)
  if image.shape.ndims != 3:
    raise ValueError("image must be rank 3, got %s" % str(image))
  output_size = tf.TensorShape(output_size)
  if len(output_size) != ndims:
    raise ValueError("output_size must have exactly %d elements, got %s" %
                     (ndims, output_size))
  image_shape = tf.shape(image)
  if start_position is None:
    start_position = tf.random.uniform((ndims,), dtype=tf.float32)
  elif start_position.shape != (ndims,):
    raise ValueError("start_positions must (%d,)" % ndims)
  velocity = tf.convert_to_tensor(velocity, dtype=tf.float32)
  if velocity.shape.ndims == 0:
    velocity = _get_random_unit_vector(ndims, tf.float32) * velocity
  elif velocity.shape.ndims != 1:
    raise ValueError("velocity must be rank 0 or rank 1, got %s" % velocity)
  t = tf.range(sequence_length, dtype=tf.float32)
  trajectory = _get_linear_trajectory(start_position, velocity, t)
  trajectory = _bounce_to_bbox(trajectory)

  total_padding = output_size - image_shape[:2]

  if not tf.executing_eagerly():
    cond = tf.compat.v1.assert_greater(total_padding, -1)
    with tf.control_dependencies([cond]):
      total_padding = tf.identity(total_padding)

  sequence_pad_lefts = tf.cast(
      tf.math.round(trajectory * tf.cast(total_padding, tf.float32)), tf.int32)

  sequence = _create_moving_sequence(image, sequence_pad_lefts, total_padding)
  sequence.set_shape([sequence_length] + output_size.as_list() +
                     [image.shape[-1]])
  return MovingSequence(
      image_sequence=sequence,
      trajectory=trajectory,
      start_position=start_position,
      velocity=velocity)

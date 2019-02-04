"""Provides `images_as_moving_sequence`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six
import tensorflow as tf
import tensorflow_datasets as tfds
import collections

_merge_fns = {
    "max": lambda x, y: tf.cast(
        tf.math.maximum(tf.cast(x, tf.int32), tf.cast(y, tf.int32)), tf.uint8)
}


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
      get_padded_image, [pad_lefts], dtype=tf.uint8, infer_shape=False,
      back_prop=False)

  return padded_images


def _create_merged_moving_sequence(
    images, sequence_pad_lefts, image_size, total_padding,
    background=tf.zeros, merge_fn="max"):
  """
  Args:
    images: [n_images, h, w, n_channels] uint8 array
    sequence_pad_lefts: [n_images, sequence_length, 2] int32 array of
      left padding values
    image_size: TensorShape (out_h, out_w)
    total_padding: tensor, images.shape[1:3] - image_size
    background: background image, or callable that takes `shape` and `dtype`
        args.
    merge_fn: "max" for maximum, or callable mapping (seq0, seq1) -> seq, where
        each of seq0, seq1 and seq2 aretensors of the same shape/dtype as
        the output.

  Returns:
    [sequence_length, out_h, out_w, n_channels] overlayed padded sequence.
  """
  if isinstance(merge_fn, six.string_types):
      merge_fn = _merge_fns[merge_fn]
  images = tf.convert_to_tensor(images, dtype=tf.uint8)
  sequence_pad_lefts = tf.convert_to_tensor(sequence_pad_lefts, dtype=tf.int32)
  if images.shape.ndims != 4:
    raise ValueError("`images` must be a rank 4 tensor")
  if sequence_pad_lefts.shape.ndims != 3:
    raise ValueError("`sequence_pad_lefts` must be a rank 3 tensor")
  if total_padding.shape != (2,):
    raise ValueError(
      "`total_padding` must be len 2, got %s"
      % str(total_padding.as_list()))

  n_channels = images.shape[3]
  out_image_shape = (
    [sequence_pad_lefts.shape[1]] +
    image_size.as_list() +
    [n_channels]
  )

  def fn(seq0, args):
    image, pad_lefts = args
    seq1 = _create_moving_sequence(image, pad_lefts, total_padding)
    seq1.set_shape(out_image_shape)
    return merge_fn(seq0, seq1)

  if callable(background):
    background = background(out_image_shape, tf.uint8)

  if background.shape != out_image_shape:
    raise ValueError(
        "background shape should be %s, got %s" %
        (str(background.shape), str(out_image_shape)))
  sequence = tf.foldl(
      fn, [images, sequence_pad_lefts],
      initializer=background,
      back_prop=False,
      name="merged_moving_sequence")

  return sequence


def _get_linear_trajectories(x0, velocity, t):
  """
  Args:
    x0: [n_trajectories, ndims] float tensor.
    velocity: [n_trajectories, ndims] float tensor
    t: [sequence_length] float tensor

  Returns:
    x: [n_trajectories, sequence_length, ndims] float tensor.
  """
  x0 = tf.convert_to_tensor(x0)
  velocity = tf.convert_to_tensor(velocity)
  if x0.shape.ndims != 2:
    raise ValueError("x0 must be a rank 2 tensor")
  if velocity.shape.ndims != 2:
    raise ValueError("velocity must be a rank 2 tensor")
  if t.shape.ndims != 1:
    raise ValueError("t must be a rank 1 tensor")
  x0 = tf.expand_dims(x0, axis=1)
  velocity = tf.expand_dims(velocity, axis=1)
  dx = velocity * tf.expand_dims(tf.expand_dims(t, axis=0), axis=-1)
  linear_trajectories = x0 + dx
  assert linear_trajectories.shape.ndims == 3, \
    "linear_trajectories should be a rank 3 tensor"
  return linear_trajectories


def _bounce_to_bbox(points):
  """
  Bounce potentially unbounded points to [0, 1].

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


def _get_random_velocities(n_velocities, ndims, speed, dtype=tf.float32):
  """Get random velocities with given speed.

  Args:
    n_velocities: int, number of velocities to generate
    ndims: number of dimensions, e.g. 2 for images
    speed: scalar speed for each velocity, or rank 1 tensor giving speed for
      each generated velocity.
    dtype: `tf.DType` of returned tensor

  Returns:
    [n_velocities, ndims] tensor where each row has length speed in a random
      direction.
  """
  velocity = tf.random_normal((n_velocities, ndims), dtype=dtype)
  speed = tf.convert_to_tensor(speed, dtype=dtype)
  if speed.shape.ndims == 1:
    if (
        speed.shape[0].value not in (1, n_velocities) and
        isinstance(n_velocities, int)):
      raise ValueError(
          "If speed is a rank 1 tensor, its length must be 1 or same as "
          "`n_trajectories`, got shape %s" % str(speed.shape))
    speed = tf.expand_dims(speed, axis=-1)
  velocity = velocity * (
    speed / tf.linalg.norm(velocity, axis=-1, keepdims=True))
  return velocity


MovingSequence = collections.namedtuple(
  "MovingSequence",
  ["image_sequence", "trajectories", "start_positions", "velocities"])


def images_as_moving_sequence(
    images, sequence_length=20, output_size=(64, 64),
    speed=0.1, velocities=None, start_positions=None,
    background=tf.zeros, merge_fn='max'):
  """Turn simple static images into sequences of the originals bouncing around.

  Adapted from Srivastava et al.
  http://www.cs.toronto.edu/~nitish/unsupervised_video/

  Example usage:
  ```python
  import tensorflow as tf
  import tensorflow_datasets as tfds
  from tensorflow_datasets.video import moving_sequence

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


  tf.enable_eager_execution()
  mnist_ds = tfds.load("mnist", split=tfds.Split.TRAIN, as_supervised=True)
  mnist_ds = mnist_ds.repeat().shuffle(1024).batch(2, drop_remainder=True)

  def map_fn(image, label):
    sequence = moving_sequence.images_as_moving_sequence(
      image, sequence_length=20)
    return dict(image_sequence=sequence.image_sequence)

  moving_mnist_ds = mnist_ds.map(map_fn)
  # # for comparison with test data provided by original authors
  # moving_mnist_ds = tfds.load("moving_mnist", split=tfds.Split.TEST)

  for seq in moving_mnist_ds:
    animate(seq["image_sequence"].numpy())
  ```

  Args:
    images: [n_images, in_h, in_w, n_channels] uint8 tensor of images.
    sequence_length: int, length of sequence.
    output_size: (out_h, out_w) size returned images.
    speed: float, length of each step. Scalar, or rank 1 tensor with length
        n_images. Ignored if velocities is not `None`.
    velocities: 2D velocity of each image. Randomly generated with speed 0.1
        if not provided. This is the normalized distance moved each time step
        by each image, where normalization occurs over the feasible distance the
        image can move. e.g if the input image is [10 x 10] and the output image
        is [60 x 60], a speed of 0.1 means the image moves (60 - 10) * 0.1 = 5
        pixels per time step.
    start_positions: [n_images, 2] float32 normalized initial position of each
        image in [0, 1]. Randomized uniformly if not given.
    background: background image, or callable that takes `shape` and `dtype`
        args.
    merge_fn: "max" for maximum, or callable mapping (seq0, seq1) -> seq, where
        each of seq0, seq1 and seq2 are tensors of the same shape/dtype as
        the output.

  Returns:
    `MovingSequence` namedtuple containing:
        `image_sequence`:
          [sequence_length, out_h, out_w, n_channels_out] uint8.
          With default arguments for `background`/`merge_fn`,
          `n_channels_out` is the same as `n_channels`
        `trajectories`: [sequence_length, n_images, 2] float32 in [0, 1]
          2D normalized coordinates of each image at every time step.
        `start_positions`: [n_images, 2] float32 initial positions in [0, 1].
          2D normalized initial position of each image.
        `velocities`: [n_images, 2] float32 normalized velocities. Each image
          moves by this amount (give or take due to pixel rounding) per time
          step.
  """
  ndims = 2
  images = tf.convert_to_tensor(images, dtype=tf.uint8)
  output_size = tf.TensorShape(output_size)
  if len(output_size) != ndims:
    raise ValueError("output_size must have exactly %d elements, got %s"
                     % (ndims, output_size))
  image_shape = tf.shape(images)
  n_images = image_shape[0]
  if start_positions is None:
    start_positions = tf.random_uniform((n_images, ndims), dtype=tf.float32)
  elif start_positions.shape.ndims != 2 or start_positions.shape[-1] != ndims:
    raise ValueError("start_positions must be rank 2 and %d-D" % ndims)
  if velocities is None:
    velocities = _get_random_velocities(n_images, ndims, speed, tf.float32)
  t = tf.range(sequence_length, dtype=tf.float32)
  trajectories = _get_linear_trajectories(start_positions, velocities, t)
  trajectories = _bounce_to_bbox(trajectories)

  total_padding = output_size - image_shape[1:3]
  with tf.control_dependencies([tf.assert_non_negative(total_padding)]):
    total_padding = tf.identity(total_padding)

  sequence_pad_lefts = tf.cast(
    tf.math.round(trajectories * tf.cast(total_padding, tf.float32)), tf.int32)

  sequence = _create_merged_moving_sequence(
    images, sequence_pad_lefts, output_size, total_padding,
    background=background, merge_fn=merge_fn)
  return MovingSequence(
    image_sequence=sequence,
    trajectories=trajectories,
    start_positions=start_positions,
    velocities=velocities)

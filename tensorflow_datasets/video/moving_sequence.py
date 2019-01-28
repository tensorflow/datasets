"""
Contains functions for creating moving sequences of smaller bouncing images.

This is a generalization of the code provided by the authors of the moving mnist
dataset.

Example usage:
```python
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_datasets.video.moving_sequence as ms


def animate(sequence):
  import matplotlib.pyplot as plt
  import matplotlib.animation as animation

  fig = plt.figure()
  plt.axis("off")
  ims = [[plt.imshow(im, cmap="gray", animated=True)] for im in sequence]
  # don't remove `anim =` as linter may suggets
  # weird behaviour, plot will freeze on last frame
  anim = animation.ArtistAnimation(
      fig, ims, interval=50, blit=True, repeat_delay=100)

  plt.show()
  plt.close()


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# get a base dataset
base_dataset = tfds.load("fashion_mnist")[tfds.Split.TRAIN]
base_dataset = base_dataset.repeat().shuffle(1024)
dataset = ms.as_moving_sequence_dataset(
    base_dataset,
    speed=lambda n: tf.random_normal(shape=(n,))*0.1,
    image_key="image",
    sequence_length=20)

data = dataset.make_one_shot_iterator().get_next()
sequence = data["image_sequence"]
sequence = tf.squeeze(sequence, axis=-1)  # output_shape [20, 64, 64]

with tf.Session() as sess:
  seq = sess.run(sequence)
  animate(seq)
```

Default arguments in `as_moving_sequence_dataset` are for the original
moving mnist dataset, with
```python
base_dataset = tfds.load("mnist")[tfds.Split.TRAIN].repeat().shuffle(1024)
dataset = ms.as_moving_sequence_dataset(base_dataset)
```

Compare results above with
```
dataset = tfds.load("moving_mnist")[tfds.Split.TEST]
```
(test data provided by original authors)
"""
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
  """See create_moving_sequence."""

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


def create_moving_sequence(image, pad_lefts, total_padding):
  """
  Create a moving image sequence from the given image and left padding values.

  Args:
    image: [h, w, n_channels] uint8 array
    pad_lefts: [sequence_length, 2] int32 array of
      left padding values
    total_padding: TensorShape or list/tuple, (out_h, out_w)

  Returns:
    [sequence_length, out_h, out_w, n_shannels] uint8 sequence.
  """
  total_padding = tf.TensorShape(total_padding)
  pad_lefts = tf.convert_to_tensor(pad_lefts, dtype=tf.float32)
  image = tf.convert_to_tensor(image, dtype=tf.uint8)
  if image.shape.ndims != 3:
    raise ValueError("`image` must be a rank 3 tensor")
  if pad_lefts.shape.ndims != 2:
    raise ValueError("`sequence_pad_lefts` must be a rank 2 tensor")
  if len(total_padding) != 2:
    raise ValueError(
      "`total_padding` must have 2 entres, got %s"
      % str(total_padding.as_list()))
  seq = _create_moving_sequence(
      image, pad_lefts, tf.convert_to_tensor(total_padding))
  ph, pw = total_padding
  h, w, n_channels = image.shape
  sequence_length = pad_lefts.shape[0]
  seq.set_shape((sequence_length, h + ph, w + pw, n_channels))
  return seq


def create_merged_moving_sequence(
    images, sequence_pad_lefts, total_padding, background=tf.zeros,
    merge_fn="max"):
  """
  Args:
    images: [n_images, h, w, n_channels] uint8 array
    sequence_pad_lefts: [n_images, sequence_length, 2] int32 array of
      left padding values
    total_padding: TensorShape (out_h, out_w)
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
    raise ValueError("`sequence_pad_lefts` must be a rank 4 tensor")
  if len(total_padding) != 2:
    raise ValueError(
      "`total_padding` must be len 2, got %s"
      % str(total_padding.as_list()))

  image_res = [i + t for i, t in zip(images.shape[1:3], total_padding)]

  n_channels = images.shape[3]
  out_image_shape = image_res + [n_channels]

  total_padding_tensor = tf.convert_to_tensor(total_padding)

  def fn(seq0, args):
    image, pad_lefts = args
    seq1 = _create_moving_sequence(image, pad_lefts, total_padding_tensor)
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


def get_random_trajectories(
    n_trajectories, sequence_length, ndims=2, speed=0.1,
    dtype=tf.float32):
  """
  Args:
    n_trajectories: int32 number of trajectories
    sequence_length: int32 length of sequence
    ndims: int32 number of dimensions
    speed: (float) length of each step, or rank 1 tensor of length
    `n_trajectories`
      dx = speed*normalized_velocity
    dtype: returned data type. Must be float

  Returns:
    trajectories: [n_trajectories, sequence_length, ndims] `dtype` tensor
      on [0, 1].
    x0: [n_trajectories, ndims] `dtype` tensor of random initial positions
      used
    velocity: [n_trajectories, ndims] `dtype` tensor of random normalized
      velocities used.
  """
  if not dtype.is_floating:
    raise ValueError("dtype must be float")
  speed = tf.convert_to_tensor(speed, dtype=dtype)
  if speed.shape.ndims not in (0, 1):
    raise ValueError("speed must be scalar or rank 1 tensor")

  nt = n_trajectories
  x0 = tf.random.uniform((nt, ndims), dtype=dtype)
  velocity = tf.random_normal((nt, ndims), dtype=dtype)
  speed = tf.convert_to_tensor(speed, dtype=dtype)
  if speed.shape.ndims == 1:
      if speed.shape[0].value not in (1, n_trajectories):
        raise ValueError(
            "If speed is a rank 1 tensor, its length must be 1 or same as "
            "`n_trajectories`, got shape %s" % str(speed.shape))
      speed = tf.expand_dims(speed, axis=-1)
  velocity = velocity * (
    speed / tf.linalg.norm(velocity, axis=-1, keepdims=True))
  t = tf.range(sequence_length, dtype=dtype)
  linear_trajectories = get_linear_trajectories(x0, velocity, t)
  bounced_trajectories = bounce_to_bbox(linear_trajectories)
  return bounced_trajectories, x0, velocity


def get_linear_trajectories(x0, velocity, t):
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


def bounce_to_bbox(points):
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


MovingSequence = collections.namedtuple(
  "MovingSequence",
  ["image_sequence", "trajectories", "start_positions", "velocities"])


def images_to_moving_sequence(
    images, sequence_length=20, speed=0.1, total_padding=(36, 36),
    **kwargs):
  """
  Convert images to a moving sequence.

  Args:
    images: [?, in_h, in_w, n_channels] uint8 tensor of images.
    sequence_length: int, length of sequence.
    speed: float, length of each step. Scalar, or rank 1 tensor with length
        the same as images.shape[0].
    total_padding: (pad_y, pad_x) total padding to be applied in each dimension.
    kwargs: passed to `create_merged_moving_sequence`

  Returns:
    `MovingSequence` namedtuple containing:
        `image_sequence`:
            [sequence_length, in_h + pad_y, in_w + pad_x, n_channels] uint8.
        `trajectories`: [sequence_length, n_images, 2] float32 in [0, 1].
        `start_positions`: [n_images, 2] float32 initial positions in [0, 1].
        `velocities`: [n_images, 2] float32 normalized velocities.
  """
  images = tf.convert_to_tensor(images, dtype=tf.uint8)
  total_padding = tf.TensorShape(total_padding)
  speed = tf.convert_to_tensor(speed, dtype=tf.float32)
  n_images = images.shape[0].value
  trajectories, x0, velocity = get_random_trajectories(
    n_images, sequence_length, ndims=2, speed=speed,
    dtype=tf.float32)
  sequence_pad_lefts = tf.cast(
    trajectories * tf.cast(total_padding, tf.float32),
    tf.int32)
  sequence = create_merged_moving_sequence(
    images, sequence_pad_lefts, total_padding, **kwargs)
  return MovingSequence(
    image_sequence=sequence,
    trajectories=trajectories,
    start_positions=x0,
    velocities=velocity)


def as_moving_sequence_dataset(
    base_dataset, n_images=2, sequence_length=20, total_padding=(36, 36),
    speed=0.1, image_key="image", num_parallel_calls=None, **kwargs):
  """
  Get a moving sequence dataset based on another image dataset.

  This is based on batching the base_dataset and mapping through
  `images_to_moving_sequence`. For good variety, consider shuffling the
  `base_dataset` before calling this rather than shuffling the returned one, as
  this will make it extremely unlikely to get the same combination of images
  in the sequence.

  Example usage:
  ```python
  base_dataset = tfds.load("fashion_mnist")[tfds.Split.TRAIN]
  base_dataset = base_dataset.repeat().shuffle(1024)
  dataset = ms.as_moving_sequence_dataset(
      base_dataset,
      speed=lambda n: tf.random_normal(shape=(n,)) / 10,
      sequence_length=20, total_padding=(36, 36))
  dataset = dataset.batch(128)
  features = dataset.make_one_shot_iterator().get_next()
  images = features["image_sequence"]
  labels = features["label"]
  print(images.shape)  # [128, 20, 64, 64, 1]
  print(labels.shape)  # [2]
  ```

  Args:
    base_dataset: base image dataset to use.
    n_images: number of sub-images making up each frame.
    sequence_length: number of frames per sequences.
    total_padding: TensorShape/list/tuple with [py, px]. Each image will be
        padded with this amount on either left or right (top/bottom) per frame.
    speed: normalized rate(s) at which sub-images move around. Each subimage
        moves this fraction of the available space each frame. Scalar or rank 1
        tensor of length `n_images`, or a callable mapping `n_images` to one
        of the above
    image_key: key from the base dataset containing the images.
    num_parallel_calls: used in dataset `map`.
    kwargs: passed to `images_to_moving_sequence`.

  Returns:
    mapped dataset dict entries
        `image_sequence`: [
            sequence_length, base_im_h + py, base_im_w + px, base_im_channels],
            uint8 tensor.
        `trajectories`: [n_images, sequence_length, 2] float tensor with values
            in range [0, 1] giving position for each base image in each frame.
        `start_positions`: [n_images, 2] starting positions of each subimage.
        `velocities`: [n_images, 2] normalized velocities
    along with other entries from the base dataset
  """
  dtypes = base_dataset.output_types
  if image_key not in dtypes:
      raise ValueError(
          "base_dataset doesn't have key `image_key='%s'`.\nAvailable keys:\n%s"
          % (image_key, "\n".join(dtypes)))
  dtype = dtypes[image_key]
  if dtype != tf.uint8:
    raise TypeError("images must be uint8, got %s" % str(dtype))
  shape = base_dataset.output_shapes[image_key]
  if shape.ndims != 3:
      raise ValueError("images must be rank 3, got %s" % str(shape))

  dataset = base_dataset.batch(n_images, drop_remainder=True)

  def map_fn(data):
    # Do this check inside `map_fn` makes the resulting `Dataset`
    # usable via `make_one_shot_iterator`
    if callable(speed):
      speed_ = speed(n_images)
    else:
      speed_ = speed
    images = data.pop(image_key)
    sequence = images_to_moving_sequence(
        images,
        sequence_length,
        total_padding=total_padding,
        speed=speed_,
        **kwargs)
    return dict(
      image_sequence=sequence.image_sequence,
      trajectories=sequence.trajectories,
      start_positions=sequence.start_positions,
      velocities=sequence.velocities,
      **data
    )

  return dataset.map(map_fn, num_parallel_calls=num_parallel_calls)

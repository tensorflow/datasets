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

"""Common corruptions to images.

Define 15+4 common image corruptions: Gaussian noise, shot noise, impulse_noise,
defocus blur, frosted glass blur, zoom blur, fog, brightness, contrast, elastic,
pixelate, jpeg compression, frost, snow, and motion blur.

4 extra corruptions: gaussian blur, saturate, spatter, and speckle noise.
"""

import io
import subprocess
import tempfile
import numpy as np
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


# To be populated by download_manager
FROST_FILENAMES = []


def _imagemagick_bin():
  return 'imagemagick'  # pylint: disable=unreachable


# /////////////// Corruption Helpers ///////////////


def around_and_astype(x):
  """Round a numpy array, and convert to uint8.

  Args:
    x: numpy array.

  Returns:
    numpy array with dtype uint8.
  """
  return np.around(x).astype(np.uint8)


def disk(radius, alias_blur=0.1, dtype=np.float32):
  """Generating a Gaussian blurring kernel with disk shape.

  Generating a Gaussian blurring kernel with disk shape using cv2 API.

  Args:
    radius: integer, radius of blurring kernel.
    alias_blur: float, standard deviation of Gaussian blurring.
    dtype: data type of kernel

  Returns:
    cv2 object of the Gaussian blurring kernel.
  """
  if radius <= 8:
    length = np.arange(-8, 8 + 1)
    ksize = (3, 3)
  else:
    length = np.arange(-radius, radius + 1)
    ksize = (5, 5)
  x_axis, y_axis = np.meshgrid(length, length)
  aliased_disk = np.array((x_axis**2 + y_axis**2) <= radius**2, dtype=dtype)
  aliased_disk /= np.sum(aliased_disk)
  # supersample disk to antialias
  return tfds.core.lazy_imports.cv2.GaussianBlur(
      aliased_disk, ksize=ksize, sigmaX=alias_blur)


def clipped_zoom(img, zoom_factor):
  """Zoom image with clipping.

  Zoom the central part of the image and clip extra pixels.

  Args:
    img: numpy array, uncorrupted image.
    zoom_factor: numpy array, a sequence of float numbers for zoom factor.

  Returns:
    numpy array, zoomed image after clipping.
  """
  h = img.shape[0]
  ch = int(np.ceil(h / float(zoom_factor)))
  top_h = (h - ch) // 2

  w = img.shape[1]
  cw = int(np.ceil(w / float(zoom_factor)))
  top_w = (w - cw) // 2

  img = tfds.core.lazy_imports.scipy.ndimage.zoom(
      img[top_h:top_h + ch, top_w:top_w + cw], (zoom_factor, zoom_factor, 1),
      order=1)

  # trim off any extra pixels
  trim_top_h = (img.shape[0] - h) // 2
  trim_top_w = (img.shape[1] - w) // 2

  return img[trim_top_h:trim_top_h + h, trim_top_w:trim_top_w + w]


def plasma_fractal(mapsize=512, wibbledecay=3):
  """Generate a heightmap using diamond-square algorithm.

  Modification of the algorithm in
  https://github.com/FLHerne/mapgen/blob/master/diamondsquare.py

  Args:
    mapsize: side length of the heightmap, must be a power of two.
    wibbledecay: integer, decay factor.

  Returns:
    numpy 2d array, side length 'mapsize', of floats in [0,255].
  """
  if mapsize & (mapsize - 1) != 0:
    raise ValueError('mapsize must be a power of two.')
  maparray = np.empty((mapsize, mapsize), dtype=np.float_)
  maparray[0, 0] = 0
  stepsize = mapsize
  wibble = 100

  def wibbledmean(array):
    return array / 4 + wibble * np.random.uniform(-wibble, wibble, array.shape)

  def fillsquares():
    """For each square, calculate middle value as mean of points + wibble."""
    cornerref = maparray[0:mapsize:stepsize, 0:mapsize:stepsize]
    squareaccum = cornerref + np.roll(cornerref, shift=-1, axis=0)
    squareaccum += np.roll(squareaccum, shift=-1, axis=1)
    maparray[stepsize // 2:mapsize:stepsize,
             stepsize // 2:mapsize:stepsize] = wibbledmean(squareaccum)

  def filldiamonds():
    """For each diamond, calculate middle value as meanof points + wibble."""
    mapsize = maparray.shape[0]
    drgrid = maparray[stepsize // 2:mapsize:stepsize,
                      stepsize // 2:mapsize:stepsize]
    ulgrid = maparray[0:mapsize:stepsize, 0:mapsize:stepsize]
    ldrsum = drgrid + np.roll(drgrid, 1, axis=0)
    lulsum = ulgrid + np.roll(ulgrid, -1, axis=1)
    ltsum = ldrsum + lulsum
    maparray[0:mapsize:stepsize,
             stepsize // 2:mapsize:stepsize] = wibbledmean(ltsum)
    tdrsum = drgrid + np.roll(drgrid, 1, axis=1)
    tulsum = ulgrid + np.roll(ulgrid, -1, axis=0)
    ttsum = tdrsum + tulsum
    maparray[stepsize // 2:mapsize:stepsize,
             0:mapsize:stepsize] = wibbledmean(ttsum)

  while stepsize >= 2:
    fillsquares()
    filldiamonds()
    stepsize //= 2
    wibble /= wibbledecay

  maparray -= maparray.min()
  return maparray / maparray.max()


# /////////////// End Corruption Helpers ///////////////

# /////////////// Corruptions ///////////////


def gaussian_noise(x, severity=1):
  """Gaussian noise corruption to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Added Gaussian noise.
  """
  c = [.08, .12, 0.18, 0.26, 0.38][severity - 1]
  x = np.array(x) / 255.
  x_clip = np.clip(x + np.random.normal(size=x.shape, scale=c), 0, 1) * 255
  return around_and_astype(x_clip)


def shot_noise(x, severity=1):
  """Shot noise corruption to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Added shot noise.
  """
  c = [60, 25, 12, 5, 3][severity - 1]
  x = np.array(x) / 255.
  x_clip = np.clip(np.random.poisson(x * c) / float(c), 0, 1) * 255
  return around_and_astype(x_clip)


def impulse_noise(x, severity=1):
  """Impulse noise corruption to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Added impulse noise.
  """
  c = [.03, .06, .09, 0.17, 0.27][severity - 1]
  x = tfds.core.lazy_imports.skimage.util.random_noise(
      np.array(x) / 255., mode='s&p', amount=c)
  x_clip = np.clip(x, 0, 1) * 255
  return around_and_astype(x_clip)


def defocus_blur(x, severity=1):
  """Defocus blurring to images.

  Apply defocus blurring to images using Gaussian kernel.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied defocus blur.
  """
  c = [(3, 0.1), (4, 0.5), (6, 0.5), (8, 0.5), (10, 0.5)][severity - 1]
  x = np.array(x) / 255.
  kernel = disk(radius=c[0], alias_blur=c[1])
  channels = []
  for d in range(3):
    channels.append(tfds.core.lazy_imports.cv2.filter2D(x[:, :, d], -1, kernel))
  channels = np.array(channels).transpose((1, 2, 0))  # 3x224x224 -> 224x224x3
  x_clip = np.clip(channels, 0, 1) * 255
  return around_and_astype(x_clip)


def glass_blur(x, severity=1):
  """Frosted glass blurring to images.

  Apply frosted glass blurring to images by shuffling pixels locally.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied frosted glass blur.
  """
  # sigma, max_delta, iterations
  c = [(0.7, 1, 2), (0.9, 2, 1), (1, 2, 3), (1.1, 3, 2),
       (1.5, 4, 2)][severity - 1]
  x = np.uint8(
      tfds.core.lazy_imports.skimage.filters.gaussian(
          np.array(x) / 255., sigma=c[0], multichannel=True) * 255)

  # locally shuffle pixels
  for _ in range(c[2]):
    for h in range(x.shape[0] - c[1], c[1], -1):
      for w in range(x.shape[1] - c[1], c[1], -1):
        dx, dy = np.random.randint(-c[1], c[1], size=(2,))
        h_prime, w_prime = h + dy, w + dx
        # swap
        x[h, w], x[h_prime, w_prime] = x[h_prime, w_prime], x[h, w]
  x_clip = np.clip(
      tfds.core.lazy_imports.skimage.filters.gaussian(
          x / 255., sigma=c[0], multichannel=True), 0, 1)
  x_clip *= 255
  return around_and_astype(x_clip)


def zoom_blur(x, severity=1):
  """Zoom blurring to images.

  Applying zoom blurring to images by zooming the central part of the images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied zoom blur.
  """
  c = [
      np.arange(1, 1.11, 0.01),
      np.arange(1, 1.16, 0.01),
      np.arange(1, 1.21, 0.02),
      np.arange(1, 1.26, 0.02),
      np.arange(1, 1.31, 0.03)
  ][severity - 1]
  x = (np.array(x) / 255.).astype(np.float32)
  out = np.zeros_like(x)
  for zoom_factor in c:
    out += clipped_zoom(x, zoom_factor)
  x = (x + out) / (len(c) + 1)
  x_clip = np.clip(x, 0, 1) * 255
  return around_and_astype(x_clip)


def fog(x, severity=1):
  """Fog corruption to images.

  Adding fog to images. Fog is generated by diamond-square algorithm.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Added fog.
  """
  c = [(1.5, 2), (2., 2), (2.5, 1.7), (2.5, 1.5), (3., 1.4)][severity - 1]
  x = np.array(x) / 255.
  max_val = x.max()
  mapsize = 512
  shape = x.shape
  max_length = max(shape[0], shape[1])
  if max_length > mapsize:
    mapsize = 2**int(np.ceil(np.log2(float(max_length))))
  tmp = plasma_fractal(mapsize=mapsize, wibbledecay=c[1])
  tmp = tmp[:x.shape[0], :x.shape[1]]
  tmp = tmp[..., np.newaxis]
  x += c[0] * tmp
  x_clip = np.clip(x * max_val / (max_val + c[0]), 0, 1) * 255
  return around_and_astype(x_clip)


def brightness(x, severity=1):
  """Change brightness of images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Changed brightness.
  """
  c = [.1, .2, .3, .4, .5][severity - 1]

  x = np.array(x) / 255.
  x = tfds.core.lazy_imports.skimage.color.rgb2hsv(x)
  x[:, :, 2] = np.clip(x[:, :, 2] + c, 0, 1)
  x = tfds.core.lazy_imports.skimage.color.hsv2rgb(x)
  x_clip = np.clip(x, 0, 1) * 255
  return around_and_astype(x_clip)


def contrast(x, severity=1):
  """Change contrast of images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Changed contrast.
  """
  c = [0.4, .3, .2, .1, .05][severity - 1]

  x = np.array(x) / 255.
  means = np.mean(x, axis=(0, 1), keepdims=True)
  x_clip = np.clip((x - means) * c + means, 0, 1) * 255
  return around_and_astype(x_clip)


def elastic_transform(x, severity=1):
  """Conduct elastic transform to images.

  Elastic transform is performed on small patches of the images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied elastic transform.
  """
  c = [(244 * 2, 244 * 0.7, 244 * 0.1), (244 * 2, 244 * 0.08, 244 * 0.2),
       (244 * 0.05, 244 * 0.01, 244 * 0.02),
       (244 * 0.07, 244 * 0.01, 244 * 0.02),
       (244 * 0.12, 244 * 0.01, 244 * 0.02)][severity - 1]

  image = np.array(x, dtype=np.float32) / 255.
  shape = image.shape
  shape_size = shape[:2]

  # random affine
  center_square = np.float32(shape_size) // 2
  square_size = min(shape_size) // 3
  pts1 = np.float32([
      center_square + square_size,
      [center_square[0] + square_size, center_square[1] - square_size],
      center_square - square_size
  ])
  pts2 = pts1 + np.random.uniform(
      -c[2], c[2], size=pts1.shape).astype(np.float32)
  affine_trans = tfds.core.lazy_imports.cv2.getAffineTransform(pts1, pts2)
  image = tfds.core.lazy_imports.cv2.warpAffine(
      image,
      affine_trans,
      shape_size[::-1],
      borderMode=tfds.core.lazy_imports.cv2.BORDER_REFLECT_101)

  dx = (tfds.core.lazy_imports.skimage.filters.gaussian(
      np.random.uniform(-1, 1, size=shape[:2]),
      c[1],
      mode='reflect',
      truncate=3) * c[0]).astype(np.float32)
  dy = (tfds.core.lazy_imports.skimage.filters.gaussian(
      np.random.uniform(-1, 1, size=shape[:2]),
      c[1],
      mode='reflect',
      truncate=3) * c[0]).astype(np.float32)
  dx, dy = dx[..., np.newaxis], dy[..., np.newaxis]

  x, y, z = np.meshgrid(
      np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
  indices = np.reshape(y + dy,
                       (-1, 1)), np.reshape(x + dx,
                                            (-1, 1)), np.reshape(z, (-1, 1))
  x_clip = np.clip(
      tfds.core.lazy_imports.scipy.ndimage.interpolation.map_coordinates(
          image, indices, order=1, mode='reflect').reshape(shape), 0, 1) * 255
  return around_and_astype(x_clip)


def pixelate(x, severity=1):
  """Pixelate images.

  Conduct pixelating corruptions to images by first shrinking the images and
  then resizing to original size.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied pixelating
    corruption.
  """
  c = [0.6, 0.5, 0.4, 0.3, 0.25][severity - 1]
  shape = x.shape
  x = tfds.core.lazy_imports.PIL_Image.fromarray(x.astype(np.uint8))
  x = x.resize((int(shape[1] * c), int(shape[0] * c)))
  x = x.resize((shape[1], shape[0]))
  return np.asarray(x)


def jpeg_compression(x, severity=1):
  """Conduct jpeg compression to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied jpeg compression.
  """
  c = [25, 18, 15, 10, 7][severity - 1]
  x = tfds.core.lazy_imports.PIL_Image.fromarray(x.astype(np.uint8))
  output = io.BytesIO()
  x.save(output, 'JPEG', quality=c)
  output.seek(0)
  x = tfds.core.lazy_imports.PIL_Image.open(output)
  return np.asarray(x)


def frost(x, severity=1):
  """Apply frost to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied frost.
  """
  c = [(1, 0.4), (0.8, 0.6), (0.7, 0.7), (0.65, 0.7), (0.6, 0.75)][severity - 1]
  filename = FROST_FILENAMES[np.random.randint(5)]
  with tempfile.NamedTemporaryFile() as im_frost:
    tf.io.gfile.copy(filename, im_frost.name, overwrite=True)
    frost_img = tfds.core.lazy_imports.cv2.imread(im_frost.name)
  # randomly crop and convert to rgb
  x_start, y_start = np.random.randint(
      0, frost_img.shape[0] - 224), np.random.randint(0,
                                                      frost_img.shape[1] - 224)
  frost_img = frost_img[x_start:x_start + 224, y_start:y_start + 224][...,
                                                                      [2, 1, 0]]

  x = np.clip(c[0] * np.array(x) + c[1] * frost_img, 0, 255)

  return around_and_astype(x)


def snow(x, severity=1):
  """Apply snow to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied snow.
  """
  cv2 = tfds.core.lazy_imports.cv2
  PIL_Image = tfds.core.lazy_imports.PIL_Image  # pylint: disable=invalid-name
  c = [(0.1, 0.3, 3, 0.5, 10, 4, 0.8), (0.2, 0.3, 2, 0.5, 12, 4, 0.7),
       (0.55, 0.3, 4, 0.9, 12, 8, 0.7), (0.55, 0.3, 4.5, 0.85, 12, 8, 0.65),
       (0.55, 0.3, 2.5, 0.85, 12, 12, 0.55)][severity - 1]

  x = np.array(x, dtype=np.float32) / 255.
  snow_layer = np.random.normal(
      size=x.shape[:2], loc=c[0], scale=c[1])  # [:2] for monochrome

  snow_layer = clipped_zoom(snow_layer[..., np.newaxis], c[2])
  snow_layer[snow_layer < c[3]] = 0

  snow_layer = PIL_Image.fromarray(
      (np.clip(snow_layer.squeeze(), 0, 1) * 255).astype(np.uint8), mode='L')

  with tempfile.NamedTemporaryFile() as im_input:
    with tempfile.NamedTemporaryFile() as im_output:
      snow_layer.save(im_input.name, format='PNG')

      convert_bin = _imagemagick_bin()
      radius = c[4]
      sigma = c[5]
      angle = np.random.uniform(-135, -45)

      subprocess.check_output([
          convert_bin, '-motion-blur', '{}x{}+{}'.format(radius, sigma, angle),
          im_input.name, im_output.name
      ])

      with open(im_output.name, 'rb') as f:
        output = f.read()

  snow_layer = cv2.imdecode(
      np.frombuffer(output, np.uint8), cv2.IMREAD_UNCHANGED) / 255.
  snow_layer = snow_layer[..., np.newaxis]

  x = c[6] * x + (1 - c[6]) * np.maximum(
      x,
      cv2.cvtColor(x, cv2.COLOR_RGB2GRAY).reshape(224, 224, 1) * 1.5 + 0.5)
  x = np.clip(x + snow_layer + np.rot90(snow_layer, k=2), 0, 1) * 255

  return around_and_astype(x)


def motion_blur(x, severity=1):
  """Apply motion blur to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied motion blur.
  """
  c = [(10, 3), (15, 5), (15, 8), (15, 12), (20, 15)][severity - 1]

  x = tfds.core.lazy_imports.PIL_Image.fromarray(x.astype(np.uint8))

  with tempfile.NamedTemporaryFile() as im_input:
    with tempfile.NamedTemporaryFile() as im_output:
      x.save(im_input.name, format='PNG')

      convert_bin = _imagemagick_bin()
      radius = c[0]
      sigma = c[1]
      angle = np.random.uniform(-45, -45)

      subprocess.check_output([
          convert_bin, '-motion-blur', '{}x{}+{}'.format(radius, sigma, angle),
          im_input.name, im_output.name
      ])

      with open(im_output.name, 'rb') as f:
        output = f.read()

  x = tfds.core.lazy_imports.cv2.imdecode(
      np.frombuffer(output, np.uint8),
      tfds.core.lazy_imports.cv2.IMREAD_UNCHANGED)

  if x.shape != (224, 224):
    x = np.clip(x[..., [2, 1, 0]], 0, 255)  # BGR to RGB
  else:  # greyscale to RGB
    x = np.clip(np.array([x, x, x]).transpose((1, 2, 0)), 0, 255)

  return around_and_astype(x)


# /////////////// Extra Corruptions ///////////////


def gaussian_blur(x, severity=1):
  """Apply gaussian blur to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied gaussian blur.
  """
  c = [1, 2, 3, 4, 6][severity - 1]

  x = tfds.core.lazy_imports.skimage.filters.gaussian(
      np.array(x) / 255., sigma=c, multichannel=True)
  x = np.clip(x, 0, 1) * 255

  return around_and_astype(x)


def saturate(x, severity=1):
  """Increase saturation of images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied saturation.
  """
  c = [(0.3, 0), (0.1, 0), (2, 0), (5, 0.1), (20, 0.2)][severity - 1]

  x = np.array(x) / 255.
  x = tfds.core.lazy_imports.skimage.color.rgb2hsv(x)
  x[:, :, 1] = np.clip(x[:, :, 1] * c[0] + c[1], 0, 1)
  x = tfds.core.lazy_imports.skimage.color.hsv2rgb(x)
  x = np.clip(x, 0, 1) * 255

  return around_and_astype(x)


def spatter(x, severity=1):
  """Apply spatter to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied spatter.
  """
  cv2 = tfds.core.lazy_imports.cv2
  skimage = tfds.core.lazy_imports.skimage
  c = [(0.65, 0.3, 4, 0.69, 0.6, 0), (0.65, 0.3, 3, 0.68, 0.6, 0),
       (0.65, 0.3, 2, 0.68, 0.5, 0), (0.65, 0.3, 1, 0.65, 1.5, 1),
       (0.67, 0.4, 1, 0.65, 1.5, 1)][severity - 1]
  x = np.array(x, dtype=np.float32) / 255.

  liquid_layer = np.random.normal(size=x.shape[:2], loc=c[0], scale=c[1])

  liquid_layer = skimage.filters.gaussian(liquid_layer, sigma=c[2])
  liquid_layer[liquid_layer < c[3]] = 0
  if c[5] == 0:
    liquid_layer = (liquid_layer * 255).astype(np.uint8)
    dist = 255 - cv2.Canny(liquid_layer, 50, 150)
    dist = cv2.distanceTransform(dist, cv2.DIST_L2, 5)
    _, dist = cv2.threshold(dist, 20, 20, cv2.THRESH_TRUNC)
    dist = cv2.blur(dist, (3, 3)).astype(np.uint8)
    dist = cv2.equalizeHist(dist)
    #     ker = np.array([[-1,-2,-3],[-2,0,0],[-3,0,1]], dtype=np.float32)
    #     ker -= np.mean(ker)
    ker = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    dist = cv2.filter2D(dist, cv2.CVX_8U, ker)
    dist = cv2.blur(dist, (3, 3)).astype(np.float32)

    m = cv2.cvtColor(liquid_layer * dist, cv2.COLOR_GRAY2BGRA)
    m /= np.max(m, axis=(0, 1))
    m *= c[4]

    # water is pale turqouise
    color = np.concatenate(
        (175 / 255. * np.ones_like(m[..., :1]), 238 / 255. *
         np.ones_like(m[..., :1]), 238 / 255. * np.ones_like(m[..., :1])),
        axis=2)

    color = cv2.cvtColor(color, cv2.COLOR_BGR2BGRA)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2BGRA)

    x = cv2.cvtColor(np.clip(x + m * color, 0, 1), cv2.COLOR_BGRA2BGR) * 255
  else:
    m = np.where(liquid_layer > c[3], 1, 0)
    m = skimage.filters.gaussian(m.astype(np.float32), sigma=c[4])
    m[m < 0.8] = 0
    #         m = np.abs(m) ** (1/c[4])

    # mud brown
    color = np.concatenate(
        (63 / 255. * np.ones_like(x[..., :1]), 42 / 255. *
         np.ones_like(x[..., :1]), 20 / 255. * np.ones_like(x[..., :1])),
        axis=2)

    color *= m[..., np.newaxis]
    x *= (1 - m[..., np.newaxis])

    x = np.clip(x + color, 0, 1) * 255
  return around_and_astype(x)


def speckle_noise(x, severity=1):
  """Apply speckle noise to images.

  Args:
    x: numpy array, uncorrupted image, assumed to have uint8 pixel in [0,255].
    severity: integer, severity of corruption.

  Returns:
    numpy array, image with uint8 pixels in [0,255]. Applied speckle noise.
  """
  c = [.15, .2, 0.35, 0.45, 0.6][severity - 1]

  x = np.array(x) / 255.
  x = np.clip(x + x * np.random.normal(size=x.shape, scale=c), 0, 1) * 255
  return around_and_astype(x)

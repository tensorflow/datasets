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

"""Image feature."""

import dataclasses
import os
import tempfile
from typing import Any, List, Optional

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json
PilImage = Any  # Require lazy deps.

_ENCODE_FN = {
    'png': tf.image.encode_png,
    'jpeg': tf.image.encode_jpeg,
}

_ACCEPTABLE_CHANNELS = {
    'png': (0, 1, 2, 3, 4),
    'jpeg': (0, 1, 3),
}

_ACCEPTABLE_DTYPES = {
    'png': [tf.uint8, tf.uint16, tf.float32],
    'jpeg': [tf.uint8],
    None: [tf.uint8, tf.uint16, tf.float32],
}

THUMBNAIL_SIZE = 128

# Framerate for the `tfds.as_dataframe` visualization
# Could add a framerate kwargs in __init__ to allow datasets to customize
# the output.
_VISU_FRAMERATE = 10


@dataclasses.dataclass
class _ImageEncoder:
  """Utils which encode/decode images."""
  shape: utils.Shape
  dtype: tf.dtypes.DType
  encoding_format: Optional[str]

  # TODO(tfds): Should deprecate the TFGraph runner in favor of simpler
  # implementation
  @utils.memoized_property
  def _runner(self) -> utils.TFGraphRunner:
    return utils.TFGraphRunner()

  def encode_image_or_path(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    if isinstance(image_or_path_or_fobj, np.ndarray):
      encoded_image = self._encode_image(image_or_path_or_fobj)
    elif isinstance(image_or_path_or_fobj, type_utils.PathLikeCls):
      image_or_path_or_fobj = os.fspath(image_or_path_or_fobj)
      with tf.io.gfile.GFile(image_or_path_or_fobj, 'rb') as image_f:
        encoded_image = image_f.read()
    elif isinstance(image_or_path_or_fobj, bytes):
      encoded_image = image_or_path_or_fobj
    else:
      encoded_image = image_or_path_or_fobj.read()
    # If encoding is explicitly set, should verify that bytes match encoding.
    return encoded_image

  def _encode_image(self, np_image: np.ndarray) -> bytes:
    """Returns np_image encoded as jpeg or png."""
    _validate_np_array(np_image, shape=self.shape, dtype=self.dtype)

    # When encoding isn't defined, default to PNG.
    # Should we be more strict about explicitly define the encoding (raise
    # error / warning instead) ?
    # It has created subtle issues for imagenet_corrupted: images are read as
    # JPEG images to apply some processing, but final image saved as PNG
    # (default) rather than JPEG.
    return self._runner.run(_ENCODE_FN[self.encoding_format or 'png'], np_image)

  def decode_image(self, img: tf.Tensor) -> tf.Tensor:
    """Decode the jpeg or png bytes to 3d tensor."""
    img = tf.image.decode_image(img, channels=self.shape[-1], dtype=self.dtype)
    img.set_shape(self.shape)
    return img


class _FloatImageEncoder(_ImageEncoder):
  """Image encoder of float32.

  Wrapper around `_ImageEncoder` which bitcast 1-channel float32 image
  into 4-channels uint8, so image can be encoded to PNG.
  """

  def __init__(
      self,
      *,
      shape: utils.Shape,
      dtype: tf.dtypes.DType,
      encoding_format: str,
  ):
    # Assert that shape and encoding are valid when dtype==tf.float32.
    if shape[-1] != 1:
      raise ValueError(
          'tfds.features.Image only support single-channel for tf.float32. '
          f'Got shape={shape}')
    if encoding_format and encoding_format != 'png':
      raise ValueError(
          'tfds.features.Image only support PNG encoding for tf.float32')
    self._float_shape = shape
    super().__init__(
        shape=shape[:2] + (4,),
        dtype=tf.uint8,
        encoding_format=encoding_format,
    )

  def encode_image_or_path(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    if not isinstance(image_or_path_or_fobj, np.ndarray):
      raise ValueError(
          'tfds.features.Image only support `np.ndarray` for tf.float32 '
          f'images, not paths. Got: {image_or_path_or_fobj!r}')
    return self._encode_image(image_or_path_or_fobj)

  def _encode_image(self, np_image: np.ndarray) -> bytes:
    _validate_np_array(np_image, shape=self._float_shape, dtype=tf.float32)
    # Bitcast 1 channel float32 -> 4 channels uint8
    np_image = np_image.view(np.uint8)
    np_image = super()._encode_image(np_image)
    return np_image

  def decode_image(self, img: tf.Tensor) -> tf.Tensor:
    img = super().decode_image(img)
    # Bitcast 4 channels uint8 -> 1 channel float32
    img = tf.bitcast(img, tf.float32)[..., None]
    return img


class Image(feature.FeatureConnector):
  """`FeatureConnector` for images.

  During `_generate_examples`, the feature connector accept as input any of:

    * `str`: path to a {bmp,gif,jpeg,png} image (ex: `/path/to/img.png`).
    * `np.array`: 3d `np.uint8` array representing an image.
    * A file object containing the png or jpeg encoded image string (ex:
      `io.BytesIO(encoded_img_bytes)`)

  Output:

    `tf.Tensor` of type `tf.uint8` and shape `[height, width, num_channels]`
    for BMP, JPEG, and PNG images and shape `[num_frames, height, width, 3]` for
    GIF images.

  Example:

    * In the `tfds.core.DatasetInfo` object:

    ```python
    features=features.FeaturesDict({
        'input': features.Image(),
        'target': features.Image(shape=(None, None, 1), encoding_format='png'),
    })
    ```

    * During generation:

    ```python
    yield {
        'input': 'path/to/img.jpg',
        'target': np.ones(shape=(64, 64, 1), dtype=np.uint8),
    }
    ```
  """

  # If updating the signature here, LabeledImage and Video should likely be
  # updated too.
  def __init__(
      self,
      *,
      shape: Optional[utils.Shape] = None,
      dtype: Optional[tf.dtypes.DType] = None,
      encoding_format: Optional[str] = None,
      use_colormap: bool = False,
  ):
    """Construct the connector.

    Args:
      shape: tuple of ints or None, the shape of decoded image.
        For GIF images: (num_frames, height, width, channels=3). num_frames,
          height and width can be None.
        For other images: (height, width, channels). height and width can be
          None. See `tf.image.encode_*` for doc on channels parameter. Defaults
          to (None, None, 3).
      dtype: `tf.uint8` (default), `tf.uint16` or `tf.float32`. * `tf.uint16`
        requires png encoding_format. * `tf.float32` only supports
        single-channel image. Internally float images are bitcasted to
        4-channels `tf.uint8` and saved as PNG.
      encoding_format: 'jpeg' or 'png'. Format to serialize `np.ndarray` images
        on disk. If None, encode images as PNG. If image is loaded from
        {bmg,gif,jpeg,png} file, this parameter is ignored, and file original
        encoding is used.
      use_colormap: Only used for gray-scale images. If `True`,
        `tfds.as_dataframe` will display each value in the image with a
        different color.

    Raises:
      ValueError: If the shape is invalid
    """
    # Set and validate values
    shape = shape or (None, None, 3)
    dtype = dtype or tf.uint8
    self._encoding_format = get_and_validate_encoding(encoding_format)
    self._shape = get_and_validate_shape(shape, self._encoding_format)
    self._dtype = get_and_validate_dtype(dtype, self._encoding_format)
    self._use_colormap = _get_and_validate_colormap(use_colormap, self._shape,
                                                    self._dtype,
                                                    self._encoding_format)

    if self._dtype == tf.float32:  # Float images encoded as 4-channels uint8
      encoder_cls = _FloatImageEncoder
    else:
      encoder_cls = _ImageEncoder
    self._image_encoder = encoder_cls(
        shape=self._shape,
        dtype=self._dtype,
        encoding_format=self._encoding_format,
    )

  def get_tensor_info(self):
    # Image is returned as a 3-d uint8 tf.Tensor.
    return feature.TensorInfo(shape=self._shape, dtype=self._dtype)

  def get_serialized_info(self):
    # Only store raw image (includes size).
    return feature.TensorInfo(shape=(), dtype=tf.string)

  def encode_example(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    return self._image_encoder.encode_image_or_path(image_or_path_or_fobj)

  def decode_example(self, example):
    """Reconstruct the image from the tf example."""
    return self._image_encoder.decode_image(example)

  def repr_html(self, ex: np.ndarray) -> str:
    """Images are displayed as thumbnail."""
    # Normalize image and resize
    img = utils.create_thumbnail(ex, use_colormap=self._use_colormap)

    # Convert to base64
    img_str = utils.get_base64(lambda buff: img.save(buff, format='PNG'))

    # Display HTML
    return f'<img src="data:image/png;base64,{img_str}" alt="Img" />'

  def repr_html_batch(self, ex: np.ndarray) -> str:
    """`Sequence(Image())` are displayed as `<video>`."""
    if ex.shape[0] == 1:
      ex = ex.squeeze(axis=0)  # (1, h, w, c) -> (h, w, c)
      return self.repr_html(ex)
    else:
      return make_video_repr_html(ex, use_colormap=self._use_colormap)

  @classmethod
  def from_json_content(cls, value: Json) -> 'Image':
    return cls(
        shape=tuple(value['shape']),
        dtype=tf.dtypes.as_dtype(value['dtype']),
        encoding_format=value['encoding_format'],
        use_colormap=value.get('use_colormap'),
    )

  def to_json_content(self) -> Json:
    return {
        'shape': list(self._shape),
        'dtype': self._dtype.name,
        'encoding_format': self._encoding_format,
        'use_colormap': self._use_colormap
    }


# Visualization Video


def make_video_repr_html(ex, *, use_colormap: bool):
  """Returns the encoded `<video>` or GIF <img/> HTML."""
  # Use GIF to generate a HTML5 compatible video if FFMPEG is not
  # installed on the system.
  images = [
      utils.create_thumbnail(frame, use_colormap=use_colormap) for frame in ex
  ]

  if not images:
    return 'Video with 0 frames.'

  # Display the video HTML (either GIF of mp4 if ffmpeg is installed)
  try:
    utils.ffmpeg_run(['-version'])  # Check for ffmpeg installation.
  except FileNotFoundError:
    # print as `stderr` is displayed poorly on Colab
    print('FFMPEG not detected. Falling back on GIF.')
    return _get_repr_html_gif(images)
  else:
    return _get_repr_html_ffmpeg(images)


def _get_repr_html_ffmpeg(images: List[PilImage]) -> str:
  """Runs ffmpeg to get the mp4 encoded <video> str."""
  # Find number of digits in len to give names.
  num_digits = len(str(len(images))) + 1
  with tempfile.TemporaryDirectory() as video_dir:
    for i, img in enumerate(images):
      f = os.path.join(video_dir, f'img{i:0{num_digits}d}.png')
      img.save(f, format='png')

    ffmpeg_args = [
        '-framerate',
        str(_VISU_FRAMERATE),
        '-i',
        os.path.join(video_dir, f'img%0{num_digits}d.png'),
        # Using native h264 to encode video stream to H.264 codec
        # Default encoding does not seems to be supported by chrome.
        '-vcodec',
        'h264',
        # When outputting H.264, `-pix_fmt yuv420p` maximize compatibility
        # with bad video players.
        # Ref: https://trac.ffmpeg.org/wiki/Slideshow
        '-pix_fmt',
        'yuv420p',
        # ffmpeg require height/width to be even, so we rescale it
        # https://stackoverflow.com/questions/20847674/ffmpeg-libx264-height-not-divisible-by-2
        '-vf',
        'pad=ceil(iw/2)*2:ceil(ih/2)*2',
        # Native encoder cannot encode images of small scale
        # or the the hardware encoder may be busy which raises
        # Error: cannot create compression session
        # so allow software encoding
        # '-allow_sw', '1',
    ]
    video_path = utils.as_path(video_dir) / 'output.mp4'
    ffmpeg_args.append(os.fspath(video_path))
    utils.ffmpeg_run(ffmpeg_args)
    video_str = utils.get_base64(video_path.read_bytes())
  return (f'<video height="{THUMBNAIL_SIZE}" width="175" '
          'controls loop autoplay muted playsinline>'
          f'<source src="data:video/mp4;base64,{video_str}"  type="video/mp4" >'
          '</video>')


def _get_repr_html_gif(images: List[PilImage]) -> str:
  """Get the <img/> str."""

  def write_buff(buff):
    images[0].save(
        buff,
        format='GIF',
        save_all=True,
        append_images=images[1:],
        duration=1000 / _VISU_FRAMERATE,
        loop=0,
    )

  # Convert to base64
  gif_str = utils.get_base64(write_buff)
  return f'<img src="data:image/png;base64,{gif_str}" alt="Gif" />'


# Other image utils


def get_and_validate_encoding(encoding_format):
  """Update the encoding format."""
  supported = _ENCODE_FN.keys()
  if encoding_format and encoding_format not in supported:
    raise ValueError(f'`encoding_format` must be one of {supported}.')
  return encoding_format


def get_and_validate_dtype(dtype, encoding_format):
  """Update the dtype."""
  dtype = tf.as_dtype(dtype)
  acceptable_dtypes = _ACCEPTABLE_DTYPES.get(encoding_format)
  if acceptable_dtypes and dtype not in acceptable_dtypes:
    raise ValueError(f'Acceptable `dtype` for {encoding_format}: '
                     f'{acceptable_dtypes} (was {dtype})')
  return dtype


def get_and_validate_shape(shape, encoding_format):
  """Update the shape."""
  if len(shape) <= 2:
    raise ValueError(f'Image shape should be (h, w, c). Got: {shape}')
  channels = shape[-1]
  acceptable_channels = _ACCEPTABLE_CHANNELS.get(encoding_format)
  if acceptable_channels and channels not in acceptable_channels:
    raise ValueError(f'Acceptable `channels` for {encoding_format}: '
                     f'{acceptable_channels} (was {channels})')
  return tuple(shape)


def _get_and_validate_colormap(use_colormap, shape, dtype, encoding_format):
  """Validate that the given colormap is valid."""
  if use_colormap:
    if encoding_format and encoding_format != 'png':
      raise ValueError(
          f'Colormap is only available for PNG images. Got: {encoding_format}')
    if shape[-1] != 1:
      raise ValueError(
          f'Colormap is only available for gray-scale images. Got: {shape}')
    if not dtype.is_integer:
      raise ValueError(
          f'Colormap is only available for interger images. Got: {dtype}')

  return use_colormap


def _validate_np_array(
    np_array: np.ndarray,
    shape: utils.Shape,
    dtype: tf.dtypes.DType,
) -> None:
  """Validate the numpy array match the expected shape/dtype."""
  if np_array.dtype != dtype.as_numpy_dtype:
    raise ValueError(f'Image dtype should be {dtype.as_numpy_dtype}. '
                     f'Detected: {np_array.dtype}.')
  utils.assert_shape_match(np_array.shape, shape)

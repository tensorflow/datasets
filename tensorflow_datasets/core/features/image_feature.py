# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

from __future__ import annotations

import dataclasses
import functools
import io
import os
import tempfile
from typing import Any, List, Optional, Type, Union

from absl import logging
from etils import epath
import numpy as np
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

try:
  PIL_Image = lazy_imports_lib.lazy_imports.PIL_Image  # pylint: disable=invalid-name
except ImportError:
  PIL_Image = None  # pylint: disable=invalid-name

try:
  cv2 = lazy_imports_lib.lazy_imports.cv2
except ImportError:
  cv2 = None

Json = type_utils.Json
PilImage = Any  # Require lazy deps.


_ENCODE_FN = {
    'png': lambda: tf.image.encode_png,
    'jpeg': lambda: tf.image.encode_jpeg,
}


_ACCEPTABLE_CHANNELS = {
    'png': (0, 1, 2, 3, 4),
    'jpeg': (0, 1, 3),
}


_ACCEPTABLE_DTYPES = {
    'png': [np.uint8, np.uint16, np.float32],
    'jpeg': [np.uint8],
    None: [np.uint8, np.uint16, np.float32],
}


THUMBNAIL_SIZE = 128

# Framerate for the `tfds.as_dataframe` visualization
# Could add a framerate kwargs in __init__ to allow datasets to customize
# the output.
_VISU_FRAMERATE = 10


def check_pil_import_or_raise_error():
  if not PIL_Image:
    raise ImportError('PIL is not installed. PIL is required for this method.')
  return True


@dataclasses.dataclass
class _ImageEncoder:
  """Utils which encode/decode images."""

  shape: utils.Shape
  dtype: type_utils.TfdsDType
  encoding_format: Optional[str]
  np_dtype: Optional[np.dtype] = None

  def __post_init__(self):
    self.np_dtype = dtype_utils.cast_to_numpy(self.dtype)

  # TODO(tfds): Should deprecate the TFGraph runner in favor of simpler
  # implementation
  @functools.cached_property
  def _runner(self) -> utils.TFGraphRunner:
    return utils.TFGraphRunner()

  def encode_image_or_path(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    if isinstance(image_or_path_or_fobj, np.ndarray):
      encoded_image = self._encode_image(image_or_path_or_fobj)
    elif isinstance(image_or_path_or_fobj, epath.PathLikeCls):
      image_or_path_or_fobj = os.fspath(image_or_path_or_fobj)
      with tf.io.gfile.GFile(image_or_path_or_fobj, 'rb') as image_f:
        encoded_image = image_f.read()
    elif isinstance(image_or_path_or_fobj, bytes):
      encoded_image = image_or_path_or_fobj
    elif PIL_Image is not None and isinstance(
        image_or_path_or_fobj, PIL_Image.Image
    ):
      encoded_image = self._encode_pil_image(image_or_path_or_fobj)
    else:
      encoded_image = image_or_path_or_fobj.read()
    # If encoding is explicitly set, should verify that bytes match encoding.
    return encoded_image

  def _encode_image(self, np_image: np.ndarray) -> bytes:
    """Returns np_image encoded as jpeg or png."""
    _validate_np_array(np_image, shape=self.shape, dtype=self.np_dtype)

    # When encoding isn't defined, default to PNG.
    # Should we be more strict about explicitly define the encoding (raise
    # error / warning instead) ?
    # It has created subtle issues for imagenet_corrupted: images are read as
    # JPEG images to apply some processing, but final image saved as PNG
    # (default) rather than JPEG.
    return self._runner.run(
        _ENCODE_FN[self.encoding_format or 'png'](), np_image
    )

  def _encode_pil_image(self, pil_image) -> bytes:
    """Encode a PIL Image object to bytes.

    Args:
      pil_image: A PIL Image object.

    Returns:
      The PIL Image's content in bytes.
    """
    check_pil_import_or_raise_error()
    buffer = io.BytesIO()
    if self.encoding_format and pil_image.format != self.encoding_format:
      raise ValueError(
          f'PIL Image format {pil_image.format} does not match encoding format '
          f'{self.encoding_format}'
      )
    pil_image.save(buffer, format=self.encoding_format or pil_image.format)
    return buffer.getvalue()

  def decode_image(self, img: tf.Tensor) -> tf.Tensor:
    """Decode the jpeg or png bytes to 3d tensor."""
    tf_dtype = tf.dtypes.as_dtype(self.dtype)
    img = tf.image.decode_image(img, channels=self.shape[-1], dtype=tf_dtype)
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
      encoding_format: str,
  ):
    # Assert that shape and encoding are valid when dtype==tf.float32.
    if shape[-1] != 1:
      raise ValueError(
          'tfds.features.Image only support single-channel for tf.float32. '
          f'Got shape={shape}'
      )
    if encoding_format and encoding_format != 'png':
      raise ValueError(
          'tfds.features.Image only support PNG encoding for tf.float32'
      )
    self._float_shape = shape
    super().__init__(
        shape=shape[:2] + (4,),
        dtype=np.uint8,
        encoding_format=encoding_format,
    )

  def encode_image_or_path(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    if not isinstance(image_or_path_or_fobj, np.ndarray):
      raise ValueError(
          'tfds.features.Image only support `np.ndarray` for tf.float32 '
          f'images, not paths. Got: {image_or_path_or_fobj!r}'
      )
    return self._encode_image(image_or_path_or_fobj)

  def _encode_image(self, np_image: np.ndarray) -> bytes:
    _validate_np_array(np_image, shape=self._float_shape, dtype=np.float32)
    # Bitcast 1 channel float32 -> 4 channels uint8
    np_image = np_image.view(np.uint8)
    np_image = super()._encode_image(np_image)
    return np_image

  def decode_image(self, img: tf.Tensor) -> tf.Tensor:
    img = super().decode_image(img)
    # Bitcast 4 channels uint8 -> 1 channel float32
    img = tf.bitcast(img, tf.float32)[..., None]
    return img


class Image(feature_lib.FeatureConnector):
  """`FeatureConnector` for images.

  During `_generate_examples`, the feature connector accept as input any of:

    * `str`: path to a {bmp,gif,jpeg,png} image (ex: `/path/to/img.png`).
    * `np.array`: 3d `np.uint8` array representing an image.
    * A file object containing the png or jpeg encoded image string (ex:
      `io.BytesIO(encoded_img_bytes)`)
    * A `PIL.Image.Image`: PIL Image object.

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
      dtype: Optional[type_utils.TfdsDType] = None,
      encoding_format: Optional[str] = None,
      use_colormap: bool = False,
      doc: feature_lib.DocArg = None,
  ):
    """Construct the connector.

    Args:
      shape: tuple of ints or None, the shape of decoded image. For GIF images:
        (num_frames, height, width, channels=3). num_frames, height and width
        can be None. For other images: (height, width, channels). height and
        width can be None. See `tf.image.encode_*` for doc on channels
        parameter. Defaults to (None, None, 3).
      dtype: `np.uint8` (default), `np.uint16` or `np.float32`. * `np.uint16`
        requires png encoding_format. * `np.float32` only supports
        single-channel image. Internally float images are bitcasted to
        4-channels `np.uint8` and saved as PNG.
      encoding_format: 'jpeg' or 'png'. Format to serialize `np.ndarray` images
        on disk. If None, encode images as PNG. If image is loaded from
        {bmg,gif,jpeg,png} file, this parameter is ignored, and file original
        encoding is used.
      use_colormap: Only used for gray-scale images. If `True`,
        `tfds.as_dataframe` will display each value in the image with a
        different color.
      doc: Documentation of this feature (e.g. description).

    Raises:
      ValueError: If the shape is invalid
    """
    super().__init__(doc=doc)
    # Set and validate values
    shape = shape or (None, None, 3)
    dtype = dtype_utils.cast_to_numpy(dtype or np.uint8)
    self._encoding_format = get_and_validate_encoding(encoding_format)
    self._shape = get_and_validate_shape(shape, self._encoding_format)
    self._dtype = get_and_validate_dtype(dtype, self._encoding_format)
    self._use_colormap = _get_and_validate_colormap(
        use_colormap, self._shape, self._dtype, self._encoding_format
    )

    if self._dtype == np.float32:  # Float images encoded as 4-channels uint8
      self._image_encoder = _FloatImageEncoder(
          shape=self._shape,
          encoding_format=self._encoding_format,
      )
    else:
      self._image_encoder = _ImageEncoder(
          shape=self._shape,
          dtype=self._dtype,
          encoding_format=self._encoding_format,
      )

  @property
  def encoding_format(self) -> Optional[str]:
    return self._encoding_format

  @property
  def use_colormap(self) -> bool:
    return self._use_colormap

  @py_utils.memoize()
  def get_tensor_info(self):
    # Image is returned as a 3-d uint8 tf.Tensor.
    return feature_lib.TensorInfo(shape=self._shape, dtype=self._dtype)

  @py_utils.memoize()
  def get_serialized_info(self):
    # Only store raw image (includes size).
    return feature_lib.TensorInfo(shape=(), dtype=np.object_)

  def encode_example(self, image_or_path_or_fobj):
    """Convert the given image into a dict convertible to tf example."""
    return self._image_encoder.encode_image_or_path(image_or_path_or_fobj)

  def decode_example(self, example):
    """Reconstruct the image with TensorFlow from the tf example."""
    return self._image_encoder.decode_image(example)

  def decode_example_np(self, example: bytes) -> np.ndarray:
    """Reconstruct the image with OpenCV from bytes, or default to PIL."""
    num_channels = self._shape[-1]
    if cv2 is not None:
      return self.decode_example_np_with_opencv(example, num_channels)
    elif PIL_Image is not None:
      logging.log_first_n(
          logging.WARNING,
          (
              'OpenCV is not installed. We recommend using OpenCV because it is'
              ' faster according to our benchmarks. Defaulting to PIL to decode'
              ' images...'
          ),
          1,
      )
      return self.decode_example_np_with_pil(example, num_channels)
    else:
      raise ImportError(
          'Decoding images with NumPy requires either OpenCV or PIL.\nWe'
          ' recommend using OpenCV because it is faster according to our'
          ' benchmarks.\nInstall them with: `pip install opencv-python` or `pip'
          ' install pillow`.'
      )

  def decode_example_np_with_opencv(
      self, example: bytes, num_channels: int
  ) -> np.ndarray:
    """Reconstruct the image with OpenCV from bytes."""
    assert cv2, 'OpenCV is not installed. OpenCV is required for this method.'
    example = np.frombuffer(example, dtype=np.uint8)
    example = cv2.imdecode(example, cv2.IMREAD_UNCHANGED)
    dtype = self.np_dtype if self.np_dtype != np.float32 else np.uint8
    example = example.astype(dtype, copy=False)
    example = _reorder_opencv_channels(example)
    example = _reshape_grayscale_image(example, num_channels)
    # Bitcast 4 channels uint8 -> 1 channel float32.
    if self.np_dtype == np.float32:
      return example.view(np.float32)
    return example

  def decode_example_np_with_pil(
      self, example: bytes, num_channels: int
  ) -> np.ndarray:
    if not PIL_Image:
      raise ImportError(
          'PIL is not installed. PIL is required for this method.'
      )
    bytes_io = io.BytesIO(example)
    with PIL_Image.open(bytes_io) as image:
      dtype = self.np_dtype if self.np_dtype != np.float32 else np.uint8
      image = np.asarray(image, dtype=dtype)
      image = _reshape_grayscale_image(image, num_channels)
      if self.np_dtype == np.uint8:
        return image
      # Bitcast 4 channels uint8 -> 1 channel float32.
      if self.np_dtype == np.float32:
        return image.view(np.float32)
      raise ValueError(
          f'PIL does not handle {self.np_dtype} images. Please, install'
          ' OpenCV instead.'
      )

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
  def from_json_content(
      cls, value: Union[Json, feature_pb2.ImageFeature]
  ) -> 'Image':
    if isinstance(value, dict):
      # For backwards compatibility
      return cls(
          shape=tuple(value['shape']),
          dtype=feature_lib.dtype_from_str(value['dtype']),
          encoding_format=value['encoding_format'],
          use_colormap=value.get('use_colormap'),
      )
    return cls(
        shape=feature_lib.from_shape_proto(value.shape),
        dtype=feature_lib.dtype_from_str(value.dtype),
        encoding_format=value.encoding_format or None,
        use_colormap=value.use_colormap,
    )

  def to_json_content(self) -> feature_pb2.ImageFeature:
    return feature_pb2.ImageFeature(
        shape=feature_lib.to_shape_proto(self._shape),
        dtype=feature_lib.dtype_to_str(self._dtype),
        encoding_format=self._encoding_format,
        use_colormap=self._use_colormap,
    )


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
    video_path = epath.Path(video_dir) / 'output.mp4'
    ffmpeg_args.append(os.fspath(video_path))
    utils.ffmpeg_run(ffmpeg_args)
    video_str = utils.get_base64(video_path.read_bytes())
  return (
      f'<video height="{THUMBNAIL_SIZE}" width="175" '
      'controls loop autoplay muted playsinline>'
      f'<source src="data:video/mp4;base64,{video_str}"  type="video/mp4" >'
      '</video>'
  )


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


def get_and_validate_encoding(encoding_format: Optional[str]) -> Optional[str]:
  """Update the encoding format."""
  supported = _ENCODE_FN.keys()
  if encoding_format and encoding_format not in supported:
    raise ValueError(f'`encoding_format` must be one of {supported}.')
  return encoding_format


def get_and_validate_dtype(dtype: np.dtype, encoding_format: Optional[str]):
  """Update the dtype."""
  acceptable_dtypes = _ACCEPTABLE_DTYPES.get(encoding_format)
  if acceptable_dtypes and dtype not in acceptable_dtypes:
    raise ValueError(
        f'Acceptable `dtype` for {encoding_format}: '
        f'{acceptable_dtypes} (was {dtype})'
    )
  return dtype


def get_and_validate_shape(shape, encoding_format):
  """Update the shape."""
  if len(shape) <= 2:
    raise ValueError(f'Image shape should be (h, w, c). Got: {shape}')
  channels = shape[-1]
  acceptable_channels = _ACCEPTABLE_CHANNELS.get(encoding_format)
  if acceptable_channels and channels not in acceptable_channels:
    raise ValueError(
        f'Acceptable `channels` for {encoding_format}: '
        f'{acceptable_channels} (was {channels})'
    )
  return tuple(shape)


def _get_and_validate_colormap(
    use_colormap, shape, dtype: np.dtype, encoding_format
):
  """Validate that the given colormap is valid."""
  if use_colormap:
    if encoding_format and encoding_format != 'png':
      raise ValueError(
          f'Colormap is only available for PNG images. Got: {encoding_format}'
      )
    if shape[-1] != 1:
      raise ValueError(
          f'Colormap is only available for gray-scale images. Got: {shape}'
      )
    if not dtype_utils.is_integer(dtype):
      raise ValueError(
          f'Colormap is only available for integer images. Got: {dtype}'
      )

  return use_colormap


def _validate_np_array(
    np_array: np.ndarray,
    shape: utils.Shape,
    dtype: Union[np.dtype, Type[np.generic]],
) -> None:
  """Validate the numpy array match the expected shape/dtype."""
  if np_array.dtype != dtype:
    raise ValueError(
        f'Image dtype should be {dtype}. Detected: {np_array.dtype}.'
    )
  utils.assert_shape_match(np_array.shape, shape)


def _reorder_opencv_channels(example: np.ndarray) -> np.ndarray:
  """Restore channels in the expected order: OpenCV uses BGR rather than RGB."""
  if example.ndim == 2:
    return example
  assert cv2, 'OpenCV is not installed. OpenCV is required for this method.'
  num_channels = example.shape[-1]
  if num_channels == 3:
    return cv2.cvtColor(example, cv2.COLOR_BGR2RGB)
  elif num_channels == 4:
    return cv2.cvtColor(example, cv2.COLOR_BGRA2RGBA)
  else:
    return example


def _reshape_grayscale_image(
    image: np.ndarray, num_channels: int
) -> np.ndarray:
  """Reshape grayscale images: (h, w) or (h, w, 1) -> (h, w, num_channels).

  This reproduces the transformation TensorFlow applies to grayscale images.

  Args:
    image: An image as an np.ndarray.
    num_channels: The number of channels in the image feature.

  Returns:
    The reshaped image.
  """
  if image.ndim == 2:  # (h, w)
    return np.repeat(image[..., None], num_channels, axis=-1)
  if image.ndim == 3 and image.shape[2] == 1:  # (h, w, 1)
    return np.repeat(image, num_channels, axis=-1)
  return image

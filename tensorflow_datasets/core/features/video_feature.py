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

"""Video feature."""

import os
import tempfile
from typing import Sequence, Optional, Union

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json


class Video(sequence_feature.Sequence):
  """`FeatureConnector` for videos, encoding frames individually on disk.

  Video: The image connector accepts as input a 4 dimensional `tf.uint8` array
  representing a video, a sequence of paths to encoded frames, or a path or a
  file object that can be decoded with ffmpeg. Note that not all formats in
  ffmpeg support reading from pipes, so providing a file object might fail.
  Furthermore, if a path is given that is not on the local file system, we first
  copy it to a temporary local file before passing it to ffmpeg.

  Output:
    video: tf.Tensor of type `tf.uint8` and shape
      [num_frames, height, width, channels], where channels must be 1 or 3

  Example:

    * In the DatasetInfo object:

    ```
    features=features.FeatureDict({
        'video': features.Video(shape=(None, 64, 64, 3)),
    })
    ```

    * During generation, you can use any of:

    ```
    yield {
        'video': np.ones(shape=(128, 64, 64, 3), dtype=np.uint8),
    }
    ```

    or list of frames:

    ```
    yield {
        'video': ['path/to/frame001.png', 'path/to/frame002.png'],
    }
    ```

    or path to video (including `os.PathLike` objects):

    ```
    yield {
        'video': '/path/to/video.avi',
    }
    ```

    or file object (or `bytes`):

    ```
    yield {
        'video': tf.io.gfile.GFile('/complex/path/video.avi'),
    }
    ```

  """

  def __init__(
      self,
      shape: Sequence[Optional[int]],
      encoding_format: str = 'png',
      ffmpeg_extra_args: Sequence[str] = (),
      use_colormap: bool = False,
      dtype=tf.uint8,
  ):
    """Initializes the connector.

    Args:
      shape: tuple of ints, the shape of the video (num_frames, height, width,
        channels), where channels is 1 or 3.
      encoding_format: The video is stored as a sequence of encoded images. You
        can use any encoding format supported by image_feature.Feature.
      ffmpeg_extra_args: A sequence of additional args to be passed to the
        ffmpeg binary. Specifically, ffmpeg will be called as: `` ffmpeg -i
          <input_file> <ffmpeg_extra_args> %010d.<encoding_format> ``
      use_colormap: Forwarded to `tfds.features.Image`. If `True`,
        `tfds.as_dataframe` will display each value in the image with a
        different color.
      dtype: tf.uint16 or tf.uint8 (default). tf.uint16 can be used only with
        png encoding_format

    Raises:
      ValueError: If the shape is invalid
    """
    shape = tuple(shape)
    if len(shape) != 4:
      raise ValueError('Video shape should be of rank 4')
    self._encoding_format = encoding_format
    self._extra_ffmpeg_args = list(ffmpeg_extra_args or [])
    super(Video, self).__init__(
        image_feature.Image(
            shape=shape[1:],
            dtype=dtype,
            encoding_format=encoding_format,
            use_colormap=use_colormap,
        ),
        length=shape[0],
    )

  def _ffmpeg_decode(self, path_or_fobj):
    if isinstance(path_or_fobj, type_utils.PathLikeCls):
      ffmpeg_args = ['-i', os.fspath(path_or_fobj)]
      ffmpeg_stdin = None
    else:
      ffmpeg_args = ['-i', 'pipe:0']
      ffmpeg_stdin = path_or_fobj.read()
    ffmpeg_args += self._extra_ffmpeg_args

    with tempfile.TemporaryDirectory() as ffmpeg_dir:
      out_pattern = os.path.join(ffmpeg_dir, f'%010d.{self._encoding_format}')
      ffmpeg_args.append(out_pattern)
      utils.ffmpeg_run(ffmpeg_args, ffmpeg_stdin)
      frames = [  # Load all encoded images
          p.read_bytes() for p in sorted(utils.as_path(ffmpeg_dir).iterdir())
      ]
    return frames

  def encode_example(self, video_or_path_or_fobj):
    """Converts the given image into a dict convertible to tf example."""
    if isinstance(video_or_path_or_fobj, type_utils.PathLikeCls):
      video_or_path_or_fobj = os.fspath(video_or_path_or_fobj)
      if not os.path.isfile(video_or_path_or_fobj):
        _, video_temp_path = tempfile.mkstemp()
        try:
          tf.io.gfile.copy(
              video_or_path_or_fobj, video_temp_path, overwrite=True)
          encoded_video = self._ffmpeg_decode(video_temp_path)
        finally:
          os.unlink(video_temp_path)
      else:
        encoded_video = self._ffmpeg_decode(video_or_path_or_fobj)
    elif isinstance(video_or_path_or_fobj, bytes):
      with tempfile.TemporaryDirectory() as tmpdirname:
        video_temp_path = os.path.join(tmpdirname, 'video')
        with tf.io.gfile.GFile(video_temp_path, 'wb') as f:
          f.write(video_or_path_or_fobj)
        encoded_video = self._ffmpeg_decode(video_temp_path)
    elif hasattr(video_or_path_or_fobj, 'read'):
      encoded_video = self._ffmpeg_decode(video_or_path_or_fobj)
    else:  # List of images, np.array,...
      encoded_video = video_or_path_or_fobj
    return super(Video, self).encode_example(encoded_video)

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.VideoFeature]) -> 'Video':
    if isinstance(value, dict):
      # For backwards compatibility
      shape = tuple(value['shape'])
      encoding_format = value['encoding_format']
      ffmpeg_extra_args = value['ffmpeg_extra_args']
      return cls(shape, encoding_format, ffmpeg_extra_args)
    return cls(
        shape=feature_lib.from_shape_proto(value.shape),
        dtype=feature_lib.parse_dtype(value.dtype),
        encoding_format=value.encoding_format or None,
        use_colormap=value.use_colormap,
        ffmpeg_extra_args=value.ffmpeg_extra_args,
    )

  def to_json_content(self) -> feature_pb2.VideoFeature:
    return feature_pb2.VideoFeature(
        shape=feature_lib.to_shape_proto(self.shape),
        dtype=feature_lib.encode_dtype(self.dtype),
        encoding_format=self._encoding_format,
        use_colormap=self._use_colormap,
        ffmpeg_extra_args=self._extra_ffmpeg_args,
    )

  def repr_html(self, ex: np.ndarray) -> str:
    """Video are displayed as `<video>`."""
    return image_feature.make_video_repr_html(
        ex,
        use_colormap=self.feature._use_colormap  # pylint: disable=protected-access  # pytype: disable=attribute-error
    )

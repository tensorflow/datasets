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

"""Video feature."""

import os
import subprocess
import tempfile

import six
import tensorflow.compat.v2 as tf
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature


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

    or path to video:

    ```
    yield {
        'video': '/path/to/video.avi',
    }
    ```

    or file object:

    ```
    yield {
        'video': tf.io.gfile.GFile('/complex/path/video.avi'),
    }
    ```

  """

  def __init__(self, shape, encoding_format='png', ffmpeg_extra_args=()):
    """Initializes the connector.

    Args:
      shape: tuple of ints, the shape of the video (num_frames, height, width,
        channels), where channels is 1 or 3.
      encoding_format: The video is stored as a sequence of encoded images.
        You can use any encoding format supported by image_feature.Feature.
      ffmpeg_extra_args: A sequence of additional args to be passed to the
        ffmpeg binary. Specifically, ffmpeg will be called as:
          ``
          ffmpeg -i <input_file> <ffmpeg_extra_args> %010d.<encoding_format>
          ``
    Raises:
      ValueError: If the shape is invalid
    """
    shape = tuple(shape)
    if len(shape) != 4:
      raise ValueError('Video shape should be of rank 4')
    self._encoding_format = encoding_format
    self._extra_ffmpeg_args = list(ffmpeg_extra_args or [])
    super(Video, self).__init__(
        image_feature.Image(shape=shape[1:], encoding_format=encoding_format),
        length=shape[0],
    )

  @property
  def _ffmpeg_path(self):
    return 'ffmpeg'


  def _ffmpeg_decode(self, path_or_fobj):
    if isinstance(path_or_fobj, six.string_types):
      ffmpeg_args = [self._ffmpeg_path, '-i', path_or_fobj]
      ffmpeg_stdin = None
    else:
      ffmpeg_args = [self._ffmpeg_path, '-i', 'pipe:0']
      ffmpeg_stdin = path_or_fobj.read()

    ffmpeg_dir = tempfile.mkdtemp()
    output_pattern = os.path.join(ffmpeg_dir, '%010d.' + self._encoding_format)
    ffmpeg_args += self._extra_ffmpeg_args
    ffmpeg_args.append(output_pattern)
    try:
      process = subprocess.Popen(ffmpeg_args,
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
      stdout_data, stderr_data = process.communicate(ffmpeg_stdin)
      ffmpeg_ret_code = process.returncode
      if ffmpeg_ret_code:
        raise ValueError(
            'ffmpeg returned error code {}, command={}\n'
            'stdout={}\nstderr={}\n'.format(ffmpeg_ret_code,
                                            ' '.join(ffmpeg_args),
                                            stdout_data,
                                            stderr_data))
      frames = []
      for image_name in sorted(tf.io.gfile.listdir(ffmpeg_dir)):
        image_path = os.path.join(ffmpeg_dir, image_name)
        with tf.io.gfile.GFile(image_path, 'rb') as frame_file:
          frames.append(six.BytesIO(frame_file.read()))
      return frames
    except OSError as exception:
      raise IOError(
          'It seems that ffmpeg is not installed on the system. Please follow '
          'the instrutions at https://ffmpeg.org/. '
          'Original exception: {}'.format(exception))
    finally:
      tf.io.gfile.rmtree(ffmpeg_dir)

  def encode_example(self, video_or_path_or_fobj):
    """Converts the given image into a dict convertible to tf example."""
    if isinstance(video_or_path_or_fobj, six.string_types):
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
    else:
      encoded_video = video_or_path_or_fobj
    return super(Video, self).encode_example(encoded_video)

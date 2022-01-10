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

"""Audio feature."""

import os
from typing import Optional, Union
import wave

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json
Encoding = tensor_feature.Encoding


class Audio(tensor_feature.Tensor):
  """`tfds.features.FeatureConnector` for audio.

  In `_generate_examples`, Audio accept:

  * A `np.ndarray` of shape `(length,)` or `(length, channels)`
  * A path to a `.mp3`, `.wav`,... file.
  * A file-object (e.g. `with path.open('rb') as fobj:`)

  By default, Audio features are decoded as the raw integer wave form
  `tf.Tensor(shape=(None,), dtype=tf.int64)`.
  """

  def __init__(
      self,
      *,
      file_format: Optional[str] = None,
      shape: utils.Shape = (None,),
      dtype: tf.dtypes.DType = tf.int64,
      sample_rate: Optional[int] = None,
      encoding: Union[str, Encoding] = Encoding.NONE,
  ):
    """Constructs the connector.

    Args:
      file_format: `str`, the audio file format. Can be any format ffmpeg
        understands. If `None`, will attempt to infer from the file extension.
      shape: `tuple`, shape of the data.
      dtype: The dtype of the data.
      sample_rate: `int`, additional metadata exposed to the user through
        `info.features['audio'].sample_rate`. This value isn't used neither in
        encoding nor decoding.
      encoding: Internal encoding. See `tfds.features.Encoding` for available
        values.
    """
    self._file_format = file_format
    if len(shape) > 2:
      raise ValueError('Audio shape should be either (length,) or '
                       f'(length, num_channels), got {shape}.')
    self._shape = shape
    self._sample_rate = sample_rate
    super().__init__(shape=shape, dtype=dtype, encoding=encoding)

  def _encode_file(self, fobj, file_format):
    audio_segment = lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
        fobj, format=file_format)
    np_dtype = np.dtype(self.numpy_dtype)
    raw_samples = np.array(audio_segment.get_array_of_samples())
    raw_samples = raw_samples.astype(np_dtype)
    if audio_segment.channels > 1:
      audio_data = raw_samples.reshape((-1, audio_segment.channels))
    else:
      audio_data = raw_samples
    return super().encode_example(audio_data)

  def encode_example(self, audio_or_path_or_fobj):
    if isinstance(audio_or_path_or_fobj, (np.ndarray, list)):
      return audio_or_path_or_fobj
    elif isinstance(audio_or_path_or_fobj, type_utils.PathLikeCls):
      filename = os.fspath(audio_or_path_or_fobj)
      file_format = self._file_format or filename.split('.')[-1]
      with tf.io.gfile.GFile(filename, 'rb') as audio_f:
        try:
          return self._encode_file(audio_f, file_format)
        except Exception as e:  # pylint: disable=broad-except
          utils.reraise(e, prefix=f'Error for {filename}: ')
    else:
      return self._encode_file(audio_or_path_or_fobj, self._file_format)

  @property
  def sample_rate(self):
    """Returns the `sample_rate` metadata associated with the dataset."""
    return self._sample_rate

  def repr_html(self, ex: np.ndarray) -> str:
    """Audio are displayed in the player."""
    if self.sample_rate:
      rate = self.sample_rate
    else:
      # We should display an error message once to warn the user the sample
      # rate was auto-infered. Requirements:
      # * Should appear only once (even though repr_html is called once per
      #   examples)
      # * Ideally should appear on Colab (while `logging.warning` is hidden
      #   by default)
      rate = 16000

    audio_str = utils.get_base64(lambda buff: _save_wav(buff, ex, rate))
    return (f'<audio controls src="data:audio/ogg;base64,{audio_str}" '
            ' controlsList="nodownload" />')

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.AudioFeature]) -> 'Audio':
    if isinstance(value, dict):
      # For backwards compatibility
      return cls(
          file_format=value['file_format'],
          shape=tuple(value['shape']),
          dtype=tf.dtypes.as_dtype(value['dtype']),
          sample_rate=value['sample_rate'],
      )
    return cls(
        shape=feature_lib.from_shape_proto(value.shape),
        dtype=feature_lib.parse_dtype(value.dtype),
        file_format=value.file_format or None,
        sample_rate=value.sample_rate,
        encoding=value.encoding)

  def to_json_content(self) -> feature_pb2.AudioFeature:
    return feature_pb2.AudioFeature(
        shape=feature_lib.to_shape_proto(self.shape),
        dtype=feature_lib.encode_dtype(self.dtype),
        file_format=self._file_format,
        sample_rate=self._sample_rate,
        encoding=self._encoding.name,
    )


def _save_wav(buff, data, rate) -> None:
  """Transform a numpy array to a PCM bytestring."""
  # Code inspired from `IPython.display.Audio`
  data = np.array(data, dtype=float)

  bit_depth = 16
  max_sample_value = int(2**(bit_depth - 1)) - 1

  num_channels = data.shape[1] if len(data.shape) > 1 else 1
  scaled = np.int16(data / np.max(np.abs(data)) * max_sample_value)
  # The WAVE spec expects little-endian integers of "sampwidth" bytes each.
  # Numpy's `astype` accepts array-protocol type strings, so we specify:
  #  - '<' to indicate little endian
  #  - 'i' to specify signed integer
  #  - the number of bytes used to represent each integer
  # See: https://numpy.org/doc/stable/reference/arrays.dtypes.html
  encoded_wav = scaled.astype(f'<i{bit_depth // 8}', copy=False).tobytes()

  with wave.open(buff, mode='wb') as waveobj:
    waveobj.setnchannels(num_channels)
    waveobj.setframerate(rate)
    waveobj.setsampwidth(bit_depth // 8)
    waveobj.setcomptype('NONE', 'NONE')
    waveobj.writeframes(encoded_wav)

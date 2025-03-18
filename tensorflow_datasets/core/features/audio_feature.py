# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from __future__ import annotations

import abc
import enum
import functools
import io
import os
from typing import BinaryIO, Optional, Union
import wave

from absl import logging
from etils import epath
import numpy as np
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

Json = type_utils.Json
Encoding = tensor_feature.Encoding


class _TfioFileFormat(enum.Enum):
  """Format of the audio files supported for decoding by `tensorflow_io`.

  Attributes:
    FLAC: Free Lossless Audio Codec
  """

  FLAC = 'flac'


@functools.lru_cache(maxsize=None)
def _tfio_decode_fn():
  tfio = lazy_imports_lib.lazy_imports.tensorflow_io

  return {
      _TfioFileFormat.FLAC: tfio.audio.decode_flac,
  }


@functools.lru_cache(maxsize=None)
def _tfio_acceptable_dtypes():
  return {
      _TfioFileFormat.FLAC: [tf.uint8, tf.int16, tf.int32],
  }


class _AudioDecoder(abc.ABC):
  """Utils which encode/decode audios."""

  def __init__(
      self, file_format: Optional[str], np_dtype: np.dtype, shape: utils.Shape
  ):
    """Constructs the lazy audio decoder.

    Args:
      file_format: `str`, the audio file format. Can be any format ffmpeg
        understands. If in `_TfioFileFormat`, then will use `tensorflow_io`
      np_dtype: The numpy dtype of the data.
      shape: `tuple`, shape of the data.
    """
    self._file_format = file_format
    self._np_dtype = np_dtype
    self._dtype = tf.dtypes.as_dtype(self._np_dtype)
    self._shape = shape
    self._channels = shape[1] if len(shape) > 1 else 1

  @abc.abstractmethod
  def encode_audio(
      self, fobj: BinaryIO, file_format: Optional[str]
  ) -> np.ndarray:
    """Encode audio into numpy array for storing as a tf-example."""
    raise NotImplementedError

  @abc.abstractmethod
  def decode_audio(self, audio_tensor: tf.Tensor) -> tf.Tensor:
    """Decode audio from the loaded tf-example."""
    raise NotImplementedError


def _pydub_load_audio(
    fobj: BinaryIO, file_format: Optional[str], channels: int
) -> np.ndarray:
  """Read audio using pydub library."""
  pydub = lazy_imports_lib.lazy_imports.pydub

  audio_segment = pydub.AudioSegment.from_file(fobj, format=file_format)
  if channels != audio_segment.channels:
    logging.info(
        'Modifying audio segment from %s to %s channel(s).',
        audio_segment.channels,
        channels,
    )
    audio_segment = audio_segment.set_channels(channels)

  raw_samples = np.array(audio_segment.get_array_of_samples())

  if audio_segment.channels > 1:
    return raw_samples.reshape((-1, audio_segment.channels))
  else:
    return raw_samples


def _pydub_decode_audio(
    audio_tensor: tf.Tensor,
    file_format_tensor: tf.experimental.Optional,
    channels: int,
) -> np.ndarray:
  """Decode audio from tf.Tensor using pydub library."""
  fobj = io.BytesIO(audio_tensor.numpy())
  if file_format_tensor.has_value():
    file_format = file_format_tensor.get_value().numpy()
  else:
    file_format = None
  return _pydub_load_audio(fobj, file_format, channels)


class _LazyDecoder(_AudioDecoder):
  """Read audio during decoding."""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    try:
      self._tfio_file_format = _TfioFileFormat(self._file_format)
    except ValueError:
      self._tfio_file_format = None
      logging.warning(
          (
              'Using lazy encoding with `file_format=%s` might be very slow'
              ' when reading prepared dataset. Consider using one of these file'
              ' formats: %s'
          ),
          self._file_format,
          [item.value for item in _TfioFileFormat],
      )

    if self._tfio_file_format:
      acceptable_dtypes = _tfio_acceptable_dtypes()[self._tfio_file_format]
      if self._dtype not in acceptable_dtypes:
        raise ValueError(
            f'Acceptable `dtype` for lazy loading {self._file_format}: '
            f'{acceptable_dtypes} (was {self._dtype})'
        )

  def encode_audio(
      self, fobj: BinaryIO, file_format: Optional[str]
  ) -> np.ndarray:
    return np.array(fobj.read(), dtype=tf.string.as_numpy_dtype)

  def decode_audio(self, audio_tensor: tf.Tensor) -> tf.Tensor:
    if self._tfio_file_format:
      decoded_audio_tensor = _tfio_decode_fn()[self._tfio_file_format](
          audio_tensor, dtype=self._dtype
      )
      decoded_audio_tensor = tf.squeeze(decoded_audio_tensor)
    else:
      if self._file_format:
        file_format_tensor = tf.experimental.Optional.from_value(
            self._file_format
        )
      else:
        file_format_tensor = tf.experimental.Optional.empty(
            tf.TensorSpec(shape=(), dtype=tf.string)
        )

      # pydub.AudioSegment.get_array_of_samples returns an array with type code
      # `b`, `h` or `i` which can be all converted to `tf.int32`
      decoded_audio_tensor = tf.py_function(
          _pydub_decode_audio,
          [audio_tensor, file_format_tensor, self._channels],
          tf.int32,
      )

    decoded_audio_tensor.set_shape(self._shape)

    return tf.cast(decoded_audio_tensor, self._dtype)


class _EagerDecoder(_AudioDecoder):
  """Read audio during encoding."""

  def encode_audio(
      self, fobj: BinaryIO, file_format: Optional[str]
  ) -> np.ndarray:
    audio = _pydub_load_audio(fobj, file_format, self._channels)
    return audio.astype(self._np_dtype)

  def decode_audio(self, audio_tensor: tf.Tensor) -> tf.Tensor:
    return audio_tensor


class Audio(tensor_feature.Tensor):
  """`tfds.features.FeatureConnector` for audio.

  In `_generate_examples`, Audio accept:

  * A `np.ndarray` of shape `(length,)` or `(length, channels)`
  * A path to a `.mp3`, `.wav`,... file.
  * A file-object (e.g. `with path.open('rb') as fobj:`)

  By default, Audio features are decoded as the raw integer wave form
  `tf.Tensor(shape=(None,), dtype=tf.int64)`.

  When encoding an audio with a different number of channels than expected by
  the feature, TFDS automatically tries to correct the number of channels.
  """

  def __init__(
      self,
      *,
      file_format: Optional[str] = None,
      shape: utils.Shape = (None,),
      dtype: type_utils.TfdsDType = np.int64,
      sample_rate: Optional[int] = None,
      encoding: Union[str, Encoding] = Encoding.NONE,
      doc: feature_lib.DocArg = None,
      lazy_decode: bool = False,
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
      doc: Documentation of this feature (e.g. description).
      lazy_decode: `bool`, if set `True` then stores audio as is and decodes it
        to numpy array when loaded. Otherwise saves decoded audio.
    """  # fmt:skip
    self._file_format = file_format
    self._sample_rate = sample_rate
    self._lazy_decode = lazy_decode
    if len(shape) > 2:
      raise ValueError(
          'Audio shape should be either (length,) or '
          f'(length, num_channels), got {shape}.'
      )

    if self._lazy_decode:
      serialized_dtype = tf.string
      serialized_shape = ()
      _Decoder = _LazyDecoder
    else:
      serialized_dtype = None
      serialized_shape = None
      _Decoder = _EagerDecoder

    super().__init__(
        shape=shape,
        dtype=dtype,
        encoding=encoding,
        doc=doc,
        serialized_dtype=serialized_dtype,
        serialized_shape=serialized_shape,
    )

    self._audio_decoder = _Decoder(
        file_format=self._file_format, np_dtype=self._dtype, shape=self._shape
    )

  def encode_example(self, audio_or_path_or_fobj):
    """Convert the given audio into a dict convertible to tf example."""
    if isinstance(audio_or_path_or_fobj, (np.ndarray, list)):
      return audio_or_path_or_fobj
    elif isinstance(audio_or_path_or_fobj, epath.PathLikeCls):
      filename = os.fspath(audio_or_path_or_fobj)
      file_format = _infer_file_format(self._file_format, filename)
      with tf.io.gfile.GFile(filename, 'rb') as audio_f:
        try:
          audio = self._audio_decoder.encode_audio(audio_f, file_format)
        except Exception as e:  # pylint: disable=broad-except
          utils.reraise(e, prefix=f'Error for {filename}: ')
    else:
      audio = self._audio_decoder.encode_audio(
          audio_or_path_or_fobj, self._file_format
      )

    return super().encode_example(audio)

  def decode_example(self, tfexample_data):
    """See base class for details."""
    audio = super().decode_example(tfexample_data)
    return self._audio_decoder.decode_audio(audio)

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
    return (
        f'<audio controls src="data:audio/ogg;base64,{audio_str}" '
        ' controlsList="nodownload" />'
    )

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.AudioFeature]
  ) -> 'Audio':
    if isinstance(value, dict):
      # For backwards compatibility
      return cls(
          file_format=value['file_format'],
          shape=tuple(value['shape']),
          dtype=feature_lib.dtype_from_str(value['dtype']),
          sample_rate=value['sample_rate'],
          lazy_decode=value.get('lazy_decode', False),
      )
    return cls(
        shape=feature_lib.from_shape_proto(value.shape),
        dtype=feature_lib.dtype_from_str(value.dtype),
        file_format=value.file_format or None,
        sample_rate=value.sample_rate,
        encoding=value.encoding,
        lazy_decode=value.lazy_decode or False,
    )

  def to_json_content(self) -> feature_pb2.AudioFeature:  # pytype: disable=signature-mismatch  # overriding-return-type-checks
    return feature_pb2.AudioFeature(
        shape=feature_lib.to_shape_proto(self.shape),
        dtype=feature_lib.dtype_to_str(self.dtype),
        file_format=self._file_format,
        sample_rate=self._sample_rate,
        encoding=self._encoding.name,
        lazy_decode=self._lazy_decode,
    )


def _save_wav(buff, data, rate) -> None:
  """Transform a numpy array to a PCM bytestring."""
  # Code inspired from `IPython.display.Audio`
  data = np.array(data, dtype=float)

  bit_depth = 16
  max_sample_value = int(2 ** (bit_depth - 1)) - 1

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


def _infer_file_format(
    file_format: Optional[str], filename: str
) -> Optional[str]:
  """Simple heuristics to infer file format. Pydub will use FFMPEG otherwise."""
  if file_format is not None:
    return file_format
  suffix = epath.Path(filename).suffix
  if suffix.startswith('.'):
    return suffix[1:]
  return None

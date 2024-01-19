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

"""Tests for tensorflow_datasets.core.features.audio_feature."""

import array
import pathlib
import tempfile

from absl.testing import parameterized
import numpy as np
import pydub
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features


class AudioFeatureTest(
    testing.FeatureExpectationsTestCase, parameterized.TestCase
):

  @parameterized.product(dtype=[np.int64, tf.int64], num_channels=[1, 2, 8])
  def test_numpy_array(self, dtype, num_channels):
    np_audio = _create_np_audio(num_channels, np.int64)

    self.assertFeature(
        feature=features.Audio(
            sample_rate=1000, shape=_shape_for_channels(num_channels)
        ),
        shape=_shape_for_channels(num_channels),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=np_audio,
                expected=np_audio,
            ),
        ],
        test_attributes=dict(
            _file_format=None,
            sample_rate=1000,
        ),
    )

  @parameterized.product(dtype=[np.float32, tf.float32], num_channels=[1, 2, 8])
  def test_numpy_array_float(self, dtype, num_channels):
    np_audio = _create_np_audio(num_channels, np.float32)

    self.assertFeature(
        feature=features.Audio(
            dtype=dtype, shape=_shape_for_channels(num_channels)
        ),
        shape=_shape_for_channels(num_channels),
        dtype=np.float32,
        tests=[
            testing.FeatureExpectationItem(
                value=np_audio,
                expected=np_audio,
            ),
        ],
    )

  @parameterized.product(
      dtype=[np.int16, np.int32],
      lazy_decode=[True, False],
      num_channels=[1, 2, 8],
  )
  def test_wav_file(self, dtype, lazy_decode, num_channels):
    file_format = 'wav'

    np_audio = _create_np_audio(num_channels, dtype)
    _, tmp_file = tempfile.mkstemp()
    _write_audio_file(np_audio, tmp_file, file_format)

    self.assertFeature(
        feature=features.Audio(
            file_format=file_format,
            shape=_shape_for_channels(num_channels),
            dtype=dtype,
            lazy_decode=lazy_decode,
        ),
        shape=_shape_for_channels(num_channels),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=tmp_file,
                expected=np_audio,
            ),
            testing.FeatureExpectationItem(
                value=pathlib.Path(tmp_file),
                expected=np_audio,
            ),
        ],
        test_attributes=dict(
            _file_format=file_format,
        ),
    )

  @parameterized.product(lazy_decode=[True, False], num_channels=[1, 2, 8])
  def test_flac_file(self, lazy_decode, num_channels):
    if lazy_decode:
      if 'dev' in tf.__version__:
        self.skipTest('`tensorflow_io` is not compatible with `tf-nightly`')

    dtype = np.int16
    file_format = 'flac'

    np_audio = _create_np_audio(num_channels, dtype)
    _, tmp_file = tempfile.mkstemp()
    _write_audio_file(np_audio, tmp_file, file_format)

    self.assertFeature(
        feature=features.Audio(
            file_format=file_format,
            shape=_shape_for_channels(num_channels),
            dtype=dtype,
            lazy_decode=lazy_decode,
        ),
        shape=_shape_for_channels(num_channels),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=tmp_file,
                expected=np_audio,
            ),
            testing.FeatureExpectationItem(
                value=pathlib.Path(tmp_file),
                expected=np_audio,
            ),
        ],
        test_attributes=dict(
            _file_format=file_format,
        ),
    )

  @parameterized.product(
      dtype=[np.int16, np.int32],
      lazy_decode=[True, False],
      num_channels=[1, 2, 8],
  )
  def test_file_object(self, dtype, lazy_decode, num_channels):
    file_format = 'wav'

    np_audio = _create_np_audio(num_channels, dtype)
    _, tmp_file = tempfile.mkstemp()
    _write_audio_file(np_audio, tmp_file, file_format)

    class GFileWithSeekOnRead(tf.io.gfile.GFile):
      """Wrapper around GFile which is reusable across multiple read() calls.

      This is needed because assertFeature reuses the same
      FeatureExpectationItem several times.
      """

      def read(self, *args, **kwargs):
        data_read = super(GFileWithSeekOnRead, self).read(*args, **kwargs)
        self.seek(0)
        return data_read

    with GFileWithSeekOnRead(tmp_file, 'rb') as file_obj:
      self.assertFeature(
          feature=features.Audio(
              file_format=file_format,
              shape=_shape_for_channels(num_channels),
              dtype=dtype,
              lazy_decode=lazy_decode,
          ),
          shape=_shape_for_channels(num_channels),
          dtype=dtype,
          tests=[
              testing.FeatureExpectationItem(
                  value=file_obj,
                  expected=np_audio,
              ),
          ],
      )

  def test_sample_rate_property(self):
    self.assertEqual(features.Audio(sample_rate=1600).sample_rate, 1600)

  def test_lazy_decode_error_file(self):
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'Acceptable `dtype` for lazy loading'
    ):
      features.Audio(file_format='flac', lazy_decode=True)

  @parameterized.parameters([(None,), 2, (10,)], [(None, 2), 1, (10, 2)])
  def test_number_of_channels_is_changed(
      self, feature_shape, example_num_channels, example_output_shape
  ):
    feature = features.Audio(
        file_format='wav', dtype=np.int16, shape=feature_shape
    )
    _, tmp_file = tempfile.mkstemp()
    np_audio = _create_np_audio(example_num_channels, np.int16)
    _write_audio_file(np_audio, tmp_file, 'wav')
    self.assertEqual(
        feature.encode_example(tmp_file).shape, example_output_shape
    )


def _shape_for_channels(num_channels, *, length=None):
  """Returns the shape."""
  return (length,) if num_channels == 1 else (length, num_channels)


def _create_np_audio(num_channels: int, dtype: np.dtype) -> np.ndarray:
  """Creates a random audio `np.array`."""
  if np.issubdtype(dtype, np.integer):
    dtype_info = np.iinfo(dtype)
  else:
    dtype_info = np.finfo(dtype)

  np_audio = np.random.randint(
      max(-(2**10), int(dtype_info.min)),
      min(2**10, int(dtype_info.max)),
      size=_shape_for_channels(num_channels, length=10),
  )

  return np_audio.astype(dtype)


def _write_audio_file(np_audio, path, file_format):
  """Creates a random audio file with the given file format."""
  dtype = np_audio.dtype

  if (file_format == 'flac' and dtype not in [np.int16]) or (
      file_format == 'wav' and dtype not in [np.int16, np.int32]
  ):
    raise ValueError(
        f'Can\'t save audio in "{file_format.upper()}" format with dtype '
        f'`{np_audio.dtype}`.'
    )

  data = array.array(np.sctype2char(dtype), np_audio.reshape((-1,)))
  sample_width = np.dtype(dtype).alignment
  num_channels = np_audio.shape[1] if len(np_audio.shape) == 2 else 1

  pydub.AudioSegment(
      data=data,
      sample_width=sample_width,
      channels=num_channels,
      frame_rate=1,
  ).export(path, format=file_format)

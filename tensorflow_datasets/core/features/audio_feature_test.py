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

"""Tests for tensorflow_datasets.core.features.audio_feature."""

import array
import pathlib
import tempfile

from absl.testing import parameterized
import numpy as np
import pydub
import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features

tf.enable_v2_behavior()


class AudioFeatureTest(
    testing.FeatureExpectationsTestCase, parameterized.TestCase
):

  @parameterized.parameters([(1,), (2,), (8,)])
  def test_numpy_array(self, num_channels):
    np_audio = _create_np_audio(num_channels)

    self.assertFeature(
        feature=features.Audio(
            sample_rate=1000,
            shape=_shape_for_channels(num_channels)
        ),
        shape=_shape_for_channels(num_channels),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=np_audio,
                expected=np_audio,
            ),
        ],
        test_attributes=dict(
            _file_format=None,
            sample_rate=1000,
        )
    )

  @parameterized.parameters([(1,), (2,), (8,)])
  def test_numpy_array_float(self, num_channels):
    np_audio = _create_np_audio(num_channels).astype(np.float32)
    self.assertFeature(
        feature=features.Audio(
            dtype=tf.float32, shape=_shape_for_channels(num_channels)
        ),
        shape=_shape_for_channels(num_channels),
        dtype=tf.float32,
        tests=[
            testing.FeatureExpectationItem(
                value=np_audio,
                expected=np_audio,
            ),
        ],
    )

  @parameterized.parameters([(1,), (2,), (8,)])
  def test_wav_file(self, num_channels):
    np_audio = _create_np_audio(num_channels)
    _, tmp_file = tempfile.mkstemp()
    _write_wave_file(np_audio, tmp_file)

    self.assertFeature(
        feature=features.Audio(
            file_format='wav', shape=_shape_for_channels(num_channels)
        ),
        shape=_shape_for_channels(num_channels),
        dtype=tf.int64,
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
        test_attributes=dict(_file_format='wav',)
    )

  @parameterized.parameters([(1,), (2,), (8,)])
  def test_file_object(self, num_channels):
    np_audio = _create_np_audio(num_channels)
    _, tmp_file = tempfile.mkstemp()
    _write_wave_file(np_audio, tmp_file)

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
              file_format='wav', shape=_shape_for_channels(num_channels)
          ),
          shape=_shape_for_channels(num_channels),
          dtype=tf.int64,
          tests=[
              testing.FeatureExpectationItem(
                  value=file_obj,
                  expected=np_audio,
              ),
          ],
      )

  def test_sample_rate_property(self):
    self.assertEqual(features.Audio(sample_rate=1600).sample_rate, 1600)


def _shape_for_channels(num_channels, *, length=None):
  """Returns the shape."""
  return (length,) if num_channels == 1 else (length, num_channels)


def _create_np_audio(num_channels: int) -> np.ndarray:
  """Creates a random audio `np.array`."""
  return np.random.randint(
      -2**10,
      2**10,
      size=_shape_for_channels(num_channels, length=10),
      dtype=np.int64
  )


def _write_wave_file(np_audio, path):
  """Creates a random audio file."""
  num_channels = np_audio.shape[1] if len(np_audio.shape) == 2 else 1
  audio = pydub.AudioSegment(
      b'',
      sample_width=2,
      channels=num_channels,
      frame_rate=1,
  )
  # See documentation for _spawn usage:
  # https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegmentget_array_of_samples
  audio = audio._spawn(array.array(audio.array_type, np_audio.reshape((-1,))))
  audio.export(path, format='wav')

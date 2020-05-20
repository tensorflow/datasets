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

# Lint as: python3
"""Audio feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import six
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.features import feature


class Audio(feature.Tensor):
  """`FeatureConnector` for audio, encoded as raw integer wave form."""

  @api_utils.disallow_positional_args
  def __init__(
      self,
      file_format=None,
      shape=(None,),
      dtype=tf.int64,
      sample_rate=None,
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
    """
    self._file_format = file_format
    if len(shape) != 1:
      raise TypeError(
          "Audio feature currently only supports 1-D values, got %s." % shape)
    self._shape = shape
    self._sample_rate = sample_rate
    super(Audio, self).__init__(shape=shape, dtype=dtype)

  def _encode_file(self, fobj, file_format):
    audio_segment = lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
        fobj, format=file_format)
    np_dtype = np.dtype(self.dtype.as_numpy_dtype)
    return super(Audio, self).encode_example(
        np.array(audio_segment.get_array_of_samples()).astype(np_dtype))

  def encode_example(self, audio_or_path_or_fobj):
    if isinstance(audio_or_path_or_fobj, (np.ndarray, list)):
      return audio_or_path_or_fobj
    elif isinstance(audio_or_path_or_fobj, six.string_types):
      filename = audio_or_path_or_fobj
      file_format = self._file_format or filename.split(".")[-1]
      with tf.io.gfile.GFile(filename, "rb") as audio_f:
        return self._encode_file(audio_f, file_format)
    else:
      return self._encode_file(audio_or_path_or_fobj, self._file_format)

  @property
  def sample_rate(self):
    """Returns the `sample_rate` metadata associated with the dataset."""
    return self._sample_rate

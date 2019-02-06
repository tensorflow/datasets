# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.lazy_imports import lazy_imports


class Audio(feature.Tensor):
  """`FeatureConnector` for audio, encoded as raw integer wave form."""

  @api_utils.disallow_positional_args
  def __init__(self, file_format=None, shape=(None,)):
    """Constructs the connector.

    Args:
      file_format: `str`, the audio file format. Can be any format ffmpeg
        understands. If `None`, will attempt to infer from the file extension.
      shape: `tuple`, shape of the data.
    """
    self._file_format = file_format
    if len(shape) != 1:
      raise TypeError(
          "Audio feature currently only supports 1-D values, got %s." % shape)
    self._shape = shape
    super(Audio, self).__init__(shape=shape, dtype=tf.int64)

  def encode_example(self, audio_or_path_or_fobj):
    audio = audio_or_path_or_fobj
    if isinstance(audio, (np.ndarray, list)):
      return audio

    with tf.io.gfile.GFile(audio, "rb") as audio_f:
      file_format = self._file_format or audio.split(".")[-1]
      audio_segment = lazy_imports.pydub.AudioSegment.from_file(
          audio_f, format=file_format)
      return super(Audio, self).encode_example(
          np.array(audio_segment.get_array_of_samples()).astype(np.int64))

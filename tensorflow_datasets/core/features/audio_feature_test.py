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

"""Tests for tensorflow_datasets.core.features.audio_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import array
import tempfile

import numpy as np
import pydub
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features

tf.compat.v1.enable_eager_execution()


class AudioFeatureTest(testing.FeatureExpectationsTestCase):

  def test_audio(self):

    np_audio = np.random.randint(-2**10, 2**10, size=(10,), dtype=np.int64)

    # Numpy array
    self.assertFeature(
        feature=features.Audio(),
        shape=(None,),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=np_audio,
                expected=np_audio,
            ),
        ],
    )

    # WAV file

    audio = pydub.AudioSegment.empty().set_sample_width(2)
    # See documentation for _spawn usage:
    # https://github.com/jiaaro/pydub/blob/master/API.markdown#audiosegmentget_array_of_samples
    audio = audio._spawn(array.array(audio.array_type, np_audio))
    _, tmp_file = tempfile.mkstemp()
    audio.export(tmp_file, format="wav")

    self.assertFeature(
        feature=features.Audio(file_format="wav"),
        shape=(None,),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=tmp_file,
                expected=np_audio,
            ),
        ],
    )


if __name__ == "__main__":
  testing.test_main()

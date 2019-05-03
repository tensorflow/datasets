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
"""Tests for Freesound Audio Tagging 2019 dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from multiprocessing import cpu_count

import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.audio import freesound_audio_tagging_2019


def test_spectrogram():
    def preprocess(row):
        audio_path = row['audio']
        blob = tf.io.read_file(audio_path)

        waveform = tf.audio.decode_wav(blob, 1, 3.0 * 44100)[0]

        x = tf.transpose(waveform)
        x = tf.signal.stft(x, 1024, 512)
        x = tf.transpose(x, (1, 2, 0))
        spectrogram = tf.abs(x)

        tags = row['tags']
        tags = tf.stack(list(tags.values()))

        return spectrogram, tags

    dataset = tfds.load(
        name='freesound_audio_tagging2019',
        split=tfds.Split.TRAIN,
    )

    batch_size = 32
    dataset = dataset.map(preprocess, cpu_count()).cache().shuffle(
        256).repeat().batch(batch_size).prefetch(1)

    for spectrogram, tags in dataset:
        print(spectrogram.shape, tags.shape)
        assert spectrogram.shape == [batch_size, 257, 513, 1]
        assert tags.shape == [batch_size, 80]
        break


# TODO
class FreesoundAudioTagging2019FullTest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = freesound_audio_tagging2019.FreesoundAudioTagging2019
    BUILDER_CONFIG_NAMES_TO_TEST = ["full-16000hz"]
    SPLITS = {
        "train": 2,
        "test": 1,
    }
    DL_EXTRACT_RESULT = ".."


if __name__ == "__main__":
    testing.test_main()

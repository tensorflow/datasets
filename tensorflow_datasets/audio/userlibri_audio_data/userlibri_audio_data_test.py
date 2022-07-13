# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for librispeech dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.audio.userlibri_audio_data import userlibri_audio_data


class UserLibriAudioTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = userlibri_audio_data.UserLibriAudio
  SPLITS = {
      # List number of fake train examples.
      "test-clean_speaker-121-book-1041": 2,
      "test-clean_speaker-121-book-1989": 2,
      "test-other_speaker-3005-book-76": 2,
      "test-other_speaker-8461-book-6328": 1,
      "test-other_speaker-8461-book-9189": 1,
  }
  DL_DOWNLOAD_RESULT = ""
  SKIP_CHECKSUMS = True


if __name__ == "__main__":
  testing.test_main()

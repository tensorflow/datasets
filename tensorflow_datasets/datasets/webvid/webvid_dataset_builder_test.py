# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""webvid dataset."""

import numpy as np

from tensorflow_datasets.datasets.webvid import webvid_dataset_builder
import tensorflow_datasets.public_api as tfds


def fake_ffmpeg_decode_diskless(*_, **__):
  img_size = webvid_dataset_builder._IMG_SIZE
  return np.ones((11, img_size[0], img_size[1], 3), dtype=np.uint8)


class WebvidTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for webvid dataset."""

  DATASET_CLASS = webvid_dataset_builder.Builder
  SPLITS = {
      'train': 3,  # Number of fake train examples.
      'validation': 1,  # Number of fake test examples.
  }

  def setUp(self):
    webvid_dataset_builder._ffmpeg_decode_diskless = fake_ffmpeg_decode_diskless
    super().setUp()


if __name__ == '__main__':
  tfds.testing.test_main()

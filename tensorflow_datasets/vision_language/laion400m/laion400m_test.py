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

"""LAION-400M image dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.vision_language.laion400m import laion400m


class Laion400MImagesTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for LAION-400M image dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = [laion400m.LAION400M_IMAGES_CONFIG.name]
  DATASET_CLASS = laion400m.Laion400m
  SPLITS = {
      'train': 3,
  }

  @classmethod
  def setUpClass(cls):
    laion400m.LAION400M_IMAGES_CONFIG.num_shards = 1
    super().setUpClass()


class Laion400MEmbeddingsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for LAION-400M image dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = [laion400m.LAION400M_EMBEDDINGS_CONFIG.name]
  DATASET_CLASS = laion400m.Laion400m
  SPLITS = {
      'train': 3,
  }
  DL_EXTRACT_RESULT = {
      'img_emb_0.npy': 'img_emb_0.npy',
      'text_emb_0.npy': 'text_emb_0.npy',
      'metadata_0.parquet': 'metadata_0.parquet',
  }

  @classmethod
  def setUpClass(cls):
    laion400m.LAION400M_EMBEDDINGS_CONFIG.num_shards = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()

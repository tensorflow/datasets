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

"""LAION-400M CLIP embeddings dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.vision_language.laion400m_emb import laion400m_emb


class Laion400mEmbTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for LAION-400M CLIP embeddings dataset."""
  DATASET_CLASS = laion400m_emb.Laion400mEmb
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
    cls.DATASET_CLASS.SHARD_NUM = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()

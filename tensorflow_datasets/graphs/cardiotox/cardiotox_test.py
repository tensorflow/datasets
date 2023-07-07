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

"""cardiotox dataset."""
from tensorflow_datasets.graphs.cardiotox import cardiotox
import tensorflow_datasets.public_api as tfds


class CardiotoxTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for cardiotox dataset."""

  DATASET_CLASS = cardiotox.Cardiotox
  SPLITS = {
      'train': 4,  # Number of fake train example
      'validation': 2,  # Number of fake test example
      'test': 2,  # Number of fake test example
      'test2': 2,  # Number of fake test example
  }

  @classmethod
  def setUpClass(cls):
    cardiotox._DATA_URL = cls.dummy_data
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()

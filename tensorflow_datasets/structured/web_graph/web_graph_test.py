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

"""web_graph dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.web_graph import web_graph


class WebGraphTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for web_graph dataset."""

  DATASET_CLASS = web_graph.WebGraph
  SPLITS = {
      'train': 10,  # Number of fake train example
      'train_t': 10,  # Number of fake train example
      'test': 10,  # Number of fake train example
  }
  OVERLAPPING_SPLITS = ['train', 'train_t']

  SKIP_TF1_GRAPH_MODE = True

  # The different configs are only different in the name of the files.
  BUILDER_CONFIG_NAMES_TO_TEST = ['in-dense']

  @classmethod
  def setUpClass(cls):
    web_graph.WebGraph.WEB_GRAPH_HOMEPAGE = cls.dummy_data
    web_graph.WebGraph.SHARDS = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()

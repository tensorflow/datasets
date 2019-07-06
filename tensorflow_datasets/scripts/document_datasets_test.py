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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.scripts.document_datasets import schema_org

DummyMnist = testing.DummyMnist


class DocumentDatasetsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DocumentDatasetsTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    builder = DummyMnist(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def setUp(self):
    self.builder = DummyMnist(data_dir=self._tfds_tmp_dir)

  @testing.run_in_graph_and_eager_modes()
  def test_schema_org(self):
    schema_str = schema_org(self.builder)
    self.assertIn("http://schema.org/Dataset", schema_str)
    self.assertIn('<meta itemprop="url" '
                  'content="https://www.tensorflow.org/'
                  'datasets/datasets#%s" />' % self.builder.name,
                  schema_str)

if __name__ == "__main__":
  testing.test_main()

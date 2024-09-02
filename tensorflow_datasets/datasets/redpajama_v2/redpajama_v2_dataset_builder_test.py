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

"""RedPajamaV2 dataset."""

from tensorflow_datasets.datasets.redpajama_v2 import redpajama_v2_dataset_builder
import tensorflow_datasets.public_api as tfds


class RedPajamaV2Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for RedPajamaV2 dataset."""

  redpajama_v2_dataset_builder._NUM_SHARDS = 1
  redpajama_v2_dataset_builder._PARTITIONS = ['tail']
  redpajama_v2_dataset_builder._LANGUAGES = ['en']

  DATASET_CLASS = redpajama_v2_dataset_builder.Builder
  SPLITS = {'train': 1}

  DL_DOWNLOAD_RESULT = {
      '1900-01/0000/en_tail': {
          redpajama_v2_dataset_builder._DOCS_COMPONENT: 'documents.json.gz'
      }
  }
  DL_EXTRACT_RESULT = 'missing_urls.txt'
  SKIP_CHECKSUMS = True


if __name__ == '__main__':
  tfds.testing.test_main()

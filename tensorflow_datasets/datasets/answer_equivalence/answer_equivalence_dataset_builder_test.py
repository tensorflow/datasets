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

"""answer_equivalence dataset."""

from tensorflow_datasets.datasets.answer_equivalence import answer_equivalence_dataset_builder
import tensorflow_datasets.public_api as tfds


class AnswerEquivalenceTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for answer_equivalence dataset."""
  DATASET_CLASS = answer_equivalence_dataset_builder.Builder
  SPLITS = {
      'train': 3,
      'ae_dev': 1,
      'ae_test': 1,
      'dev_xlnet': 1,
      'dev_luke': 1,
      'dev_bidaf': 1,
  }

  DL_EXTRACT_RESULT = {
      'train': 'dummy_data_train.jsonl',
      'ae_dev': 'dummy_data_ae_dev.jsonl',
      'ae_test': 'dummy_data_ae_test.jsonl',
      'dev_xlnet': 'dev_by_system/dummy_data_dev_xlnet.jsonl',
      'dev_luke': 'dev_by_system/dummy_data_dev_luke.jsonl',
      'dev_bidaf': 'dev_by_system/dummy_data_dev_bidaf.jsonl'
  }


if __name__ == '__main__':
  tfds.testing.test_main()

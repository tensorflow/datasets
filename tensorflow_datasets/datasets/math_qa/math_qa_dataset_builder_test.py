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

"""math_qa dataset."""

from absl.testing import parameterized
from tensorflow_datasets.datasets.math_qa import math_qa_dataset_builder
import tensorflow_datasets.public_api as tfds


class MathQaTest(tfds.testing.DatasetBuilderTestCase, parameterized.TestCase):
  """Tests for math_qa dataset."""

  DATASET_CLASS = math_qa_dataset_builder.Builder
  SPLITS = {"train": 2, "validation": 1, "test": 1}

  @parameterized.named_parameters(
      ("flattened", "a ) 1 , 2 , b )3 , c ) none of these"),
      ("list", "['a ) 1 , 2', 'b )3', 'c ) none of these']"),
  )
  def test_extract_answer_text(self, options_text):
    self.assertEqual(
        math_qa_dataset_builder.extract_answer_text(options_text, "a"), "1 , 2"
    )
    self.assertEqual(
        math_qa_dataset_builder.extract_answer_text(options_text, "b"), "3"
    )
    self.assertEqual(
        math_qa_dataset_builder.extract_answer_text(options_text, "c"),
        "none of these",
    )


if __name__ == "__main__":
  tfds.testing.test_main()

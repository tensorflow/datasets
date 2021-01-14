# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""AbstractReasoning dataset test."""

from tensorflow_datasets.image import abstract_reasoning
import tensorflow_datasets.testing as tfds_test


class AbstractReasoningTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = abstract_reasoning.AbstractReasoning
  SPLITS = {"train": 5, "validation": 5, "test": 5}
  DL_EXTRACT_RESULT = [
      "neutral.tar.gz",
      "interpolation.tar.gz",
      "extrapolation.tar.gz",
      "attr.rel.pairs.tar.gz",
      "attr.rels.tar.gz",
      "attrs.pairs.tar.gz",
      "attrs.shape.color.tar.gz",
      "attrs.line.type.tar.gz",
  ]
  # The configs only differ in the data contained in the files.
  BUILDER_CONFIG_NAMES_TO_TEST = ["neutral"]


if __name__ == "__main__":
  tfds_test.test_main()

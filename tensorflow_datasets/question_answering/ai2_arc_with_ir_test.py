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

"""Tests for the ai2_arc_with_ir dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import ai2_arc_with_ir


class Ai2ArcWithIRTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = ai2_arc_with_ir.Ai2ArcWithIR
  BUILDER_CONFIG_NAMES_TO_TEST = ["ARC-Challenge-IR"]
  SPLITS = {
      "train": 2,
      "validation": 2,
      "test": 2,
  }


if __name__ == "__main__":
  tfds.testing.test_main()

# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Tests for WIDER FACE dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import wider_face
import tensorflow_datasets.public_api as tfds


class WiderFaceTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = wider_face.WiderFace
  SPLITS = {
      tfds.Split.TRAIN: 3,
      tfds.Split.VALIDATION: 3,
      tfds.Split.TEST: 3,
  }
  DL_EXTRACT_RESULT = {
      'wider_train': 'wider_train',
      'wider_val': 'wider_val',
      'wider_test': 'wider_test',
      'wider_annot': 'wider_annot',
  }


if __name__ == '__main__':
  testing.test_main()

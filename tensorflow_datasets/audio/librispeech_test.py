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

"""Tests for librispeech dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.audio import librispeech 


class LibrispeechTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = librispeech.Librispeech
  BUILDER_CONFIG_NAMES_TO_TEST = ["clean-100"]
  SPLITS = {
      "train": 2,
      "test": 1,
      "dev": 1,
  }
  
  DL_EXTRACT_RESULT = {
      tfds.Split.TRAIN: "train-clean-100",
      tfds.Split.TEST: "test-clean",
      tfds.Split.VALIDATION: "dev-clean",
  }
  
  
class LibrispeechTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = librispeech.Librispeech
  BUILDER_CONFIG_NAMES_TO_TEST = ["clean-360"]
  SPLITS = {
      "train": 1,
      "test": 1,
      "dev": 1,
  }
  
  DL_EXTRACT_RESULT = {
      tfds.Split.TRAIN: ["train-clean-100", "train-clean-360"], 
      tfds.Split.TEST: "test-clean",
      tfds.Split.VALIDATION: "dev-clean",
  }  


if __name__ == "__main__":
  testing.test_main()

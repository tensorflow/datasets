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

"""Nsynth Dataset Builder test."""
from tensorflow_datasets.audio import nsynth
import tensorflow_datasets.testing as tfds_test


class NsynthFullTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = nsynth.Nsynth
  BUILDER_CONFIG_NAMES_TO_TEST = ["full"]
  SPLITS = {"train": 3, "test": 3, "valid": 3}
  DL_EXTRACT_RESULT = {
      "train": "nsynth-train.tfrecord",
      "test": "nsynth-test.tfrecord",
      "valid": "nsynth-valid.tfrecord",
      "instrument_labels": "nsynth-instrument_labels.txt"
  }


class GANsynthTest(NsynthFullTest):
  BUILDER_CONFIG_NAMES_TO_TEST = ["iclr2019_gansynth_subset"]
  SPLITS = {"train": 1, "test": 0, "valid": 0}


if __name__ == "__main__":
  tfds_test.test_main()

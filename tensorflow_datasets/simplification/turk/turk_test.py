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

"""turk dataset."""

import sys
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.simplification.turk import turk

sys.path.insert(0, ".")


class TurkTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for turk dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ["simplification"]
  DATASET_CLASS = turk.Turk

  _URL_LIST = [
    (
      "test.8turkers.tok.norm",
      "simplification/1.0.0/test.8turkers.tok.norm",
    ),
    (
      "tune.8turkers.tok.norm",
      "simplification/1.0.0/tune.8turkers.tok.norm",
    ),
  ]
  _URL_LIST += [
    (
      f"{spl}.8turkers.tok.turk.{i}",
      f"simplification/1.0.0/{spl}.8turkers.tok.turk.{i}",
    )
    for spl in ["tune", "test"]
    for i in range(8)
  ]
  DL_EXTRACT_RESULT = dict(_URL_LIST)

  SPLITS = {"validation": 4, "test": 4}


if __name__ == "__main__":
  tfds.testing.test_main()

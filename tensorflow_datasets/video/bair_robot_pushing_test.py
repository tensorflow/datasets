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

"""Tests for tensorflow_datasets.video.bair_robot_pushing."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.video import bair_robot_pushing


class BairRobotPushingTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = bair_robot_pushing.BairRobotPushingSmall

  SPLITS = {
      "train": 1,
      "test": 1,
  }


if __name__ == "__main__":
  testing.test_main()

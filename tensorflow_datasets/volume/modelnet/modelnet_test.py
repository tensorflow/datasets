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

"""Tests for colorectal_histology dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import six
from tensorflow_datasets.volume import modelnet
from tensorflow_datasets import testing

# testing/modelnet.py generates fake input data
num_train_examples = 4
num_test_examples = 2
num_sampled_points = 10


def base_dl_extract_result(num_classes=10):
  return "data%d.tar.gz" % num_classes


modelnet.ModelnetSampledConfig.num_points = num_sampled_points

splits = {
  "train": num_train_examples,
  "test": num_test_examples,
}


class Modelnet10Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = modelnet.Modelnet10
  DL_EXTRACT_RESULT = base_dl_extract_result(10)
  SPLITS = splits


class Modelnet40Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = modelnet.Modelnet40
  DL_EXTRACT_RESULT = base_dl_extract_result(40)
  SPLITS = splits


class ModelnetAlignedTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = modelnet.ModelnetAligned40
  DL_EXTRACT_RESULT = "data40.tar"
  SPLITS = splits


class ModelnetSampledTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = modelnet.ModelnetSampled
  SPLITS = splits


if __name__ == "__main__":
  testing.test_main()

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

"""testing/tiered_imagenet_generate.py generates fake input data"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import tiered_imagenet
import tensorflow_datasets.testing as tfds_test

class TieredImagenetTest(tfds_test.DatasetBuilderTestCase):
	"""Tests for tiered_imagenet dataset module."""
	DATASET_CLASS = tiered_imagenet.TieredImagenet
	SPLITS = {
			"train": 1,
			"test": 1,
			"validation": 1
	}
	MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = False


if __name__ == "__main__":
	tfds_test.test_main()

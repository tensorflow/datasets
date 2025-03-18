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

"""Tests for tfds.features.Scalar."""

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features


class ScalarFeatureTest(testing.FeatureExpectationsTestCase):

  def test_scalar(self):
    self.assertFeature(
        feature=features.Scalar(dtype=tf.int64, doc='Some description'),
        shape=(),
        dtype=tf.int64,
        tests=[
            testing.FeatureExpectationItem(
                value=42,
                expected=42,
            ),
        ],
    )


if __name__ == '__main__':
  testing.test_main()

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

"""Tests for bounding_boxes."""

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features


class BBoxFeatureTest(testing.FeatureExpectationsTestCase):

  def test_feature(self):

    self.assertFeature(
        feature=features.BBoxFeature(),
        shape=(4,),
        dtype=tf.float32,
        tests=[
            # Numpy array
            testing.FeatureExpectationItem(
                value=features.BBox(
                    ymin=0.0,
                    xmin=0.25,
                    ymax=1.0,
                    xmax=0.75,
                ),
                expected=[0.0, 0.25, 1.0, 0.75],
            ),
        ],
    )


if __name__ == '__main__':
  testing.test_main()

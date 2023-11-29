# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features
from tensorflow_datasets.core.features import bounding_boxes


class BBoxFeatureTest(testing.FeatureExpectationsTestCase):

  def test_feature(self):
    self.assertFeature(
        feature=features.BBoxFeature(),
        shape=(4,),
        dtype=tf.float32,
        tests=[
            testing.FeatureExpectationItem(
                value=features.BBox(
                    ymin=0.0,
                    xmin=0.25,
                    ymax=1.0,
                    xmax=0.75,
                ),
                expected=[0.0, 0.25, 1.0, 0.75],
            ),
            testing.FeatureExpectationItem(
                # 1D numpy array, float32
                value=np.array([0.0, 0.25, 1.0, 0.75], dtype=np.float32),
                expected=[0.0, 0.25, 1.0, 0.75],
            ),
            testing.FeatureExpectationItem(
                # 1D numpy array, float64
                value=np.array([0.0, 0.25, 1.0, 0.75], dtype=np.float64),
                expected=[0.0, 0.25, 1.0, 0.75],
            ),
        ],
    )

  def test_format_xyxy(self):
    self.assertFeature(
        feature=features.BBoxFeature(bbox_format='XYXY'),
        shape=(4,),
        dtype=tf.float32,
        tests=[
            testing.FeatureExpectationItem(
                value=np.array([0.0, 0.25, 1.0, 0.75], dtype=np.float32),
                expected=[0.25, 0.0, 0.75, 1.0],
            ),
        ],
    )


TEST_INPUT_LIST = [199.84, 200.46, 270.72, 278.17]


@pytest.mark.parametrize(
    'test_input,bbox_format,expected',
    [
        (TEST_INPUT_LIST, 'YXYX', TEST_INPUT_LIST),
        (TEST_INPUT_LIST, None, TEST_INPUT_LIST),
        (TEST_INPUT_LIST, 'XYXY', [200.46, 199.84, 278.17, 270.72]),
        ([200.46, 199.84, 77.71, 70.88], 'XYWH', TEST_INPUT_LIST),
    ],
)
def test_convert_to_bbox(test_input, bbox_format, expected):
  actual = bounding_boxes.convert_to_bbox(
      coordinates=np.array(test_input), bbox_format=bbox_format
  )
  expected_bbox = bounding_boxes.BBox(
      ymin=expected[0],
      xmin=expected[1],
      ymax=expected[2],
      xmax=expected[3],
  )
  assert actual == expected_bbox


@pytest.mark.parametrize(
    'test_input,bbox_format,error_match',
    [
        ([1, 2, 3], None, 'Expected 4'),
        (TEST_INPUT_LIST, 'NonExistentConverter', 'Unsupported bbox'),
    ],
)
def test_convert_to_bbox_raises_valueerror(
    test_input, bbox_format, error_match
):
  with pytest.raises(ValueError, match=rf'{error_match}'):
    bounding_boxes.convert_to_bbox(
        coordinates=np.array(test_input), bbox_format=bbox_format
    )


if __name__ == '__main__':
  testing.test_main()

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

"""Tests for bounding_boxes_utils."""

import numpy as np
import pytest
from tensorflow_datasets.core.features import bounding_boxes_utils as bb_utils


TEST_INPUT_LIST = [199.84, 200.46, 270.72, 278.17]


@pytest.mark.parametrize(
    'test_input,input_format,img_shape,normalize,expected',
    [
        (TEST_INPUT_LIST, 'YXYX', None, False, TEST_INPUT_LIST),
        (
            TEST_INPUT_LIST,
            bb_utils.BBoxFormat.YXYX,
            None,
            False,
            TEST_INPUT_LIST,
        ),
        (
            TEST_INPUT_LIST,
            'XYXY',
            None,
            False,
            [200.46, 199.84, 278.17, 270.72],
        ),
        ([200.46, 199.84, 77.71, 70.88], 'XYWH', None, False, TEST_INPUT_LIST),
    ],
)
def test_convert_to_bbox(
    test_input, input_format, img_shape, normalize, expected
):
  actual = bb_utils.convert_coordinates_to_bbox(
      coordinates=np.array(test_input),
      input_format=input_format,
      img_shape=img_shape,
      normalize=normalize,
  )
  expected_bbox = bb_utils.BBox(
      ymin=expected[0],
      xmin=expected[1],
      ymax=expected[2],
      xmax=expected[3],
  )
  assert actual == expected_bbox


@pytest.mark.parametrize(
    'test_input,input_format,error_match',
    [
        ([1, 2, 3], None, 'Expected 4'),
        (TEST_INPUT_LIST, 'NonExistentConverter', 'Unsupported bbox format'),
        (
            TEST_INPUT_LIST,
            bb_utils.BBoxFormat.XYXY,
            'If normalize is True, img_shape must be provided, but got None.',
        ),
        (
            TEST_INPUT_LIST,
            bb_utils.BBoxFormat.REL_XYXY,
            (
                'If the input format is normalized, then normalize should be'
                ' False.'
            ),
        ),
    ],
)
def test_convert_coordinates_to_bbox_valueerror(
    test_input, input_format, error_match
):
  with pytest.raises(ValueError, match=rf'{error_match}'):
    bb_utils.convert_coordinates_to_bbox(
        coordinates=np.array(test_input), input_format=input_format
    )


@pytest.mark.parametrize(
    'bbox,img_shape,expected',
    [
        ([10, 20, 110, 120], [100, 200], [0.1, 0.1, 1.1, 0.6]),
        ([10, 20, 110, 120], np.array([1000, 2000]), [0.01, 0.01, 0.11, 0.06]),
    ],
)
def test_normalize_bbox(bbox, img_shape, expected):
  bbox = bb_utils.BBox(ymin=bbox[0], xmin=bbox[1], ymax=bbox[2], xmax=bbox[3])
  actual = bb_utils.normalize_bbox(bbox, img_shape)
  expected_bbox = bb_utils.BBox(
      ymin=expected[0], xmin=expected[1], ymax=expected[2], xmax=expected[3]
  )
  assert actual == expected_bbox


@pytest.mark.parametrize(
    'bbox,img_shape,match',
    [
        (TEST_INPUT_LIST, [1], 'Expected 2'),
        (TEST_INPUT_LIST, np.array([1, 2, 3]), 'Expected 2'),
        (TEST_INPUT_LIST, [0, 0], 'shapes cannot be zero'),
    ],
)
def test_normalize_bbox_valueerror(bbox, img_shape, match):
  with pytest.raises(ValueError, match=rf'{match}'):
    bb_utils.normalize_bbox(bbox, img_shape)

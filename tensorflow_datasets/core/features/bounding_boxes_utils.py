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

"""Utils for interacting with BoundingBox features.

This script contains various functions to convert commonly used bounding boxes
formats to the YXYX format, which is used by TFDS.

A list of such formats can be found at:
https://keras.io/api/keras_cv/bounding_box/formats/
"""

import collections
from collections.abc import Sequence
import enum
from typing import Union

import numpy as np


# A BBox contains the bounding boox coordinates in the YXYX format, following
# this order: [top, left, bottom, right].
BBox = collections.namedtuple('BBox', 'ymin, xmin, ymax, xmax')


@enum.unique
class BBoxFormat(enum.Enum):
  """Supported bounding box formats by TFDS.

  If you add to this enum, you will also probably need to update the function
  `convert_coordinates_to_bbox`.
  """

  XYXY = 'XYXY'
  YXYX = 'YXYX'
  XYWH = 'XYWH'
  REL_XYXY = 'REL_XYXY'
  REL_YXYX = 'REL_YXYX'


BBoxFormatType = Union[BBoxFormat, str]


def convert_coordinates_to_bbox(
    coordinates: np.ndarray,
    input_format: BBoxFormatType = 'YXYX',
    img_shape=None,
    normalize: bool = True,
) -> BBox:
  """Converts four coordinates to a BBox using the YXYX format.

  Args:
    coordinates: np.array with the four coordinates expressing a bounding box.
    input_format: the format of the coordinates, e.g. 'XYXY' or 'XYWH'. See
      https://keras.io/api/keras_cv/bounding_box/formats/ for a list of popular
        bounding boxes formats.
    img_shape: 2-dimensions np.ndarray or iterable with (img_heigth, img_width).
    normalize: Whether to normalize the axes. If True, it will normalize the x
      coordinates using the image width, and the y coordinates using the image
      height. Defaults to True.

  Returns:
    A BBox in the correct format.

  Raises:
    ValueError if input_format is unknown, or if the
  """
  if len(coordinates) != 4:
    raise ValueError(f'Expected 4 coordinates, got {coordinates}.')
  coordinates = coordinates.astype(np.float64)

  try:
    if isinstance(input_format, str):
      input_format = BBoxFormat(input_format)
  except ValueError as e:
    raise ValueError(
        f'Unsupported bbox format: {format}. Currently supported bounding box'
        f' formats are: {[format.value for format in BBoxFormat]}'
    ) from e
  if (
      input_format == BBoxFormat.REL_XYXY or input_format == BBoxFormat.REL_YXYX
  ) and normalize:
    raise ValueError(
        'If the input format is normalized, then normalize should be False.'
    )
  if normalize and img_shape is None:
    raise ValueError(
        'If normalize is True, img_shape must be provided, but got None.'
    )
  if input_format == BBoxFormat.YXYX or input_format == BBoxFormat.REL_YXYX:
    bbox = BBox(
        ymin=coordinates[0],
        xmin=coordinates[1],
        ymax=coordinates[2],
        xmax=coordinates[3],
    )
  elif input_format == BBoxFormat.XYXY or input_format == BBoxFormat.REL_XYXY:
    bbox = BBox(
        ymin=coordinates[1],
        xmin=coordinates[0],
        ymax=coordinates[3],
        xmax=coordinates[2],
    )
  elif input_format == BBoxFormat.XYWH:
    x, y, width, height = coordinates
    bbox = BBox(ymin=y, xmin=x, ymax=(y + height), xmax=(x + width))
  else:
    raise ValueError(
        f'Unsupported bbox format: {format}. Currently supported bounding box'
        f' formats are: {[format.value for format in BBoxFormat]}'
    )

  if normalize:
    bbox = normalize_bbox(bbox, img_shape)

  return bbox


def normalize_bbox(
    bbox: BBox,
    img_shape: Union[np.ndarray, Sequence[float]],
) -> BBox:
  """Normalizes a bbox in the YXYX format.

  The x coordinates are normalized using the image's height, while the y
  coordinates using the image width.

  Args:
    bbox: The input BBox in YXYX format.
    img_shape: 2-dimensions np.ndarray or iterable with (imgage_heigth,
      image_width).

  Returns:
    Normalized BBox.

  Raises:
    ValueError if the img_shape shape or length is different than 2, or if any
    of the image shapes is zero.
  """
  if (isinstance(img_shape, np.ndarray) and img_shape.shape != (2,)) or (
      isinstance(img_shape, Sequence) and len(img_shape) != 2
  ):
    raise ValueError(f'Expected 2-dimensional img_shape, got {img_shape}.')

  height, width = img_shape[0], img_shape[1]
  if height == 0 or width == 0:
    raise ValueError(
        f'Valid image shapes cannot be zero, but got: {img_shape}.'
    )

  return BBox(
      ymin=bbox.ymin / height,
      xmin=bbox.xmin / width,
      ymax=bbox.ymax / height,
      xmax=bbox.xmax / width,
  )

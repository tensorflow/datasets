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

"""Bounding boxes feature."""

from __future__ import annotations

from typing import Any, Union

import numpy as np
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import bounding_boxes_utils as bb_utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json

PilImage = Any


class BBoxFeature(tensor_feature.Tensor):
  """`FeatureConnector` for a normalized bounding box.

  By default, TFDS uses normalized YXYX bbox format. This can be changed by
  passing the `bbox_format` argument, e.g.
  ```
    features=features.FeatureDict({
        'bbox': tfds.features.BBox(bbox_format=bb_utils.BBoxFormat.XYWH),
    })
  ```
  If you don't know the format of the bbox, you can use `bbox_format=None`. In
  this case, the only check that is done is that 4 floats coordinates are
  provided.

  Note: If you have multiple bounding boxes, you may want to wrap the feature
  inside a `tfds.features.Sequence`.

  Input:
    * `tfds.features.BBox` tuple or 4-dim `np.ndarray`.

  Output:
    bbox: tf.Tensor of type `tf.float32` and shape `[4,]` which contains the
      normalized coordinates of the bounding box `[ymin, xmin, ymax, xmax]`

  Example:
    * In the DatasetInfo object:

    ```
    features=features.FeatureDict({
        'bbox': tfds.features.BBox(),
    })
    ```

    * During generation:

    ```
    yield {
        'input': tfds.features.BBox(ymin=0.3, xmin=0.8, ymax=0.5, xmax=1.0),
    }
    ```
  """

  def __init__(
      self,
      *,
      doc: feature_lib.DocArg = None,
      bbox_format: (
          bb_utils.BBoxFormatType | None
      ) = bb_utils.BBoxFormat.REL_YXYX,
  ):
    if isinstance(bbox_format, str):
      bbox_format = bb_utils.BBoxFormat(bbox_format)
    self.bbox_format = bbox_format
    super().__init__(shape=(4,), dtype=np.float32, doc=doc)

  def encode_example(self, bbox: Union[bb_utils.BBox, np.ndarray]):
    """See base class for details."""
    if isinstance(bbox, np.ndarray):
      if bbox.shape != (4,):
        raise ValueError(
            'array representing BBox should have exactly 4 floats. '
            f'Instead, it has {bbox.shape}.'
        )
      bbox = bbox.astype(np.float64)
      bbox = bb_utils.BBox(
          ymin=bbox[0], xmin=bbox[1], ymax=bbox[2], xmax=bbox[3]
      )

    # Validate the coordinates
    for coordinate in bbox:
      if (
          self.bbox_format == bb_utils.BBoxFormat.REL_YXYX
          or self.bbox_format == bb_utils.BBoxFormat.REL_XYXY
      ):
        if not isinstance(coordinate, (float, np.floating)):
          raise ValueError(
              'BBox coordinates should be float. Got {}.'.format(bbox)
          )
        if not 0.0 <= coordinate <= 1.0:
          raise ValueError(
              'BBox coordinates should be between 0 and 1. Got {}.'.format(bbox)
          )
    if (
        self.bbox_format == bb_utils.BBoxFormat.YXYX
        or self.bbox_format == bb_utils.BBoxFormat.REL_YXYX
    ):
      if bbox.xmax < bbox.xmin or bbox.ymax < bbox.ymin:
        raise ValueError(
            'BBox coordinates should have min <= max. Got {}.'.format(bbox)
        )

    return super(BBoxFeature, self).encode_example(
        [bbox.ymin, bbox.xmin, bbox.ymax, bbox.xmax]
    )

  def repr_html(self, ex: np.ndarray) -> str:
    """Returns the HTML str representation of an Image with BBoxes."""
    ex = np.expand_dims(ex, axis=0)  # Expand single bounding box to batch.
    return _repr_html(ex, bbox_format=self.bbox_format)

  def repr_html_batch(self, ex: np.ndarray) -> str:
    """Returns the HTML str representation of an Image with BBoxes (Sequence)."""
    return _repr_html(ex, bbox_format=self.bbox_format)

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.BoundingBoxFeature]
  ) -> 'BBoxFeature':
    if isinstance(value, dict):
      return cls(**value)
    return cls(
        bbox_format=bb_utils.BBoxFormat(value.bbox_format)
        if value.bbox_format
        else None
    )

  def to_json_content(
      self,
  ) -> (
      feature_pb2.BoundingBoxFeature
  ):  # pytype: disable=signature-mismatch  # overriding-return-type-checks
    bbox_format = None
    if self.bbox_format:
      bbox_format = (
          self.bbox_format
          if isinstance(self.bbox_format, str)
          else self.bbox_format.value
      )
    return feature_pb2.BoundingBoxFeature(
        shape=feature_lib.to_shape_proto(self._shape),
        dtype=feature_lib.dtype_to_str(self._dtype),
        bbox_format=bbox_format,
    )


def _repr_html(
    ex: np.ndarray, bbox_format: bb_utils.BBoxFormatType | None
) -> str:
  """Returns the HTML str representation of an Image with BBoxes."""
  # If the bbox format is not normalized, we don't draw the bbox on a blank
  # image but we return a string representation of the bbox instead.
  if bbox_format != bb_utils.BBoxFormat.REL_YXYX:
    return repr(ex)
  img = _build_thumbnail_with_bbox(ex)
  img_str = utils.get_base64(lambda buff: img.save(buff, format='PNG'))
  return f'<img src="data:image/png;base64,{img_str}" alt="Img" />'


def _build_thumbnail_with_bbox(ex: np.ndarray) -> PilImage:
  """Returns blank image with Bboxes drawn on it."""
  PIL_Image = lazy_imports_lib.lazy_imports.PIL_Image  # pylint: disable=invalid-name
  PIL_ImageDraw = lazy_imports_lib.lazy_imports.PIL_ImageDraw  # pylint: disable=invalid-name

  shape = (image_feature.THUMBNAIL_SIZE, image_feature.THUMBNAIL_SIZE)
  blank_img = PIL_Image.new('RGB', shape, (255, 255, 255))
  draw = PIL_ImageDraw.Draw(blank_img)
  rs = np.random.RandomState(97531)  # freeze random state

  for i in range(ex.shape[0]):
    # Rescale coordinates to match size of blank_image
    ymin, xmin, ymax, xmax = ex[i, :] * image_feature.THUMBNAIL_SIZE
    # Generate random rgb values for Bbox ouline
    r, g, b = list(rs.randint(0, 256, size=3))
    draw.rectangle(((xmin, ymin), (xmax, ymax)), outline=(r, g, b))
  return blank_img

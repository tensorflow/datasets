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

"""Image feature."""

from typing import Dict, List, Optional, Union

import tensorflow as tf
from tensorflow_datasets.core.features import class_label_feature
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.utils import type_utils

Json = type_utils.Json

_LabelArg = Union[List[str], type_utils.PathLike, None, int]


class LabeledImage(image_feature.Image):
  """Image with additional label metadata.

  This feature connector is similar to `tfds.features.Image`, but expose
  additional attributes from `tfds.features.ClassLabel` to access label
  metadata.

  This can be used for segmentation tasks were each pixel is labeled.

  ```python
  builder = tfds.builder('my_dataset')
  builder.info.features['label_image'].names == ['background', 'car', ...]
  ```

  """

  def __init__(
      self,
      *,
      labels: _LabelArg,
      shape: Optional[type_utils.Shape] = None,
      dtype: Optional[tf.dtypes.DType] = None,
      encoding_format: Optional[str] = None,
  ):
    """Constructor.

    Labels can be defined as:

    * `List[str]` (e.g. `['background', 'car', 'truck', ...]`): The list of
      label strings.
    * `PathLike` (e.g. `'/path/to/label.txt'`): A file containing the labels
      (one per-line).
    * `int` (e.g. `12`): The total number of labels, if the actual label names
      string are unknown (discouraged).
    * `None`: If the number of label is unknown (discouraged).

    Args:
      labels: Labels metadata (see docstring above)
      shape: Image shape (see `tfds.features.Image.__init__`)
      dtype: Image dtype (see `tfds.features.Image.__init__`)
      encoding_format: 'jpeg' or 'png' (see `tfds.features.Image.__init__`)
    """
    super().__init__(
        # Label images have a single channel
        shape=shape or (None, None, 1),
        dtype=dtype,
        encoding_format=encoding_format,
        use_colormap=True,  # LabeledImage always use colormap
    )
    if self.shape[-1] != 1:
      raise ValueError(
          f'LabeledImage shape should have a single channel. Got: {shape}')
    label_kwargs = _labels_to_kwarg(labels)
    self._class_label = class_label_feature.ClassLabel(**label_kwargs)

  @property
  def num_classes(self) -> Optional[int]:
    return self._class_label.num_classes

  @property
  def names(self) -> List[str]:
    return self._class_label.names

  def save_metadata(self, data_dir, feature_name=None) -> None:
    super().save_metadata(data_dir=data_dir, feature_name=feature_name)
    self._class_label.save_metadata(
        data_dir=data_dir, feature_name=feature_name)

  def load_metadata(self, data_dir, feature_name=None) -> None:
    super().load_metadata(data_dir=data_dir, feature_name=feature_name)
    self._class_label.load_metadata(
        data_dir=data_dir, feature_name=feature_name)

  def _additional_repr_info(self):
    return {'num_classes': self.num_classes}

  @classmethod
  def from_json_content(cls, value: Json) -> 'LabeledImage':
    return cls(**value)

  def to_json_content(self) -> Json:
    content = super().to_json_content()
    content.pop('use_colormap')
    content['labels'] = self.num_classes
    return content


def _labels_to_kwarg(labels: _LabelArg) -> Dict[str, _LabelArg]:
  """Creates the `ClassLabel.__init__` kwargs."""
  if labels is None:
    return {}
  elif isinstance(labels, int):
    kwarg_name = 'num_classes'
  elif isinstance(labels, type_utils.PathLikeCls):
    kwarg_name = 'names_file'
  elif isinstance(labels, list):
    kwarg_name = 'names'
  else:
    raise TypeError(f'Invalid `labels` type: {type(labels)}. Should be one of '
                    'list[labels], path, num_labels')
  return {kwarg_name: labels}

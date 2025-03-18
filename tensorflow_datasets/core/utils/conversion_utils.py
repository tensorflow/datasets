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

"""Utility functions to convert from other formats to TFDS conventions."""

from collections.abc import Mapping, Sequence
import datetime
from typing import Any

from etils import epath
import numpy as np
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import py_utils

_DEFAULT_IMG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178U\x00\x00\x00\x00IEND\xaeB`\x82'


def to_tfds_name(name: str) -> str:
  """Converts a name to a TFDS compatible dataset name.

  Huggingface names can contain characters that are not supported in
  TFDS. For example, in Huggingface a dataset name like `a/b` is supported,
  while in TFDS `b` would be parsed as the config.

  Examples:
  - `name='codeparrot/github-code'` becomes `codeparrot__github_code`.

  Args:
    name: A name to be converted to a TFDS compatible name.

  Returns:
    The TFDS compatible dataset name (dataset names, config names and split
    names).
  """
  name = name.lower().replace('/', '__')
  return py_utils.make_valid_name(name)


def _get_default_value(
    feature: feature_lib.FeatureConnector,
) -> Mapping[str, Any] | Sequence[Any] | bytes | int | float | bool:
  """Returns the default value for a feature.

  Non-TFDS features can be loose as far as typing is concerned. For example,
  HuggingFace accepts None values. As long as `tfds.features.Optional` does not
  exist, we default to a constant default value.

  For int and float, we do not return 0 or -1, but rather -inf, as 0 or -1 can
  be contained in the values of the dataset. In practice, you can compare your
  value to:

  ```
  np.iinfo(np.int32).min  # for integers
  np.finfo(np.float32).min  # for floats
  ...
  ```

  For None images, we set a default value which corresponds to a PNG of 1px,
  black.

  Args:
    feature: The TFDS feature from which we want the default value.

  Raises:
    TypeError: If couldn't recognize feature dtype.
  """
  match feature:
    case feature_lib.FeaturesDict():
      return {
          name: _get_default_value(inner_feature)
          for name, inner_feature in feature.items()
      }
    case feature_lib.Sequence():
      match feature.feature:
        case feature_lib.FeaturesDict():
          return {feature_name: [] for feature_name in feature.feature.keys()}
        case _:
          return []
    case feature_lib.Image():
      # Return an empty PNG image of 1x1 pixel, black.
      return _DEFAULT_IMG
    case _:
      if dtype_utils.is_string(feature.np_dtype):
        return b''
      elif dtype_utils.is_integer(feature.np_dtype):
        return np.iinfo(feature.np_dtype).min
      elif dtype_utils.is_floating(feature.np_dtype):
        return np.finfo(feature.np_dtype).min
      elif dtype_utils.is_bool(feature.np_dtype):
        return False
      else:
        raise TypeError(f'Could not recognize the dtype of {feature}')


def to_tfds_value(value: Any, feature: feature_lib.FeatureConnector) -> Any:
  """Converts a value to a TFDS compatible value.

  Args:
    value: The value to be converted to follow TFDS conventions.
    feature: The TFDS feature for which we want the compatible value.

  Returns:
    The TFDS compatible value.

  Raises:
    TypeError: If couldn't recognize the given feature type.
  """
  match value:
    case None:
      return _get_default_value(feature)
    case datetime.datetime():
      return int(value.timestamp())

  match feature:
    case feature_lib.ClassLabel() | feature_lib.Scalar():
      return value
    case feature_lib.FeaturesDict():
      return {
          name: to_tfds_value(value.get(name), inner_feature)
          for name, inner_feature in feature.items()
      }
    case feature_lib.Sequence():
      match value:
        case dict():
          # Should be a dict of lists:
          return {
              name: [
                  to_tfds_value(inner_hf_value, inner_feature)
                  for inner_hf_value in value.get(name)
              ]
              for name, inner_feature in feature.feature.items()
          }
        case list():
          return [
              to_tfds_value(inner_hf_value, feature.feature)
              for inner_hf_value in value
          ]
        case _:
          return [value]
    case feature_lib.Audio():
      if (array := value.get('array')) is not None:
        # Hugging Face uses floats, TFDS uses integers.
        # Here we convert the float in [-1, 1] range into signed int32
        # range [-2**32, 2**32-1]. Nevertheless, the mantissa size of
        # float32 is 23 bits, therefore the maximum bit depth possible is 23.
        dtype = feature.dtype
        return (array * np.iinfo(dtype).max).astype(dtype=dtype)
      elif (path := value.get('path')) and (path := epath.Path(path)).exists():
        return path
    case feature_lib.Image():
      value: lazy_imports_lib.lazy_imports.PIL_Image.Image
      # Ensure RGB format for PNG encoding.
      return value.convert('RGB')
    case feature_lib.Tensor():
      if isinstance(value, float):
        # In some cases, for example when loading jsonline files using pandas,
        # empty non-float values, such as strings, are converted to float nan.
        # We spot those occurrences as the feature.np_dtype is not float.
        if np.isnan(value) and not dtype_utils.is_floating(feature.np_dtype):
          return _get_default_value(feature)
      return value

  raise TypeError(
      f'Conversion of value {value} to feature {feature} is not supported.'
  )

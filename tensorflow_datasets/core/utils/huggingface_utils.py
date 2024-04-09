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

"""Utility functions for huggingface_dataset_builder."""

from collections.abc import Mapping, Sequence
import datetime
from typing import Any, Type, TypeVar

from etils import epath
import immutabledict
import numpy as np
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import datasets as hf_datasets
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


_HF_DTYPE_TO_NP_DTYPE = immutabledict.immutabledict({
    'bool': np.bool_,
    'float': np.float32,
    'double': np.float64,
    'large_string': np.object_,
    'utf8': np.object_,
    'string': np.object_,
})
_IMAGE_ENCODING_FORMAT = 'png'
_DEFAULT_IMG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x04\x00\x01\xf6\x178U\x00\x00\x00\x00IEND\xaeB`\x82'
_StrOrNone = TypeVar('_StrOrNone', str, None)


def _convert_to_np_dtype(hf_dtype: str) -> Type[np.generic]:
  """Returns the `np.dtype` scalar feature.

  Args:
    hf_dtype: Huggingface dtype.

  Raises:
    TypeError: If couldn't recognize Huggingface dtype.
  """
  if np_dtype := _HF_DTYPE_TO_NP_DTYPE.get(hf_dtype):
    return np_dtype
  elif hasattr(np, hf_dtype):
    return getattr(np, hf_dtype)
  if hf_dtype.startswith('timestamp'):
    # Timestamps are converted to seconds since UNIX epoch.
    return np.int64
  elif hasattr(tf.dtypes, hf_dtype):
    return getattr(tf.dtypes, hf_dtype)
  else:
    raise TypeError(
        f'Unrecognized type {hf_dtype}. Please open an issue if you think '
        'this is a bug.'
    )


def convert_hf_features(hf_features) -> feature_lib.FeatureConnector:
  """Converts Huggingface feature spec to a TFDS compatible feature spec.

  Args:
    hf_features: Huggingface feature spec.

  Returns:
    The TFDS compatible feature spec.

  Raises:
    ValueError: If the given Huggingface features is a list with length > 1.
    TypeError: If couldn't recognize the given feature spec.
  """
  match hf_features:
    case hf_datasets.Features() | dict():
      return feature_lib.FeaturesDict({
          name: convert_hf_features(hf_inner_feature)
          for name, hf_inner_feature in hf_features.items()
      })
    case hf_datasets.Sequence():
      return feature_lib.Sequence(
          feature=convert_hf_features(hf_features.feature)
      )
    case list():
      if len(hf_features) != 1:
        raise ValueError(f'List {hf_features} should have a length of 1.')
      return feature_lib.Sequence(feature=convert_hf_features(hf_features[0]))
    case hf_datasets.Value():
      return feature_lib.Scalar(dtype=_convert_to_np_dtype(hf_features.dtype))
    case hf_datasets.ClassLabel():
      if hf_features.names:
        return feature_lib.ClassLabel(names=hf_features.names)
      if hf_features.names_file:
        return feature_lib.ClassLabel(names_file=hf_features.names_file)
      if hf_features.num_classes:
        return feature_lib.ClassLabel(num_classes=hf_features.num_classes)
    case hf_datasets.Translation():
      return feature_lib.Translation(languages=hf_features.languages)
    case hf_datasets.TranslationVariableLanguages():
      return feature_lib.TranslationVariableLanguages(
          languages=hf_features.languages
      )
    case hf_datasets.Image():
      return feature_lib.Image(encoding_format=_IMAGE_ENCODING_FORMAT)
    case hf_datasets.Audio():
      return feature_lib.Audio(sample_rate=hf_features.sampling_rate)

  raise TypeError(f'Type {type(hf_features)} is not supported.')


def _get_default_value(
    feature: feature_lib.FeatureConnector,
) -> Mapping[str, Any] | Sequence[Any] | bytes | int | float | bool:
  """Returns the default value for a feature.

  Hugging Face is loose as far as typing is concerned. It accepts None values.
  As long as `tfds.features.Optional` does not exist, we default to a constant
  default value.

  For int and float, we do not return 0 or -1, but rather -inf, as 0 or -1 can
  be contained in the values of the dataset. In practice, you can compare your
  value to:

  ```
  np.iinfo(np.int32).min  # for integers
  np.finfo(np.float32).min  # for floats
  ...
  ```

  For images, if the HuggingFace dataset does not contain an image, we
  set a default value which corresponds to a PNG of 1px, black.

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


def convert_hf_value(
    hf_value: Any, feature: feature_lib.FeatureConnector
) -> Any:
  """Converts Huggingface value to a TFDS compatible value.

  Args:
    hf_value: Huggingface value.
    feature: The TFDS feature for which we want the compatible value.

  Returns:
    The TFDS compatible value.

  Raises:
    TypeError: If couldn't recognize the given feature type.
  """
  match hf_value:
    case None:
      return _get_default_value(feature)
    case datetime.datetime():
      return int(hf_value.timestamp())

  match feature:
    case feature_lib.ClassLabel() | feature_lib.Scalar():
      return hf_value
    case feature_lib.FeaturesDict():
      return {
          name: convert_hf_value(hf_value.get(name), inner_feature)
          for name, inner_feature in feature.items()
      }
    case feature_lib.Sequence():
      match hf_value:
        case dict():
          # Should be a dict of lists:
          return {
              name: [
                  convert_hf_value(inner_hf_value, inner_feature)
                  for inner_hf_value in hf_value.get(name)
              ]
              for name, inner_feature in feature.feature.items()
          }
        case list():
          return [
              convert_hf_value(inner_hf_value, feature.feature)
              for inner_hf_value in hf_value
          ]
        case _:
          return [hf_value]
    case feature_lib.Audio():
      if array := hf_value.get('array'):
        # Hugging Face uses floats, TFDS uses integers.
        return [int(sample * feature.sample_rate) for sample in array]
      elif (path := hf_value.get('path')) and (
          path := epath.Path(path)
      ).exists():
        return path
    case feature_lib.Image():
      hf_value: lazy_imports_lib.lazy_imports.PIL_Image.Image
      # Ensure RGB format for PNG encoding.
      return hf_value.convert('RGB')
    case feature_lib.Tensor():
      return hf_value

  raise TypeError(
      f'Conversion of value {hf_value} to feature {feature} is not supported.'
  )


def convert_hf_name(hf_name: _StrOrNone) -> _StrOrNone:
  """Converts Huggingface name to a TFDS compatible dataset name.

  Huggingface names can contain characters that are not supported in
  TFDS. For example, in Huggingface a dataset name like `a/b` is supported,
  while in TFDS `b` would be parsed as the config.

  Examples:
  - `hf_name='codeparrot/github-code'` becomes `codeparrot__github_code`.

  Args:
    hf_name: Huggingface name.

  Returns:
    The TFDS compatible dataset name (dataset names, config names and split
    names).
  """
  if hf_name is None:
    return hf_name
  hf_name = hf_name.lower().replace('/', '__')
  return py_utils.make_valid_name(hf_name)


def convert_tfds_dataset_name(tfds_dataset_name: str) -> str:
  """Converts TFDS dataset name to a Huggingface compatible dataset name.

  As TFDS doesn't support case-sensitive names, we list all HF datasets and pick
  the dataset that has a case-insensitive match.

  Args:
    tfds_dataset_name: TFDS dataset name.

  Returns:
    The Huggingface compatible dataset name.

  Raises:
    DatasetNotFoundError: If the TFDS dataset name doesn't correspond to any
    existing Huggingface dataset.
  """
  for hf_dataset_name in hf_datasets.list_datasets():
    if convert_hf_name(hf_dataset_name) == tfds_dataset_name.lower():
      return hf_dataset_name
  raise registered.DatasetNotFoundError(
      f'"{tfds_dataset_name}" is not listed in Huggingface datasets.'
  )

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

from __future__ import annotations

from typing import Type, TypeVar

import immutabledict
import numpy as np
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import datasets as hf_datasets
from tensorflow_datasets.core.utils.lazy_imports_utils import huggingface_hub
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


_HF_DTYPE_TO_NP_DTYPE = immutabledict.immutabledict({
    'bool': np.bool_,
    'float': np.float32,
    'double': np.float64,
    'large_string': np.object_,
    'utf8': np.object_,
    'string': np.object_,
    'binary': np.bytes_,
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


def to_huggingface_name(tfds_dataset_name: str) -> str:
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
  for hf_dataset_name in huggingface_hub.list_datasets():
    if (
        conversion_utils.to_tfds_name(hf_dataset_name)
        == tfds_dataset_name.lower()
    ):
      return hf_dataset_name
  raise registered.DatasetNotFoundError(
      f'"{tfds_dataset_name}" is not listed in Huggingface datasets.'
  )

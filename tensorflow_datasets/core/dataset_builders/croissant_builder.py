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

"""DatasetBuilder initialized from a Croissant config file.

Croissant is a high-level format for machine learning datasets
https://github.com/mlcommons/croissant

A CroissantBuilder initialized a TFDS DatasetBuilder from a Croissant dataset
file; each of the record_set_names specified will result in a separate
ConfigBuilder.

```python

titanic_file="path/to/titanic/metadata.json"
d = croissant_builder.CroissantBuilder(
      file=titanic_file, record_set_names=["passengers"]
  )
```
"""

from typing import Any, Dict, Optional, Sequence

from etils import epath
import numpy as np
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import download
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc
from tensorflow_datasets.core.utils.lazy_imports_utils import pandas as pd


def datatype_converter(
    field,
    int_dtype: Optional[type_utils.TfdsDType] = np.int64,
    float_dtype: Optional[type_utils.TfdsDType] = np.float32,
):
  """Converts a Croissant field to a TFDS-compatible feature.

  Args:
    field: A mlcroissant Field object.
    int_dtype: The dtype to use for TFDS integer features. Defaults to np.int64.
    float_dtype: The dtype to use for TFDS float features. Defaults to
      np.float32.

  Returns:
    Converted datatype for TFDS.

  Raises:
    NotImplementedError
  """
  if field.is_enumeration:
    raise NotImplementedError("Not implemented yet.")

  field_data_type = field.data_type

  if not field_data_type:
    return None
  elif field_data_type == int:
    return int_dtype
  elif field_data_type == float:
    return float_dtype
  elif field_data_type == bool:
    return np.bool_
  elif field_data_type == bytes:
    return text_feature.Text(doc=field.description)
  # We return a text feature for mlc.DataType.DATE features.
  elif field_data_type == pd.Timestamp:
    return text_feature.Text(doc=field.description)
  elif field_data_type == mlc.DataType.IMAGE_OBJECT:
    return image_feature.Image(doc=field.description)
  else:
    raise ValueError(f"Unknown data type: {field_data_type}.")


class CroissantBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """DatasetBuilder initialized from a Croissant config file."""

  def __init__(
      self,
      *,
      file: epath.PathLike,
      record_set_names: Sequence[str],
      disable_shuffling: Optional[bool] = False,
      int_dtype: Optional[type_utils.TfdsDType] = np.int64,
      float_dtype: Optional[type_utils.TfdsDType] = np.float32,
      **kwargs: Any,
  ):
    """Initializes a CroissantBuilder.

    Args:
      file: The Croissant config file for the given dataset.
      record_set_names: The names of the record sets to generate. Each record
        set will correspond to a separate config.
      disable_shuffling: Specify whether to shuffle the examples.
      int_dtype: The dtype to use for TFDS integer features. Defaults to
        np.int64.
      float_dtype: The dtype to use for TFDS float features. Defaults to
        np.float32.
      **kwargs: kwargs to pass to GeneratorBasedBuilder directly.
    """
    self.dataset = mlc.Dataset(file)
    self.name = self.dataset.metadata.name
    self.metadata = self.dataset.metadata

    # pylint: disable=g-bad-todo
    # TODO(https://github.com/mlcommons/croissant/issues/91): Correctly
    # populate the version once versioning is fixed for Croissant.
    self.VERSION = "1.0.0"  # pylint: disable=invalid-name
    self.RELEASE_NOTES = {}  # pylint: disable=invalid-name

    self.BUILDER_CONFIGS: Sequence[dataset_builder.BuilderConfig] = [  # pylint: disable=invalid-name
        dataset_builder.BuilderConfig(name=record_set_name)
        for record_set_name in record_set_names
    ]

    self._disable_shuffling = disable_shuffling

    self._int_dtype = int_dtype
    self._float_dtype = float_dtype

    super().__init__(
        **kwargs,
    )

  @property
  def builder_config(self) -> dataset_builder.BuilderConfig:
    """`tfds.core.BuilderConfig` for this builder."""
    return self._builder_config  # pytype: disable=bad-return-type  # always-use-return-annotations

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(
        builder=self,
        description=self.dataset.metadata.description,
        features=self.get_features(),
        homepage=self.dataset.metadata.url,
        citation=self.dataset.metadata.citation,
        license=self.dataset.metadata.license,
        disable_shuffling=self._disable_shuffling,
    )

  def get_record_set(self, record_set_name: str):
    """Returns the desired record set from self.metadata."""
    for record_set in self.dataset.metadata.record_sets:
      if record_set.name == record_set_name:
        return record_set
    raise ValueError(
        f"Did not find any record set with the name {record_set_name}."
    )

  def get_features(self) -> Optional[feature_lib.FeatureConnector]:
    """Infers the features dict for the required record set."""
    record_set = self.get_record_set(self.builder_config.name)

    fields = record_set.fields
    features = {}
    for field in fields:
      feature = datatype_converter(
          field, int_dtype=self._int_dtype, float_dtype=self._float_dtype
      )
      if field.repeated:
        feature = sequence_feature.Sequence(feature)
      features[field.name] = feature
    return features_dict.FeaturesDict(features)

  def _split_generators(
      self, dl_manager: download.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    # This will be updated when partitions are implemented in Croissant, ref to:
    # https://docs.google.com/document/d/1saz3usja6mk5ugJXNF64_uSXsOzIgbIV28_bu1QamVY
    return {"default": self._generate_examples()}  # pylint: disable=unreachable

  def _generate_examples(
      self,
  ) -> split_builder_lib.SplitGenerator:
    records = self.dataset.records(self.builder_config.name)
    for i, record in enumerate(records):
      yield i, record

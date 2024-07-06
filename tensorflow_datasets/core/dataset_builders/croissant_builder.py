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

"""DatasetBuilder initialized from a Croissant config file.

Croissant is a high-level format for machine learning datasets
https://github.com/mlcommons/croissant

A CroissantBuilder initializes a TFDS DatasetBuilder from a Croissant dataset
file; each of the record_set_ids specified will result in a separate
ConfigBuilder.

```python
import tensorflow_datasets as tfds
builder = tfds.dataset_builders.CroissantBuilder(
    jsonld="https://raw.githubusercontent.com/mlcommons/croissant/main/datasets/0.8/huggingface-mnist/metadata.json",
    file_format='array_record',
)
builder.download_and_prepare()
ds = builder.as_data_source()
print(ds['default'][0])
```
"""

from collections.abc import Mapping
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
from tensorflow_datasets.core.utils import croissant_utils
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils import version as version_utils
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
    raise NotImplementedError('Not implemented yet.')

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
    raise ValueError(f'Unknown data type: {field_data_type}.')


def _extract_license(license_: Any) -> str | None:
  """Extracts the full terms of a license as a string.

  In case the license is a CreativeWork, we join the name, description and url
  fields with brackets, e.g.
  [U.S. Government Works][https://www.usa.gov/government-works/].

  Args:
    license_: The license from mlcroissant.

  Returns:
    The full terms of the license as a string.
  """
  if isinstance(license_, str):
    return license_
  elif isinstance(license_, mlc.CreativeWork):
    possible_fields = [license_.name, license_.description, license_.url]
    fields = [field for field in possible_fields if field]
    return '[' + ']['.join(fields) + ']'
  raise ValueError(
      f'license_ should be mlc.CreativeWork | str. Got {type(license_)}'
  )


def _get_license(metadata: Any) -> str | None:
  """Gets the license from the metadata."""
  if not isinstance(metadata, mlc.Metadata):
    raise ValueError(f'metadata should be mlc.Metadata. Got {type(metadata)}')
  licenses = metadata.license
  if licenses:
    return ', '.join([_extract_license(l) for l in licenses if l])
  return None


class CroissantBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """DatasetBuilder initialized from a Croissant config file."""

  def __init__(
      self,
      *,
      jsonld: epath.PathLike,
      record_set_ids: Sequence[str] | None = None,
      disable_shuffling: bool | None = False,
      int_dtype: type_utils.TfdsDType | None = np.int64,
      float_dtype: type_utils.TfdsDType | None = np.float32,
      mapping: Mapping[str, epath.PathLike] | None = None,
      overwrite_version: str | None = None,
      **kwargs: Any,
  ):
    """Initializes a CroissantBuilder.

    Args:
      jsonld: The Croissant JSON-LD for the given dataset: either a file path or
        a URL.
      record_set_ids: The @ids of the record sets for the dataset. Each record
        set will correspond to a separate config. If not specified, a config
        will be generated for each record set defined in the Croissant JSON-LD,
        except for the record sets which specify `cr:data`.
      disable_shuffling: Specify whether to shuffle the examples.
      int_dtype: The dtype to use for TFDS integer features. Defaults to
        np.int64.
      float_dtype: The dtype to use for TFDS float features. Defaults to
        np.float32.
      mapping: Mapping filename->filepath as a Python dict[str, str] to handle
        manual downloads. If `document.csv` is the FileObject and you downloaded
        it to `~/Downloads/document.csv`, you can specify
        `mapping={"document.csv": "~/Downloads/document.csv"}`.
      overwrite_version: Semantic version of the dataset to be set.
      **kwargs: kwargs to pass to GeneratorBasedBuilder directly.
    """
    if mapping is None:
      mapping = {}
    self.dataset = mlc.Dataset(jsonld, mapping=mapping)
    self.name = croissant_utils.get_tfds_dataset_name(self.dataset)
    self.metadata = self.dataset.metadata

    # In TFDS, version is a mandatory attribute, while in Croissant it is only a
    # recommended attribute. If the version is unspecified in Croissant, we set
    # it to `1.0.0` in TFDS.
    self.VERSION = version_utils.Version(  # pylint: disable=invalid-name
        overwrite_version or self.dataset.metadata.version or '1.0.0'
    )
    self.RELEASE_NOTES = {}  # pylint: disable=invalid-name

    if not record_set_ids:
      record_set_ids = croissant_utils.get_record_set_ids(self.metadata)
    config_names = [
        huggingface_utils.convert_hf_name(record_set)
        for record_set in record_set_ids
    ]
    self.BUILDER_CONFIGS: Sequence[dataset_builder.BuilderConfig] = [  # pylint: disable=invalid-name
        dataset_builder.BuilderConfig(name=config_name)
        for config_name in config_names
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
        citation=self.dataset.metadata.cite_as,
        license=_get_license(self.dataset.metadata),
        disable_shuffling=self._disable_shuffling,
    )

  def get_record_set(self, record_set_id: str):
    """Returns the desired record set from self.metadata."""
    for record_set in self.dataset.metadata.record_sets:
      if huggingface_utils.convert_hf_name(record_set.id) == record_set_id:
        return record_set
    raise ValueError(
        f'Did not find any record set with the name {record_set_id}.'
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
    return {'default': self._generate_examples()}  # pylint: disable=unreachable

  def _generate_examples(
      self,
  ) -> split_builder_lib.SplitGenerator:
    record_set = self.get_record_set(self.builder_config.name)
    records = self.dataset.records(record_set.id)
    for i, record in enumerate(records):
      # Some samples might not be TFDS-compatible as-is, e.g. from croissant
      # describing HuggingFace datasets, so we convert them here. This shouldn't
      # impact datasets which are already TFDS-compatible.
      record = huggingface_utils.convert_hf_value(record, self.info.features)
      yield i, record

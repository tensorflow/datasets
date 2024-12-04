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
    jsonld="https://raw.githubusercontent.com/mlcommons/croissant/main/datasets/1.0/huggingface-mnist/metadata.json",
    file_format='array_record',
)
builder.download_and_prepare()
ds = builder.as_data_source()
print(ds['default'][0])
```
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import json
from typing import Any

from etils import epath
import numpy as np
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import download
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.features import bounding_boxes
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils import croissant_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils import version as version_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc
from tensorflow_datasets.core.utils.lazy_imports_utils import pandas as pd


_RecordOrFeature = Mapping[str, Any]


def _strip_record_set_prefix(
    record_or_feature: _RecordOrFeature, record_set_id: str
) -> _RecordOrFeature:
  """Removes the record set prefix from the field ids of a record or feature."""
  return {
      field_id.removeprefix(f'{record_set_id}/'): value
      for field_id, value in record_or_feature.items()
  }


def datatype_converter(
    field: mlc.Field,
    int_dtype: type_utils.TfdsDType = np.int64,
    float_dtype: type_utils.TfdsDType = np.float32,
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
    # Fields with sub fields are of type None
    if field.sub_fields:
      feature = features_dict.FeaturesDict(
          {
              subfield.id: datatype_converter(
                  subfield, int_dtype=int_dtype, float_dtype=float_dtype
              )
              for subfield in field.sub_fields
          },
          doc=field.description,
      )
    else:
      feature = None
  elif field_data_type == int:
    feature = int_dtype
  elif field_data_type == float:
    feature = float_dtype
  elif field_data_type == bool:
    feature = np.bool_
  elif field_data_type == bytes:
    feature = text_feature.Text(doc=field.description)
  # We return a text feature for mlc.DataType.DATE features.
  elif field_data_type == pd.Timestamp:
    feature = text_feature.Text(doc=field.description)
  elif field_data_type == mlc.DataType.IMAGE_OBJECT:
    feature = image_feature.Image(doc=field.description)
  elif field_data_type == mlc.DataType.BOUNDING_BOX:
    # TFDS uses REL_YXYX by default, but Hugging Face doesn't enforce a format.
    feature = bounding_boxes.BBoxFeature(
        doc=field.description, bbox_format=None
    )
  else:
    raise ValueError(f'Unknown data type: {field_data_type}.')

  if feature and field.repeated:
    feature = sequence_feature.Sequence(feature, doc=field.description)
  return feature


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
      jsonld: epath.PathLike | Mapping[str, Any],
      record_set_ids: Sequence[str] | None = None,
      disable_shuffling: bool | None = False,
      int_dtype: type_utils.TfdsDType = np.int64,
      float_dtype: type_utils.TfdsDType = np.float32,
      mapping: Mapping[str, epath.PathLike] | None = None,
      overwrite_version: version_lib.VersionOrStr | None = None,
      filters: Mapping[str, Any] | None = None,
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
      filters: A dict of filters to apply to the records at preparation time (in
        the `_generate_examples` function). The keys should be field names and
        the values should be the values to filter by. If a record matches all
        the filters, it will be included in the dataset.
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
    self.VERSION = version_lib.Version(  # pylint: disable=invalid-name
        overwrite_version or self.dataset.metadata.version or '1.0.0'
    )
    self.RELEASE_NOTES = {}  # pylint: disable=invalid-name

    if not record_set_ids:
      record_set_ids = croissant_utils.get_record_set_ids(self.metadata)
    config_names = [
        conversion_utils.to_tfds_name(record_set_id)
        for record_set_id in record_set_ids
    ]
    self.BUILDER_CONFIGS: list[dataset_builder.BuilderConfig] = [  # pylint: disable=invalid-name
        dataset_builder.BuilderConfig(name=config_name)
        for config_name in config_names
    ]

    self._disable_shuffling = disable_shuffling

    self._int_dtype = int_dtype
    self._float_dtype = float_dtype
    self._filters = filters or {}

    super().__init__(
        **kwargs,
    )

  @property
  def builder_config(self) -> dataset_builder.BuilderConfig:
    """`tfds.core.BuilderConfig` for this builder."""
    return (
        self._builder_config
    )  # pytype: disable=bad-return-type  # always-use-return-annotations

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

  def get_features(self) -> features_dict.FeaturesDict:
    """Infers the features dict for the required record set."""
    record_set = croissant_utils.get_record_set(
        self.builder_config.name, metadata=self.metadata
    )
    fields = record_set.fields
    features = {}
    for field in fields:
      feature = datatype_converter(
          field, int_dtype=self._int_dtype, float_dtype=self._float_dtype
      )
      features[field.id] = feature
    features = _strip_record_set_prefix(features, record_set.id)
    return features_dict.FeaturesDict(features)

  def _split_generators(
      self,
      dl_manager: download.DownloadManager,
      pipeline: beam.Pipeline,
  ) -> dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager  # unused
    del pipeline  # unused
    # If a split recordset is joined for the required record set, we generate
    # splits accordingly. Otherwise, it generates a single `default` split with
    # all the records.
    record_set = croissant_utils.get_record_set(
        self.builder_config.name, metadata=self.metadata
    )
    if split_reference := croissant_utils.get_split_recordset(
        record_set, metadata=self.metadata
    ):
      # The key used in the split recordset's data is referenced in the
      # reference field.
      split_key = split_reference.reference_field.references.field
      return {
          split[split_key]: self._generate_examples(
              filters={
                  **self._filters,
                  split_reference.reference_field.id: split[split_key],
              },
          )
          for split in split_reference.split_record_set.data
      }
    else:
      return {'default': self._generate_examples(filters=self._filters)}

  def _generate_examples(
      self,
      filters: dict[str, Any],
  ) -> beam.PTransform:
    """Generates the examples for the given record set.

    Args:
      filters: A dict of filters to apply to the records. The keys should be
        field names and the values should be the values to filter by. If a
        record matches all the filters, it will be included in the dataset.

    Returns:
      A collection with tuple of (index, record) for each record in the dataset.
    """
    record_set = croissant_utils.get_record_set(
        self.builder_config.name, metadata=self.metadata
    )
    records = self.dataset.records(record_set.id, filters=filters)

    def convert_to_tfds_format(
        global_index: int,
        record: _RecordOrFeature,
        features: feature_lib.FeatureConnector | None = None,
        record_set_id: str | None = None,
    ) -> tuple[int, _RecordOrFeature]:
      if not features:
        raise ValueError('features should not be None.')
      if not record_set_id:
        raise ValueError('record_set_id should not be None.')
      record = _strip_record_set_prefix(record, record_set_id)
      return (
          global_index,
          conversion_utils.to_tfds_value(record, features),
      )

    return (
        records.beam_reader()
        | f'Convert to TFDS format for filters: {json.dumps(filters)}'
        >> beam.MapTuple(
            convert_to_tfds_format,
            features=self.info.features,
            record_set_id=record_set.id,
        )
    )

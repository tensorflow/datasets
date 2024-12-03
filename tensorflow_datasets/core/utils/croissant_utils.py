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

"""Utility functions for croissant_builder."""

from __future__ import annotations

import dataclasses
import typing

from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc

if typing.TYPE_CHECKING:
  # pylint: disable=g-bad-import-order
  import mlcroissant as mlc

_HUGGINGFACE_URL_PREFIX = "https://huggingface.co/datasets/"


@dataclasses.dataclass(frozen=True)
class SplitReference:
  """Information about a split reference in a Croissant dataset."""

  # A split record set in a Croissant dataset.
  split_record_set: mlc.RecordSet
  # A field from another record set that references split_record_set.
  reference_field: mlc.Field


def get_dataset_name(dataset: mlc.Dataset) -> str:
  """Returns dataset name of the given MLcroissant dataset."""
  if (url := dataset.metadata.url) and url.startswith(_HUGGINGFACE_URL_PREFIX):
    return url.removeprefix(_HUGGINGFACE_URL_PREFIX)
  return dataset.metadata.name


def get_tfds_dataset_name(dataset: mlc.Dataset) -> str:
  """Returns TFDS compatible dataset name of the given MLcroissant dataset."""
  dataset_name = get_dataset_name(dataset)
  return conversion_utils.to_tfds_name(dataset_name)


def get_record_set(
    tfds_config_name: str, metadata: mlc.Metadata
) -> mlc.RecordSet:
  """Returns the desired record set from a dataset's metadata."""
  for record_set in metadata.record_sets:
    if conversion_utils.to_tfds_name(record_set.id) == tfds_config_name:
      return record_set
  raise ValueError(
      f"Did not find any record set with the name {tfds_config_name}."
  )


def get_field(field_id: str, metadata: mlc.Metadata) -> mlc.Field:
  """Returns the desired field from a dataset's metadata."""
  for record_set in metadata.record_sets:
    for field in record_set.fields:
      if field.id == field_id:
        return field
  raise ValueError(f"Did not find any field with the name {field_id}.")


def get_record_set_for_field(
    field_id: str, metadata: mlc.Metadata
) -> mlc.RecordSet:
  """Given a field id, returns the record set it belongs to, if any."""
  for record_set in metadata.record_sets:
    for field in record_set.fields:
      if field.id == field_id:
        return record_set
  raise ValueError(f"Did not find any record set with field {field_id}.")


def get_split_recordset(
    record_set: mlc.RecordSet, metadata: mlc.Metadata
) -> SplitReference | None:
  """If a given recordset references a split recordset, returns it.

  Args:
    record_set: The record set to check.
    metadata: The metadata of the dataset.

  Returns:
    If found, a tuple containing: (the field referencing the split record set,
    and the split record set), None otherwise.
  """
  for field in record_set.fields:
    if field.references and field.references.field:
      # Check that the referenced record set is of type `cr:Split`.
      referenced_field = get_field(field.references.field, metadata)
      record_sets = [
          node
          for node in referenced_field.predecessors
          if isinstance(node, mlc.RecordSet)
      ]
      if not record_sets:
        raise ValueError("field {field.id} has no RecordSet")
      referenced_record_set = record_sets[0]
      if mlc.DataType.SPLIT in referenced_record_set.data_types:
        return SplitReference(referenced_record_set, field)
  return None


def get_record_set_ids(metadata: mlc.Metadata) -> list[str]:
  """Returns record set ids of the given MLcroissant metadata.

  Record sets which have the attribute `cr:Data` are excluded (e.g. splits that
  specify split or labels mappings).

  Args:
    metadata: The metadata of the dataset.
  """
  record_set_ids = []
  for record_set in metadata.record_sets:
    if record_set.data is not None:
      continue
    record_set_ids.append(record_set.id)
  return record_set_ids

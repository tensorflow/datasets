# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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
import re
import typing

from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc

if typing.TYPE_CHECKING:
  # pylint: disable=g-bad-import-order
  import mlcroissant as mlc

_HUGGINGFACE_URL_PREFIX = "https://huggingface.co/datasets/"
_VERSION_REGEX_WITHOUT_PATCH = re.compile(r"^(?P<major>\d+)\.(?P<minor>\d+)$")


@dataclasses.dataclass(frozen=True)
class SplitReference:
  """Information about a split reference in a Croissant dataset."""

  # A split record set in a Croissant dataset.
  split_record_set: mlc.RecordSet
  # A field from another record set that references split_record_set.
  reference_field: mlc.Field


def get_croissant_version(version: str | None) -> str | None:
  """Returns the possibly corrected Croissant version in TFDS format.

  TFDS expects versions to follow the Semantic versioning 2.0.0 syntax, but
  Croissant is more lax and accepts also {major.minor}. To avoid raising errors
  in these cases, we add a `0` as a patch version to the Croissant-provided
  version.

  Args:
    version: The Croissant version.

  Returns:
    The Croissant version in TFDS format.
  """
  if not version:
    return None
  if _VERSION_REGEX_WITHOUT_PATCH.match(version):
    return f"{version}.0"
  return version


def extract_localized_string(
    attribute: str | dict[str, str] | None,
    language: str | None = None,
    field_name: str = "text field",
) -> str | None:
  """Returns the text in the specified language from a potentially localized object.

  Some attributes in Croissant (e.g., `name` and `description`) can be
  localized, meaning that they can be either simple strings, or dictionaries
  mapping language codes to strings (e.g., `{"en": "English Name", "fr": "Nom
  français"}`). This function extracts the text in the specified language from a
  potentially localized object.

  Args:
    attribute: The object containing the text, which can be a simple string, a
      dictionary mapping language codes to strings, or None.
    language: The desired language code. If None, a heuristic is used: 'en' is
      preferred, otherwise the first available language in the dictionary.
    field_name: The name of the field being processed (e.g., "name",
      "description"), used for error messages.

  Returns:
    The text string in the desired language, or None if the input is None.

  Raises:
    ValueError: If the text_object is an empty dictionary, or if the specified
      language is not found.
    TypeError: If attribute is not a str, dict, or None.
  """
  if attribute is None:
    return None
  if isinstance(attribute, str):
    return attribute

  if not isinstance(attribute, dict):
    raise TypeError(
        f"{field_name} must be a string, dictionary, or None. Got"
        f" {type(attribute)}"
    )

  if language is None:
    # Try a heuristic language, e.g., 'en'.
    if "en" in attribute:
      return attribute["en"]
    # Otherwise, take the first language in the dict.
    try:
      first_lang = next(iter(attribute))
      return attribute[first_lang]
    except StopIteration as exc:
      raise ValueError(f"Dataset `{field_name}` dictionary is empty.") from exc
  elif language in attribute:
    return attribute[language]
  else:
    raise ValueError(
        f"Language '{language}' not found in {field_name} keys:"
        f" {list(attribute.keys())}."
    )


def get_dataset_name(dataset: mlc.Dataset, language: str | None = None) -> str:
  """Returns dataset name of the given MLcroissant dataset.

  Args:
    dataset: The MLcroissant dataset.
    language: For datasets with multiple names in different languages, this
      argument specifies the language to use.
  """
  if (url := dataset.metadata.url) and url.startswith(_HUGGINGFACE_URL_PREFIX):
    return url.removeprefix(_HUGGINGFACE_URL_PREFIX)
  name = extract_localized_string(
      dataset.metadata.name, language=language, field_name="name"
  )
  if name is None:
    # This case should ideally be prevented by mlcroissant's validation
    # ensuring metadata.name is not None.
    raise ValueError("Dataset name is missing.")
  return name


def get_tfds_dataset_name(
    dataset: mlc.Dataset, language: str | None = None
) -> str:
  """Returns TFDS compatible dataset name of the given MLcroissant dataset.

  Args:
    dataset: The MLcroissant dataset.
    language: For datasets with multiple names in different languages, this
      argument specifies the language to use.
  """
  dataset_name = get_dataset_name(dataset, language=language)
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
        raise ValueError(f"Field {field.id} has no RecordSet.")
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

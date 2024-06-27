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

import typing

from tensorflow_datasets.core.utils import huggingface_utils

if typing.TYPE_CHECKING:
  # pylint: disable=g-bad-import-order
  import mlcroissant as mlc

_HUGGINGFACE_URL_PREFIX = 'https://huggingface.co/datasets/'


def get_dataset_name(dataset: mlc.Dataset) -> str:
  """Returns dataset name of the given MLcroissant dataset."""
  if (url := dataset.metadata.url) and url.startswith(_HUGGINGFACE_URL_PREFIX):
    return url.removeprefix(_HUGGINGFACE_URL_PREFIX)
  return dataset.metadata.name


def get_tfds_dataset_name(dataset: mlc.Dataset) -> str:
  """Returns TFDS compatible dataset name of the given MLcroissant dataset."""
  dataset_name = get_dataset_name(dataset)
  return huggingface_utils.convert_hf_name(dataset_name)


def get_record_set_ids(metadata: mlc.Metadata) -> typing.Sequence[str]:
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

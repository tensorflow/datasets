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

"""Xtreme dataset collection."""
import collections

from typing import Mapping

from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import naming


class Xtreme(dataset_collection_builder.DatasetCollection):
  """Xtreme collection."""

  @property
  def info(self) -> dataset_collection_builder.DatasetCollectionInfo:
    return dataset_collection_builder.DatasetCollectionInfo.from_cls(
        dataset_collection_class=self.__class__,
        release_notes={
            "1.0.0": "Initial release",
        },
        homepage="https://sites.research.google/xtreme",
    )

  @property
  def datasets(
      self,
  ) -> Mapping[str, Mapping[str, naming.DatasetReference]]:
    return collections.OrderedDict(
        {
            "1.0.0": naming.references_for({
                "xnli": "xtreme_xnli:1.1.0",
                "pawsx": "xtreme_pawsx:1.0.0",
                "pos": "xtreme_pos:1.0.0",
                "ner": "wikiann:1.0.0",
                "xquad": "xquad:3.0.0",
                "mlqa": "mlqa:1.0.0",
                "tydiqa": "tydi_qa:3.0.0",
                "bucc": "bucc:1.0.0",
                "tatoeba": "tatoeba:1.0.0",
            })
        }
    )

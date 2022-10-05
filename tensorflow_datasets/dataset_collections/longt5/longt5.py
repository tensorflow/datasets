# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Long T5 dataset collection."""
import collections

from typing import Mapping

from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import naming


class Longt5(dataset_collection_builder.DatasetCollection):
  """Long T5 dataset collection."""

  @property
  def info(self) -> dataset_collection_builder.DatasetCollectionInfo:
    return dataset_collection_builder.DatasetCollectionInfo.from_cls(
        dataset_collection_class=self.__class__,
        release_notes={
            "1.0.0": "Initial release",
        },
        homepage="https://github.com/google-research/longt5",
    )

  @property
  def datasets(self,) -> Mapping[str, Mapping[str, naming.DatasetReference]]:
    return collections.OrderedDict({
        "1.0.0":
            naming.references_for({
                "natural_questions": "natural_questions/longt5:0.1.0",
                "media_sum": "media_sum:1.0.0",
            })
    })

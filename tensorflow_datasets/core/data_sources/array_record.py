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

"""ArrayRecord DataSource base class.

Warning: this is an experimental module. The interface might change in the
future without backwards compatibility.
"""

import dataclasses
from typing import Any, Optional

from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.data_sources import base
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_data_source


@dataclasses.dataclass(repr=False)
class ArrayRecordDataSource(base.BaseDataSource):
  """ArrayRecord DataSource class.

  Warning: this is an experimental class. The interface might change in the
  future without backwards compatibility.

  It acts as a wrapper around `array_record.ArrayRecordDataSource` that can read
  from ArrayRecords. It exposes `__len__` and `__getitem__` to serve as a data
  source.
  """

  dataset_info: dataset_info_lib.DatasetInfo
  split: splits_lib.Split = None
  decoders: Optional[type_utils.TreeDict[decode.partial_decode.DecoderArg]] = (
      None
  )
  # In order to lazy load array_record, we don't load
  # `array_record_data_source.ArrayRecordDataSource` here.
  data_source: Any = dataclasses.field(init=False)
  length: int = dataclasses.field(init=False)

  def __post_init__(self):
    file_instructions = base.file_instructions(self.dataset_info, self.split)
    self.data_source = array_record_data_source.ArrayRecordDataSource(
        file_instructions
    )

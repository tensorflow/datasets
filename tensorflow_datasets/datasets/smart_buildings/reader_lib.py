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

"""Utilities to read smart control protos from endpoint.

Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import abc
import dataclasses
from typing import Final, Mapping, NewType, Sequence, TypeVar

from absl import logging
import pandas as pd
from tensorflow_datasets.proto import smart_control_building_generated_pb2 as smart_control_building_pb2
from tensorflow_datasets.proto import smart_control_normalization_generated_pb2 as smart_control_normalization_pb2
from tensorflow_datasets.proto import smart_control_reward_generated_pb2 as smart_control_reward_pb2

VariableId = NewType('VariableId', str)

T = TypeVar('T')


class BaseReader(metaclass=abc.ABCMeta):
  """Abstract base class for writing the building and reward protos."""

  @abc.abstractmethod
  def read_observation_responses(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_building_pb2.ObservationResponse]:
    """Reads observation_responses from endpoint bounded by start & end time."""

  @abc.abstractmethod
  def read_action_responses(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_building_pb2.ActionResponse]:
    """Reads action_responses from endpoint bounded by start and end time."""

  @abc.abstractmethod
  def read_reward_infos(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_reward_pb2.RewardInfo]:
    """Reads reward infos from endpoint bounded by start and end time."""

  @abc.abstractmethod
  def read_reward_responses(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_reward_pb2.RewardInfo]:
    """Reads reward responses from endpoint bounded by start and end time."""

  @abc.abstractmethod
  def read_normalization_info(
      self,
  ) -> Mapping[
      VariableId, smart_control_normalization_pb2.ContinuousVariableInfo
  ]:
    """Reads variable normalization info from RecordIO."""

  @abc.abstractmethod
  def read_zone_infos(self) -> Sequence[smart_control_building_pb2.ZoneInfo]:
    """Reads the zone infos for the Building."""

  @abc.abstractmethod
  def read_device_infos(
      self,
  ) -> Sequence[smart_control_building_pb2.DeviceInfo]:
    """Reads the device infos for the Building."""


@dataclasses.dataclass(frozen=True)
class Readers:

  def __init__(self, readers: Sequence[BaseReader]):
    self._readers: Final[Sequence[BaseReader]] = readers
    logging.info('There are %d readers available.', len(readers))

  @property
  def readers(self) -> Sequence[BaseReader]:
    return self._readers

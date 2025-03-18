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

"""Utilities to read smart control protos from endpoint."""

import glob
import operator
import os
import re
from typing import Callable, Mapping, Sequence, TypeVar, Union

from absl import logging
from etils import epath
import pandas as pd
from tensorflow_datasets.datasets.smart_buildings import constants
from tensorflow_datasets.datasets.smart_buildings import reader_lib
from tensorflow_datasets.proto import smart_control_building_generated_pb2 as smart_control_building_pb2
from tensorflow_datasets.proto import smart_control_normalization_generated_pb2 as smart_control_normalization_pb2
from tensorflow_datasets.proto import smart_control_reward_generated_pb2 as smart_control_reward_pb2

T = TypeVar('T')


class ProtoReader(reader_lib.BaseReader):
  """Implementation for reading building and reward protos from .txtpb Files.

  Reads Smart Control protos as hourly shards to serialized protos. Each type of
  message uses a different file prefix (e.g., action_response) to
  identify the type of proto. Each shard is identified with a serial
  based on the timestamp. For example, a file of ActionResponses written
  on the 4th hour (UTC) of 5/25, would be action_response_2021.05.25.04.

  Attributes:
    input_dir: directory path where the files are located
  """

  def __init__(self, input_dir: epath.PathLike):
    self._input_dir = epath.Path(input_dir)
    logging.info('Reader lib input directory %s', self._input_dir)

  def read_observation_responses(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_building_pb2.ObservationResponse]:
    """Reads the observation response obtained from the environment."""
    return self._read_messages(
        start_time,
        end_time,
        constants.OBSERVATION_RESPONSE_FILE_PREFIX,
        smart_control_building_pb2.ObservationResponse.FromString,
    )

  def read_action_responses(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_building_pb2.ActionResponse]:
    """Reads the action response obtained from the environment."""

    return self._read_messages(
        start_time,
        end_time,
        constants.ACTION_RESPONSE_FILE_PREFIX,
        smart_control_building_pb2.ActionResponse.FromString,
    )

  def read_reward_infos(
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_reward_pb2.RewardInfo]:
    """Reads the reward info obtained from the environment."""
    return self._read_messages(
        start_time,
        end_time,
        constants.REWARD_INFO_PREFIX,
        smart_control_reward_pb2.RewardInfo.FromString,
    )

  def read_reward_responses(  # pytype: disable=signature-mismatch  # overriding-return-type-checks
      self, start_time: pd.Timestamp, end_time: pd.Timestamp
  ) -> Sequence[smart_control_reward_pb2.RewardResponse]:
    """Reads the reward responses obtained from the environment."""

    return self._read_messages(
        start_time,
        end_time,
        constants.REWARD_RESPONSE_PREFIX,
        smart_control_reward_pb2.RewardResponse.FromString,
    )

  def read_zone_infos(self) -> Sequence[smart_control_building_pb2.ZoneInfo]:
    """Reads the zone infos for the Building from .pbtxt."""
    filename = self._input_dir / constants.ZONE_INFO_PREFIX
    return self._read_streamed_protos(
        filename, smart_control_building_pb2.ZoneInfo.FromString
    )

  def read_device_infos(
      self,
  ) -> Sequence[smart_control_building_pb2.DeviceInfo]:
    """Reads the device infos for the Building."""

    filename = self._input_dir / constants.DEVICE_INFO_PREFIX
    return self._read_streamed_protos(
        filename, smart_control_building_pb2.DeviceInfo.FromString
    )

  def _read_messages(
      self,
      start_time: pd.Timestamp,
      end_time: pd.Timestamp,
      file_prefix: str,
      from_string_func: Callable[[Union[bytearray, bytes, memoryview]], T],
  ) -> Sequence[T]:
    """Reads all proto messages from sharded RIO files.

    Args:
      start_time: start time of the window
      end_time: end time of the window
      file_prefix: file prefix of the shards
      from_string_func: function to deserialize the proto from string

    Returns:
      List of protos.
    """

    messages = []

    shards = self._read_shards(self._input_dir, file_prefix)
    shards = self._select_shards(start_time, end_time, shards)

    for shard in shards:
      file_messages = self._read_streamed_protos(shard, from_string_func)
      messages.extend(file_messages)
    return messages

  def _read_shards(
      self, input_dir: epath.Path, file_prefix: str
  ) -> Sequence[epath.Path]:
    """Returns full paths in input_dir of files starting with file_prefix."""
    return list(input_dir.glob(f'{file_prefix}*'))

  def _select_shards(
      self,
      start_time: pd.Timestamp,
      end_time: pd.Timestamp,
      shards: Sequence[epath.Path],
  ) -> Sequence[epath.Path]:
    """Returns the shards that fall inside the start and end times."""

    def _read_timestamp(filepath: epath.Path) -> pd.Timestamp:
      """Reads the timestamp from the filepath."""
      assert filepath
      ts = pd.Timestamp(
          re.findall(r'\d{4}\.\d{2}\.\d{2}\.\d{2}', os.fspath(filepath))[-1]
      )
      return ts

    def _between(
        timestamp: pd.Timestamp,
        start_time: pd.Timestamp,
        end_time: pd.Timestamp,
    ) -> bool:
      """Turns true if timestamp is equal or between start and end times."""
      return (timestamp >= start_time) and (timestamp <= end_time)

    return [
        f for f in shards if _between(_read_timestamp(f), start_time, end_time)
    ]

  def _read_streamed_protos(
      self,
      full_path: epath.Path,
      from_string_func: Callable[[Union[bytearray, bytes, memoryview]], T],
  ) -> Sequence[T]:
    """Reads a proto which has byte size preceding the message."""

    messages = []
    with full_path.open('rb') as f:
      while True:
        # Read size as a varint
        size_bytes = f.read(4)
        if not size_bytes:
          break
        size = int.from_bytes(size_bytes, byteorder='little')

        # Read serialized data of the protobuf
        serialized_data = f.read(size)

        # Deserialize and create protobuf message
        messages.append(from_string_func(serialized_data))
    return messages

  def read_normalization_info(
      self,
  ) -> Mapping[
      reader_lib.VariableId,
      smart_control_normalization_pb2.ContinuousVariableInfo,
  ]:
    """Reads variable normalization info from .pbtxt."""
    filepath = os.path.join(self._input_dir, constants.NORMALIZATION_FILENAME)
    normalization_info = {}
    with open(filepath, 'rb') as f:
      while True:
        # Read size as a varint
        size_bytes = f.read(4)
        if not size_bytes:
          break
        size = int.from_bytes(size_bytes, byteorder='little')

        # Read serialized data of the protobuf
        serialized_data = f.read(size)
        variable = (
            smart_control_normalization_pb2.ContinuousVariableInfo().FromString(
                serialized_data
            )
        )
        if reader_lib.VariableId(variable.id) in normalization_info:
          raise ValueError(
              'Duplicate entry for variable %s found.' % variable.id
          )
        normalization_info[reader_lib.VariableId(variable.id)] = variable
    return normalization_info


def get_episode_data(working_dir: str) -> pd.DataFrame:
  """Returns a dataframe with details about each episode.

  In retrieving the summaries of the of the experiment there are various
  time-stamped files/directories:
    (1) The episode directory format is [episode_label]_[yymmdd_hhmmss UTC].
    (2) The updates (RewardInfo, RewardResponse, ActionResponse, and
    ObservationResponse) are time-stamped .pbtxt files in the following
    [update_label]_[yyyy.mm.dd.hh local].

  Episode labels include bc_collect, bc_eval, sac_collect, sac_eval, with
  the name of the algorithm followed by the type or episode.

  Update labeled include reward_info, reward_response, action_response,
  and observation_response.

  Since the labels are variable length, we extract the time stamps from the
  end of the string (i.e., indexes -13, -14).

  Also note that simulation time is local only; since it follows the
  building's local time activities and weather conditions.

  Args:
    working_dir: A directory containing the episode runs.

  Returns:
    A dataframe with episode label, timestamps, number of updates.
  """
  episode_dirs = list(epath.Path(working_dir).iterdir())
  date_extractor = operator.itemgetter(slice(-13, None))

  execution_times = pd.to_datetime(
      list(map(date_extractor, episode_dirs)), format='%y%m%d_%H%M%S', utc=True
  )
  episode_start_times = []
  episode_end_times = []
  number_updates = []
  durations = []
  labels = []
  episode_execution_times = []
  episode_datas = []

  for episode_dir, execution_time in zip(episode_dirs, execution_times):
    glob_pattern = os.path.join(
        working_dir, episode_dir, 'observation_response*'
    )
    obs_files = glob.glob(glob_pattern)
    # Simulation/Real update times are always in local time, since it is
    # affected by the local conditions and local time of day of the building.
    obs_times = pd.to_datetime(
        [obs_file[-13:] for obs_file in obs_files],
        format='%Y.%m.%d.%H',
        utc=False,
    )
    if obs_times.size:
      start_time = obs_times.min()
      end_time = obs_times.max()
      episode_start_times.append(start_time)
      episode_end_times.append(end_time)
      durations.append((end_time - start_time).total_seconds())
      number_updates.append(len(obs_files))
      episode_datas.append(episode_dir)
      episode_execution_times.append(execution_time)
      labels.append(episode_dir[:-14])
  episodes_df = pd.DataFrame(
      {
          'execution_time': episode_execution_times,
          'episode_start_time': episode_start_times,
          'episode_end_time': episode_end_times,
          'duration': durations,
          'number_updates': number_updates,
          'label': labels,
      },
      index=episode_datas,
  )
  return episodes_df.sort_values(by='execution_time')

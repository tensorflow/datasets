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

"""smart_buildings dataset."""

from collections.abc import Iterable
import datetime
from typing import Any

from absl import logging
from etils import epath
from google.protobuf import json_format
import numpy as np
import pandas as pd
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.datasets.smart_buildings import controller_reader
import tensorflow_datasets.public_api as tfds

# The years in the dataset.
YEARS = [19, 20, 21, 22, 23, 24]

_MAX_EXAMPLES_PER_DAY = 24 * 12  # 288 per day

_REWARD_RESPONSES = [
    'agentRewardValue',
    'productivityReward',
    'electricityEnergyCost',
    'carbonEmitted',
    'productivityWeight',
    'energyCostWeight',
    'carbonEmissionWeight',
    'personProductivity',
    'totalOccupancy',
    'rewardScale',
    'productivityRegret',
    'normalizedProductivityRegret',
    'normalizedEnergyCost',
    'normalizedCarbonEmission',
    'naturalGasEnergyCost',
]


def to_ns_timestamp(proto_timestamp) -> int:
  """Converts a protobuf.Timestamp to number of nanoseconds since epoch."""
  return proto_timestamp.seconds * 1e9 + proto_timestamp.nanos


class BuilderConfig(tfds.core.BuilderConfig):
  building: str


def _make_building_config(building: str) -> BuilderConfig:
  config = BuilderConfig(
      name=building,
      version=tfds.core.utils.version.Version('1.0.0'),
      description=f'Building {building}',
  )
  config.building = building
  return config


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for smart_buildings dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      _make_building_config(building='sb1'),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'observation': tfds.features.FeaturesDict({
                'timestamp': tfds.features.Text(),
                'request': tfds.features.FeaturesDict({
                    'timestamp': tfds.features.Text(),
                    'singleObservationRequests': tfds.features.Sequence(
                        tfds.features.FeaturesDict({
                            'deviceId': tfds.features.Text(),
                            'measurementName': tfds.features.Text(),
                        })
                    ),
                }),
                'singleObservationResponses': tfds.features.Sequence(
                    tfds.features.FeaturesDict({
                        'singleObservationRequest': tfds.features.FeaturesDict({
                            'deviceId': tfds.features.Text(),
                            'measurementName': tfds.features.Text(),
                        }),
                        'timestamp': tfds.features.Text(),
                        'continuousValue': tfds.features.Scalar(
                            dtype=np.float32
                        ),
                        'observationValid': tfds.features.Text(),
                    })
                ),
            }),
            'action': tfds.features.FeaturesDict({
                'timestamp': tfds.features.Text(),
                'request': tfds.features.FeaturesDict({
                    'timestamp': tfds.features.Text(),
                    'singleActionRequests': tfds.features.Sequence(
                        tfds.features.FeaturesDict({
                            'deviceId': tfds.features.Text(),
                            'setpointName': tfds.features.Text(),
                            'continuousValue': tfds.features.Scalar(
                                dtype=np.float32
                            ),
                        })
                    ),
                }),
                'singleActionResponses': tfds.features.Sequence(
                    tfds.features.FeaturesDict({
                        'request': tfds.features.FeaturesDict({
                            'deviceId': tfds.features.Text(),
                            'setpointName': tfds.features.Text(),
                            'continuousValue': tfds.features.Scalar(
                                dtype=np.float32
                            ),
                        }),
                        'responseType': tfds.features.Text(),
                        'additionalInfo': tfds.features.Text(),
                    }),
                ),
            }),
            'reward': tfds.features.FeaturesDict({
                'productivityWeight': tfds.features.Scalar(dtype=np.float32),
                'energyCostWeight': tfds.features.Scalar(dtype=np.float32),
                'carbonEmissionWeight': tfds.features.Scalar(dtype=np.float32),
                'rewardScale': tfds.features.Scalar(dtype=np.float32),
                'startTimestamp': tfds.features.Text(),
                'endTimestamp': tfds.features.Text(),
                'agentRewardValue': tfds.features.Scalar(dtype=np.float32),
                'carbonEmitted': tfds.features.Scalar(dtype=np.float32),
                'electricityEnergyCost': tfds.features.Scalar(dtype=np.float32),
                'normalizedCarbonEmission': tfds.features.Scalar(
                    dtype=np.float32
                ),
                'normalizedEnergyCost': tfds.features.Scalar(dtype=np.float32),
                'normalizedProductivityRegret': tfds.features.Scalar(
                    dtype=np.float32
                ),
                'personProductivity': tfds.features.Scalar(dtype=np.float32),
                'productivityRegret': tfds.features.Scalar(dtype=np.float32),
                'productivityReward': tfds.features.Scalar(dtype=np.float32),
                'totalOccupancy': tfds.features.Scalar(dtype=np.float32),
                'naturalGasEnergyCost': tfds.features.Scalar(dtype=np.float32),
            }),
        }),
        homepage='https://github.com/google/sbsim',
        disable_shuffling=True,  # our dataset needs to be in order
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager, pipeline
  ):
    """Download the data and define splits."""
    building = self.builder_config.building
    building_upper = building.upper()

    path_by_year: dict[int, epath.Path] = dl_manager.download_and_extract({
        year: f'https://storage.googleapis.com/gresearch/smart_buildings_dataset/{building_upper}/{building_upper}_{year}.zip'
        for year in YEARS
    })

    splits_dict = {}
    for year, path in path_by_year.items():
      splits_dict[f'{building}_{year}'] = self._generate_examples(
          path=path / 'dataset' / building_upper / str(year),
          year=year,
          pipeline=pipeline,
      )
    return splits_dict

  def _generate_examples(self, path: epath.Path, year: int, pipeline):
    """Yields examples."""
    logging.info('Processing year %d in path %s', year, path)

    start_date = datetime.date(2000 + year, 1, 1)
    end_date = datetime.date(2000 + year + 1, 1, 1)
    all_dates = pd.date_range(start_date, end_date)

    return (
        pipeline
        | f'CreateDates_{year}' >> beam.Create(enumerate(all_dates))
        | f'ProcessDate_{year}' >> beam.FlatMap(process_date, path=path)
        | f'Reshuffle_{year}' >> beam.Reshuffle()
    )


def process_date(
    day_index_and_start_time: tuple[int, pd.Timestamp],
    path: epath.Path,
) -> Iterable[tuple[int, dict[str, Any]]]:
  """Process a single date."""
  day_index, start_time = day_index_and_start_time
  end_time = start_time + pd.Timedelta(hours=23)
  key_offset = day_index * _MAX_EXAMPLES_PER_DAY

  reader = controller_reader.ProtoReader(path)
  observation_responses = reader.read_observation_responses(
      start_time, end_time
  )
  action_responses = reader.read_action_responses(start_time, end_time)
  reward_responses = reader.read_reward_responses(start_time, end_time)

  # make sure all are sorted by data
  observation_responses = sorted(
      observation_responses,
      key=lambda o: to_ns_timestamp(o.timestamp),
  )
  action_responses = sorted(
      action_responses,
      key=lambda o: to_ns_timestamp(o.timestamp),
  )
  reward_responses = sorted(
      reward_responses,
      key=lambda o: to_ns_timestamp(o.start_timestamp),
  )

  if len(observation_responses) > _MAX_EXAMPLES_PER_DAY:
    raise ValueError(
        f'Too many observation responses for date {start_time}: '
        f'{len(observation_responses)} > {_MAX_EXAMPLES_PER_DAY}'
    )

  for i in range(len(observation_responses)):
    observation_response = json_format.MessageToDict(observation_responses[i])
    action_response = json_format.MessageToDict(action_responses[i])
    reward_response = json_format.MessageToDict(reward_responses[i])

    # fill missing values
    for single_observation_response in observation_response[
        'singleObservationResponses'
    ]:
      if 'continuousValue' not in single_observation_response:
        single_observation_response['continuousValue'] = 0.0
      if 'observationValid' not in single_observation_response:
        single_observation_response['observationValid'] = 'False'
      else:
        single_observation_response['observationValid'] = str(
            single_observation_response['observationValid']
        )  # parse bool to string
      if 'timestamp' not in single_observation_response:
        single_observation_response['timestamp'] = observation_response[
            'timestamp'
        ]
    for val in _REWARD_RESPONSES:
      if val not in reward_response:
        reward_response[val] = -1  # sentinal value

    beam.metrics.Metrics.counter(f'date_{start_time}', 'example_count').inc()
    key = key_offset + i
    yield key, {
        'observation': observation_response,
        'action': action_response,
        'reward': reward_response,
    }

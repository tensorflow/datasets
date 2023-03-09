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

"""Types and configurations for the Robomimic datasets."""

import dataclasses
import enum

import tensorflow_datasets.public_api as tfds


class Task(enum.Enum):
  LIFT = 'lift'
  CAN = 'can'
  SQUARE = 'square'
  TRANSPORT = 'transport'
  TOOL_HANG = 'tool_hang'

  def __str__(self) -> str:
    return self.value


class Dataset(enum.Enum):
  PH = 'ph'  # proficient human, i.e. expert demonstrations
  MH = 'mh'  # mixed-human, i.e. more suboptimal than proficient human
  MG = 'mg'  # machine generated, i.e. soft actor critic with dense reward

  def __str__(self) -> str:
    return self.value


class DataType(enum.Enum):
  IMAGE = 'image'  # image-based observations (i.e. exteroception)
  LOW_DIM = 'low_dim'  # internal state-based observations (i.e. proprioception)
  DEMO = 'demo'  # test data

  def __str__(self) -> str:
    return self.value


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  """Configuration of the dataset versions."""

  task: Task = Task.LIFT
  dataset: Dataset = Dataset.PH
  filename: DataType = DataType.DEMO
  horizon: int = 100


TASKS = {
    Task.LIFT: {
        'datasets': [Dataset.PH, Dataset.MH, Dataset.MG],
        'object': 10,
        'states': 32,
        'horizon': 400,
        'action_size': 7,
    },
    Task.CAN: {
        'datasets': [Dataset.PH, Dataset.MH, Dataset.MG],
        'object': 14,
        'states': 71,
        'horizon': 400,
        'action_size': 7,
    },
    Task.SQUARE: {
        'datasets': [Dataset.PH, Dataset.MH],
        'object': 14,
        'states': 45,
        'horizon': 400,
        'action_size': 7,
    },
    Task.TRANSPORT: {
        'datasets': [Dataset.PH, Dataset.MH],
        'object': 41,
        'states': 115,
        'horizon': 700,
        'action_size': 14,
    },
    Task.TOOL_HANG: {
        'datasets': [
            Dataset.PH,
        ],
        'object': 44,
        'states': 58,
        'horizon': 700,
        'action_size': 7,
    },
}


def make_builder_configs(dataset: Dataset):
  """Creates the PH build configs."""
  configs = []
  for task, details in TASKS.items():
    types = [DataType.IMAGE, DataType.LOW_DIM]
    if dataset in details['datasets']:
      for obs_type in types:
        # pytype: disable=wrong-keyword-args
        configs.append(
            # name is inherited from base dataclass unbeknownst to the linter
            BuilderConfig(  # pylint: disable=unexpected-keyword-arg
                name=f'{task}_{dataset}_{obs_type}',
                task=task,
                dataset=dataset,
                filename=obs_type,
                horizon=details['horizon'],
            )
        )
        # pytype: enable=wrong-keyword-args
  return configs

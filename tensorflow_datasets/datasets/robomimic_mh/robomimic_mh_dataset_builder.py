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

"""robomimic_mh dataset."""

from __future__ import annotations

from typing import Any, Dict

import numpy as np
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robomimic import dataset_utils as utils


class Builder(utils.RobomimicBuilder):
  """DatasetBuilder for robomimic_mh dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = utils.make_builder_configs(utils.DataSource.MH)
  DATASET_NAME = 'robomimic_mh'

  def _get_metadata(self) -> Dict[Any, Any]:
    if self.builder_config.task == utils.Task.TRANSPORT:
      episode_metadata = {
          '20_percent': np.bool_,
          '20_percent_train': np.bool_,
          '20_percent_valid': np.bool_,
          '50_percent': np.bool_,
          '50_percent_train': np.bool_,
          '50_percent_valid': np.bool_,
          'better': np.bool_,
          'better_train': np.bool_,
          'better_valid': np.bool_,
          'okay': np.bool_,
          'okay_better': np.bool_,
          'okay_better_train': np.bool_,
          'okay_better_valid': np.bool_,
          'okay_train': np.bool_,
          'okay_valid': np.bool_,
          'train': np.bool_,
          'valid': np.bool_,
          'worse': np.bool_,
          'worse_better': np.bool_,
          'worse_better_train': np.bool_,
          'worse_better_valid': np.bool_,
          'worse_okay': np.bool_,
          'worse_okay_train': np.bool_,
          'worse_okay_valid': np.bool_,
          'worse_train': np.bool_,
          'worse_valid': np.bool_,
      }
    else:
      episode_metadata = {
          '20_percent': np.bool_,
          '20_percent_train': np.bool_,
          '20_percent_valid': np.bool_,
          '50_percent': np.bool_,
          '50_percent_train': np.bool_,
          '50_percent_valid': np.bool_,
          'better': np.bool_,
          'better_operator_1': np.bool_,
          'better_operator_1_train': np.bool_,
          'better_operator_1_valid': np.bool_,
          'better_operator_2': np.bool_,
          'better_operator_2_train': np.bool_,
          'better_operator_2_valid': np.bool_,
          'better_train': np.bool_,
          'better_valid': np.bool_,
          'okay': np.bool_,
          'okay_better': np.bool_,
          'okay_better_train': np.bool_,
          'okay_better_valid': np.bool_,
          'okay_operator_1': np.bool_,
          'okay_operator_1_train': np.bool_,
          'okay_operator_1_valid': np.bool_,
          'okay_operator_2': np.bool_,
          'okay_operator_2_train': np.bool_,
          'okay_operator_2_valid': np.bool_,
          'okay_train': np.bool_,
          'okay_valid': np.bool_,
          'train': np.bool_,
          'valid': np.bool_,
          'worse': np.bool_,
          'worse_better': np.bool_,
          'worse_better_train': np.bool_,
          'worse_better_valid': np.bool_,
          'worse_okay': np.bool_,
          'worse_okay_train': np.bool_,
          'worse_okay_valid': np.bool_,
          'worse_operator_1': np.bool_,
          'worse_operator_1_train': np.bool_,
          'worse_operator_1_valid': np.bool_,
          'worse_operator_2': np.bool_,
          'worse_operator_2_train': np.bool_,
          'worse_operator_2_valid': np.bool_,
          'worse_train': np.bool_,
          'worse_valid': np.bool_,
      }
    return episode_metadata

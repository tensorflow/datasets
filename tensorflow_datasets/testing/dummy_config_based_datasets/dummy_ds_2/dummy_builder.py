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

"""Dummy config-based dataset self-contained in a directory.

The builder module intentionally does not follow the naming conventions.
This is used in registered_test.py to check the logic to infer dataset
name.
"""

from __future__ import annotations

import numpy as np
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """Dummy dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({'x': np.int64}),
    )

  def _split_generators(self, dl_manager):
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
        ),
    ]

  def _generate_examples(self):
    for i in range(10):
      yield i, {'x': i}

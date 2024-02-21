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

"""Dummy dataset self-contained in a directory."""

from __future__ import annotations

import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds


class DummyDataset(tfds.core.GeneratorBasedBuilder):
  """Dummy dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({'x': np.int64}),
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download('http://dummy.org/data.txt')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'path': os.path.join(path, 'train.txt')},
        ),
    ]

  def _generate_examples(self, path):
    with epath.Path(path).open() as f:
      value = f.read()
    for i in range(int(value)):
      yield i, {'x': i}

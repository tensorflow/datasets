# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
"""smartwatch_gestures_dataset dataset."""

import tensorflow_datasets as tfds
from . import smartwatch_gestures


class SmartwatchGesturesTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for smartwatch_gestures_dataset dataset."""
  # TODO(smartwatch_gestures_dataset):
  DATASET_CLASS = smartwatch_gestures.SmartwatchGesturesDataset
  SPLITS = {
      'train': 3,  # Number of fake train example
  }


if __name__ == '__main__':
  tfds.testing.test_main()

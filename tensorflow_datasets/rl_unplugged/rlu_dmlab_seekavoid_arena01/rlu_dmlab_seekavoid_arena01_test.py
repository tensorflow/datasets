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

"""rlu_dmlab_seekavoid_arena01 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged.rlu_dmlab_seekavoid_arena01 import rlu_dmlab_seekavoid_arena01


class RluDmlabSeekavoidArena01Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for rlu_dmlab_seekavoid_arena01 dataset."""
  # TODO(rlu_dmlab_seekavoid_arena01):
  DATASET_CLASS = rlu_dmlab_seekavoid_arena01.RluDmlabSeekavoidArena01
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {
      'file_paths': [
          'dmlab_seekavoid_arena01_training_0_tfrecord-00000-of-00500'
      ]
  }
  DL_DOWNLOAD_RESULT = {
      'file_paths': [
          'dmlab_seekavoid_arena01_training_0_tfrecord-00000-of-00500'
      ]
  }

  # The different configs are only different in the name of the files.
  BUILDER_CONFIG_NAMES_TO_TEST = ['training_0']

if __name__ == '__main__':
  tfds.testing.test_main()

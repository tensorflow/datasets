# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.video import ucf101


class Ucf101Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = ucf101.Ucf101

  SPLITS = {
      'train': 3,
      'test': 2,
  }

  DL_EXTRACT_RESULT = {
      'videos': 'videos',
      'splits': 'splits',
  }

  BUILDER_CONFIG_NAMES_TO_TEST = ['ucf101_1_256', 'ucf101_2']

  def _assertAsDataset(self, builder):
    """Check the label distribution for each split."""
    super(Ucf101Test, self)._assertAsDataset(builder)
    label_frequncies = {}
    label_feature = builder.info.features['label']
    dataset = builder.as_dataset()
    for split_name in Ucf101Test.SPLITS:
      label_frequncies[split_name] = collections.defaultdict(int)
      for features in dataset_utils.as_numpy(dataset[split_name]):
        label_name = label_feature.int2str(features['label'])
        label_frequncies[split_name][label_name] += 1
    self.assertEqual(dict(label_frequncies),
                     {'test': {'Archery': 1, 'Nunchucks': 1},
                      'train': {'Archery': 1, 'Nunchucks': 2}})


if __name__ == '__main__':
  testing.test_main()

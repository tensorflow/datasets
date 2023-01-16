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

import collections

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.datasets.imagenet_a import imagenet_a_dataset_builder
import tensorflow_datasets.public_api as tfds


class ImagenetATest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagenet_a_dataset_builder.Builder
  SPLITS = {
      'test': 10,  # Number of fake test examples.
  }

  DL_EXTRACT_RESULT = 'imagenet-a.tar'

  def _assertAsDataset(self, builder):
    """Check the label distribution.

    This checks that lable get correctly converted between the synset ids
    and integers.

    Args:
      builder: The ImagenetA dataset builder.
    """
    super()._assertAsDataset(builder)
    label_frequncies = collections.Counter()
    label_feature = builder.info.features['label']
    dataset = builder.as_dataset()
    for features in dataset_utils.as_numpy(dataset['test']):
      label_frequncies.update([label_feature.int2str(features['label'])])
    self.assertEqual(
        dict(label_frequncies), {'n01580077': 2, 'n01616318': 3, 'n07697313': 5}
    )


if __name__ == '__main__':
  tfds.testing.test_main()

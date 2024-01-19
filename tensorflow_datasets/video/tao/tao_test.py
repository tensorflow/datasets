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

"""tao dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.video.tao import tao


class TaoTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for tao dataset."""

  DATASET_CLASS = tao.Tao
  SPLITS = {
      tfds.Split.TRAIN: 1,
      tfds.Split.VALIDATION: 1,
  }
  DL_EXTRACT_RESULT = {
      'train': '',
      'val': '',
      'annotations': '',
  }

  BUILDER_CONFIG_NAMES_TO_TEST = ['test_config']

  @classmethod
  def setUpClass(cls):
    tao.Tao.BUILDER_CONFIGS = [
        tao.TaoConfig(
            name='test_config',
            description='All images are bilinearly resized to 28 X 42',
            height=28,
            width=42,
        ),
    ]
    super().setUpClass()

  def _download_and_prepare_as_dataset(self, builder):
    super()._download_and_prepare_as_dataset(builder)

    if not tf.executing_eagerly():  # Only test the following in eager mode.
      return

    with self.subTest('check_annotations'):
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      for ex in [train_ex, val_ex]:
        # There should be the same number of each of these; a number
        # per group of bboxes indicating which frame they correspond to.
        self.assertEqual(
            ex['tracks']['bboxes'].shape[0], ex['tracks']['frames'].shape[0]
        )

    with self.subTest('check_video'):
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      # NOTE: For real images, this will be a list of potentially a thousand or
      # more frames. For testing purposes we load a single dummy 10 X 10 image.
      self.assertEqual(train_ex['video'].shape, (1, 28, 42, 3))
      self.assertEqual(val_ex['video'].shape, (1, 28, 42, 3))


if __name__ == '__main__':
  tfds.testing.test_main()

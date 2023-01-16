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

"""Davis dataset test."""

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.video.davis import davis


class DavisTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for davis dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['480p', 'full_resolution']
  DATASET_CLASS = davis.Davis
  SPLITS = {
      tfds.Split.TRAIN: 1,  # Number of fake train examples.
      tfds.Split.VALIDATION: 1,
  }

  def _download_and_prepare_as_dataset(self, builder):
    super()._download_and_prepare_as_dataset(builder)

    if not tf.executing_eagerly():  # Only test the following in eager mode.
      return

    with self.subTest('annotations_classes'):
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      # Check that the dataset examples contain the correct number of classes.
      self.assertSetEqual(
          set(np.unique(train_ex['video']['segmentations'].numpy())), {0, 1}
      )
      self.assertSetEqual(
          set(np.unique(val_ex['video']['segmentations'].numpy())), {0, 1, 2}
      )

    with self.subTest('dataset_shapes'):
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      train_num_frames = train_ex['metadata']['num_frames'].numpy()
      val_num_frames = val_ex['metadata']['num_frames'].numpy()
      # Check that the shapes of the dataset examples is correct.
      self.assertEqual(train_num_frames, 4)
      self.assertEqual(val_num_frames, 4)
      _, height, width, _ = train_ex['video']['frames'].numpy().shape
      self.assertEqual(
          train_ex['video']['frames'].numpy().shape, (4, height, width, 3)
      )
      self.assertEqual(
          train_ex['video']['segmentations'].numpy().shape,
          (4, height, width, 1),
      )
      _, height, width, _ = val_ex['video']['frames'].numpy().shape
      self.assertEqual(
          val_ex['video']['frames'].numpy().shape, (4, height, width, 3)
      )
      self.assertEqual(
          val_ex['video']['segmentations'].numpy().shape, (4, height, width, 1)
      )


if __name__ == '__main__':
  tfds.testing.test_main()

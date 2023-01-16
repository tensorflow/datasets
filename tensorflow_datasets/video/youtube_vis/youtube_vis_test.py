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

"""youtube_vis dataset."""

import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.video.youtube_vis import youtube_vis


class YoutubeVisTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for youtube_vis dataset."""

  DATASET_CLASS = youtube_vis.YoutubeVis
  SPLITS = {
      tfds.Split.TRAIN: 1,  # Number of fake train examples.
      tfds.Split.VALIDATION: 1,  # Number of fake test examples.
      tfds.Split.TEST: 1,  # Number of fake test examples.
  }
  SKIP_CHECKSUMS = True  # All data is manually downloaded.

  # When testing the "custom split" functionality the splits are overlapping.
  OVERLAPPING_SPLITS = [
      tfds.Split.TRAIN,
      tfds.Split.VALIDATION,
      tfds.Split.TEST,
  ]

  BUILDER_CONFIG_NAMES_TO_TEST = ['test_config', 'test_config_custom_split']

  @classmethod
  def setUpClass(cls):
    youtube_vis.YoutubeVis.BUILDER_CONFIGS = [
        youtube_vis.YoutubeVisConfig(
            name='test_config',
            description='All images are bilinearly resized to 28 X 42',
            height=28,
            width=42,
        ),
        youtube_vis.YoutubeVisConfig(
            name='test_config_custom_split',
            description='All splits are the train data resized to 28 X 42.',
            height=28,
            width=42,
            split_train_data_range=(0, 1),
            split_val_data_range=(0, 1),
            split_test_data_range=(0, 1),
        ),
    ]
    super().setUpClass()

  def _download_and_prepare_as_dataset(self, builder):
    super()._download_and_prepare_as_dataset(builder)

    if not tf.executing_eagerly():  # Only test the following in eager mode.
      return

    with self.subTest('check_annotations'):
      # Makes certain sanity checks like the number of segmentations
      # should be equal to the number of labeled frame indices, etc.
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      test_ex = list(splits[tfds.Split.TEST])[0]
      self.assertEqual(
          train_ex['tracks']['bboxes'].shape[0],
          train_ex['tracks']['segmentations'].shape[0],
      )
      self.assertEqual(
          train_ex['tracks']['segmentations'].shape[0],
          train_ex['tracks']['frames'].shape[0],
      )
      if builder.builder_config.name != 'test_config_custom_split':
        # No annotations are provided on the val and test data if not using
        # the custom split.
        self.assertEqual(val_ex['tracks']['bboxes'].shape[0], 0)
        self.assertEqual(test_ex['tracks']['bboxes'].shape[0], 0)

    with self.subTest('check_video'):
      # Checks that the video data matches the metadata.
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      val_ex = list(splits[tfds.Split.VALIDATION])[0]
      test_ex = list(splits[tfds.Split.TEST])[0]

      self.assertEqual(
          train_ex['metadata']['height'].numpy(), builder.builder_config.height
      )
      self.assertEqual(
          train_ex['metadata']['width'].numpy(), builder.builder_config.width
      )
      self.assertEqual(
          val_ex['metadata']['height'].numpy(), builder.builder_config.height
      )
      self.assertEqual(
          val_ex['metadata']['width'].numpy(), builder.builder_config.width
      )
      self.assertEqual(
          test_ex['metadata']['height'].numpy(), builder.builder_config.height
      )
      self.assertEqual(
          test_ex['metadata']['width'].numpy(), builder.builder_config.width
      )
      self.assertEqual(
          train_ex['video'].shape,
          (
              train_ex['metadata']['num_frames'].numpy(),
              train_ex['metadata']['height'].numpy(),
              train_ex['metadata']['width'].numpy(),
              3,
          ),
      )
      self.assertEqual(
          val_ex['video'].shape,
          (
              val_ex['metadata']['num_frames'].numpy(),
              val_ex['metadata']['height'].numpy(),
              val_ex['metadata']['width'].numpy(),
              3,
          ),
      )
      self.assertEqual(
          test_ex['video'].shape,
          (
              test_ex['metadata']['num_frames'].numpy(),
              test_ex['metadata']['height'].numpy(),
              test_ex['metadata']['width'].numpy(),
              3,
          ),
      )

    with self.subTest('check_segmentations'):
      # Checks that the segmentations match the metadata and have the correct
      # label count.
      splits = builder.as_dataset()
      train_ex = list(splits[tfds.Split.TRAIN])[0]
      for segmentation in train_ex['tracks']['segmentations']:
        unique_pixels = set(np.unique(segmentation.numpy()))
        self.assertSetEqual(unique_pixels, set([0, 1]))
        self.assertEqual(
            (
                train_ex['metadata']['height'].numpy(),
                train_ex['metadata']['width'].numpy(),
            ),
            segmentation.shape[1:3],
        )

    if builder.builder_config.name == 'test_config_custom_split':
      with self.subTest('check_custom_split'):
        # Checks that all splits contain exactly the same data, since
        # that is what was requested by this custom split.
        splits = builder.as_dataset()
        train_ex = list(splits[tfds.Split.TRAIN])[0]
        val_ex = list(splits[tfds.Split.VALIDATION])[0]
        val_ex = list(splits[tfds.Split.TEST])[0]
        self.assertDictEqual(train_ex['metadata'], val_ex['metadata'])
        self.assertDictEqual(test_ex['metadata'], val_ex['metadata'])


if __name__ == '__main__':
  tfds.testing.test_main()

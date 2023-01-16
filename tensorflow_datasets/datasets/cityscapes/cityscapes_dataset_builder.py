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

"""Cityscapes Datasets."""

import os
import re

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class CityscapesConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Cityscapes.

  Args:
    right_images (bool): Enables right images for stereo image tasks.
    segmentation_labels (bool): Enables image segmentation labels.
    disparity_maps (bool): Enables disparity maps.
    train_extra_split (bool): Enables train_extra split. This automatically
      enables coarse grain segmentations, if segmentation labels are used.
  """

  def __init__(
      self,
      *,
      right_images=False,
      segmentation_labels=True,
      disparity_maps=False,
      train_extra_split=False,
      **kwargs,
  ):
    super(CityscapesConfig, self).__init__(version='1.0.0', **kwargs)

    self.right_images = right_images
    self.segmentation_labels = segmentation_labels
    self.disparity_maps = disparity_maps
    self.train_extra_split = train_extra_split

    self.ignored_ids = set()

    # Setup required zips and their root dir names
    self.zip_root = {}
    self.zip_root['images_left'] = (
        'leftImg8bit_trainvaltest.zip',
        'leftImg8bit',
    )

    if self.train_extra_split:
      self.zip_root['images_left/extra'] = (
          'leftImg8bit_trainextra.zip',
          'leftImg8bit',
      )

    if self.right_images:
      self.zip_root['images_right'] = (
          'rightImg8bit_trainvaltest.zip',
          'rightImg8bit',
      )
      if self.train_extra_split:
        self.zip_root['images_right/extra'] = (
            'rightImg8bit_trainextra.zip',
            'rightImg8bit',
        )

    if self.segmentation_labels:
      if not self.train_extra_split:
        self.zip_root['segmentation_labels'] = (
            'gtFine_trainvaltest.zip',
            'gtFine',
        )
        self.label_suffix = 'gtFine_labelIds'
      else:
        # The 'train extra' split only has coarse labels unlike train and val.
        # Therefore, for consistency across splits, we also enable coarse labels
        # using the train_extra_split flag.
        self.zip_root['segmentation_labels'] = ('gtCoarse.zip', 'gtCoarse')
        self.zip_root['segmentation_labels/extra'] = (
            'gtCoarse.zip',
            'gtCoarse',
        )
        self.label_suffix = 'gtCoarse_labelIds'

    if self.disparity_maps:
      self.zip_root['disparity_maps'] = (
          'disparity_trainvaltest.zip',
          'disparity',
      )
      if self.train_extra_split:
        self.zip_root['disparity_maps/extra'] = (
            'disparity_trainextra.zip',
            'disparity',
        )
        # No disparity for this file
        self.ignored_ids.add('troisdorf_000000_000073')


class Builder(tfds.core.GeneratorBasedBuilder):
  """Base class for Cityscapes datasets."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  You have to download files from https://www.cityscapes-dataset.com/login/
  (This dataset requires registration).
  For basic config (semantic_segmentation) you must download
  'leftImg8bit_trainvaltest.zip' and 'gtFine_trainvaltest.zip'.
  Other configs do require additional files - please see code for more details.
  """

  BUILDER_CONFIGS = [
      CityscapesConfig(
          name='semantic_segmentation',
          description='Cityscapes semantic segmentation dataset.',
          right_images=False,
          segmentation_labels=True,
          disparity_maps=False,
          train_extra_split=False,
      ),
      CityscapesConfig(
          name='semantic_segmentation_extra',
          description=(  # pylint: disable=line-too-long
              'Cityscapes semantic segmentation dataset with train_extra split'
              ' and coarse labels.'
          ),
          right_images=False,
          segmentation_labels=True,
          disparity_maps=False,
          train_extra_split=True,
      ),
      CityscapesConfig(
          name='stereo_disparity',
          description='Cityscapes stereo image and disparity maps dataset.',
          right_images=True,
          segmentation_labels=False,
          disparity_maps=True,
          train_extra_split=False,
      ),
      CityscapesConfig(
          name='stereo_disparity_extra',
          description=(  # pylint: disable=line-too-long
              'Cityscapes stereo image and disparity maps dataset with'
              ' train_extra split.'
          ),
          right_images=True,
          segmentation_labels=False,
          disparity_maps=True,
          train_extra_split=True,
      ),
  ]

  def _info(self):
    # Enable features as necessary
    features = {}
    features['image_id'] = tfds.features.Text()
    features['image_left'] = tfds.features.Image(
        shape=(1024, 2048, 3), encoding_format='png'
    )

    if self.builder_config.right_images:
      features['image_right'] = tfds.features.Image(
          shape=(1024, 2048, 3), encoding_format='png'
      )

    if self.builder_config.segmentation_labels:
      features['segmentation_label'] = tfds.features.Image(
          shape=(1024, 2048, 1), encoding_format='png', use_colormap=True
      )

    if self.builder_config.disparity_maps:
      features['disparity_map'] = tfds.features.Image(
          shape=(1024, 2048, 1), encoding_format='png'
      )

    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(features),
        homepage='https://www.cityscapes-dataset.com',
    )

  def _split_generators(self, dl_manager):
    paths = {}
    for split, (zip_file, _) in self.builder_config.zip_root.items():
      paths[split] = os.path.join(dl_manager.manual_dir, zip_file)

    if any(not tf.io.gfile.exists(z) for z in paths.values()):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join(paths.values())
      raise AssertionError(msg)

    for split, (_, zip_root) in self.builder_config.zip_root.items():
      paths[split] = os.path.join(dl_manager.extract(paths[split]), zip_root)

    splits = [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                feat_dir: os.path.join(path, 'train')
                for feat_dir, path in paths.items()
                if not feat_dir.endswith('/extra')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                feat_dir: os.path.join(path, 'val')
                for feat_dir, path in paths.items()
                if not feat_dir.endswith('/extra')
            },
        ),
    ]

    # Test split does not exist in coarse dataset
    if not self.builder_config.train_extra_split:
      splits.append(
          tfds.core.SplitGenerator(
              name=tfds.Split.TEST,
              gen_kwargs={
                  feat_dir: os.path.join(path, 'test')
                  for feat_dir, path in paths.items()
                  if not feat_dir.endswith('/extra')
              },
          )
      )
    else:
      splits.append(
          tfds.core.SplitGenerator(
              name='train_extra',
              gen_kwargs={  # pylint: disable=g-complex-comprehension
                  feat_dir.replace('/extra', ''): os.path.join(
                      path, 'train_extra'
                  )
                  for feat_dir, path in paths.items()
                  if feat_dir.endswith('/extra')
              },
          )
      )
    return splits

  def _generate_examples(self, **paths):
    left_imgs_root = paths['images_left']
    for city_id in tf.io.gfile.listdir(left_imgs_root):
      paths_city_root = {
          feat_dir: os.path.join(path, city_id)
          for feat_dir, path in paths.items()
      }

      left_city_root = paths_city_root['images_left']
      for left_img in tf.io.gfile.listdir(left_city_root):
        left_img_path = os.path.join(left_city_root, left_img)
        image_id = _get_left_image_id(left_img)

        if image_id in self.builder_config.ignored_ids:
          continue

        features = {
            'image_id': image_id,
            'image_left': left_img_path,
        }

        if self.builder_config.right_images:
          features['image_right'] = os.path.join(
              paths_city_root['images_right'],
              '{}_rightImg8bit.png'.format(image_id),
          )

        if self.builder_config.segmentation_labels:
          features['segmentation_label'] = os.path.join(
              paths_city_root['segmentation_labels'],
              '{}_{}.png'.format(image_id, self.builder_config.label_suffix),
          )

        if self.builder_config.disparity_maps:
          features['disparity_map'] = os.path.join(
              paths_city_root['disparity_maps'],
              '{}_disparity.png'.format(image_id),
          )

        yield image_id, features


# Helper functions

LEFT_IMAGE_FILE_RE = re.compile(r'([a-z\-]+)_(\d+)_(\d+)_leftImg8bit\.png')


def _get_left_image_id(left_image):
  """Returns the id of an image file.

  Used to associate an image file with its corresponding label.
  Example:
    'bonn_000001_000019_leftImg8bit' -> 'bonn_000001_000019'

  Args:
    left_image: name of the image file.

  Returns:
    Id of the image (see example above).
  """
  match = LEFT_IMAGE_FILE_RE.match(left_image)
  return '{}_{}_{}'.format(*match.groups())

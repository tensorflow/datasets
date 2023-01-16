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

"""Lost and Found Road Hazard Dataset."""

from os import path
import re

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class LostAndFoundConfig(tfds.core.BuilderConfig):
  """BuilderConfig for 'Lost and Found'.

  Args:
    right_images (bool): Enables right images for stereo image tasks.
    segmentation_labels (bool): Enables image segmentation labels.
    instance_ids (bool): Enables instance-id labels.
    disparity_maps (bool): Enables disparity maps.
    use_16bit (bool): Loads 16 bit (rgb) images instead of 8bit.
  """

  def __init__(
      self,
      right_images=False,
      segmentation_labels=False,
      instance_ids=False,
      disparity_maps=False,
      use_16bit=False,
      **kwargs,
  ):
    super(LostAndFoundConfig, self).__init__(**kwargs)

    self.features = ['image_left']
    if right_images:
      self.features.append('image_right')
    if segmentation_labels:
      self.features.append('segmentation_label')
    if instance_ids:
      self.features.append('instance_id')
    if disparity_maps:
      self.features.append('disparity_map')

    self.left_image_string = 'leftImg{}bit'.format('16' if use_16bit else '8')
    self.right_image_string = 'rightImg{}bit'.format('16' if use_16bit else '8')


class Builder(tfds.core.GeneratorBasedBuilder):
  """Lost and Found Road Hazard Dataset."""

  VERSION = tfds.core.Version('1.0.0')

  BUILDER_CONFIGS = [
      LostAndFoundConfig(
          name='semantic_segmentation',
          description='Lost and Found semantic segmentation dataset.',
          version='1.0.0',
          right_images=False,
          segmentation_labels=True,
          instance_ids=False,
          disparity_maps=False,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='stereo_disparity',
          description='Lost and Found stereo images and disparity maps.',
          version='1.0.0',
          right_images=True,
          segmentation_labels=False,
          instance_ids=False,
          disparity_maps=True,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='full',
          description='Full Lost and Found dataset.',
          version='1.0.0',
          right_images=True,
          segmentation_labels=True,
          instance_ids=True,
          disparity_maps=True,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='full_16bit',
          description='Full Lost and Found dataset.',
          version='1.0.0',
          right_images=True,
          segmentation_labels=True,
          instance_ids=True,
          disparity_maps=True,
          use_16bit=True,
      ),
  ]

  def _info(self):
    possible_features = {
        'image_left': tfds.features.Image(
            shape=(1024, 2048, 3), encoding_format='png'
        ),
        'image_right': tfds.features.Image(
            shape=(1024, 2048, 3), encoding_format='png'
        ),
        'segmentation_label': tfds.features.Image(
            shape=(1024, 2048, 1), encoding_format='png', use_colormap=True
        ),
        'instance_id': tfds.features.Image(
            shape=(1024, 2048, 1), encoding_format='png', use_colormap=True
        ),
        'disparity_map': tfds.features.Image(
            shape=(1024, 2048, 1), encoding_format='png'
        ),
    }
    features = {
        feat: possible_features[feat] for feat in self.builder_config.features
    }
    features['image_id'] = tfds.features.Text()
    features = tfds.features.FeaturesDict(features)
    return self.dataset_info_from_configs(
        # tfds.features.FeatureConnectors
        features=features,
        # Homepage of the dataset for documentation
        homepage='http://www.6d-vision.com/lostandfounddataset',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    base_url = (
        'http://www.dhbw-stuttgart.de/~sgehrig/lostAndFoundDataset/{}.zip'
    )

    # For each feature, this is the name of the zipfile and
    # root-directory in the archive
    zip_file_names = {
        'image_left': self.builder_config.left_image_string,
        'image_right': self.builder_config.right_image_string,
        'segmentation_label': 'gtCoarse',
        'instance_id': 'gtCoarse',
        'disparity_map': 'disparity',
    }

    download_urls = {
        feat: base_url.format(zip_file_names[feat])
        for feat in self.builder_config.features
    }
    # Split download and extract in two functions such that mock-data can
    # replace the result of the download function and is still used as input to
    # extract. Therefore, fake_data can be compressed zip archives.
    dl_paths = dl_manager.extract(dl_manager.download(download_urls))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                feat: path.join(dl_paths[feat], zip_file_names[feat], 'train')
                for feat in self.builder_config.features
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                feat: path.join(dl_paths[feat], zip_file_names[feat], 'test')
                for feat in self.builder_config.features
            },
        ),
    ]

  def _generate_examples(self, **paths):
    """Yields examples."""
    # different file-suffixes dependent on the feature to load
    file_suffix = {
        'image_left': self.builder_config.left_image_string,
        'image_right': self.builder_config.right_image_string,
        'segmentation_label': 'gtCoarse_labelIds',
        'instance_id': 'gtCoarse_instanceIds',
        'disparity_map': 'disparity',
    }

    for scene_id in tf.io.gfile.listdir(paths['image_left']):
      paths_city_root = {
          feat: path.join(feat_dir, scene_id)
          for feat, feat_dir in paths.items()
      }

      left_city_root = paths_city_root['image_left']
      for left_img in tf.io.gfile.listdir(left_city_root):
        image_id = _get_id_from_left_image(left_img)

        features = {
            feat: path.join(
                paths_city_root[feat],
                '{}_{}.png'.format(image_id, file_suffix[feat]),
            )
            for feat in paths
        }
        features['image_id'] = image_id

        yield image_id, features


# Helper functions

LEFT_IMAGE_FILE_RE = re.compile(r'(.+)_leftImg(?:8|16)bit\.png')


def _get_id_from_left_image(left_image):
  """Returns the id of an image file.

  Used to associate an image file
  with its corresponding label.
  Example:
    'bonn_000001_000019_leftImg8bit' -> 'bonn_000001_000019'

  Args:
    left_image: left image file name.

  Returns:
    id of the image.
  """
  return LEFT_IMAGE_FILE_RE.match(left_image).group(1)

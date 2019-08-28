"""Lost and Found Road Hazard Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path
import re

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import api_utils


_CITATION = """
@inproceedings{pinggera2016lost,
  title={Lost and found: detecting small road hazards for self-driving vehicles},
  author={Pinggera, Peter and Ramos, Sebastian and Gehrig, Stefan and Franke, Uwe and Rother, Carsten and Mester, Rudolf},
  booktitle={2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  year={2016}
}
"""

_DESCRIPTION = """
The LostAndFound Dataset addresses the problem of detecting unexpected small obstacles on
the road often caused by lost cargo. The dataset comprises 112 stereo video sequences
with 2104 annotated frames (picking roughly every tenth frame from the recorded data).

The dataset is designed analogous to the 'Cityscapes' dataset. The datset provides:
- stereo image pairs in either 8 or 16 bit color resolution
- precomputed disparity maps
- coarse semantic labels for objects and street

Descriptions of the labels are given here: http://www.6d-vision.com/laf_table.pdf
"""


class LostAndFoundConfig(tfds.core.BuilderConfig):
  '''BuilderConfig for 'Lost and Found'

    Args:
      right_images (bool): Enables right images for stereo image tasks.
      segmentation_labels (bool): Enables image segmentation labels.
      instance_ids (bool): Enables instance-id labels.
      disparity_maps (bool): Enables disparity maps.
      use_16bit (bool): Loads 16 bit (rgb) images instead of 8bit.
  '''

  @api_utils.disallow_positional_args
  def __init__(self, right_images=False, segmentation_labels=False,
               instance_ids=False, disparity_maps=False, use_16bit=False,
               **kwargs):
    super().__init__(**kwargs)

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


class LostAndFound(tfds.core.GeneratorBasedBuilder):
  """Lost and Found Road Hazard Dataset."""

  VERSION = tfds.core.Version('1.0.0')

  BUILDER_CONFIGS = [
      LostAndFoundConfig(
          name='semantic_segmentation',
          description='Lost and Found semantic segmentation dataset.',
          version="1.0.0",
          right_images=False,
          segmentation_labels=True,
          instance_ids=False,
          disparity_maps=False,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='stereo_disparity',
          description='Lost and Found stereo images and disparity maps.',
          version="1.0.0",
          right_images=True,
          segmentation_labels=False,
          instance_ids=False,
          disparity_maps=True,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='full',
          description='Full Lost and Found dataset.',
          version="1.0.0",
          right_images=True,
          segmentation_labels=True,
          instance_ids=True,
          disparity_maps=True,
          use_16bit=False,
      ),
      LostAndFoundConfig(
          name='full_16bit',
          description='Full Lost and Found dataset.',
          version="1.0.0",
          right_images=True,
          segmentation_labels=True,
          instance_ids=True,
          disparity_maps=True,
          use_16bit=True,
      )]

  def _info(self):
    possible_features = {
        'image_left': tfds.features.Image(shape=(1024, 2048, 3),
                                          encoding_format='png'),
        'image_right': tfds.features.Image(shape=(1024, 2048, 3),
                                           encoding_format='png'),
        'segmentation_label': tfds.features.Image(shape=(1024, 2048, 1),
                                                  encoding_format='png'),
        'instance_id': tfds.features.Image(shape=(1024, 2048, 1),
                                           encoding_format='png'),
        'disparity_map': tfds.features.Image(shape=(1024, 2048, 1),
                                             encoding_format='png')}
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'image_id': tfds.features.Text(),
            **{feat: possible_features[feat]
               for feat in self.builder_config.features}}),
        # Homepage of the dataset for documentation
        urls=['http://www.6d-vision.com/lostandfounddataset'],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    base_url = 'http://www.dhbw-stuttgart.de/~sgehrig/lostAndFoundDataset/{}.zip'
    download_urls = {
        'image_left': base_url.format(self.builder_config.left_image_string)}
    if 'image_right' in self.builder_config.features:
      download_urls['image_right'] = base_url.format(
          self.builder_config.right_image_string)
    if 'segmentation_label' in self.builder_config.features \
            or 'instance_id' in self.builder_config.features:
      download_urls['gt'] = base_url.format('gtCoarse')
    if 'disparity_map' in self.builder_config.features:
      download_urls['disparity_map'] = base_url.format('disparity')
    # split into two steps to save space for testing data
    dl_paths = dl_manager.download(download_urls)
    dl_paths = dl_manager.extract(dl_paths)

    # point segmentation label and instance IDs both to directory for ground-truth
    if 'gt' in dl_paths:
      dl_paths['segmentation_label'] = dl_paths['gt']
      dl_paths['instance_id'] = dl_paths['gt']

    # first directory in the zipfile, dependent on feature to load
    sub_dirs = {
        'image_left': self.builder_config.left_image_string,
        'image_right': self.builder_config.right_image_string,
        'segmentation_label': 'gtCoarse',
        'instance_id': 'gtCoarse',
        'disparity_map': 'disparity'}

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={feat: path.join(dl_paths[feat], sub_dirs[feat], 'train')
                        for feat in self.builder_config.features},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={feat: path.join(dl_paths[feat], sub_dirs[feat], 'test')
                        for feat in self.builder_config.features},
        )
    ]

  def _generate_examples(self, **paths):
    """Yields examples."""
    # different file-suffixes dependent on the feature to load
    file_suffix = {
        'image_left': self.builder_config.left_image_string,
        'image_right': self.builder_config.right_image_string,
        'segmentation_label': 'gtCoarse_labelIds',
        'instance_id': 'gtCoarse_instanceIds',
        'disparity_map': 'disparity'}

    for scene_id in tf.io.gfile.listdir(paths['image_left']):
      paths_city_root = {feat: path.join(feat_dir, scene_id)
                         for feat, feat_dir in paths.items()}

      left_city_root = paths_city_root['image_left']
      for left_img in tf.io.gfile.listdir(left_city_root):
        image_id = _get_id_from_left_image(left_img)

        features = {
            'image_id': image_id,
            **{feat: path.join(paths_city_root[feat],
                               '{}_{}.png'.format(image_id, file_suffix[feat]))
               for feat in paths}}

        yield image_id, features

# Helper functions

LEFT_IMAGE_FILE_RE = re.compile(r'(.+)_leftImg(?:8|16)bit\.png')

def _get_id_from_left_image(left_image):
  '''Returns the id of an image file. Used to associate an image file
  with its corresponding label.
  Example:
    'bonn_000001_000019_leftImg8bit' -> 'bonn_000001_000019'
  '''
  return LEFT_IMAGE_FILE_RE.match(left_image).group(1)

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

"""Visual Domain Decathlon Datasets."""

import json
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL_PREFIX_VGG = 'http://www.robots.ox.ac.uk/~vgg/share/'
_URL_PREFIX_IMAGENET = 'http://www.image-net.org/image/decathlon/'
_CONFIG_DESCRIPTION_PATTERN = (
    'Data based on "{}", with images resized isotropically to have a shorter '
    'size of 72 pixels.'
)


class VisualDomainDecathlonConfig(tfds.core.BuilderConfig):

  def __init__(self, num_classes, **kwargs):
    self.num_classes = num_classes
    if 'version' not in kwargs:
      kwargs['version'] = tfds.core.Version('1.2.0')
    super(VisualDomainDecathlonConfig, self).__init__(**kwargs)


def _get_builder_configs():
  """Returns the list of builder configs for the dataset."""
  configs = []
  for short_name, full_name, num_classes in [
      ('aircraft', 'Aircraft', 100),
      ('cifar100', 'CIFAR-100', 100),
      ('daimlerpedcls', 'Daimler Pedestrian Classification', 2),
      ('dtd', 'Describable Textures', 47),
      ('gtsrb', 'German Traffic Signs', 43),
      ('imagenet12', 'Imagenet', 1000),
      ('omniglot', 'Omniglot', 1623),
      ('svhn', 'Street View House Numbers', 10),
      ('ucf101', 'UCF101 Dynamic Images', 101),
      ('vgg-flowers', 'VGG-Flowers', 102),
  ]:
    description = _CONFIG_DESCRIPTION_PATTERN.format(full_name)
    configs.append(
        VisualDomainDecathlonConfig(
            name=short_name, num_classes=num_classes, description=description
        )
    )
  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """Visual Domain Decathlon Datasets."""

  BUILDER_CONFIGS = _get_builder_configs()

  def _info(self):
    num_classes = self.builder_config.num_classes
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'name': tfds.features.Text(),
            'image': tfds.features.Image(
                shape=(None, None, 3), encoding_format='jpeg'
            ),
            'label': tfds.features.ClassLabel(num_classes=num_classes),
        }),
        supervised_keys=('image', 'label'),
        homepage='https://www.robots.ox.ac.uk/~vgg/decathlon/',
    )

  def _split_generators(self, dl_manager):
    if self.builder_config.name == 'imagenet12':
      devkit_path, images_archive = dl_manager.download_and_extract([
          _URL_PREFIX_VGG + 'decathlon-1.0-devkit.tar.gz',
          tfds.download.Resource(
              url=_URL_PREFIX_IMAGENET + 'decathlon-1.0-data-imagenet.tar',
              extract_method=tfds.download.ExtractMethod.NO_EXTRACT,
          ),
      ])
    else:
      devkit_path, data_path = dl_manager.download_and_extract([
          _URL_PREFIX_VGG + 'decathlon-1.0-devkit.tar.gz',
          _URL_PREFIX_VGG + 'decathlon-1.0-data.tar.gz',
      ])
      images_archive = os.path.join(
          data_path, self.builder_config.name + '.tar'
      )
    annotations_path = os.path.join(devkit_path, 'decathlon-1.0', 'annotations')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                images_archive=images_archive,
                annotations_path=annotations_path,
                split='train',
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                images_archive=images_archive,
                annotations_path=annotations_path,
                split='test',
            ),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(
                images_archive=images_archive,
                annotations_path=annotations_path,
                split='val',
            ),
        ),
    ]

  def _generate_examples(self, images_archive, annotations_path, split):
    """Yields examples."""
    filename_to_label = _get_filename_to_label_map(
        annotations_path=annotations_path,
        dataset_name=self.builder_config.name,
        split=split,
    )
    for image_fname, image_fobj in tfds.download.iter_archive(
        path=images_archive, method=tfds.download.ExtractMethod.TAR_STREAM
    ):
      image_fname = image_fname.replace('\\', '/')  # For windows compatibility
      if image_fname in filename_to_label:
        label = filename_to_label[image_fname]
        example = {
            'name': image_fname,
            'image': image_fobj,
            'label': label,
        }
        yield image_fname, example


def _get_filename_to_label_map(annotations_path, dataset_name, split):
  """Returns a mapping from image filenames to labels, for the given split."""
  filename_to_label = {}
  if split == 'test':
    filepath = os.path.join(
        annotations_path, dataset_name + '_test_stripped.json'
    )
  else:
    filepath = os.path.join(annotations_path, dataset_name + '_%s.json' % split)
  prefix = 'data/'
  with tf.io.gfile.GFile(filepath, mode='r') as f:
    annotations = json.load(f)
    if split == 'test':
      # For test, labels are unknown.
      for example_info in annotations['images']:
        image_filename = example_info['file_name']
        image_filename = image_filename[len(prefix) :]
        filename_to_label[image_filename] = -1
    else:
      # Load a map from category ID to label index.
      category_id_to_label = {}
      for i, category_info in enumerate(annotations['categories']):
        category_id_to_label[category_info['id']] = i
      # Load a map from image ID to image filename.
      image_id_to_filename = {}
      for example_info in annotations['images']:
        image_id_to_filename[example_info['id']] = example_info['file_name']
      # Load the map from image filename to label.
      for example_info in annotations['annotations']:
        image_filename = image_id_to_filename[example_info['image_id']]
        image_filename = image_filename[len(prefix) :]
        label = category_id_to_label[example_info['category_id']]
        filename_to_label[image_filename] = label
  return filename_to_label

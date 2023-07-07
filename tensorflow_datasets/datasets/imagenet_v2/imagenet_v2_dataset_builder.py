# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""The ImageNet-v2 image classification dataset."""
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

# Note: Bump the version if the links change.

_ROOT_URL = 'https://huggingface.co/datasets/vaishaal/ImageNetV2/resolve/main'
_IMAGENET_V2_URLS = {
    'matched-frequency': _ROOT_URL + '/imagenetv2-matched-frequency.tar.gz',
    'threshold-0.7': _ROOT_URL + '/imagenetv2-threshold0.7.tar.gz',
    'topimages': _ROOT_URL + '/imagenetv2-top-images.tar.gz',
}
_TAR_TOPDIR = {
    'matched-frequency': 'imagenetv2-matched-frequency-format-val',
    'threshold-0.7': 'imagenetv2-threshold0.7-format-val',
    'topimages': 'imagenetv2-top-images-format-val',
}


class ImagenetV2Config(tfds.core.BuilderConfig):
  """Configuration specifying the variant to use."""

  def __init__(self, *, variant, **kwargs):
    """The parameters specifying how the dataset will be processed.

    The dataset comes in three different variants. Please refer to the paper
    on more details how they were collected.

    Args:
      variant: One of 'matched-frequency', 'threshold-0.7', or 'topimages'.
      **kwargs: Passed on to the constructor of `BuilderConfig`.
    """
    super(ImagenetV2Config, self).__init__(**kwargs)
    if variant not in _IMAGENET_V2_URLS:
      raise ValueError(
          'Unknown split number {}, must be one of {}'.format(
              variant, list(_IMAGENET_V2_URLS)
          )
      )
    self.variant = variant


def _create_builder_configs():
  for variant in _IMAGENET_V2_URLS:
    yield ImagenetV2Config(
        variant=variant,
        name=variant,
    )


class Builder(tfds.core.GeneratorBasedBuilder):
  """An ImageNet test set recollected by following the original protocol."""

  VERSION = tfds.core.Version('3.0.0')
  SUPPORTED_VERSIONS = [
      tfds.core.Version('2.0.0'),
  ]
  RELEASE_NOTES = {
      '1.0.0': 'Initial version.',
      '2.0.0': 'Files updated.',
      '3.0.0': (
          'Fix file_name, from absolute path to path relative to '
          'data directory, ie: "class_id/filename.jpg".'
      ),
      '3.1.0': 'New URLs for resources from Hugging Face.',
  }
  BUILDER_CONFIGS = list(_create_builder_configs())

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),
        }),
        # Used if as_supervised=True in builder.as_dataset.
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/modestyachts/ImageNetV2',
    )

  def _split_generators(self, dl_manager):
    """Returns a SplitGenerator for the test set."""
    variant_url = _IMAGENET_V2_URLS[self.builder_config.variant]
    imagenet_v2_root = os.path.join(
        dl_manager.download_and_extract(variant_url),
        _TAR_TOPDIR[self.builder_config.variant],
    )
    return [
        tfds.core.SplitGenerator(
            # The dataset provides only a test split.
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'imagenet_v2_root': imagenet_v2_root},
        ),
    ]

  def _generate_examples(self, imagenet_v2_root):
    """Yields the examples."""
    # The directory structure is `class_number/filename_number.jpg`, where
    # class_number is in [0, 1000) and filename_number in [0, 10).
    for class_id in tf.io.gfile.listdir(imagenet_v2_root):
      class_dir = os.path.join(imagenet_v2_root, class_id)
      for image_filename in tf.io.gfile.listdir(class_dir):
        image_path = os.path.join(class_dir, image_filename)
        features = {
            'image': image_path,
            'label': int(class_id),
            'file_name': os.path.join(class_id, image_filename),
        }
        yield f'{class_id}_{image_filename}', features

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

"""The ImageNet-A image classification dataset."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds

_IMAGENET_A_URL = r'https://people.eecs.berkeley.edu/~hendrycks/imagenet-a.tar'


class Builder(tfds.core.GeneratorBasedBuilder):
  """Natural adversarial examples with ImageNet labels."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),
        }),
        # Used if as_supervised=True in # builder.as_dataset.
        supervised_keys=('image', 'label'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/hendrycks/natural-adv-examples',
    )

  def _split_generators(self, dl_manager):
    """Returns a SplitGenerator for the test set."""
    imagenet_a_root = os.path.join(
        dl_manager.download_and_extract(_IMAGENET_A_URL), 'imagenet-a'
    )
    return [
        tfds.core.SplitGenerator(
            # The dataset provides only a test split.
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'imagenet_a_root': imagenet_a_root},
        ),
    ]

  def _generate_examples(self, imagenet_a_root):
    """Yields the examples."""
    # The directory structure is `imagenet-a/imagenet_synset_id/filename.jpg`.
    for class_synset in tf.io.gfile.listdir(imagenet_a_root):
      class_dir = os.path.join(imagenet_a_root, class_synset)
      if not tf.io.gfile.isdir(class_dir):
        continue
      for image_filename in tf.io.gfile.listdir(class_dir):
        image_path = os.path.join(class_dir, image_filename)
        features = {
            'image': image_path,
            'label': class_synset,
            'file_name': image_filename,
        }
        yield image_filename, features

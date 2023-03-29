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

"""Imagenet few-shot datasets."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
from tensorflow_datasets.datasets.imagenet2012_subset import imagenet2012_subset_dataset_builder
import tensorflow_datasets.public_api as tfds

# pylint: disable=line-too-long
SUBSET2FILES = {
    '1shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/1shot.txt'),
    '5shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/5shot.txt'),
    '10shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/10shot.txt'),
}
TUNE_FILE = tfds.core.gcs_path('downloads/imagenet2012_fewshot/tune.txt')


class Builder(imagenet2012_subset_dataset_builder.Builder):
  """Class balanced subset of Imagenet 2012 dataset for few-shot learning."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(  # pylint: disable=g-complex-comprehension
          name=subset_size,
          description='{} of total ImageNet training set.'.format(subset_size),
          version=tfds.core.Version('5.0.1'),
      )
      for subset_size in SUBSET2FILES
  ]

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='http://image-net.org/',
    )

  def _split_generators(self, dl_manager):
    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, val_path
          )
      )

    # Download and load subset file.
    subset_file = SUBSET2FILES[self.builder_config.name]
    if isinstance(subset_file, list):  # it will only be a list during testing,
      subset_file = subset_file[0]  # where the first entry is 1shot.txt.
    subset = set(subset_file.read_text().splitlines())

    # Get the file for tune split.
    tuneset = set(TUNE_FILE.read_text().splitlines())

    return {
        tfds.Split.TRAIN: self._generate_examples(
            archive=dl_manager.iter_archive(train_path), subset=subset
        ),
        tfds.Split('tune'): self._generate_examples(
            archive=dl_manager.iter_archive(train_path), subset=tuneset
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            archive=dl_manager.iter_archive(val_path),
            validation_labels=imagenet_common.get_validation_labels(val_path),
        ),
    }

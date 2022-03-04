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

"""Imagenet few-shot datasets."""

import os

import tensorflow as tf
from tensorflow_datasets.image_classification import imagenet
from tensorflow_datasets.image_classification import imagenet2012_subset
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Imagenet2012Fewshot is a subset of original ImageNet ILSVRC 2012 dataset.
The dataset share the *same* validation set as the original ImageNet ILSVRC 2012
dataset. However, the training set is subsampled in a label balanced fashion.
In `5shot` configuration, 5 images per label, or 5000 images are sampled; and
in `10shot` configuration, 10 images per label, or 10000 images are sampled.
"""

_CITATION = """\
@article{ILSVRC15,
  Author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
  Title = {{ImageNet Large Scale Visual Recognition Challenge}},
  Year = {2015},
  journal   = {International Journal of Computer Vision (IJCV)},
  doi = {10.1007/s11263-015-0816-y},
  volume={115},
  number={3},
  pages={211-252}
}
"""

# pylint: disable=line-too-long
_LABELS_FNAME = 'image_classification/imagenet2012_labels.txt'
SUBSET2FILES = {
    '1shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/1shot.txt'),
    '5shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/5shot.txt'),
    '10shot': tfds.core.gcs_path('downloads/imagenet2012_fewshot/10shot.txt')
}
TUNE_FILE = tfds.core.gcs_path('downloads/imagenet2012_fewshot/tune.txt')


class Imagenet2012Fewshot(imagenet2012_subset.Imagenet2012Subset):
  """Class balanced subset of Imagenet 2012 dataset for few-shot learning."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(  # pylint: disable=g-complex-comprehension
          name=subset_size,
          description='{} of total ImageNet training set.'.format(subset_size),
          version=tfds.core.Version('5.0.1'),
      ) for subset_size in SUBSET2FILES
  ]

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
            'label': tfds.features.ClassLabel(names_file=names_file),
            'file_name': tfds.features.Text(),  # Eg: 'n15075141_54.JPEG'
        }),
        supervised_keys=('image', 'label'),
        homepage='http://image-net.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):

    train_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_train.tar')
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')

    if not tf.io.gfile.exists(train_path) or not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}, {}'.format(
              train_path, val_path))

    # Download and load subset file.
    subset_file = SUBSET2FILES[self.builder_config.name]
    if isinstance(subset_file, list):  # it will only be a list during testing,
      subset_file = subset_file[0]  # where the first entry is 1shot.txt.
    subset = set(subset_file.read_text().splitlines())

    # Get the file for tune split.
    tuneset = set(TUNE_FILE.read_text().splitlines())

    return {
        tfds.Split.TRAIN:
            self._generate_examples(
                archive=dl_manager.iter_archive(train_path), subset=subset),
        tfds.Split('tune'):
            self._generate_examples(
                archive=dl_manager.iter_archive(train_path), subset=tuneset),
        tfds.Split.VALIDATION:
            self._generate_examples(
                archive=dl_manager.iter_archive(val_path),
                validation_labels=imagenet.get_validation_labels(val_path)),
    }

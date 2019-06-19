# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""PatchCamelyon images dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import h5py
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
The PatchCamelyon benchmark is a new and challenging image classification
dataset. It consists of 327.680 color images (96 x 96px) extracted from
histopathologic scans of lymph node sections. Each image is annoted with a
binary label indicating presence of metastatic tissue. PCam provides a new
benchmark for machine learning models: bigger than CIFAR10, smaller than
Imagenet, trainable on a single GPU.
"""
_CITATION = """\
@misc{b_s_veeling_j_linmans_j_winkens_t_cohen_2018_2546921,
  author       = {B. S. Veeling, J. Linmans, J. Winkens, T. Cohen, M. Welling},
  title        = {Rotation Equivariant CNNs for Digital Pathology},
  month        = sep,
  year         = 2018,
  doi          = {10.1007/978-3-030-00934-2_24},
  url          = {https://doi.org/10.1007/978-3-030-00934-2_24}
}
"""
_URL = 'https://patchcamelyon.grand-challenge.org/'


class PatchCamelyon(tfds.core.GeneratorBasedBuilder):
  """PatchCamelyon."""

  VERSION = tfds.core.Version('0.1.0')
  SUPPORTED_VERSIONS = [
      tfds.core.Version('1.0.0', experiments={tfds.core.Experiment.S3: True}),
      tfds.core.Version('0.1.0'),
  ]
  # Version history:
  # 1.0.0: S3 (new shuffling, sharding and slicing mechanism).

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'id':
                tfds.features.Text(),
            'image':
                tfds.features.Image(shape=(96, 96, 3), encoding_format='png'),
            'label':
                tfds.features.ClassLabel(num_classes=2),
        }),
        supervised_keys=('image', 'label'),
        urls=[_URL],
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    base_url = 'https://zenodo.org/record/2546921/files/'
    resources = {
        'test_x': base_url + 'camelyonpatch_level_2_split_test_x.h5.gz',
        'test_y': base_url + 'camelyonpatch_level_2_split_test_y.h5.gz',
        'train_x': base_url + 'camelyonpatch_level_2_split_train_x.h5.gz',
        'train_y': base_url + 'camelyonpatch_level_2_split_train_y.h5.gz',
        'valid_x': base_url + 'camelyonpatch_level_2_split_valid_x.h5.gz',
        'valid_y': base_url + 'camelyonpatch_level_2_split_valid_y.h5.gz',
    }
    paths = dl_manager.download_and_extract(resources)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(split='test', paths=paths)),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(split='train', paths=paths)),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs=dict(split='valid', paths=paths)),
    ]

  def _generate_examples(self, split, paths):
    """Generates images and labels given the image directory path.

    Args:
      split: name of the split to generate examples for (test, train, valid).
      paths: dictionary with the paths to the h5 files for each split.

    Yields:
      A dictionary with the image and the corresponding label.
    """
    filepath_x = paths[split + '_x']
    filepath_y = paths[split + '_y']
    h5x_file = h5py.File(filepath_x, 'r')
    h5y_file = h5py.File(filepath_y, 'r')
    images = h5x_file['x']
    labels = h5y_file['y']  # Note: Labels are in a N x 1 x 1 x 1 tensor.
    for i, (image, label) in enumerate(zip(images, labels)):
      label = label.flatten()[0]
      id_ = '%s_%d' % (split, i)
      record = {'id': id_, 'image': image, 'label': label}
      if self.version.implements(tfds.core.Experiment.S3):
        yield id_, record
      else:
        yield record

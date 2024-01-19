# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Imagenet val. annotated by ReaL labels (https://arxiv.org/abs/2006.07159)."""

import json
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.datasets.imagenet2012 import imagenet_common
import tensorflow_datasets.public_api as tfds


_REAL_LABELS_URL = 'https://raw.githubusercontent.com/google-research/reassessed-imagenet/master/real.json'


class Builder(tfds.core.GeneratorBasedBuilder):
  """ImageNet validation images with ReaL labels."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  manual_dir should contain `ILSVRC2012_img_val.tar` file.
  You need to register on http://www.image-net.org/download-images in order
  to get the link to download the dataset.
  """

  def _info(self):
    names_file = imagenet_common.label_names_file()
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(encoding_format='jpeg'),
            'original_label': tfds.features.ClassLabel(names_file=names_file),
            'real_label': tfds.features.Sequence(
                tfds.features.ClassLabel(names_file=names_file)
            ),
            'file_name': tfds.features.Text(),
        }),
        supervised_keys=('image', 'real_label'),
        homepage='https://github.com/google-research/reassessed-imagenet',
    )

  def _get_real_labels(self, dl_manager):
    with tf.io.gfile.GFile(dl_manager.download(_REAL_LABELS_URL), 'r') as f:
      # ReaL labels are ordered in the lexicographical order.
      return {
          'ILSVRC2012_val_{:08}.JPEG'.format(i + 1): labels
          for i, labels in enumerate(json.load(f))
      }

  def _split_generators(self, dl_manager):
    val_path = os.path.join(dl_manager.manual_dir, 'ILSVRC2012_img_val.tar')
    if not tf.io.gfile.exists(val_path):
      raise AssertionError(
          'ImageNet requires manual download of the data. Please download '
          'the train and val set and place them into: {}'.format(val_path)
      )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'archive': dl_manager.iter_archive(val_path),
                'original_labels': imagenet_common.get_validation_labels(
                    val_path
                ),
                'real_labels': self._get_real_labels(dl_manager),
            },
        ),
    ]

  def _generate_examples(self, archive, original_labels, real_labels):
    for fname, fobj in archive:
      record = {
          'file_name': fname,
          'image': fobj,
          'original_label': original_labels[fname],
          'real_label': real_labels[fname],
      }
      yield fname, record

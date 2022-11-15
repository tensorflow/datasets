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

"""Stanford 3D Objects for Disentangling (S3O4D) dataset."""

import itertools

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for s3o4d dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(256, 256, 3)),
            'label': tfds.features.ClassLabel(names=['bunny', 'dragon']),
            'illumination': tfds.features.Tensor(shape=(3,), dtype=tf.float32),
            'pose_quat': tfds.features.Tensor(shape=(4,), dtype=tf.float32),
            'pose_mat': tfds.features.Tensor(shape=(3, 3), dtype=tf.float32),
        }),
        supervised_keys=None,
        homepage='https://github.com/deepmind/deepmind-research/tree/master/geomancer#stanford-3d-objects-for-disentangling-s3o4d',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    suffices = {'img': 'images.zip', 'latent': 'latents.npz'}
    prod = itertools.product(['bunny', 'dragon'], ['train', 'test'],
                             ['img', 'latent'])
    path_dict = dict([
        ('_'.join([a, b, c]),
         f'https://storage.googleapis.com/dm_s3o4d/{a}/{b}_{suffices[c]}')
        for a, b, c in prod
    ])
    paths = dl_manager.download(path_dict)

    return dict([
        (  # pylint: disable=g-complex-comprehension
            '_'.join([a, b]),
            self._generate_examples(dl_manager, paths['_'.join([a, b, 'img'])],
                                    paths['_'.join([a, b, 'latent'])], a))
        for a, b in itertools.product(['bunny', 'dragon'], ['train', 'test'])
    ])

  def _generate_examples(self, dl_manager: tfds.download.DownloadManager,
                         img_path, latent_path, label):
    """Yields examples."""
    with tf.io.gfile.GFile(latent_path, 'rb') as f:
      latents = dict(np.load(f))
    for key in latents:
      latents[key] = latents[key].astype(np.float32)
    for fname, fobj in dl_manager.iter_archive(img_path):
      idx = int(fname[-9:-4]) % 80000
      yield label + '_' + fname[-9:-4], {
          'image': fobj,
          'label': label,
          'illumination': latents['illumination'][idx],
          'pose_mat': latents['pose_mat'][idx],
          'pose_quat': latents['pose_quat'][idx],
      }

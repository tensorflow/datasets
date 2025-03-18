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

"""sift1m dataset."""

import h5py
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = 'http://ann-benchmarks.com/sift-128-euclidean.hdf5'


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for sift1m dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'index': tfds.features.Scalar(
                dtype=np.int64, doc='Index within the split.'
            ),
            'embedding': tfds.features.Tensor(shape=(128,), dtype=np.float32),
            'neighbors': tfds.features.Sequence(
                {
                    'index': tfds.features.Scalar(
                        dtype=np.int64, doc='Neighbor index.'
                    ),
                    'distance': tfds.features.Scalar(
                        dtype=np.float32, doc='Neighbor distance.'
                    ),
                },
                doc=(
                    'The computed neighbors, which is only available for'
                    ' the test split.'
                ),
            ),
        }),
        homepage='http://corpus-texmex.irisa.fr/',
        disable_shuffling=True,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract({'file': _URL})
    return {
        'database': self._generate_examples(path, True),
        'test': self._generate_examples(path, False),
    }

  def _generate_examples(self, path, is_database):
    """Pulls data from hdf5 into splits."""
    with tf.io.gfile.GFile(path['file'], 'rb') as f:
      with h5py.File(f, 'r') as dataset_file:
        if is_database:
          for idx, val in enumerate(dataset_file['train']):
            yield idx, {'index': idx, 'embedding': val, 'neighbors': []}
        else:
          for idx, (val, n_indices, distances) in enumerate(
              zip(
                  dataset_file['test'],
                  dataset_file['neighbors'],
                  dataset_file['distances'],
              )
          ):
            neighbors = []
            for nn_idx, nn_dist in zip(n_indices, distances):
              neighbors.append({'index': nn_idx, 'distance': nn_dist})
            yield idx, {
                'index': idx,
                'embedding': val,
                'neighbors': neighbors,
            }

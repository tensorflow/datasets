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

"""deep1b dataset."""

import h5py
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Pre-trained embeddings for approximate nearest neighbor search using the
cosine distance. This dataset consists of two splits:

  1. 'database': consists of 9,990,000 data points, each has features:
    'embedding' (96 floats), 'index' (int64), 'neighbors' (empty list).
  2. 'test': consists of 10,000 data points, each has features: 'embedding' (96
    floats), 'index' (int64), 'neighbors' (list of 'index' and 'distance'
    of the nearest neighbors in the database.)
"""

_CITATION = """
@inproceedings{babenko2016efficient,
  title={Efficient indexing of billion-scale datasets of deep descriptors},
  author={Babenko, Artem and Lempitsky, Victor},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={2055--2063},
  year={2016}
}
"""

_URL = 'http://ann-benchmarks.com/deep-image-96-angular.hdf5'


class Deep1b(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for deep1b dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'index':
                tfds.features.Scalar(
                    dtype=tf.int64, doc='Index within the split.'),
            'embedding':
                tfds.features.Tensor(shape=(96,), dtype=tf.float32),
            'neighbors':
                tfds.features.Sequence(
                    {
                        'index':
                            tfds.features.Scalar(
                                dtype=tf.int64, doc='Neighbor index.'),
                        'distance':
                            tfds.features.Scalar(
                                dtype=tf.float32, doc='Neighbor distance.'),
                    },
                    doc='The computed neighbors, which is only available for the test split.'
                )
        }),
        homepage='http://sites.skoltech.ru/compvision/noimi/',
        citation=_CITATION,
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
              zip(dataset_file['test'], dataset_file['neighbors'],
                  dataset_file['distances'])):
            neighbors = []
            for nn_idx, nn_dist in zip(n_indices, distances):
              neighbors.append({'index': nn_idx, 'distance': nn_dist})
            yield idx, {
                'index': idx,
                'embedding': val,
                'neighbors': neighbors,
            }

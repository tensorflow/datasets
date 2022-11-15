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

"""TensorFlow dataset for Binary Alphadigits."""
import six.moves.urllib as urllib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = 'https://cs.nyu.edu/~roweis/data/'

_DESCRIPTION = ("Binary 20x16 digits of '0' through '9' and capital 'A' "
                "through 'Z'. 39 examples of each class.")

_IMAGE_SHAPE = (20, 16, 1)

_NAMES = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]


class Builder(tfds.core.GeneratorBasedBuilder):
  """Binary alphadigits dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    """Define the Dataset info."""

    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=_IMAGE_SHAPE),
            'label': tfds.features.ClassLabel(names=_NAMES),
        }),
        supervised_keys=('image', 'label'),
        homepage=_URL,
    )

  def _split_generators(self, dl_manager):
    """Define Splits for training data."""

    path = dl_manager.download(
        {'train': urllib.parse.urljoin(_URL, 'binaryalphadigs.mat')})

    return [
        tfds.core.SplitGenerator(
            name='train',
            gen_kwargs={
                'data_dir_path': path['train'],
            },
        )
    ]

  def _generate_examples(self, data_dir_path):
    """Generate Splits for training data."""

    with tf.io.gfile.GFile(data_dir_path, 'rb') as f:
      mat = tfds.core.lazy_imports.scipy.io.loadmat(f)
    for i in range(len(mat['dat'])):
      label = mat['classlabels'][0][i].item()
      for j in range(len(mat['dat'][i])):
        image = mat['dat'][i][j].reshape(20, 16, 1)
        yield '%d_%d' % (i, j), {'label': label, 'image': image}

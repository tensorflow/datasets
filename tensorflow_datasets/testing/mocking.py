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

"""Mock util for tfds.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import os
import random

from absl.testing import absltest
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import features as features_lib


@contextlib.contextmanager
def mock_data(num_examples=1, as_dataset_fn=None, data_dir=None):
  """Mock tfds to generate random data.

  This function requires the true metadata files (dataset_info.json, label.txt,
  vocabulary files) to be stored in `data_dir/dataset_name/version`, as they
  would be for the true dataset.
  The actual examples will be randomly generated using
  `builder.info.features.get_tensor_info()`.
  Download and prepare step will be skipped.

  Warning: As the mocked builder will use the true metadata (label names,...),
  the `info.split['train'].num_examples` won't match `len(list(ds_train))`.

  Usage (automated):

  ```
  with mock_data(num_examples=5):
    ds = tfds.load('some_dataset', split='train')

    for ex in ds:  # ds will yield randomly generated examples.
      ex
  ```

  If you want more fine grain control over the generated examples, you can
  manually overwrite the `DatasetBuilder._as_dataset` method.
  Usage (manual):

  ```
  def as_dataset(self, *args, **kwargs):
    return tf.data.Dataset.from_generator(
        lambda: ({
            'image': np.ones(shape=(28, 28, 1), dtype=np.uint8),
            'label': i % 10,
        } for i in range(num_examples)),
        output_types=self.info.features.dtype,
        output_shapes=self.info.features.shape,
    )

  with mock_data(as_dataset_fn=as_dataset):
    ds = tfds.load('some_dataset', split='train')

    for ex in ds:  # ds will yield the fake data example of 'as_dataset'.
      ex
  ```

  Args:
    num_examples: `int`, the number of fake example to generate.
    as_dataset_fn: if provided, will replace the default random example
      generator. This function mock the `FileAdapterBuilder._as_dataset`
    data_dir: `str`, `data_dir` folder from where to load the metadata.
      Will overwrite `data_dir` kwargs from `tfds.load`.

  Yields:
    None
  """

  def mock_download_and_prepare(self, *args, **kwargs):
    del args
    del kwargs
    if not tf.io.gfile.exists(self._data_dir):  # pylint: disable=protected-access
      raise ValueError(
          'TFDS has been mocked, but metadata files where not found in {}. '
          'You should copy the real metadata files, so that the dataset '
          'can be loaded properly, or set the data_dir kwarg of'
          'tfds.testing.mock_tfds(data_dir=...).'
          ''.format(self._data_dir)  # pylint: disable=protected-access
      )

  def mock_as_dataset(self, *args, **kwargs):
    del args
    del kwargs
    ds = tf.data.Dataset.from_generator(
        lambda: (_generate_random_example(self) for _ in range(num_examples)),
        output_types=self.info.features.dtype,
        output_shapes=self.info.features.shape,
    )
    return ds

  if not as_dataset_fn:
    as_dataset_fn = mock_as_dataset

  if not data_dir:
    data_dir = os.path.join(os.path.dirname(__file__), 'metadata')

  download_and_prepare_path = 'tensorflow_datasets.core.dataset_builder.DatasetBuilder.download_and_prepare'
  as_dataset_path = 'tensorflow_datasets.core.dataset_builder.FileAdapterBuilder._as_dataset'
  data_dir_path = 'tensorflow_datasets.core.constants.DATA_DIR'

  with absltest.mock.patch(as_dataset_path, as_dataset_fn), \
       absltest.mock.patch(
           download_and_prepare_path, mock_download_and_prepare), \
       absltest.mock.patch(data_dir_path, data_dir):
    yield


def _generate_random_array(feature, tensor_info):
  """Generates a random tensor for a single feature."""
  # TODO(tfds): Could improve the fake generatiion:
  # * Use the feature statistics (min, max)
  # * For Sequence features
  # * For Text
  shape = [  # Fill dynamic shape with random values
      np.random.randint(5, 50) if s is None else s
      for s in tensor_info.shape
  ]
  if isinstance(features_lib, features_lib.ClassLabel):
    max_value = feature.num_classes
  elif isinstance(features_lib, features_lib.Text) and feature.vocab_size:
    max_value = feature.vocab_size
  else:
    max_value = 255

  # Generate some random values, depending on the dtype
  if tensor_info.dtype.is_integer:
    return np.random.randint(0, max_value, shape)
  elif tensor_info.dtype.is_floating:
    return np.random.random_sample(shape)
  elif tensor_info.dtype == tf.string:
    return ''.join(
        random.choice(' abcdefghij') for _ in range(random.randint(10, 20)))
  else:
    raise ValueError('Fake generation not supported for {}'.format(
        tensor_info.dtype))


def _generate_random_example(builder):
  root_feature = builder.info.features

  flat_features = root_feature._flatten(root_feature)  # pylint: disable=protected-access
  flat_tensor_info = root_feature._flatten(root_feature.get_tensor_info())  # pylint: disable=protected-access
  flat_np = [
      _generate_random_array(feature, tensor_info)
      for feature, tensor_info in zip(flat_features, flat_tensor_info)
  ]
  return root_feature._nest(flat_np)  # pylint: disable=protected-access

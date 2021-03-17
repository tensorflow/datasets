# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import contextlib
import enum
import functools
import os
import random
from typing import Callable, Iterator, Optional
from unittest import mock

from absl import logging
import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import load
from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.testing import test_utils


class MockPolicy(enum.Enum):
  """Strategy to use with `tfds.testing.mock_data` to mock the dataset.

  Attributes:
    AUTO: Try `USE_FILES`, and fallback to `USE_CODE` if the metadata files
      (`dataset_info.json`,...) are not found.
    USE_FILES: Load dataset from the metadata files (present in the `data_dir`
      kwarg of `tfds.testing.mock_data`, raise error if data_dir is not
      reachable.
    USE_CODE: Load the data from the original dataset generation class. Do
      not use any generated files. More is more convenient but less
      safe than `USE_FILES`. Not all features might be available (e.g. no
      split-names).
  """
  AUTO = enum.auto()
  USE_CODE = enum.auto()
  USE_FILES = enum.auto()


@contextlib.contextmanager
def mock_data(
    num_examples: int = 1,
    *,
    policy: MockPolicy = MockPolicy.AUTO,
    as_dataset_fn: Optional[Callable[..., tf.data.Dataset]] = None,
    data_dir: Optional[str] = None,
) -> Iterator[None]:
  """Mock tfds to generate random data.

  ### Usage

  * Usage (automated):

  ```py
  with tfds.testing.mock_data(num_examples=5):
    ds = tfds.load('some_dataset', split='train')

    for ex in ds:  # ds will yield randomly generated examples.
      ex
  ```

  * Usage (manual):

  For more control over the generated examples, you can
  manually overwrite the `DatasetBuilder._as_dataset` method:

  ```py
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

  ### Policy

  For improved results, you can copy the true metadata files
  (`dataset_info.json`, `label.txt`, vocabulary files) in
  `data_dir/dataset_name/version`. This will allow the mocked dataset to use
  the true metadata computed during generation (split names,...).

  If metadata files are not found, then info from the original class will be
  used, but the features computed during generation won't be available (e.g.
  unknown split names, so any splits are accepted).

  ### Miscellaneous

  * The examples are deterministically generated. Train and test split will
    yield the same examples.
  * The actual examples will be randomly generated using
    `builder.info.features.get_tensor_info()`.
  * Download and prepare step will always be a no-op.
  * Warning: `info.split['train'].num_examples` won't match
    `len(list(ds_train))`

  Some of those points could be improved. If you have suggestions, issues with
  this functions, please open a new issue on our Github.

  Args:
    num_examples: number of fake example to generate.
    policy: Strategy to use to generate the fake examples. See
      `tfds.testing.MockPolicy`.
    as_dataset_fn: if provided, will replace the default random example
      generator. This function mock the `FileAdapterBuilder._as_dataset`
    data_dir: Folder containing the metadata file (searched in
      `data_dir/dataset_name/version`).
      Overwrite `data_dir` kwargs from `tfds.load`.
      Used in `MockPolicy.USE_FILES` mode.

  Yields:
    None
  """

  original_init_fn = dataset_builder.DatasetBuilder.__init__
  original_as_dataset_fn = dataset_builder.DatasetBuilder.as_dataset
  original_builder_fn = load.builder

  def mock_download_and_prepare(self, *args, **kwargs):
    """`builder.download_and_prepare` is a no-op."""
    del self, args, kwargs  # Unused

  def mock_as_dataset_base(self, **kwargs):
    """Function which overwrite `builder.as_dataset`."""
    # When `USE_FILES` is used, make sure the metadata actually exists.
    if tf.io.gfile.exists(self.data_dir):
      logging.info('Metadata found for %s at %s', self.name, self.data_dir)
    else:
      if policy == MockPolicy.USE_FILES:
        raise ValueError(
            'TFDS has been mocked with `MockPolicy.USE_FILES`, but metadata '
            f'files were not found in {self.data_dir}. '
            'You should copy the real metadata files, so that the dataset '
            'can be loaded properly, or set the data_dir kwarg of '
            'tfds.testing.mock_tfds(data_dir=...).\n'
        )
      if policy == MockPolicy.AUTO:
        logging.info(
            'Metadata NOT found for %s at %s. Will use `MockPolicy.USE_CODE.`',
            self.name,
            self.data_dir,
        )

    # Info is already restored at this point, so can mock the file system
    # safely in case of `USE_CODE` mode.
    # The only gfile access is to check `self.data_dir` existance.
    with test_utils.MockFs() as fs:
      fs.add_file(os.path.join(self.data_dir, 'tmp.txt'))
      return original_as_dataset_fn(self, **kwargs)

  def mock_as_dataset(self, split, decoders=None, read_config=None, **kwargs):
    """Function which overwrite `builder._as_dataset`."""
    del split
    del kwargs

    if decoders is None:
      generator_cls = RandomFakeGenerator
      specs = self.info.features.get_tensor_info()
      decode_fn = lambda ex: ex  # identity
    else:
      # If a decoder is passed, encode/decode the examples.
      generator_cls = EncodedRandomFakeGenerator
      specs = self.info.features.get_serialized_info()
      decode_fn = functools.partial(
          self.info.features.decode_example, decoders=decoders)

    ds = tf.data.Dataset.from_generator(
        # `from_generator` takes a callable with signature () -> iterable
        # Recreating a new generator each time ensure that all pipelines are
        # using the same examples
        lambda: generator_cls(builder=self, num_examples=num_examples),
        output_types=tf.nest.map_structure(lambda t: t.dtype, specs),
        output_shapes=tf.nest.map_structure(lambda t: t.shape, specs),
    )
    ds = ds.apply(tf.data.experimental.assert_cardinality(num_examples))
    ds.map(decode_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)

    if read_config and read_config.add_tfds_id:
      ds_id = tfrecords_reader._make_id_dataset(  # pylint: disable=protected-access
          filename=f'{self.name}-split.tfrecord-00000-of-00001',
          start_index=0,
      )
      ds = tf.data.Dataset.zip((ds, ds_id))
      ds = ds.map(lambda ex, id: {'tfds_id': id, **ex})

    return ds

  if not as_dataset_fn:
    as_dataset_fn = mock_as_dataset

  if policy == MockPolicy.USE_CODE:
    mock_data_dir = '/tmp/non-existing/tfds/data_dir/'
  elif not data_dir:
    mock_data_dir = os.path.join(os.path.dirname(__file__), 'metadata')
  else:  # AUTO or USE_FILES with explicitly given `data_dir`
    mock_data_dir = data_dir

  def mock_builder(*args, data_dir=None, **kwargs):
    del data_dir  # Unused. Inject `mock_data_dir` instead.
    return original_builder_fn(*args, data_dir=mock_data_dir, **kwargs)

  def mock_init(*args, data_dir=None, **kwargs):
    del data_dir  # Unused. Inject `mock_data_dir` instead.
    return original_init_fn(*args, data_dir=mock_data_dir, **kwargs)

  core = 'tensorflow_datasets.core'
  with contextlib.ExitStack() as stack:
    for path, mocked_fn in [
        # All GCS access should fail (is_dataset_on_gcs,...).
        (f'{core}.utils.gcs_utils.exists', lambda path: False),
        # Patch `data_dir`: `data_dir` explicitly set by users will be ignored.
        # `data_dir` is used at two places:
        # * `tfds.builder` to search read-only datasets loaded from config.
        # * `DatasetBuilder.__init__` otherwise
        (f'{core}.dataset_builder.DatasetBuilder.__init__', mock_init),
        (f'{core}.load.builder', mock_builder),
        # Patch DatasetBuilder
        (
            f'{core}.dataset_builder.DatasetBuilder.download_and_prepare',
            mock_download_and_prepare,
        ),
        (
            f'{core}.dataset_builder.DatasetBuilder.as_dataset',
            mock_as_dataset_base,
        ),
        (
            f'{core}.dataset_builder.FileReaderBuilder._as_dataset',
            as_dataset_fn,
        ),
    ]:
      stack.enter_context(mock.patch(path, mocked_fn))
    # We patch `tfds.builder` alias separatelly, as the alias only exists
    # when the public `__init__` API is imported.
    try:
      stack.enter_context(
          mock.patch('tensorflow_datasets.builder', mock_builder),
      )
    except AttributeError:
      pass
    yield


class RandomFakeGenerator(object):
  """Generator of fake examples randomly and deterministically generated."""

  def __init__(self, builder, num_examples, seed=0):
    self._rgn = np.random.RandomState(seed)  # Could use the split name as seed
    self._py_rng = random.Random(seed)
    self._builder = builder
    self._num_examples = num_examples

  def _generate_random_array(self, feature, tensor_info):
    """Generates a random tensor for a single feature."""
    # TODO(tfds): Could improve the fake generatiion:
    # * Use the feature statistics (min, max)
    # * For Sequence features
    # * For Text
    shape = [  # Fill dynamic shape with random values
        self._rgn.randint(5, 50) if s is None else s
        for s in tensor_info.shape
    ]
    if isinstance(feature, features_lib.ClassLabel):
      max_value = feature.num_classes
    elif isinstance(feature, features_lib.Text) and feature.vocab_size:
      max_value = feature.vocab_size
    else:
      max_value = 255

    # We cast the data to make sure `encode_example` don't raise errors
    dtype = tensor_info.dtype
    # Generate some random values, depending on the dtype
    if dtype.is_integer:
      return self._rgn.randint(0, max_value, shape).astype(dtype.as_numpy_dtype)
    elif dtype.is_floating:
      return self._rgn.random_sample(shape).astype(dtype.as_numpy_dtype)
    elif dtype.is_bool:
      return (self._rgn.random_sample(shape) < .5).astype(dtype.as_numpy_dtype)
    elif dtype == tf.string:
      return ''.join(
          self._py_rng.choice(' abcdefghij')
          for _ in range(self._py_rng.randint(10, 20))
      )
    raise ValueError('Fake generation not supported for {}'.format(dtype))

  def _generate_example(self):
    """Generate the next example."""
    root_feature = self._builder.info.features
    flat_features = root_feature._flatten(root_feature)  # pylint: disable=protected-access
    flat_tensor_info = root_feature._flatten(root_feature.get_tensor_info())  # pylint: disable=protected-access
    flat_np = [
        self._generate_random_array(feature, tensor_info)
        for feature, tensor_info in zip(flat_features, flat_tensor_info)
    ]
    return root_feature._nest(flat_np)  # pylint: disable=protected-access

  def __iter__(self):
    """Yields all fake examples."""
    for _ in range(self._num_examples):
      yield self._generate_example()


class EncodedRandomFakeGenerator(RandomFakeGenerator):
  """Generator of fake encoded examples."""

  def __iter__(self):
    """Yields all fake examples."""
    for ex in super(EncodedRandomFakeGenerator, self).__iter__():
      yield self._builder.info.features.encode_example(ex)

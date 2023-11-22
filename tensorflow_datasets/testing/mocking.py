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

"""Mock util for tfds."""

from __future__ import annotations

import contextlib
import enum
import functools
import os
from typing import Any, Callable, Iterator, Optional, Sequence
from unittest import mock

from absl import logging
from etils import epath
import numpy as np
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import reader as reader_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.data_sources import array_record
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import tree_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.testing import test_utils


def _get_fake_data_components(decoders, features):
  """Gets all the components to generate fake data in the tests.

  Args:
    decoders: The decoders to override, or `None` if no decoding is used.
    features: The original features.

  Returns:
    A tuple with the data generator class, the features, the feature specs and
      the decode function.
  """
  # Partial decoding
  if isinstance(decoders, decode.PartialDecoding):
    # TODO(epot): Should be moved inside `features.decode_example`
    features = decoders.extract_features(features)
    decoders = decoders.decoders
  # Full decoding (all features decoded)
  else:
    decoders = decoders  # pylint: disable=self-assigning-variable

  has_nested_dataset = any(
      isinstance(f, features_lib.Dataset) for f in features._flatten(features)  # pylint: disable=protected-access
  )
  if decoders is not None or has_nested_dataset:
    # If a decoder is passed, encode/decode the examples.
    generator_cls = EncodedRandomFakeGenerator
    specs = features.get_serialized_info()
    decode_fn = functools.partial(features.decode_example, decoders=decoders)
  else:
    generator_cls = RandomFakeGenerator
    specs = features.get_tensor_info()
    decode_fn = lambda ex: ex  # identity
  return generator_cls, features, specs, decode_fn


class PickableDataSourceMock(mock.MagicMock):
  """Makes MagicMock pickable in order to work with multiprocessing in Grain."""

  def __getstate__(self):
    return {'num_examples': len(self), 'generator': self._generator}

  def __setstate__(self, state):
    num_examples, generator = state['num_examples'], state['generator']
    self.__len__.return_value = num_examples
    self.__getitem__ = functools.partial(_getitem, generator=generator)
    self.__getitems__ = functools.partial(_getitems, generator=generator)

  def __reduce__(self):
    return (PickableDataSourceMock, (), self.__getstate__())


def _getitem(self, record_key: int, generator: RandomFakeGenerator) -> Any:
  """Function to overwrite __getitem__ in data sources."""
  del self
  return generator[record_key]


def _getitems(
    self, record_keys: Sequence[int], generator: RandomFakeGenerator
) -> Sequence[Any]:
  """Function to overwrite __getitems__ in data sources."""
  del self
  return [generator[record_key] for record_key in record_keys]


def _deserialize_example_np(serialized_example, *, decoders=None):
  """Function to overwrite dataset_info.features.deserialize_example_np.

  Warning: this has to be defined in the outer scope in order for the function
  to be pickable.

  Args:
    serialized_example: the example to deserialize.
    decoders: optional decoders.

  Returns:
    The serialized example, because deserialization is taken care by
      RandomFakeGenerator.
  """
  del decoders
  return serialized_example


class MockPolicy(enum.Enum):
  """Strategy to use with `tfds.testing.mock_data` to mock the dataset.

  Attributes:
    AUTO: Try `USE_FILES`, and fallback to `USE_CODE` if the metadata files
      (`dataset_info.json`,...) are not found.
    USE_FILES: Load dataset from the metadata files (present in the `data_dir`
      kwarg of `tfds.testing.mock_data`, raise error if data_dir is not
      reachable.
    USE_CODE: Load the data from the original dataset generation class. Do not
      use any generated files. More is more convenient but less safe than
      `USE_FILES`. Not all features might be available (e.g. no split-names).
  """

  AUTO = enum.auto()
  USE_CODE = enum.auto()
  USE_FILES = enum.auto()


@contextlib.contextmanager
def mock_data(
    num_examples: int = 1,
    num_sub_examples: int = 1,
    max_value: Optional[int] = None,
    *,
    policy: MockPolicy = MockPolicy.AUTO,
    as_dataset_fn: Optional[Callable[..., tf.data.Dataset]] = None,
    data_dir: Optional[str] = None,
    mock_array_record_data_source: Optional[PickableDataSourceMock] = None,
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

  All calls to `tfds.load`/`tfds.data_source` within the context manager then
  return deterministic mocked data.

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
    num_examples: Number of fake example to generate.
    num_sub_examples: Number of examples to generate in nested Dataset features.
    max_value: The maximum value present in generated tensors; if max_value is
      None or it is set to 0, then random numbers are generated from the range
      from 0 to 255.
    policy: Strategy to use to generate the fake examples. See
      `tfds.testing.MockPolicy`.
    as_dataset_fn: If provided, will replace the default random example
      generator. This function mock the `FileAdapterBuilder._as_dataset`
    data_dir: Folder containing the metadata file (searched in
      `data_dir/dataset_name/version`). Overwrite `data_dir` kwargs from
      `tfds.load`. Used in `MockPolicy.USE_FILES` mode.
    mock_array_record_data_source: Overwrite a mock for the underlying
      ArrayRecord data source if it is used. Note: If used the same mock will be
      used for all data sources loaded within this context.

  Yields:
    None
  """

  original_init_fn = dataset_builder.DatasetBuilder.__init__
  original_as_dataset_fn = dataset_builder.DatasetBuilder.as_dataset
  original_builder_from_files = read_only_builder.builder_from_files
  if mock_array_record_data_source and not isinstance(
      mock_array_record_data_source, PickableDataSourceMock
  ):
    raise ValueError(
        '`mock_array_record_data_source` must be a'
        ' `tfds.testing.PickableDataSourceMock` because it must be pickable.'
    )

  def mock_download_and_prepare(self, *args, **kwargs):
    """`builder.download_and_prepare` is a no-op."""
    del self, args, kwargs  # Unused

  def _check_policy(self) -> MockPolicy:
    """Checks the policy and returns the actual used policy for mocking."""
    # When `USE_FILES` is used, make sure the metadata actually exists.
    if epath.Path(self.data_dir).exists():
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
        return MockPolicy.USE_CODE
    return policy

  def mock_as_dataset_base(self, **kwargs):
    """Mocks `builder.as_dataset`."""
    _check_policy(self)

    # Info is already restored at this point, so can mock the file system
    # safely in case of `USE_CODE` mode.
    # The only gfile access is to check `self.data_dir` existance.
    with test_utils.MockFs() as fs:
      fs.add_file(os.path.join(self.data_dir, 'tmp.txt'))
      return original_as_dataset_fn(self, **kwargs)

  def mock_as_dataset(self, split, decoders=None, read_config=None, **kwargs):
    """Mocks `builder._as_dataset`."""
    del kwargs

    generator_cls, features, specs, decode_fn = _get_fake_data_components(
        decoders, self.info.features
    )

    ds = tf.data.Dataset.from_generator(
        # `from_generator` takes a callable with signature () -> iterable
        # Recreating a new generator each time ensure that all pipelines are
        # using the same examples
        functools.partial(
            generator_cls,
            features=features,
            num_examples=num_examples,
            num_sub_examples=num_sub_examples,
            max_value=max_value,
        ),
        # pylint: enable=g-long-lambda]
        output_types=tf.nest.map_structure(lambda t: t.dtype, specs),
        output_shapes=tf.nest.map_structure(lambda t: t.shape, specs),
    )
    ds = ds.apply(tf.data.experimental.assert_cardinality(num_examples))
    ds = ds.map(decode_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)

    if read_config and read_config.add_tfds_id:
      ds_id = reader_lib._make_id_dataset(  # pylint: disable=protected-access
          filename=f'{self.name}-{split}.tfrecord-00000-of-00001',
          start_index=0,  # pytype: disable=wrong-arg-types
      )
      ds = tf.data.Dataset.zip((ds, ds_id))
      ds = ds.map(lambda ex, id: {'tfds_id': id, **ex})

    return ds

  def mock_as_data_source(self, split, decoders=None, **kwargs):
    """Mocks `builder.as_data_source`."""
    del kwargs
    nonlocal mock_array_record_data_source
    mock_data_source = mock_array_record_data_source or PickableDataSourceMock()
    actual_policy = _check_policy(self)
    if split is None:
      split = {s: s for s in self.info.splits}

    generator_cls, features, _, _ = _get_fake_data_components(
        decoders, self.info.features
    )
    generator = generator_cls(features, num_examples)

    if actual_policy == MockPolicy.USE_CODE:
      # Mock `SplitDict`, because splits are not known in advance.
      split_dict = mock.MagicMock(spec=splits_lib.SplitDict)
    else:
      # Use the real `SplitDict`.
      split_dict = splits_lib.SplitDict
    with mock.patch.object(
        splits_lib,
        'SplitDict',
        new=split_dict,
    ), mock.patch(
        'array_record.python.array_record_data_source.ArrayRecordDataSource',
        mock_data_source,
    ), mock.patch(
        'tensorflow_datasets.core.dataset_info.DatasetInfo.file_format',
        new_callable=mock.PropertyMock,
        # Force ARRAY_RECORD as the default file_format.
        return_value=file_adapters.FileFormat.ARRAY_RECORD,
    ):
      self.info.features.deserialize_example_np = _deserialize_example_np
      mock_data_source.return_value.__len__.return_value = num_examples
      mock_data_source.return_value._generator = (  # pylint:disable=protected-access
          generator
      )
      mock_data_source.return_value.__getitem__ = functools.partial(
          _getitem, generator=generator
      )
      mock_data_source.return_value.__getitems__ = functools.partial(
          _getitems, generator=generator
      )

      def build_single_data_source(split):
        single_data_source = array_record.ArrayRecordDataSource(
            dataset_info=self.info, split=split, decoders=decoders
        )
        return single_data_source

      return tree_utils.map_structure(build_single_data_source, split)

  if not as_dataset_fn:
    as_dataset_fn = mock_as_dataset

  if policy == MockPolicy.USE_CODE:
    mock_data_dir = '/tmp/non-existing/tfds/data_dir/'
  elif not data_dir:
    mock_data_dir = os.path.join(os.path.dirname(__file__), 'metadata')
  else:  # AUTO or USE_FILES with explicitly given `data_dir`
    mock_data_dir = data_dir

  def mock_init(*args, data_dir=None, **kwargs):
    del data_dir  # Unused. Inject `mock_data_dir` instead.
    return original_init_fn(*args, data_dir=mock_data_dir, **kwargs)

  def new_builder_from_files(*args, **kwargs):
    # Replace the user-given data dir by the mocked one
    kwargs.pop('data_dir', None)
    # `DatasetBuilder.__init__` is mocked above to inject the wrong data_dir.
    # So we restore the original `DatasetBuilder.__init__` inside
    # `builder_from_files` calls.
    with mock.patch(
        f'{core}.dataset_builder.DatasetBuilder.__init__', original_init_fn
    ):
      return original_builder_from_files(
          *args, data_dir=mock_data_dir, **kwargs
      )

  core = 'tensorflow_datasets.core'
  with contextlib.ExitStack() as stack:
    for path, mocked_fn in [
        # All GCS access should fail (is_dataset_on_gcs,...).
        (f'{core}.utils.gcs_utils.exists', lambda path: False),
        # Patch `data_dir`: `data_dir` explicitly set by users will be ignored.
        # `data_dir` is used at two places:
        # * `builder_from_files` to search read-only datasets loaded from config
        # * `DatasetBuilder.__init__` otherwise
        (f'{core}.dataset_builder.DatasetBuilder.__init__', mock_init),
        (
            f'{core}.read_only_builder.builder_from_files',
            new_builder_from_files,
        ),
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
            f'{core}.dataset_builder.DatasetBuilder.as_data_source',
            mock_as_data_source,
        ),
        (
            f'{core}.dataset_builder.FileReaderBuilder._as_dataset',
            as_dataset_fn,
        ),
    ]:
      stack.enter_context(mock.patch(path, mocked_fn))
    yield


class RandomFakeGenerator(object):
  """Generator of fake examples randomly and deterministically generated."""

  def __init__(
      self,
      features,
      num_examples: int,
      num_sub_examples: int = 1,
      max_value: Optional[int] = None,
      constant_dynamic_shape: bool = False,
      seed: int = 0,
  ):
    self._seed = seed
    self._features = features
    self._num_examples = num_examples
    self._num_sub_examples = num_sub_examples
    self._max_value = max_value
    self._constant_dynamic_shape = constant_dynamic_shape

  def _generate_random_string_array(self, shape, rng):
    """Generates an array of random strings."""

    def rand_str():
      return ''.join(
          rng.choice(list(' abcdefghij'), size=(rng.integers(low=10, high=20)))
      )

    if not shape:
      return rand_str()

    return np.array(
        [rand_str() for _ in range(np.prod(shape, dtype=np.int32))]
    ).reshape(shape)

  def _generate_random_obj(self, feature, tensor_info, rng):
    """Generates a random tensor for a single feature."""
    # TODO(tfds): Could improve the fake generatiion:
    # * Use the feature statistics (min, max)
    # * For Sequence features
    # * For Text

    # First we deal with the case of sub-datasets:
    if isinstance(feature, features_lib.Dataset):
      # For sub-datasets self._num_sub_examples examples are generated.
      generator = RandomFakeGenerator(
          feature.feature,
          num_examples=self._num_sub_examples,
          num_sub_examples=1,
          max_value=self._max_value,
      )
      # Returns the list of examples in the nested dataset.
      return list(generator)

    if self._constant_dynamic_shape:
      shape = [10 if s is None else s for s in tensor_info.shape]
    else:
      shape = [  # Fill dynamic shape with random values
          rng.integers(low=5, high=50) if s is None else s
          for s in tensor_info.shape
      ]
    if isinstance(feature, features_lib.ClassLabel):
      max_value = feature.num_classes
    elif isinstance(feature, features_lib.Text) and feature.vocab_size:
      max_value = feature.vocab_size
    elif self._max_value:
      max_value = self._max_value
    else:
      max_value = 255

    # We cast the data to make sure `encode_example` don't raise errors
    dtype = tensor_info.np_dtype
    # Generate some random values, depending on the dtype
    if dtype_utils.is_integer(dtype):
      return rng.integers(0, max_value, size=shape).astype(dtype)
    elif dtype_utils.is_floating(dtype):
      return rng.random(size=shape).astype(dtype)
    elif dtype_utils.is_bool(dtype):
      return (rng.random(size=shape) < 0.5).astype(dtype)
    elif dtype_utils.is_string(dtype):
      return self._generate_random_string_array(shape, rng)
    raise ValueError('Fake generation not supported for {}'.format(dtype))

  def _generate_example(self, rng):
    """Generates the next example."""
    root_feature = self._features
    flat_features = root_feature._flatten(root_feature)  # pylint: disable=protected-access
    flat_tensor_info = root_feature._flatten(root_feature.get_tensor_info())  # pylint: disable=protected-access
    flat_objs = [
        self._generate_random_obj(feature, tensor_info, rng)
        for feature, tensor_info in zip(flat_features, flat_tensor_info)
    ]
    return root_feature._nest(flat_objs)  # pylint: disable=protected-access

  def __iter__(self):
    """Yields all fake examples deterministically."""
    rng = np.random.default_rng(self._seed)
    for _ in range(self._num_examples):
      yield self._generate_example(rng)

  def __getitem__(self, index: int):
    """Returns a single fake example deterministically."""
    rng = np.random.default_rng(self._seed + index)
    return self._generate_example(rng)


class EncodedRandomFakeGenerator(RandomFakeGenerator):
  """Generator of fake encoded examples."""

  def __iter__(self):
    """Yields all fake examples."""
    for ex in super().__iter__():
      yield self._features.encode_example(ex)

  def __getitem__(self, index: int):
    decoded_example = super().__getitem__(index)
    return self._features.encode_example(decoded_example)


class SerializedRandomFakeGenerator(RandomFakeGenerator):
  """Generator of fake serialized examples."""

  def __iter__(self):
    """Yields all fake examples."""
    for ex in super().__iter__():
      yield self._features.serialize_example(ex)

  def __getitem__(self, index: int):
    example = super().__getitem__(index)
    return self._features.serialize_example(example)

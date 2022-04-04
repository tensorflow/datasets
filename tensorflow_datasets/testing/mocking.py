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

"""Mock util for tfds."""

import contextlib
import dataclasses
import enum
import functools
import os
from typing import Any, Callable, Iterator, List, Mapping, MutableMapping, Optional
from unittest import mock

from absl import logging
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.testing import test_utils
from typing_extensions import Protocol

TreeDict = type_utils.TreeDict


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


def random_shape(shape, rgn: np.random.RandomState):
  if not shape:
    return []
  # Fill dynamic shape with random values
  return [rgn.randint(5, 50) if s is None else s for s in shape]


class DataFactory(Protocol):

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    raise NotImplementedError


@contextlib.contextmanager
def mock_data(
    num_examples: int = 1,
    num_sub_examples: int = 1,
    *,
    policy: MockPolicy = MockPolicy.AUTO,
    as_dataset_fn: Optional[Callable[..., tf.data.Dataset]] = None,
    data_dir: Optional[str] = None,
    custom_factories: Optional[Mapping[str, DataFactory]] = None,
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
    num_examples: Number of fake example to generate.
    num_sub_examples: Number of examples to generate in nested Dataset features.
    policy: Strategy to use to generate the fake examples. See
      `tfds.testing.MockPolicy`.
    as_dataset_fn: If provided, will replace the default random example
      generator. This function mock the `FileAdapterBuilder._as_dataset`
    data_dir: Folder containing the metadata file (searched in
      `data_dir/dataset_name/version`). Overwrite `data_dir` kwargs from
      `tfds.load`. Used in `MockPolicy.USE_FILES` mode.
    custom_factories: Mapping between feature name and custom random data
      factories. If no data factory is provided, a default one is used.

  Yields:
    None
  """

  original_init_fn = dataset_builder.DatasetBuilder.__init__
  original_as_dataset_fn = dataset_builder.DatasetBuilder.as_dataset
  original_builder_from_files = read_only_builder.builder_from_files

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
    del kwargs

    # Partial decoding
    if isinstance(decoders, decode.PartialDecoding):
      # TODO(epot): Should be moved inside `features.decode_example`
      features = decoders.extract_features(self.info.features)
      decoders = decoders.decoders
    # Full decoding (all features decoded)
    else:
      features = self.info.features
      decoders = decoders  # pylint: disable=self-assigning-variable

    has_nested_dataset = any(
        isinstance(f, features_lib.Dataset)
        for f in features._flatten(features))  # pylint: disable=protected-access
    if decoders is not None or has_nested_dataset:
      # If a decoder is passed, encode/decode the examples.
      generator_cls = EncodedRandomFakeGenerator
      specs = features.get_serialized_info()
      decode_fn = functools.partial(features.decode_example, decoders=decoders)
    else:
      generator_cls = RandomFakeGenerator
      specs = features.get_tensor_info()
      decode_fn = lambda ex: ex  # identity

    ds = tf.data.Dataset.from_generator(
        # `from_generator` takes a callable with signature () -> iterable
        # Recreating a new generator each time ensure that all pipelines are
        # using the same examples
        # pylint: disable=g-long-lambda]
        lambda: generator_cls(
            features=features,
            num_examples=num_examples,
            num_sub_examples=num_sub_examples,
            custom_factories=custom_factories),
        # pylint: enable=g-long-lambda]
        output_signature=tf.nest.map_structure(
            lambda t: tf.TensorSpec(shape=t.shape, dtype=t.dtype), specs),
    )
    ds = ds.apply(tf.data.experimental.assert_cardinality(num_examples))
    ds = ds.map(decode_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)

    if read_config and read_config.add_tfds_id:
      ds_id = tfrecords_reader._make_id_dataset(  # pylint: disable=protected-access
          filename=f'{self.name}-{split}.tfrecord-00000-of-00001',
          start_index=0,  # pytype: disable=wrong-arg-types
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

  def mock_init(*args, data_dir=None, **kwargs):
    del data_dir  # Unused. Inject `mock_data_dir` instead.
    return original_init_fn(*args, data_dir=mock_data_dir, **kwargs)

  def new_builder_from_files(*args, **kwargs):
    # Replace the user-given data dir by the mocked one
    kwargs.pop('data_dir', None)
    # `DatasetBuilder.__init__` is mocked above to inject the wrong data_dir.
    # So we restore the original `DatasetBuilder.__init__` inside
    # `builder_from_files` calls.
    with mock.patch(f'{core}.dataset_builder.DatasetBuilder.__init__',
                    original_init_fn):
      return original_builder_from_files(
          *args, data_dir=mock_data_dir, **kwargs)

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
            f'{core}.dataset_builder.FileReaderBuilder._as_dataset',
            as_dataset_fn,
        ),
    ]:
      stack.enter_context(mock.patch(path, mocked_fn))
    yield


@dataclasses.dataclass
class SpecificValueFactory(DataFactory):
  """Randomly picks elements from a given list."""
  allowed_values: List[Any]

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    shape = random_shape(tensor_spec.shape, rgn)
    return rgn.choice(
        self.allowed_values,
        size=shape).astype(tensor_spec.dtype.as_numpy_dtype)


@dataclasses.dataclass
class IntInRangeFactory(DataFactory):
  """Generates integers in a specified range."""
  min_value: int = 0
  max_value: int = 255

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    shape = random_shape(tensor_spec.shape, rgn)
    return rgn.randint(self.min_value, self.max_value,
                       shape).astype(tensor_spec.dtype.as_numpy_dtype)


@dataclasses.dataclass
class StringFactory(DataFactory):
  """Random string generator."""
  min_chars: int = 10
  max_chars: int = 20
  allowable_chars: List[str] = dataclasses.field(
      default_factory=lambda: list(' abcdefghij'))

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    """Generates an array of random strings."""

    def rand_str():
      size = rgn.randint(self.min_chars, self.max_chars)
      return ''.join(rgn.choice(self.allowable_chars, size=size))

    if not tensor_spec.shape:
      return rand_str()

    shape = random_shape(tensor_spec.shape, rgn)
    return np.array([rand_str() for _ in range(np.prod(shape, dtype=np.int32))
                    ]).reshape(shape)


@dataclasses.dataclass
class FloatFactory(DataFactory):
  """Generates random floats in the half-open interval [0.0, 1.0)."""

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    shape = random_shape(tensor_spec.shape, rgn)
    return rgn.random_sample(shape).astype(tensor_spec.dtype.as_numpy_dtype)


@dataclasses.dataclass
class BoolFactory(DataFactory):

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    shape = random_shape(tensor_spec.shape, rgn)
    return rgn.choice([True, False],
                      size=shape).astype(tensor_spec.dtype.as_numpy_dtype)


@dataclasses.dataclass
class FeatureFactory:
  tensor_spec: tf.TensorSpec
  data_factory: DataFactory

  def generate(self, rgn: np.random.RandomState) -> Any:
    return self.data_factory(tensor_spec=self.tensor_spec, rgn=rgn)


class SequenceFactory(DataFactory):
  """Factory for Sequences."""

  def __init__(self,
               features: features_lib.FeaturesDict,
               num_sub_examples: int = 1,
               custom_factories: Optional[Mapping[str, DataFactory]] = None):
    self._features = features
    self._num_sub_examples = num_sub_examples
    custom_factories = custom_factories or {}
    self._feature_factories = {}
    tensor_info_dict = self._features.get_tensor_info()
    for feature_name, feature in self._features.items():
      data_factory = custom_factories.get(
          feature_name,
          data_factory_for(
              feature,
              num_sub_examples=num_sub_examples,
              custom_factories=custom_factories))
      self._feature_factories[feature_name] = FeatureFactory(
          tensor_info_dict[feature_name], data_factory)
    super().__init__()

  def generate_example(self,
                       rgn: np.random.RandomState) -> MutableMapping[str, Any]:
    return {
        feature_name: feature_factory.generate(rgn)
        for feature_name, feature_factory in self._feature_factories.items()
    }

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    return self.generate_example(rgn)


class DatasetFactory(SequenceFactory):
  """Factory for datasets."""

  def __call__(self, tensor_spec: tf.TensorSpec,
               rgn: np.random.RandomState) -> Any:
    return [self.generate_example(rgn) for _ in range(self._num_sub_examples)]


def data_factory_for(
    feature: features_lib.FeatureConnector,
    num_sub_examples: int = 1,
    custom_factories: Optional[Mapping[str,
                                       DataFactory]] = None) -> DataFactory:
  """Creates the data factory for the given feature.

  If a custom factory is specified for the feature, then that factory is used.

  Args:
    feature: the feature or feature dictionary for which to create the factory.
    num_sub_examples: how many examples should be created for nested feature.
    custom_factories: allows specifying custom factories for features, even if
      the features are nested.

  Returns:
    A data factory that can generate random data for the given feature.
  """
  if isinstance(feature, features_lib.Dataset):
    return DatasetFactory(
        feature,
        num_sub_examples=num_sub_examples,
        custom_factories=custom_factories)
  if isinstance(feature, features_lib.Sequence):
    return SequenceFactory(
        feature,
        num_sub_examples=num_sub_examples,
        custom_factories=custom_factories)

  if isinstance(feature, features_lib.ClassLabel):
    return IntInRangeFactory(max_value=feature.num_classes)
  if isinstance(feature, features_lib.Text) and feature.vocab_size:
    return IntInRangeFactory(max_value=feature.vocab_size)

  dtype = feature.get_tensor_info().dtype
  if dtype.is_integer:
    return IntInRangeFactory()
  elif dtype.is_floating:
    return FloatFactory()
  elif dtype.is_bool:
    return BoolFactory()
  elif dtype == tf.string:
    return StringFactory()
  raise ValueError('Fake generation not supported for {}'.format(dtype))


class RandomFakeGenerator(object):
  """Generator of fake examples randomly and deterministically generated."""

  def __init__(
      self,
      features,
      num_examples: int,
      num_sub_examples: int = 1,
      seed: int = 0,
      custom_factories: Optional[Mapping[str, DataFactory]] = None,
  ):
    self._data_generator = DatasetFactory(
        features,
        num_sub_examples=num_sub_examples,
        custom_factories=custom_factories)
    self._rgn = np.random.RandomState(seed)  # Could use the split name as seed
    self._features = features
    self._num_examples = num_examples
    self._num_sub_examples = num_sub_examples

  def __iter__(self):
    """Yields all fake examples."""
    for _ in range(self._num_examples):
      example = self._data_generator.generate_example(rgn=self._rgn)
      yield example


class EncodedRandomFakeGenerator(RandomFakeGenerator):
  """Generator of fake encoded examples."""

  def __iter__(self):
    """Yields all fake examples."""
    for ex in super(EncodedRandomFakeGenerator, self).__iter__():
      yield self._features.encode_example(ex)

# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""DatasetBuilder base class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import collections
import os
import enum

import six
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download_manager as download_manager_lib
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered

__all__ = [
    "Split",
    "SplitFiles",
    "DatasetBuilder",
    "SplitGenerator",
    "GeneratorBasedDatasetBuilder",
]


class Split(enum.Enum):
  """`Enum` for dataset splits.

  Datasets are typically split into different subsets to be used at various
  stages of training and evaluation. All datasets have at least the `TRAIN` and
  `TEST` splits.

  Note that for datasets without a `VALIDATION` split, you should use a fraction
  of the `TRAIN` data for evaluation as you iterate on your model so as not to
  overfit to the `TEST` data. You can do so by...

  TODO(rsepassi): update when as_dataset supports this.

  * `TRAIN`: the training data.
  * `VALIDATION`: the validation data. If present, this is typically used as
    evaluation data while iterating on a model (e.g. changing hyperparameters,
    model architecture, etc.).
  * `TEST`: the testing data. This is the data to report metrics on. Typically
    you do not want to use this during model iteration as you may overfit to it.
  """
  TRAIN = "train"
  VALIDATION = "validation"
  TEST = "test"


class SplitFiles(object):
  """Utility to produce filepaths and filepatterns for a Split."""

  def __init__(self, dataset_name, split, num_shards, data_dir,
               filetype_suffix=None):
    """Constructs a SplitFiles object.

    Args:
      dataset_name (str): name of the dataset. Typically `DatasetBuilder.name`.
      split (Split): which split of the dataset.
      num_shards (int): number of file shards for this split on disk.
      data_dir (str): directory containing the data files.
      filetype_suffix (str): if provided, will be added to the filenames before
        the sharding specification (e.g.
        "foo_dataset-train.csv-00000-of-00001").
    """
    self.dataset_name = dataset_name
    self.split = split
    self.num_shards = num_shards
    self.data_dir = data_dir
    self.filetype_suffix = filetype_suffix

  @property
  def filepaths(self):
    """Returns list of filepaths for this split."""
    return naming.filepaths_for_dataset_split(
        dataset_name=self.dataset_name,
        split=self.split,
        num_shards=self.num_shards,
        data_dir=self.data_dir,
        filetype_suffix=self.filetype_suffix)

  @property
  def filepattern(self):
    """Returns a Glob filepattern for this split."""
    return naming.filepattern_for_dataset_split(
        dataset_name=self.dataset_name,
        split=self.split,
        data_dir=self.data_dir,
        filetype_suffix=self.filetype_suffix)

  def exists(self):
    return file_format_adapter.do_files_exist(self.filepaths)


# TODO(rsepassi): Add info() property
@six.add_metaclass(registered.RegisteredDataset)
class DatasetBuilder(object):
  """Abstract base class for datasets.

  Typical usage:

  ```python
  mnist_builder = tfds.MNIST(data_dir="~/tfds_data")
  mnist_builder.download_and_prepare()
  train_dataset = mnist_builder.as_dataset(tfds.Split.TRAIN)
  assert isinstance(train_dataset, tf.data.Dataset)

  # And then the rest of your input pipeline
  train_dataset = train_dataset.repeat().shuffle(1024).batch(128).prefetch(4)
  features = train_dataset.make_one_shot_iterator().get_next()
  image, label = features['input'], features['target']
  ```
  """

  @api_utils.disallow_positional_args
  def __init__(self, data_dir=api_utils.REQUIRED_ARG, download_manager=None):
    """Construct a DatasetBuilder.

    Callers must pass arguments as keyword arguments.

    Args:
      data_dir (str): directory to read/write data.
      download_manager (DownloadManager): manager to download and extract data.
        Optional, useful for testing.
    """
    self._data_dir = os.path.expanduser(data_dir)
    self._download_manager = (
        download_manager or
        download_manager_lib.DownloadManager(
            download_dir=os.path.join(
                download_manager_lib.DEFAULT_DOWNLOAD_DIR, self.name)))

  @api_utils.disallow_positional_args
  def download_and_prepare(self):
    """Downloads and prepares dataset for reading.

    Subclasses must override _download_and_prepare.
    """
    self._download_and_prepare()

  # TODO(rsepassi): Make it easy to further shard the TRAIN data (e.g. for
  # synthetic VALIDATION splits).
  @api_utils.disallow_positional_args
  def as_dataset(self, split, shuffle_files=None):
    """Constructs a `tf.data.Dataset`.

    Callers must pass arguments as keyword arguments.

    Subclasses must override _as_dataset.

    Args:
      split (`tfds.Split`): which subset of the data to read.
      shuffle_files (bool): whether to shuffle the input files. Optional,
        defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.

    Returns:
      `tf.data.Dataset`
    """
    return self._as_dataset(split=split, shuffle_files=shuffle_files)

  def numpy_iterator(self, **as_dataset_kwargs):
    """Generates numpy elements from the given `tfds.Split`.

    This generator can be useful for non-TensorFlow programs.

    Args:
      **as_dataset_kwargs: Keyword arguments passed on to
        `tfds.DatasetBuilder.as_dataset`.

    Returns:
      Generator yielding feature dictionaries
      `dict<str feature_name, numpy.array feature_val>`.
    """
    def iterate():
      dataset = self.as_dataset(**as_dataset_kwargs)
      dataset = dataset.prefetch(128)
      return dataset_utils.iterate_over_dataset(dataset)

    if tf.executing_eagerly():
      return iterate()
    else:
      with tf.Graph().as_default():
        return iterate()

  def _split_files(self, **kwargs):
    kwargs["dataset_name"] = self.name
    kwargs["data_dir"] = self._data_dir
    return SplitFiles(**kwargs)

  @abc.abstractmethod
  def _download_and_prepare(self):
    raise NotImplementedError

  @abc.abstractmethod
  def _as_dataset(self, split, shuffle_files=None):
    raise NotImplementedError


class SplitGenerator(collections.namedtuple("_SplitGenerator",
                                            ["generator_fn", "split_files"])):
  """Contains a generator to produce examples across splits.

  Args:
    generator_fn: function with no arguments yielding feature dictionaries.
    split_files (list<SplitFiles>): splits that the examples from `generator_fn`
      should be sharded across.
  """

  def output_files_exist(self):
    """Whether all the specified output files exist."""
    return all([split.exists() for split in self.split_files])

  @property
  def output_files(self):
    """Output files combined across `split_files`."""
    output_files = []
    for split in self.split_files:
      output_files.extend(split.filepaths)
    return output_files

  @property
  def splits(self):
    return [sf.split for sf in self.split_files]


class GeneratorBasedDatasetBuilder(DatasetBuilder):
  """Base class for datasets with data generation based on dict generators.

  `GeneratorBasedDatasetBuilder` is a convenience class that abstracts away much
  of the data writing and reading of `DatasetBuilder`. It expects subclasses to
  implement generators of feature dictionaries across the dataset splits
  (`_dataset_split_generators`) and to specify a file type
  (`_file_format_adapter`). See the method docstrings for details.

  Minimally, subclasses must override `_dataset_split_generators` and
  `_file_format_adapter`. Subclasses may also override `_preprocess` if they
  wish to do further runtime pre-processing on the `tf.data.Dataset`.

  `FileFormatAdapter`s are defined in
  `tensorflow_datasets.core.file_format_adapter` and specify constraints on the
  feature dictionaries yielded by example generators. See the class docstrings.
  """

  @abc.abstractmethod
  def _dataset_split_generators(self):
    """Specify feature dictionary generators and dataset splits.

    This function returns a list of `SplitGenerator`s.
    Each generator yields feature dictionaries (`dict<str feature_name,
    feature_value>`).  The examples yielded by each generator will be written to
    the specified `SplitFile`s.

    If a generator produces data exclusively for a single split, then the
    `SplitGenerator` should have only a single `SplitFile`.

    If a generator produces examples that should be sharded across multiple
    splits (this is the case if the underlying dataset does not have pre-defined
    data splits), then the `SplitGenerator` will have multiple `SplitFile`s
    (equal to the number of splits the examples should be sharded across). The
    proportion of the examples that will end up in each split is defined by the
    relative number of shards each `ShardFiles` object specifies. For example:

    ```
    def _dataset_split_generators(self):
      return [
          SplitGenerator(
              generator_fn=my_generator_fn,
              split_files=[
                  self._split_files(split=Split.TRAIN, num_shards=2),
                  self._split_files(split=Split.VALIDATION, num_shards=2),
                  self._split_files(split=Split.TEST, num_shards=2)
              ]
          )
      ]
    ```

    The examples from `my_generator_fn` would be split evenly across the 3
    `Split`s provided.

    Each `SplitFiles` can be constructed with the `_split_files` helper method
    (`self._split_files(split=Split.TRAIN, num_shards=10)`) which fills in
    common fields.

    For downloads and extractions, use `self._download_manager`.
    Note that the `DownloadManager` caches downloads, so it is fine to have each
    generator attempt to download the source data.

    Returns:
      `list<SplitGenerator`>.
    """
    raise NotImplementedError()

  @abc.abstractproperty
  def _file_format_adapter(self):
    """Returns a FileFormatAdapter.

    FileFormatAdapters are defined in file_format_adapter.py and implement
    methods to write and read data from a particular file format. See the
    constructor for each adapter to see what arguments it takes.

    For example, to write and read from TFRecord files you would provide the
    name, shape, and type of each feature on disk:

    ```python
    return TFRecordExampleAdapter({
        "x": tf.FixedLenFeature(tuple(), tf.int64)})
    ```

    Returns:
      FileFormatAdapter instance
    """
    raise NotImplementedError

  def _preprocess(self, feature_dict):
    """Preprocess the feature dictionary.

    Note that this is a TensorFlow function that has Tensor inputs and Tensor
    outputs and must use TensorFlow ops. It will be used as a `map_fn` to the
    `tf.data.Dataset`.

    Args:
      feature_dict (dict): Feature name to Tensor, a single entry from the
        `tf.data.Dataset`.

    Returns:
      feature_dict, possibly modified.
    """
    return feature_dict

  def _download_and_prepare(self):
    if not tf.gfile.Exists(self._data_dir):
      tf.gfile.MakeDirs(self._data_dir)
    for split_generator in self._dataset_split_generators():
      if split_generator.output_files_exist():
        tf.logging.info("Skipping download_and_prepare for splits %s as all "
                        "files exist.", split_generator.splits)
        continue
      self._file_format_adapter.write_from_generator(
          split_generator.generator_fn, split_generator.output_files)

  def _as_dataset(self, split=Split.TRAIN, shuffle_files=None):
    return dataset_utils.build_dataset(
        filepattern=self._split_files(num_shards=None, split=split).filepattern,
        dataset_from_file_fn=self._file_format_adapter.dataset_from_filename,
        process_fn=self._preprocess,
        shuffle_files=(
            split == Split.TRAIN if shuffle_files is None else shuffle_files))

  def _split_files(self, **kwargs):
    kwargs["dataset_name"] = self.name
    kwargs["data_dir"] = self._data_dir
    kwargs["filetype_suffix"] = self._file_format_adapter.filetype_suffix
    return SplitFiles(**kwargs)

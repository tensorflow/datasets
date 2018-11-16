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
import datetime
import functools
import os

import six
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import file_format_adapter
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import units
from tensorflow_datasets.core import utils

import termcolor


__all__ = [
    "DatasetBuilder",
    "GeneratorBasedDatasetBuilder",
]


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
  train_dataset = train_dataset.repeat().shuffle(1024).batch(128)
  train_dataset = train_dataset.prefetch(tf.data.experimental.AUTOTUNE)
  features = train_dataset.make_one_shot_iterator().get_next()
  image, label = features['image'], features['label']
  ```
  """

  # Name of the dataset, filled by metaclass based on class name.
  name = None

  @api_utils.disallow_positional_args
  def __init__(self, data_dir=None):
    """Construct a DatasetBuilder.

    Callers must pass arguments as keyword arguments.

    Args:
      data_dir: (str) directory to read/write data. Defaults to
        "~/tensorflow_datasets".
    """
    self._data_dir_root = os.path.expanduser(data_dir or constants.DATA_DIR)
    # Get the last dataset if it exists (or None otherwise)
    self._data_dir = self._get_data_dir()

    # If a previous dataset version exists, reload the dataset info as well.
    if self._data_dir:
      self.info.read_from_directory(self._data_dir)

  @utils.memoized_property
  def info(self):
    """Return the dataset info object. See `DatasetInfo` for details."""
    return self._info()

  @api_utils.disallow_positional_args
  def download_and_prepare(
      self,
      cache_dir=None,
      manual_dir=None,
      mode=None,
      dl_manager=None,
      compute_stats=True):
    """Downloads and prepares dataset for reading.

    Subclasses must override _download_and_prepare.

    Args:
      cache_dir: `str`, Cached directory where to extract the data. If None,
        a default data_dir/tmp directory is used.
      manual_dir: `str`, Cached directory where the manually extracted data is.
        If None, a default data_dir/manual/{dataset_name}/ directory is used.
        For DatasetBuilder, this is a read-only directory.
      mode: `tfds.GenerateMode`: Mode to FORCE_REDOWNLOAD, REUSE_CACHE_IF_EXISTS
        or REUSE_DATASET_IF_EXISTS. Default to REUSE_DATASET_IF_EXISTS.
      dl_manager: `tfds.download.DownloadManager` DownloadManager to use
       instead of the default one. If set, none of the cache_dir, manual_dir,
       mode should be set.
      compute_stats: `boolean` If True, compute statistics over the generated
        data and write the `tfds.core.DatasetInfo` protobuf to disk.

    Raises:
      ValueError: If the user defines both cache_dir and dl_manager
    """

    if dl_manager is not None and (cache_dir or manual_dir or mode):
      raise ValueError(
          ".download_and_prepare kwargs should not be set if dl_manager "
          "is passed to download_and_prepare.")

    # If None are set. Set values to default:
    cache_dir = cache_dir or os.path.join(self._data_dir_root, "tmp")
    manual_dir = manual_dir or os.path.join(self._data_dir_root, "manual")
    manual_dir = os.path.join(manual_dir, self.name)
    mode = mode or download.GenerateMode.REUSE_DATASET_IF_EXISTS
    mode = download.GenerateMode(mode)

    # If the dataset already exists (data_dir not empty) and that we do not
    # overwrite the dataset
    if (self._data_dir and
        mode == download.GenerateMode.REUSE_DATASET_IF_EXISTS):
      tf.logging.info("Reusing dataset %s (%s)", self.name, self._data_dir)
      return

    # Create the download manager
    if dl_manager is None:
      dl_manager = download.DownloadManager(
          cache_dir=cache_dir,
          manual_dir=manual_dir,
          mode=mode,
      )

    # Otherwise, create a new version in a new data_dir.
    curr_date = datetime.datetime.now()
    version_str = curr_date.strftime("v_%Y%m%d_%H%M")
    data_dir = self._get_data_dir(version=version_str)
    self._data_dir = None
    tf.logging.info("Generating dataset %s (%s)", self.name, data_dir)

    # Print is intentional: we want this to always go to stdout so user has
    # information needed to cancel download/preparation if needed.
    # This comes right before the progress bar.
    size_text = units.size_str(self.info.size_in_bytes)
    termcolor.cprint("Downloading / extracting dataset %s (%s) to %s..." %
                     (self.name, size_text, data_dir), attrs=["bold"])

    # Wrap the Dataset generation in a .incomplete directory
    with file_format_adapter.incomplete_dir(data_dir) as data_dir_tmp:
      self._download_and_prepare(dl_manager=dl_manager, data_dir=data_dir_tmp)

    # Update the DatasetInfo metadata by computing statistics from the data.
    self._data_dir = data_dir
    if compute_stats:
      # Update the info object with the statistics and schema.
      # Note: self.info already contains static information about the dataset
      self.info.compute_dynamic_properties(self)

    # Write DatasetInfo to disk, even if we haven't computed the statistics.
    self.info.write_to_directory(self._data_dir)

  # TODO(rsepassi): Make it easy to further shard the TRAIN data (e.g. for
  # synthetic VALIDATION splits).
  @api_utils.disallow_positional_args
  def as_dataset(self,
                 split,
                 shuffle_files=None,
                 as_supervised=False):
    """Constructs a `tf.data.Dataset`.

    Callers must pass arguments as keyword arguments.

    Subclasses must override _as_dataset.

    Args:
      split: `tfds.Split`, which subset of the data to read.
      shuffle_files: `bool` (optional), whether to shuffle the input files.
        Defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.
      as_supervised: `bool`, if `True`, the returned `tf.data.Dataset`
        will have a 2-tuple structure `(input, label)` according to
        `builder.info.supervised_keys`. If `False`, the default,
        the returned `tf.data.Dataset` will have a dictionary with all the
        features.

    Returns:
      `tf.data.Dataset`
    """
    if not self._data_dir:
      raise AssertionError(
          ("Dataset %s: could not find data in %s. Please make sure to call "
           "dataset_builder.download_and_prepare(), or pass download=True to "
           "tfds.load() before trying to access the tf.data.Dataset object."
          ) % (self.name, self._data_dir_root))

    if shuffle_files is None:
      shuffle_files = split == splits.Split.TRAIN

    dataset = self._as_dataset(split=split, shuffle_files=shuffle_files)
    if as_supervised:
      if not self.info.supervised_keys:
        raise ValueError(
            "as_supervised=True but %s does not support a supervised "
            "(input, label) structure." % self.name)
      input_f, target_f = self.info.supervised_keys
      dataset = dataset.map(lambda fs: (fs[input_f], fs[target_f]),
                            num_parallel_calls=tf.data.experimental.AUTOTUNE)

    dataset = dataset.prefetch(tf.data.experimental.AUTOTUNE)

    # If shuffling, allow pipeline to be non-deterministic
    options = tf.data.Options()
    options.experimental_deterministic = not shuffle_files
    dataset = dataset.with_options(options)
    return dataset

  def numpy_iterator(self, **as_dataset_kwargs):
    """Generates numpy elements from the given `tfds.Split`.

    This generator can be useful for non-TensorFlow programs.

    Args:
      **as_dataset_kwargs: Keyword arguments passed on to
        `tfds.core.DatasetBuilder.as_dataset`.

    Returns:
      Generator yielding feature dictionaries
      `dict<str feature_name, numpy.array feature_val>`.
    """
    def iterate():
      dataset = self.as_dataset(**as_dataset_kwargs)
      dataset = dataset.prefetch(tf.data.experimental.AUTOTUNE)
      return dataset_utils.iterate_over_dataset(dataset)

    if tf.executing_eagerly():
      return iterate()
    else:
      with tf.Graph().as_default():
        return iterate()

  def _get_data_dir(self, version=None):
    """Return the data directory of one dataset version.

    Args:
      version: (str) If specified, return the data_dir associated with the
        given version

    Returns:
      data_dir: (str)
        If version is given, return the data_dir associated with this version.
        Otherwise, automatically extract the last version from the directory.
        If no previous version is found, return None.
    """
    data_root_dir = os.path.join(self._data_dir_root, self.name)
    if version is not None:
      return os.path.join(data_root_dir, version)

    # Get the most recent directory
    if tf.gfile.Exists(data_root_dir):
      version_dirnames = [
          f for f in sorted(tf.gfile.ListDirectory(data_root_dir))
          if ".incomplete" not in f
      ]
      if version_dirnames:
        return os.path.join(data_root_dir, version_dirnames[-1])

    # No directory found
    return None

  @abc.abstractmethod
  def _info(self):
    """Construct the DatasetInfo object. See `DatasetInfo` for details.

    Warning: This function is only called once and the result is cached for all
    following .info() calls.

    Returns:
      dataset_info: (DatasetInfo) The dataset information
    """
    raise NotImplementedError

  @abc.abstractmethod
  def _download_and_prepare(self, dl_manager, data_dir):
    """Downloads and prepares dataset for reading.

    This is the internal implementation to overwritte called when user call
    `download_and_prepare`. It should download all required data and generate
    the pre-processed datasets files.

    Args:
      dl_manager: (DownloadManager) `DownloadManager` used to download and cache
        data.
      data_dir: (str) Temporary folder on which generating the data
    """
    raise NotImplementedError

  @abc.abstractmethod
  def _as_dataset(self, split, shuffle_files=None):
    """Constructs a `tf.data.Dataset`.

    This is the internal implementation to overwritte called when user call
    `as_dataset`. It should read the pre-processed datasets files and generate
    the `tf.data.Dataset` object.

    Args:
      split (`tfds.Split`): which subset of the data to read.
      shuffle_files (bool): whether to shuffle the input files. Optional,
        defaults to `True` if `split == tfds.Split.TRAIN` and `False` otherwise.

    Returns:
      `tf.data.Dataset`
    """
    raise NotImplementedError


class GeneratorBasedDatasetBuilder(DatasetBuilder):
  """Base class for datasets with data generation based on dict generators.

  `GeneratorBasedDatasetBuilder` is a convenience class that abstracts away much
  of the data writing and reading of `DatasetBuilder`. It expects subclasses to
  implement generators of feature dictionaries across the dataset splits
  (`_split_generators`) and to specify a file type
  (`_file_format_adapter`). See the method docstrings for details.

  Minimally, subclasses must override `_split_generators` and
  `_file_format_adapter`.

  `FileFormatAdapter`s are defined in
  `tensorflow_datasets.core.file_format_adapter` and specify constraints on the
  feature dictionaries yielded by example generators. See the class docstrings.
  """

  @api_utils.disallow_positional_args
  def __init__(self, **kwargs):
    """Builder constructor.

    Args:
      **kwargs: Constructor kwargs forwarded to DatasetBuilder
    """
    super(GeneratorBasedDatasetBuilder, self).__init__(**kwargs)

  @utils.memoized_property
  def _file_format_adapter(self):
    # Load the format adapter (CSV, TF-Record,...)
    file_adapter_cls = file_format_adapter.TFRecordExampleAdapter
    serialized_features = self.info.features.get_serialized_features()
    return file_adapter_cls(serialized_features)

  @abc.abstractmethod
  def _split_generators(self, dl_manager):
    """Specify feature dictionary generators and dataset splits.

    This function returns a list of `SplitGenerator`s defining how to generate
    data and what splits to use.

    Example:

      return[
          tfds.SplitGenerator(
              name=tfds.Split.TRAIN,
              num_shards=10,
              gen_kwargs={'file': 'train_data.zip'},
          ),
          tfds.SplitGenerator(
              name=tfds.Split.TEST,
              num_shards=5,
              gen_kwargs={'file': 'test_data.zip'},
          ),
      ]

    The above code will first call `_generate_samples(file='train_data.zip')` to
    write the train data, then `_generate_samples(file='test_data.zip')` to
    write the test data.

    Datasets are typically split into different subsets to be used at various
    stages of training and evaluation.

    Note that for datasets without a `VALIDATION` split, you can use a
    fraction of the `TRAIN` data for evaluation as you iterate on your model
    so as not to overfit to the `TEST` data.

    You can use a single generator shared between splits by providing list
    instead of values for `tfds.SplitGenerator` (this is the case if the
    underlying dataset does not have pre-defined data splits):

      return [tfds.SplitGenerator(
          name=[tfds.Split.TRAIN, tfds.Split.VALIDATION],
          num_shards=[10, 3],
      )]

    This will call `_generate_samples()` once but will automatically distribute
    the samples between train and validation set.
    The proportion of the examples that will end up in each split is defined
    by the relative number of shards each `ShardFiles` object specifies. In
    the previous case, the train split would contains 10/13 of the samples,
    while the validation split would contain 3/13.

    For downloads and extractions, use the given `download_manager`.
    Note that the `DownloadManager` caches downloads, so it is fine to have each
    generator attempt to download the source data.

    A good practice is to download all data in this function, and then
    distribute the relevant parts to each split with the `gen_kwargs` argument

    Args:
      dl_manager: (DownloadManager) Download manager to download the data

    Returns:
      `list<SplitGenerator>`.
    """
    raise NotImplementedError()

  @abc.abstractmethod
  def _generate_samples(self, **kwargs):
    """Default function generating samples for each `SplitGenerator`.

    This function preprocess the samples from the raw data to the preprocessed
    dataset files.
    This function is called once for each `SplitGenerator` defined in
    `_split_generators`. The examples yielded here will be written on
    disk.

    Args:
      **kwargs: (dict) Arguments forwarded from the SplitGenerator.gen_kwargs

    Yields:
      sample: (dict) Sample dict<str feature_name, feature_value>. The sample
        should usually be encoded with `self.info.features.encode_sample({...})`
    """
    raise NotImplementedError()

  def _download_and_prepare(self, dl_manager, data_dir):
    if not tf.gfile.Exists(data_dir):
      tf.gfile.MakeDirs(data_dir)

    # Generating datata for all splits
    split_dict = splits.SplitDict()
    for split_generator in self._split_generators(dl_manager):
      # Keep track of all split_info
      for s in split_generator.split_info_list:
        split_dict.add(s)

      # Generate the filenames and write the sample on disk
      generator_fn = functools.partial(
          self._generate_samples,
          **split_generator.gen_kwargs
      )
      output_files = self._build_split_filenames(
          data_dir=data_dir,
          split_info_list=split_generator.split_info_list,
      )
      self._file_format_adapter.write_from_generator(
          generator_fn,
          output_files,
      )

    # TODO(afrozm): Make it so that basic split information is known without
    # having to call download_and_prepare. Maybe dataset definitions should
    # include it.
    # Update the info object with the splits.
    self.info.splits = split_dict

  def _as_dataset(self, split=splits.Split.TRAIN, shuffle_files=None):
    # Automatically activate shuffling if training
    if isinstance(split, six.string_types):
      split = splits.NamedSplit(split)

    # Resolve all the named split tree by real ones
    read_instruction = split.get_read_instruction(self.info.splits)
    # Extract the list of SlicedSplitInfo objects containing the splits
    # to use and their associated slice
    list_sliced_split_info = read_instruction.get_list_sliced_split_info()
    # Resolve the SlicedSplitInfo objects into a list of
    # {'filepath': 'path/to/data-00032-00100', 'mask': [True, True, False, ...]}
    instruction_dicts = self._slice_split_info_to_instruction_dicts(
        list_sliced_split_info)

    # Load the dataset
    dataset = dataset_utils.build_dataset(
        instruction_dicts=instruction_dicts,
        dataset_from_file_fn=self._file_format_adapter.dataset_from_filename,
        shuffle_files=shuffle_files,
    )
    dataset = dataset.map(self.info.features.decode_sample,
                          num_parallel_calls=tf.data.experimental.AUTOTUNE)
    return dataset

  def _slice_split_info_to_instruction_dicts(self, list_sliced_split_info):
    """Return the list of files and reading mask of the files to read."""
    instruction_dicts = []
    for sliced_split_info in list_sliced_split_info:
      # Compute filenames from the given split
      for filepath in self._build_split_filenames(
          data_dir=self._data_dir,
          split_info_list=[sliced_split_info.split_info],
      ):
        mask = splits.slice_to_percent_mask(sliced_split_info.slice_value)
        instruction_dicts.append({
            "filepath": filepath,
            "mask": mask,
        })
    return instruction_dicts

  def _build_split_filenames(self, data_dir, split_info_list):
    """Construct the split filenames associated with the split info.

    Args:
      data_dir: (str) Root directory of the filenames
      split_info_list: (list[SplitInfo]) List of split from which generate the
        filenames

    Returns:
      filenames: (list[str]) The list of filenames path corresponding to the
        split info object
    """

    filenames = []
    for split_info in split_info_list:
      filenames.extend(naming.filepaths_for_dataset_split(
          dataset_name=self.name,
          split=split_info.name,
          num_shards=split_info.num_shards,
          data_dir=data_dir,
          filetype_suffix=self._file_format_adapter.filetype_suffix,
      ))
    return filenames

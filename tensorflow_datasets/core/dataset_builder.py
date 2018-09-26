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


class Split(enum.Enum):
  """Enum for dataset splits on disk.

  Datasets are typically split into different subsets to be used at various
  stages of training and evaluation. All datasets have at least the TRAIN and
  TEST splits.

  Note that for datasets without a VALIDATION split, you should use a fraction
  of the TRAIN data for evaluation as you iterate on your model so as not to
  overfit to the TEST data. You can do so by...
  TODO(rsepassi): update when as_dataset supports this.

  * TRAIN: the training data.
  * VALIDATION: the validation data. If present, this is typically used as
    evaluation data while iterating on a model (e.g. changing hyperparameters,
    model architecture, etc.).
  * TEST: the testing data. This is the data to report metrics on. Typically you
    do not want to use this during model iteration as you may overfit to it.
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
  """Base class for datasets."""
  REGISTERED = False

  @api_utils.disallow_positional_args
  def __init__(self, data_dir=api_utils.REQUIRED_ARG, download_manager=None):
    """Construct a DatasetBuilder.

    Args:
      data_dir (str): directory to read/write data.
      download_manager (DownloadManager): manager to download and extract data.
    """
    self._data_dir = data_dir
    self._download_manager = (
        download_manager or
        download_manager_lib.DownloadManager(
            download_dir=os.path.join(
                download_manager_lib.DEFAULT_DOWNLOAD_DIR, self.name)))

  @api_utils.disallow_positional_args
  def download_and_prepare(self):
    """Download and prepare dataset.

    Subclasses override _download_and_prepare.
    """
    self._download_and_prepare()

  # TODO(rsepassi): Make it easy to further shard the TRAIN data (e.g. for
  # synthetic VALIDATION splits).
  @api_utils.disallow_positional_args
  def as_dataset(self, split, shuffle_files=None):
    """Constructs a `tf.data.Dataset`.

    Subclasses override _as_dataset.

    Args:
      split (Split): which subset of the data to read.
      shuffle_files (bool): whether to shuffle the input files.

    Returns:
      `tf.data.Dataset`
    """
    return self._as_dataset(split=split, shuffle_files=shuffle_files)

  def numpy_iterator(self, **as_dataset_kwargs):
    """Yields numpy elements from dataset."""
    def iterate():
      dataset = self.as_dataset(**as_dataset_kwargs)
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

  def _download_and_prepare(self):
    raise NotImplementedError()

  def _as_dataset(self, split, shuffle_files=None):
    raise NotImplementedError


class GeneratorBasedDatasetBuilder(DatasetBuilder):
  """Base class for datasets with data generation based on dict generators.

  Minimally, subclasses must override _dataset_split_generators and
  _file_format_adapter.

  The FileFormatAdapters are defined in
  tensorflow_datasets.core.file_format_adapter.

  If subclasses need to do further preprocessing on the records, they should
  override _preprocess.
  """
  REGISTERED = False

  def _dataset_split_generators(self):
    """Specify example generators and dataset splits.

    For downloads and extractions, use `self._download_manager`.
    Note that the `DownloadManager` caches downloads, so it is fine to have each
    generator attempt to download the source data.

    Returns:
      List of tuple(generator_fn, list<SplitFiles>).

      If you have a separate generator per split, then the
      list<SplitFiles> per element should have length == 1. If you only
      have a single generator and want the records to be automatically split for
      you, then the list<SplitFiles> should have length > 1.

      The generator_fns should take no arguments and yield dicts of feature name
      to feature value.
    """
    raise NotImplementedError()

  @property
  def _file_format_adapter(self):
    """Returns a FileFormatAdapter.

    FileFormatAdapters are defined in file_format_adapter.py and implement
    methods to write and read data from a particular file format. See the
    constructor for each adapter to see what arguments it takes.

    For example, to write and read from TFRecord files:

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
    outputs and should use TensorFlow ops. It will be used as a `map_fn` to the
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
    # Flatten out the output files for generators going to multiple splits.
    flattened = []
    for (generator_fn, split_files) in self._dataset_split_generators():
      output_files = []
      if all([split.exists() for split in split_files]):
        tf.logging.info("Skipping download_and_prepare for splits %s as all "
                        "files exist.",
                        [split.split for split in split_files])
        continue
      for split in split_files:
        output_files.extend(split.filepaths)
      flattened.append((generator_fn, output_files))
    if flattened:
      self._file_format_adapter.write_from_generators(flattened)

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

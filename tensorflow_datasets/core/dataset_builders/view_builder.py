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

"""Builder whose configs are transformations applied to other datasets.

Note that this is an experimental new feature, so the API may change.
"""

from __future__ import annotations

import functools
from typing import Callable, Dict, Iterator, List, Optional, Union

from tensorflow_datasets.core import beam_utils
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import load as load_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import transform as transform_lib
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

Key = transform_lib.Key
Example = transform_lib.Example
KeyExample = transform_lib.KeyExample


class ViewConfig(dataset_builder.BuilderConfig):
  """Builder config for a view transforming another dataset."""

  def __init__(
      self,
      *,
      name: str,
      input_dataset: Union[None, str, naming.DatasetReference] = None,
      ex_transformations: Optional[
          List[transform_lib.ExampleTransformFn]
      ] = None,
      ds_transformations: Optional[
          List[Callable[[tf.data.Dataset], tf.data.Dataset]]
      ] = None,
      **kwargs,
  ):
    """Initialize a ViewConfig.

    Arguments:
      name: the name of this config.
      input_dataset: the dataset on which this view is being applied. If `None`,
        the input dataset needs to be specified in the `ViewBuilder`.
      ex_transformations: transformations that need to be applied to individual
        examples / rows. The transformations are normal Python functions. See
        the documentation for more information. Note that you cannot specify
        both example and dataset transformations.
      ds_transformations: `tf.data` transformations that are applied on the
        whole `tf.data.Dataset`. Note that you cannot specify both example and
        dataset transformations.
      **kwargs: additional arguments passed to the `BuilderConfig` such as
        `version`, `release_notes`, `supported_versions`, and `description`.
    """
    if isinstance(input_dataset, str):
      input_dataset = naming.DatasetReference.from_tfds_name(input_dataset)
    self.input_dataset = input_dataset
    if ex_transformations and ds_transformations:
      raise ValueError(
          "It is not supported to use both TF data and example transformations!"
      )
    self.ex_transformations = ex_transformations
    self.ds_transformations = ds_transformations
    super().__init__(name=name, **kwargs)

  def input_dataset_builder(
      self,
      data_dir: Optional[str] = None,
  ) -> dataset_builder.DatasetBuilder:
    assert self.input_dataset, "Input dataset must be specified."
    tfds_name = self.input_dataset.tfds_name(include_version=True)
    data_dir = self.input_dataset.data_dir or data_dir
    return load_lib.builder(name=tfds_name, data_dir=data_dir)


def _transform_per_example(
    builder: dataset_builder.DatasetBuilder,
    split_info: splits_lib.SplitInfo,
    transformations: List[transform_lib.ExampleTransformFn],
) -> split_builder_lib.SplitGenerator:
  """Yields transformed examples of the given builder and split.

  Arguments:
    builder: the builder whose data should be transformed.
    split_info: the split that needs to be transformed.
    transformations: the example transformations that need to be applied.

  Yields:
    transformed examples of the given builder and split.
  """
  row_read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  for file_instruction in split_info.file_instructions:
    file_info = naming.FilenameInfo.from_str(file_instruction.filename)
    split_shard = f"{file_info.split}[{file_info.shard_index}shard]"
    ds = builder.as_dataset(split=split_shard, read_config=row_read_config)
    for example in dataset_utils.as_numpy(ds):
      key = example.pop("tfds_id")
      yield from transform_lib.apply_transformations(
          key=key, example=example, transformations=transformations
      )


def _transform_example(
    example: Example, transformations: List[transform_lib.ExampleTransformFn]
) -> Iterator[KeyExample]:
  key = example.pop("tfds_id")
  yield from transform_lib.apply_transformations(
      key=key, example=example, transformations=transformations
  )


def _transform_per_example_beam(
    builder: dataset_builder.DatasetBuilder,
    split_info: splits_lib.SplitInfo,
    transformations: List[transform_lib.ExampleTransformFn],
    workers_per_shard: int = 1,
) -> split_builder_lib.SplitGenerator:
  beam = lazy_imports_lib.lazy_imports.apache_beam
  split = split_info.name
  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  return (
      f"read_tfds_dataset@{split}"
      >> beam_utils.ReadFromTFDS(
          builder=builder,
          split=split,
          read_config=read_config,
          workers_per_shard=workers_per_shard,
      )
      | f"convert_to_numpy@{split}" >> beam.Map(dataset_utils.as_numpy)
      | f"transform_examples@{split}"
      >> beam.ParDo(_transform_example, transformations=transformations)
  )


def _transform_dataset(
    builder: dataset_builder.DatasetBuilder,
    split_info: splits_lib.SplitInfo,
    transformations: List[Callable[[tf.data.Dataset], tf.data.Dataset]],
) -> split_builder_lib.SplitGenerator:
  """Yields transformed examples of the given builder and split.

  Arguments:
    builder: the builder whose data should be transformed.
    split_info: the split that needs to be transformed.
    transformations: the dataset transformations that need to be applied.

  Yields:
    transformed examples of the given builder and split.
  """
  row_read_config = read_config_lib.ReadConfig(add_tfds_id=False)
  ds = builder.as_dataset(split=split_info.name, read_config=row_read_config)
  for transformation in transformations:
    ds = transformation(ds)
  for i, example in enumerate(dataset_utils.as_numpy(ds)):
    key = i
    yield key, example


class ViewBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """[Experimental] Base builder for views.

  Note that this is an experimental new feature, so the API may change.

  `ViewBuilder` can be used to define a new dataset as the transformation of an
  existing dataset.
  """

  # The dataset that this view transforms. The `input_dataset` in `ViewConfig`
  # takes precedence if specified.
  INPUT_DATASET: Union[None, str, naming.DatasetReference] = None

  # The transformations that need to be applied. Transformations in `ViewConfig`
  # take precedence if specified. Note that one should not specify both
  # `EX_TRANSFORMATIONS` and `DS_TRANSFORMATIONS`.
  # Transformations that are applied per example / row.
  EX_TRANSFORMATIONS: List[transform_lib.ExampleTransformFn] = []
  # Transformations that are applied on the full `tf.data.Dataset`.
  DS_TRANSFORMATIONS: List[Callable[[tf.data.Dataset], tf.data.Dataset]] = []

  # Whether to use Beam to generate this view.
  USE_BEAM = False

  # The number of workers that should read a single shard. If set to higher
  # than 1, multiple Beam workers will read a single shard. For tfrecord, that
  # means that some redundant reads are done.
  BEAM_WORKERS_PER_SHARD = 1

  @functools.cached_property
  def view_config(self) -> Optional[ViewConfig]:
    if isinstance(self.builder_config, ViewConfig):
      return self.builder_config
    return None

  def _src_dataset(self) -> naming.DatasetReference:
    input_dataset = self.view_config and self.view_config.input_dataset
    if input_dataset:
      return input_dataset
    elif self.INPUT_DATASET is not None:
      if isinstance(self.INPUT_DATASET, str):
        return naming.DatasetReference.from_tfds_name(self.INPUT_DATASET)
      return self.INPUT_DATASET
    raise ValueError("Input dataset was not specified!")

  def _src_dataset_builder(self) -> dataset_builder.DatasetBuilder:
    tfds_name = self._src_dataset().tfds_name(include_version=True)
    # First try to load the dataset from the data_dir where this dataset is
    # downloaded to. If that fails, load it from the default data dir.
    try:
      data_dir = self._src_dataset().data_dir or self._data_dir_root
      builder = load_lib.builder(name=tfds_name, data_dir=data_dir)
      if builder.is_prepared():
        return builder
    except registered.DatasetNotFoundError:
      pass
    return load_lib.builder(name=tfds_name)

  def _example_transformations(self) -> List[transform_lib.ExampleTransformFn]:
    ex_transformations = (
        self.view_config and self.view_config.ex_transformations
    )
    if ex_transformations:
      return ex_transformations
    return self.EX_TRANSFORMATIONS

  def _data_transformations(
      self,
  ) -> List[Callable[[tf.data.Dataset], tf.data.Dataset]]:
    if self.view_config and self.view_config.ds_transformations:
      return self.view_config.ds_transformations
    return self.DS_TRANSFORMATIONS

  def _split_generators(
      self, dl_manager: download_manager.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager
    builder = self._src_dataset_builder()
    split_generators = {}
    for split, split_info in builder.info.splits.items():
      split_generators[split] = self._generate_examples(
          builder=builder,
          split_info=split_info,
          ex_transformations=self._example_transformations(),
          ds_transformations=self._data_transformations(),
      )
    return split_generators

  def _generate_examples(
      self,
      builder: dataset_builder.DatasetBuilder,
      split_info: splits_lib.SplitInfo,
      ex_transformations: List[transform_lib.ExampleTransformFn],
      ds_transformations: List[Callable[[tf.data.Dataset], tf.data.Dataset]],
  ) -> split_builder_lib.SplitGenerator:
    if ex_transformations and ds_transformations:
      raise ValueError(
          "It is not supported to have toth example and dataset "
          "transformations!"
      )
    if ex_transformations:
      if self.USE_BEAM:
        return _transform_per_example_beam(
            builder=builder,
            split_info=split_info,
            transformations=ex_transformations,
            workers_per_shard=self.BEAM_WORKERS_PER_SHARD,
        )
      else:
        return _transform_per_example(
            builder=builder,
            split_info=split_info,
            transformations=ex_transformations,
        )
    elif ds_transformations:
      if self.USE_BEAM:
        # TODO(weide): add support for using Beam with tf.data transformations.
        raise ValueError(
            "Using Apache Beam in combination with tf.data "
            "transformations is not yet supported!"
        )
      return _transform_dataset(
          builder=builder,
          split_info=split_info,
          transformations=ds_transformations,
      )
    raise ValueError("No transformations were specified!")

# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""A dataset builder proxying data files from GCS."""

from __future__ import annotations

import abc
import os
from typing import Any

from tensorflow_datasets.core import beam_utils
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import tree



class DatasetImporterBuilder(
    tfds.core.GeneratorBasedBuilder, skip_registration=True
):
  """DatasetBuilder for RLDS datasets which proxies data files from GCS.

  RLDS datasets are already converted to TFDS format. This
  builder just effectively downloads them from GCS.
  """

  VERSION = tfds.core.Version('0.1.0')
  RELEASE_NOTES = {
      '0.1.0': 'Initial release.',
  }
  _GCS_BUCKET = 'gs://gresearch/robotics/'
  KEYS_TO_STRIP = [
      'episode_id',
      'legacy_datasets',
      'project_name',
      'publish_timestamp',
      'session_pb',
      'ssot_session_key',
  ]


  @abc.abstractmethod
  def get_description(self):
    pass

  @abc.abstractmethod
  def get_citation(self):
    pass

  @abc.abstractmethod
  def get_homepage(self):
    pass

  @abc.abstractmethod
  def get_relative_dataset_location(self):
    pass

  def get_dataset_location(self):
    return os.path.join(
        str(self._GCS_BUCKET), self.get_relative_dataset_location()
    )

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    description = self.get_description()
    features = self.get_ds_builder().info.features

    tmp = dict(features)

    for key in self.KEYS_TO_STRIP:
      if key in tmp:
        del tmp[key]
    features = tfds.features.FeaturesDict(tmp)

    return tfds.core.DatasetInfo(
        builder=self,
        description=description,
        features=features,
        supervised_keys=None,
        homepage=self.get_homepage(),
        citation=self.get_citation(),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_builder = self.get_ds_builder()

    splits = {}
    for split, split_info in ds_builder.info.splits.items():
      splits[split] = self._generate_examples(ds_builder, split_info)
    return splits

  def _generate_examples(
      self,
      builder: dataset_builder.DatasetBuilder,
      split_info: splits_lib.SplitInfo,
  ):
    beam = tfds.core.lazy_imports.apache_beam
    split = split_info.name
    read_config = read_config_lib.ReadConfig(add_tfds_id=True)

    decode_fn = builder.info.features['steps'].feature.decode_example

    def converter_fn(example):
      # Decode the RLDS Episode and transform it to numpy.
      example_out = dict(example)
      example_out['steps'] = tf.data.Dataset.from_tensor_slices(
          example_out['steps']
      ).map(decode_fn)
      steps = list(iter(example_out['steps'].take(-1)))
      example_out['steps'] = steps

      example_out = dataset_utils.as_numpy(example_out)

      example_id = example_out['tfds_id'].decode('utf-8')
      del example_out['tfds_id']
      for key in self.KEYS_TO_STRIP:
        if key in example_out:
          del example_out[key]

      yield example_id, example_out

    return f'read_tfds_dataset@{split}' >> beam_utils.ReadFromTFDS(
        builder=builder,
        split=split,
        read_config=read_config,
        workers_per_shard=1,
        decoders={'steps': tfds.decode.SkipDecoding()},
    ) | f'convert_to_numpy@{split}' >> beam.FlatMap(converter_fn)

  def get_ds_builder(self):
    ds_location = self.get_dataset_location()
    ds_builder = tfds.builder_from_directory(ds_location)
    return ds_builder


class TFDSDatasetImporterBuilder(
    tfds.core.GeneratorBasedBuilder, skip_registration=True
):
  """DatasetBuilder for TFDS datasets which proxies data files from GCS.

  This builder just effectively downloads already converted datasets from GCS.
  """

  VERSION = tfds.core.Version('0.1.0')
  RELEASE_NOTES = {
      '0.1.0': 'Initial release.',
  }
  _GCS_BUCKET = 'gs://gresearch/robotics/'


  @abc.abstractmethod
  def get_description(self):
    pass

  @abc.abstractmethod
  def get_citation(self):
    pass

  @abc.abstractmethod
  def get_homepage(self):
    pass

  @abc.abstractmethod
  def get_relative_dataset_location(self):
    pass

  def get_dataset_location(self):
    return os.path.join(
        str(self._GCS_BUCKET), self.get_relative_dataset_location()
    )

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    description = self.get_description()
    features = self.get_ds_builder().info.features

    return tfds.core.DatasetInfo(
        builder=self,
        description=description,
        features=features,
        supervised_keys=None,
        homepage=self.get_homepage(),
        citation=self.get_citation(),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_builder = self.get_ds_builder()
    splits = {}
    for split, split_info in ds_builder.info.splits.items():
      splits[split] = self._generate_examples(ds_builder, split_info)
    return splits

  def _generate_examples(
      self,
      builder: dataset_builder.DatasetBuilder,
      split_info: splits_lib.SplitInfo,
  ):
    beam = tfds.core.lazy_imports.apache_beam
    split = split_info.name
    read_config = read_config_lib.ReadConfig(add_tfds_id=True)

    def converter_fn(example):
      example_out = tree.map_structure(to_np, example)
      example_id = example_out['tfds_id'].decode('utf-8')
      del example_out['tfds_id']

      yield example_id, example_out

    return f'read_tfds_dataset@{split}' >> beam_utils.ReadFromTFDS(
        builder=builder,
        split=split,
        read_config=read_config,
        workers_per_shard=1,
    ) | f'convert_to_numpy@{split}' >> beam.FlatMap(converter_fn)

  def get_ds_builder(self):
    ds_location = self.get_dataset_location()
    ds_builder = tfds.builder_from_directory(ds_location)
    return ds_builder


def to_np(tensor):
  """Convert tensor to numpy."""
  if isinstance(tensor, tf.Tensor) or isinstance(tensor, tf.RaggedTensor):
    return tensor.numpy()
  return tensor

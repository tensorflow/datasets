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

"""Builder whose configs are transformations applied to other datasets."""
from typing import Dict, Optional, Union
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import load as load_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import transformation as transformation_lib
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.utils import read_config as read_config_lib


class ViewConfig(dataset_builder.BuilderConfig):
  """Builder config for a view transforming another dataset."""

  def __init__(
      self,
      input_dataset: Union[str, naming.DatasetReference],
      view: transformation_lib.BaseTransformation,
      **kwargs,
  ):
    if isinstance(input_dataset, str):
      input_dataset = naming.DatasetReference.from_tfds_name(input_dataset)
    self.input_dataset = input_dataset
    self.view = view
    super().__init__(**kwargs)

  def input_dataset_builder(
      self,
      data_dir: Optional[str] = None,
  ) -> dataset_builder.DatasetBuilder:
    tfds_name = self.input_dataset.tfds_name(include_version=True)
    data_dir = self.input_dataset.data_dir or data_dir
    return load_lib.builder(name=tfds_name, data_dir=data_dir)


class ViewBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True):
  """Base builder for views."""

  def _split_generators(
      self, dl_manager: download_manager.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager
    if not isinstance(self.builder_config, ViewConfig):
      raise ValueError("Builder config was not of type ViewConfig, "
                       f"but {type(self.builder_config)}.")
    builder = self.builder_config.input_dataset_builder(
        data_dir=self._data_dir_root)
    read_config = read_config_lib.ReadConfig(add_tfds_id=True)
    return {
        split: self._generate_examples(
            builder=builder,
            split_info=split_info,
            view_config=self.builder_config,
            read_config=read_config)
        for split, split_info in builder.info.splits.items()
    }

  def _generate_examples(
      self,
      builder: dataset_builder.DatasetBuilder,
      split_info: splits_lib.SplitInfo,
      view_config: ViewConfig,
      read_config: read_config_lib.ReadConfig,
  ) -> split_builder_lib.SplitGenerator:
    for file_instruction in split_info.file_instructions:
      file_info = naming.FilenameInfo.from_str(file_instruction.filename)
      ds = builder.as_dataset(
          split=f"{file_info.split}[{file_info.shard_index}shard]",
          read_config=read_config)
      if isinstance(view_config.view, transformation_lib.RowTransformation):
        for example in dataset_utils.as_numpy(ds):
          key = example.pop("tfds_id")
          for k, v in view_config.view.apply(key, example):
            yield k, v
      elif isinstance(view_config.view,
                      transformation_lib.DatasetTransformation):
        transformed_ds = view_config.view.apply(ds)
        for i, example in enumerate(dataset_utils.as_numpy(transformed_ds)):
          key = f"{file_instruction.filename}-{i}"
          yield key, example

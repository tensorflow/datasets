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

"""DatasetBuilder that stores data as a TFDS dataset.

Adhoc builders can be used to easily create a new TFDS dataset without having to
define a new `DatasetBuilder` class. This can be handy when working in a
notebook. For example, if you are in a notebook and you want to transform a
`tf.data.Dataset` into a TFDS dataset, then you can do so as follows:

```
import numpy as np

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

my_ds_train = tf.data.Dataset.from_tensor_slices({"number": [1, 2, 3]})
my_ds_test = tf.data.Dataset.from_tensor_slices({"number": [4, 5]})

# Optionally define a custom `data_dir`. If None, then the default data dir is
# used.
custom_data_dir = "/my/folder"

builder = tfds.dataset_builders.store_as_tfds_dataset(
    name="my_dataset",
    config="single_number",
    version="1.0.0",
    data_dir=custom_data_dir,
    split_datasets={
        "train": my_ds_train,
        "test": my_ds_test,
    },
    features=tfds.features.FeaturesDict({
        "number": tfds.features.Scalar(dtype=np.int64),
    }),
    description="My dataset with a single number.",
    release_notes={
        "1.0.0": "Initial release with numbers up to 5!",
    }
)
```

The `config` argument is optional and can be useful if you want to store
different configs under the same TFDS dataset.

The `data_dir` argument can be used to store the generated TFDS dataset in a
different folder, for example in your own sandbox if you don't want to share
this with others (yet). Note that when doing this, you also need to pass the
`data_dir` to `tfds.load`. If the `data_dir` argument is not specified, then
the default TFDS data dir will be used.

After the TFDS dataset has been stored, it can be loaded from other scripts:

```
# If no custom data dir was specified:
ds_test = tfds.load("my_dataset/single_number", split="test")

# When there are multiple versions, you can also specify the version.
ds_test = tfds.load("my_dataset/single_number:1.0.0", split="test")

# If the TFDS was stored in a custom folder, then it can be loaded as follows:
custom_data_dir = "/my/folder"
ds_test = tfds.load("my_dataset/single_number:1.0.0", split="test",
data_dir=custom_data_dir)
```
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
import typing
from typing import Any, Dict

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

KeyExample = split_builder_lib.KeyExample


if typing.TYPE_CHECKING:
  BeamInput = beam.PTransform | beam.PCollection[KeyExample]
  InputData = (
      tf.data.Dataset
      | beam.PTransform
      | beam.PCollection[KeyExample]
      | Iterable[KeyExample]
  )


class AdhocBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """Dataset builder that allows building a dataset without defining a class."""

  def __init__(
      self,
      *,
      name: str,
      version: utils.Version | str,
      features: feature_lib.FeatureConnector,
      split_datasets: Mapping[str, InputData],
      config: None | str | dataset_builder.BuilderConfig = None,
      data_dir: epath.PathLike | None = None,
      description: str | None = None,
      release_notes: Mapping[str, str] | None = None,
      homepage: str | None = None,
      citation: str | None = None,
      file_format: str | file_adapters.FileFormat | None = None,
      disable_shuffling: bool | None = False,
      **kwargs: Any,
  ):
    self.name = name
    self.VERSION = utils.Version(version)  # pylint: disable=invalid-name
    self.RELEASE_NOTES = release_notes  # pylint: disable=invalid-name
    if config:
      if isinstance(config, str):
        config = dataset_builder.BuilderConfig(
            name=config, version=version, release_notes=release_notes
        )
      self.BUILDER_CONFIGS = [config]  # pylint: disable=invalid-name
    self._split_datasets = split_datasets
    self._feature_spec = features
    self._description = (
        description or "Dataset built without a DatasetBuilder class."
    )
    self._homepage = homepage
    self._citation = citation
    self._disable_shuffling = disable_shuffling
    super().__init__(
        data_dir=data_dir,
        config=config,
        version=version,
        file_format=file_format,
        **kwargs,
    )

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(
        builder=self,
        description=self._description,
        features=self._feature_spec,
        homepage=self._homepage,
        citation=self._citation,
        disable_shuffling=self._disable_shuffling,
    )

  def _split_generators(
      self, dl_manager: download.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager
    split_generators = {}
    for split_name, dataset in self._split_datasets.items():
      if isinstance(dataset, tf.data.Dataset):
        split_generators[split_name] = self._generate_examples_tf_data(dataset)
      elif isinstance(dataset, Iterable):
        split_generators[split_name] = self._generate_examples_iterator(dataset)
      elif isinstance(dataset, beam.PTransform) or isinstance(
          dataset, beam.PCollection
      ):
        split_generators[split_name] = dataset
      else:
        raise ValueError(f"Dataset type {type(dataset)} not supported.")
    return split_generators

  def _generate_examples_tf_data(
      self, ds: tf.data.Dataset
  ) -> split_builder_lib.SplitGenerator:
    for i, example in enumerate(dataset_utils.as_numpy(ds)):
      yield i, example

  def _generate_examples_iterator(
      self,
      ds: Iterable[KeyExample],
  ) -> split_builder_lib.SplitGenerator:
    yield from ds

  def _generate_examples(
      self, **kwargs: Any
  ) -> split_builder_lib.SplitGenerator:
    raise NotImplementedError()


def store_as_tfds_dataset(
    name: str,
    version: utils.Version | str,
    features: feature_lib.FeatureConnector,
    split_datasets: Mapping[str, InputData],
    config: None | str | dataset_builder.BuilderConfig = None,
    data_dir: epath.PathLike | None = None,
    description: str | None = None,
    release_notes: Mapping[str, str] | None = None,
    homepage: str | None = None,
    citation: str | None = None,
    file_format: str | file_adapters.FileFormat | None = None,
    download_config: download.DownloadConfig | None = None,
    disable_shuffling: bool | None = False,
) -> AdhocBuilder:
  """Store a dataset as a TFDS dataset."""
  if not split_datasets:
    raise ValueError("No splits with datasets were given.")
  ds_types = {type(ds) for ds in split_datasets.values()}
  if len(ds_types) > 1:
    raise TypeError(
        f"All split datasets should have the same type. Got: {ds_types}"
    )

  builder = AdhocBuilder(
      name=name,
      version=version,
      features=features,
      split_datasets=split_datasets,
      config=config,
      data_dir=data_dir,
      description=description,
      release_notes=release_notes,
      homepage=homepage,
      citation=citation,
      disable_shuffling=disable_shuffling,
  )
  if builder.is_prepared():
    raise RuntimeError(
        f"Dataset '{name}' was already prepared as a TFDS dataset. Dataset"
        f" info: {builder.info}"
    )
  builder.download_and_prepare(
      download_config=download_config, file_format=file_format
  )
  logging.info(
      "Dataset '%s' was prepared as a TFDS dataset in folder %s",
      name,
      builder.data_dir,
  )
  return builder


class TfDataBuilder(AdhocBuilder, skip_registration=True):
  """Builds datasets from tf.data.Dataset without defining a class.

  This is kept for backwards-compatibility.
  """

  def __init__(
      self,
      *,
      split_datasets: Mapping[str, tf.data.Dataset],
      **kwargs: Any,
  ):
    logging.warning(
        "This class is deprecated. "
        "Please use tfds.dataset_builders.store_as_tfds_dataset instead."
    )
    super().__init__(split_datasets=split_datasets, **kwargs)

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

"""Generic DatasetBuilder that transforms a tf.data.Dataset into a TFDS dataset.
"""
from __future__ import annotations
import typing
from typing import Any, Dict, Mapping, Optional, Union

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
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

if typing.TYPE_CHECKING:
  import tensorflow as tf


class TfDataBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True):
  """DatasetBuilder that builds a TFDS dataset from a tf.data.Dataset.

  This class can be used to create a new dataset builder class, but also in an
  adhoc manner, e.g. from a notebook.

  If you are in a notebook and you want to transform a `tf.data.Dataset` into a
  TFDS dataset, then you can do so as follows:

  ```
  from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
  import tensorflow_datasets.public_api as tfds

  my_ds_train = tf.data.Dataset.from_tensor_slices({"number": [1, 2, 3]})
  my_ds_test = tf.data.Dataset.from_tensor_slices({"number": [4, 5]})

  # Optionally define a custom `data_dir`. If None, then the default data dir is
  # used.
  custom_data_dir = "/my/folder"

  # Define the builder.
  builder = tfds.dataset_builders.TfDataBuilder(
      name="my_dataset",
      config="single_number",
      version="1.0.0",
      data_dir=custom_data_dir,
      split_datasets={
          "train": my_ds_train,
          "test": my_ds_test,
      },
      features=tfds.features.FeaturesDict({
          "number": tfds.features.Scalar(dtype=int64),
      }),
      description="My dataset with a single number.",
      release_notes={
          "1.0.0": "Initial release with numbers up to 5!",
      }
  )

  # Make the builder store the data as a TFDS dataset.
  builder.download_and_prepare()
  ```

  The `config` argument is optional and can be useful if you want to store
  different configs under the same dataset.

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

  You can also define a new DatasetBuilder based on this class.

  ```
  from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
  import tensorflow_datasets.public_api as tfds

  class MyDatasetBuilder(tfds.dataset_builders.TfDataBuilder):
    def __init__(self):
      ds_train = tf.data.Dataset.from_tensor_slices([1, 2, 3])
      ds_test = tf.data.Dataset.from_tensor_slices([4, 5])
      super().__init__(
        name="my_dataset",
        version="1.0.0",
        split_datasets={
            "train": ds_train,
            "test": ds_test,
        },
        features=tfds.features.FeaturesDict({
            "number": tfds.features.Scalar(dtype=int64),
        }),
        config="single_number",
        description="My dataset with a single number.",
        release_notes={
            "1.0.0": "Initial release with numbers up to 5!",
        }
      )
  ```
  """

  def __init__(
      self,
      *,
      name: str,
      version: Union[utils.Version, str],
      split_datasets: Mapping[str, tf.data.Dataset],
      features: feature_lib.FeatureConnector,
      config: Union[None, str, dataset_builder.BuilderConfig] = None,
      data_dir: Optional[epath.PathLike] = None,
      description: Optional[str] = None,
      release_notes: Optional[Mapping[str, str]] = None,
      file_format: Optional[Union[str, file_adapters.FileFormat]] = None,
      **kwargs: Any,
  ):
    self.name = name
    self.VERSION = utils.Version(version)  # pylint: disable=invalid-name
    self.RELEASE_NOTES = release_notes  # pylint: disable=invalid-name
    if config:
      if isinstance(config, str):
        config = dataset_builder.BuilderConfig(name=config, version=version)
      self.BUILDER_CONFIGS = [config]  # pylint: disable=invalid-name
    self._split_datasets = split_datasets
    self._feature_spec = features
    self._description = description or 'Dataset built from tf.data.Dataset'
    super().__init__(
        data_dir=data_dir,
        config=config,
        version=version,
        file_format=file_format,
        **kwargs)

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo(
        builder=self,
        description=self._description,
        features=self._feature_spec,
    )

  def _split_generators(
      self, dl_manager: download.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager
    return {
        split_name: self._generate_examples(ds=raw_dataset)
        for split_name, raw_dataset in self._split_datasets.items()
    }

  def _generate_examples(
      self, ds: tf.data.Dataset) -> split_builder_lib.SplitGenerator:
    for i, example in enumerate(dataset_utils.as_numpy(ds)):
      yield i, example

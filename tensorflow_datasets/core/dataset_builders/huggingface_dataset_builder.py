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

"""Dataset builder for Huggingface datasets.

Instead of changing the Huggingface dataset builder code to directly construct a
TFDS dataset, here we first download and prepare a Huggingface dataset and use
the resulting dataset to create a new TFDS dataset. This is to support
Huggingface community datasets that are hosted on external repositories.

Furthermore, this also enables creating datasets based on datasets in
Huggingface.
"""

from __future__ import annotations

import functools
import itertools
import multiprocessing
import os
from typing import Any, Dict, Mapping, Optional, Union

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import download
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils import version as version_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import datasets as hf_datasets

_EMPTY_SPLIT_WARNING_MSG = "%s split doesn't have any examples"


def _extract_supervised_keys(hf_info):
  if hf_info.supervised_keys is not None:
    sk_input = hf_info.supervised_keys.input
    sk_output = hf_info.supervised_keys.output
    if sk_input is not None and sk_output is not None:
      return (sk_input, sk_output)
  return None


def _remove_empty_splits(
    splits: Dict[str, split_builder_lib.SplitGenerator]
) -> Dict[str, split_builder_lib.SplitGenerator]:
  """Removes empty splits."""
  non_empty_splits = {}

  for split, examples_iterable in splits.items():
    examples_iterator = iter(examples_iterable)
    # ensure the iterator is not empty
    try:
      first_example = next(examples_iterator)
      non_empty_splits[split] = itertools.chain(
          [first_example], examples_iterator
      )
    except StopIteration:
      logging.warning(_EMPTY_SPLIT_WARNING_MSG, split)

  return non_empty_splits


class HuggingfaceDatasetBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """A TFDS builder for Huggingface datasets.

  If a Huggingface config name is given to this builder, it will construct a
  TFDS BuilderConfig. Note that TFDS has some restrictions on config names such
  as it is not allowed to use the config name `all`. Therefore, `all` is
  converted to `_all`.
  """

  VERSION = version_lib.Version("1.0.0")  # This will be replaced in __init__.

  def __init__(
      self,
      *,
      file_format: Optional[Union[str, file_adapters.FileFormat]] = None,
      hf_repo_id: str,
      hf_config: Optional[str] = None,
      ignore_verifications: bool = False,
      data_dir: Optional[epath.PathLike] = None,
      hf_hub_token: Optional[str] = None,
      hf_num_proc: Optional[int] = None,
      tfds_num_proc: Optional[int] = None,
      disable_shuffling: bool = True,
      **config_kwargs,
  ):
    self._hf_repo_id = hf_repo_id
    self._hf_config = hf_config
    self.config_kwargs = config_kwargs
    tfds_config = huggingface_utils.convert_hf_config_name(hf_config)
    try:
      self._hf_builder = hf_datasets.load_dataset_builder(
          self._hf_repo_id, self._hf_config, **self.config_kwargs
      )
    except Exception as e:
      raise RuntimeError(
          "Failed to load Huggingface dataset builder with"
          f" hf_repo_id={self._hf_repo_id}, hf_config={self._hf_config},"
          f" config_kwargs={self.config_kwargs}"
      ) from e
    self._hf_info = self._hf_builder.info
    version = str(self._hf_info.version or self._hf_builder.VERSION or "1.0.0")
    self.VERSION = version_lib.Version(version)  # pylint: disable=invalid-name
    if self._hf_config:
      self._converted_builder_config = dataset_builder.BuilderConfig(
          name=tfds_config,
          version=self.VERSION,
          description=self._hf_info.description,
      )
    else:
      self._converted_builder_config = None
    self.name = huggingface_utils.convert_hf_dataset_name(hf_repo_id)
    self._hf_hub_token = hf_hub_token
    self._hf_num_proc = hf_num_proc
    self._tfds_num_proc = tfds_num_proc
    self._verification_mode = (
        "no_checks" if ignore_verifications else "all_checks"
    )
    self._disable_shuffling = disable_shuffling
    super().__init__(
        file_format=file_format, config=tfds_config, data_dir=data_dir
    )
    if self._hf_config:
      self._builder_config = self._converted_builder_config
    self.generation_errors = []

  @property
  def builder_config(self) -> Optional[Any]:
    return self._converted_builder_config

  def _create_builder_config(
      self, builder_config, version
  ) -> Optional[dataset_builder.BuilderConfig]:
    return self._converted_builder_config

  @functools.lru_cache(maxsize=1)
  def _download_and_prepare_for_hf(self) -> Mapping[str, Any]:
    login_to_hf(self._hf_hub_token)
    self._hf_builder.download_and_prepare(
        num_proc=self._hf_num_proc,
        verification_mode=self._verification_mode,
    )
    return self._hf_builder.as_dataset(
        verification_mode=self._verification_mode,
    )

  def _hf_features(self):
    if self._hf_info.features is not None:
      return self._hf_info.features
    # We need to download and prepare the data to know its features.
    dataset_dict = self._download_and_prepare_for_hf()
    for dataset in dataset_dict.values():
      return dataset.info.features

  def _info(self) -> dataset_info_lib.DatasetInfo:
    return dataset_info_lib.DatasetInfo(
        builder=self,
        description=self._hf_info.description,
        features=huggingface_utils.convert_hf_features(self._hf_features()),
        citation=self._hf_info.citation,
        license=self._hf_info.license,
        supervised_keys=_extract_supervised_keys(self._hf_info),
        disable_shuffling=self._disable_shuffling,
    )

  def _split_generators(
      self, dl_manager: download.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    del dl_manager
    ds = self._download_and_prepare_for_hf()
    splits = {
        split: self._generate_examples(data) for split, data in ds.items()
    }
    return _remove_empty_splits(splits)

  def _generate_examples(self, data) -> split_builder_lib.SplitGenerator:
    convert_example = functools.partial(
        huggingface_utils.convert_hf_value, feature=self.info.features
    )
    if self._tfds_num_proc is None:
      yield from enumerate(map(convert_example, data))
    else:
      with multiprocessing.Pool(processes=self._tfds_num_proc) as pool:
        yield from enumerate(pool.imap(convert_example, data))


def builder(
    name: str, config: Optional[str] = None, **builder_kwargs
) -> HuggingfaceDatasetBuilder:
  hf_repo_id = huggingface_utils.convert_tfds_dataset_name(name)
  return HuggingfaceDatasetBuilder(
      hf_repo_id=hf_repo_id, hf_config=config, **builder_kwargs
  )


def login_to_hf(hf_hub_token: Optional[str] = None):
  """Logs in to Hugging Face Hub with the token as arg or env variable."""
  hf_hub_token = hf_hub_token or os.environ.get("HUGGING_FACE_HUB_TOKEN")
  if hf_hub_token is not None:
    huggingface_hub = lazy_imports_lib.lazy_imports.huggingface_hub
    huggingface_hub.login(token=hf_hub_token)

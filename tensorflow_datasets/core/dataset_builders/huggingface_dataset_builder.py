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

import collections
from collections.abc import Iterable, Mapping, Sequence
import dataclasses
import functools
import math
import os
from typing import Any

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils import version as version_lib
from tensorflow_datasets.core.utils.lazy_imports_utils import datasets as hf_datasets
from tensorflow_datasets.core.utils.lazy_imports_utils import huggingface_hub


def _extract_supervised_keys(hf_info):
  if hf_info.supervised_keys is not None:
    sk_input = hf_info.supervised_keys.input
    sk_output = hf_info.supervised_keys.output
    if sk_input is not None and sk_output is not None:
      return (sk_input, sk_output)
  return None


@dataclasses.dataclass(frozen=True)
class _ShardSpec:
  """Spec to write a shard.

  Attributes:
    hf_split: HuggingFace split name.
    split: TFDS split name.
    start_index: Index of the shard start.
    end_index: Index of the shard end.
    num_examples: Number of examples in the shard.
    shard_split: HuggingFace split for the shard.
  """

  hf_split: str
  start_index: int
  end_index: int

  @property
  def num_examples(self) -> int:
    return self.end_index - self.start_index

  @property
  def shard_split(self) -> str:
    return f'{self.hf_split}[{self.start_index}:{self.end_index}]'


class HuggingfaceDatasetBuilder(
    dataset_builder.ShardBasedBuilder, skip_registration=True
):
  """A TFDS builder for Huggingface datasets.

  If a Huggingface config name is given to this builder, it will construct a
  TFDS BuilderConfig. Note that TFDS has some restrictions on config names such
  as it is not allowed to use the config name `all`. Therefore, `all` is
  converted to `_all`.
  """

  VERSION = version_lib.Version('1.0.0')  # This will be replaced in __init__.

  def __init__(
      self,
      *,
      file_format: str | file_adapters.FileFormat | None = None,
      hf_repo_id: str,
      hf_config: str | None = None,
      ignore_verifications: bool = False,
      data_dir: epath.PathLike | None = None,
      hf_hub_token: str | None = None,
      hf_num_proc: int | None = None,
      ignore_hf_errors: bool = False,
      overwrite_version: str | None = None,
      **config_kwargs,
  ):
    self._hf_repo_id = hf_repo_id
    self._hf_config = hf_config
    self.config_kwargs = config_kwargs
    tfds_config = (
        conversion_utils.to_tfds_name(hf_config) if hf_config else None
    )
    try:
      self._hf_builder = hf_datasets.load_dataset_builder(
          self._hf_repo_id, self._hf_config, **self.config_kwargs
      )
    except Exception as e:
      raise RuntimeError(
          'Failed to load Huggingface dataset builder with'
          f' hf_repo_id={self._hf_repo_id}, hf_config={self._hf_config},'
          f' config_kwargs={self.config_kwargs}'
      ) from e
    self._overwrite_version = overwrite_version
    version = str(
        overwrite_version
        or self._hf_info.version
        or self._hf_builder.VERSION
        or '1.0.0'
    )
    self.VERSION = version_lib.Version(version)  # pylint: disable=invalid-name
    self.name = conversion_utils.to_tfds_name(hf_repo_id)
    self.homepage = f'https://huggingface.co/datasets/{hf_repo_id}'
    self._hf_hub_token = hf_hub_token
    self._hf_num_proc = hf_num_proc
    self._ignore_verifications = ignore_verifications
    self._verification_mode = (
        'no_checks' if self._ignore_verifications else 'all_checks'
    )
    if self._hf_config:
      description = self._get_text_field('description')
      if self._is_gated():
        description = self._gated_text + '\n' + description
      self._converted_builder_config = dataset_builder.BuilderConfig(
          name=tfds_config,
          version=self.VERSION,
          description=description,
      )
    else:
      self._converted_builder_config = None
    super().__init__(
        file_format=file_format, config=tfds_config, data_dir=data_dir
    )
    if self._hf_config:
      self._builder_config = self._converted_builder_config
    self.generation_errors = []
    self._ignore_hf_errors = ignore_hf_errors

  def __getstate__(self):
    state = super().__getstate__()
    state['_hf_state'] = dict(
        hf_repo_id=self._hf_repo_id,
        hf_config=self._hf_config,
        ignore_verifications=self._ignore_verifications,
        hf_hub_token=self._hf_hub_token,
        hf_num_proc=self._hf_num_proc,
        ignore_hf_errors=self._ignore_hf_errors,
        overwrite_version=self._overwrite_version,
        config_kwargs=self.config_kwargs,
    )
    return state

  def __setstate__(self, state):
    kwargs = state['_original_state']
    kwargs.update(state['_hf_state'])
    self.__init__(**kwargs)

  @property
  def builder_config(self) -> Any | None:
    return self._converted_builder_config

  def _create_builder_config(
      self, builder_config, version
  ) -> dataset_builder.BuilderConfig | None:
    return self._converted_builder_config

  @functools.lru_cache(maxsize=1)
  def _hf_download_and_prepare(self):
    login_to_hf(self._hf_hub_token)
    self._hf_builder.download_and_prepare(
        num_proc=self._hf_num_proc,
        verification_mode=self._verification_mode,
    )

  @property
  def _hf_info(self) -> hf_datasets.DatasetInfo:
    """Retrieves the dataset info from the HuggingFace Datasets."""
    return self._hf_builder.info

  @functools.cached_property
  def _hf_hub_info(self) -> huggingface_hub.hf_api.DatasetInfo:
    """Retrieves the dataset info from the HuggingFace Hub and caches it."""
    return huggingface_hub.dataset_info(
        self._hf_repo_id, token=self._hf_hub_token
    )

  def _is_gated(self) -> bool:
    """Whether the dataset is gated."""
    # Gated datasets return a string ('manual' or 'automatic').
    if isinstance(self._hf_hub_info.gated, str):
      return True
    return False

  @property
  def _gated_dataset_warning(self) -> str:
    """The warning message for a gated dataset."""
    gated_dataset_warning = (
        'WARNING: This dataset is gated. Before using it, make sure '
        + f'to sign the conditions at: {self.homepage}. Important: access'
        ' requests are always granted to individual users rather than to'
        ' entire organizations.'
    )
    return gated_dataset_warning

  @property
  def _gated_text(self) -> str | None:
    """Returns the conditions for a dataset, if it is gated.

    All datasets share the same default conditions. Extra conditions are stored
    in the dataset card:
    https://huggingface.co/docs/hub/en/datasets-gated

    Returns:
      The gated text if the dataset is gated. None otherwise.
    """
    if self._is_gated():
      # This condition is the same for all gated datasets.
      conditions = (
          'The conditions consist of:\nBy agreeing you accept to share your'
          ' contact information (email and username) with the repository'
          ' authors.'
      )
      if dataset_card := self._hf_hub_info.card_data:
        gated_text = dataset_card.get('extra_gated_prompt', None)
        if gated_text:
          conditions = conditions + '\n' + gated_text
      return self._gated_dataset_warning + '\n' + conditions
    return None

  def _hf_features(self) -> hf_datasets.Features:
    if not self._hf_info.features:
      # We need to download and prepare the data to know its features.
      self._hf_download_and_prepare()

    return self._hf_info.features

  def _info(self) -> dataset_info_lib.DatasetInfo:
    ds_description = self._get_text_field('description')
    ds_license = self._get_license()
    if self._is_gated():
      ds_description = (
          f'{self._gated_text}\n{ds_description}'
          if ds_description
          else self._gated_text
      )
      ds_license = (
          f'{ds_license} {self._gated_dataset_warning}'
          if ds_license
          else self._gated_dataset_warning
      )
    return dataset_info_lib.DatasetInfo(
        builder=self,
        description=ds_description,
        features=huggingface_utils.convert_hf_features(self._hf_features()),
        citation=self._get_text_field('citation'),
        license=ds_license,
        supervised_keys=_extract_supervised_keys(self._hf_info),
        homepage=self.homepage,
    )

  def _shard_iterators_per_split(
      self, dl_manager: download_manager.DownloadManager
  ) -> Mapping[str, Sequence[split_builder_lib.ExampleGeneratorFn]]:
    del dl_manager  # Unused.
    self._hf_download_and_prepare()
    if self._hf_info.splits is None:
      raise ValueError('No splits found in the HuggingFace dataset.')

    features = self.info.features
    if features is None:
      raise ValueError('No features found in the TFDS dataset.')

    def _example_generator(
        shard_spec: _ShardSpec,
    ) -> Iterable[split_builder_lib.KeyExample]:
      dataset = self._hf_builder.as_dataset(
          split=shard_spec.shard_split, run_post_process=False
      )
      for i in range(shard_spec.num_examples):
        try:
          hf_value = dataset[i]
        except Exception:  # pylint: disable=broad-exception-caught
          if self._ignore_hf_errors:
            logging.exception('Ignoring Hugging Face error')
            continue
          else:
            raise
        example = conversion_utils.to_tfds_value(hf_value, feature=features)
        encoded_example = features.encode_example(example)
        yield i, encoded_example

    example_generators_per_split: dict[
        str, list[split_builder_lib.ExampleGeneratorFn]
    ] = collections.defaultdict(list)
    for hf_split, hf_split_info in self._hf_info.splits.items():
      split = conversion_utils.to_tfds_name(hf_split)
      shard_specs = self._compute_shard_specs(hf_split_info)
      for shard_spec in shard_specs:
        example_generators_per_split[split].append(
            functools.partial(_example_generator, shard_spec=shard_spec)
        )
    return example_generators_per_split

  def _compute_shard_specs(
      self, hf_split_info: hf_datasets.SplitInfo
  ) -> Sequence[_ShardSpec]:
    """Returns specs for evenly spread shards.

    Args:
      hf_split_info: HuggingFace split info.
    """
    shard_lengths = []
    if hf_split_info.shard_lengths is None:
      if hf_split_info.num_bytes:
        # Aim for 1 GB per shard.
        num_1gb_shards = math.ceil(
            hf_split_info.num_bytes / (1024 * 1024 * 1024)
        )
        num_examples_per_shard = hf_split_info.num_examples // num_1gb_shards
        shard_lengths = [num_examples_per_shard] * (num_1gb_shards - 1)
        # Put the remaining examples in the last shard.
        current_num_examples = sum(shard_lengths)
        shard_lengths.append(hf_split_info.num_examples - current_num_examples)
      else:
        shard_lengths = [hf_split_info.num_examples]
      logging.info(
          'No shard lengths found for split %s, using %d output shards.',
          hf_split_info.name,
          len(shard_lengths),
      )
    else:
      shard_lengths = hf_split_info.shard_lengths

    shard_specs: list[_ShardSpec] = []
    prev_shard_boundary = 0
    for shard_length in shard_lengths:
      next_shard_boundary = prev_shard_boundary + shard_length
      shard_specs.append(
          _ShardSpec(
              hf_split=hf_split_info.name,
              start_index=prev_shard_boundary,
              end_index=next_shard_boundary,
          )
      )
      prev_shard_boundary = next_shard_boundary

    return shard_specs

  def _get_license(self) -> str | None:
    """Implements heuristics to get the license from HuggingFace."""
    # Heuristic #1: check the DatasetInfo from Hugging Face Hub/Datasets.
    if info_license := self._get_text_field('license'):
      return info_license
    dataset_info = self._hf_hub_info
    # Heuristic #2: check the card data.
    if dataset_info.card_data:
      if card_data_license := dataset_info.card_data.get('license'):
        return card_data_license
    # Heuristic #3: check the tags.
    if dataset_info.tags:
      for tag in dataset_info.tags:
        if tag.startswith('license:'):
          return tag.removeprefix('license:')
    return None

  def _get_text_field(self, field: str) -> str | None:
    """Get the field from either HF Hub or HF Datasets."""
    # The information retrieved from the Hub has priority over the one in the
    # builder, because the Hub which is allegedly the new source of truth.
    for dataset_info in [self._hf_hub_info, self._hf_info]:
      # `description` and `citation` are not official fields in the Hugging Face
      # Hub API but they're still exposed in its __dict__.
      if value := getattr(dataset_info, field, None):
        return value
    return None


def builder(
    name: str, config: str | None = None, **builder_kwargs
) -> HuggingfaceDatasetBuilder:
  hf_repo_id = huggingface_utils.to_huggingface_name(name)
  return HuggingfaceDatasetBuilder(
      hf_repo_id=hf_repo_id, hf_config=config, **builder_kwargs
  )


def login_to_hf(hf_hub_token: str | None = None):
  """Logs in to Hugging Face Hub with the token as arg or env variable."""
  hf_hub_token = hf_hub_token or os.environ.get('HUGGING_FACE_HUB_TOKEN')
  if hf_hub_token is not None:
    huggingface_hub.login(token=hf_hub_token)

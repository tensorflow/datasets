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

from collections.abc import Mapping, Sequence
import dataclasses
import functools
import itertools
import multiprocessing
import os
from typing import Any, Dict, Optional, Union

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import download
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import conversion_utils
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils import tqdm_utils
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
    path: Shard path.
    hf_split: HuggingFace split name.
    split: TFDS split name.
    start_index: Index of the shard start.
    end_index: Index of the shard end.
    num_examples: Number of examples in the shard.
    shard_split: HuggingFace split for the shard.
  """

  path: epath.Path
  hf_split: str
  split: str
  start_index: int
  end_index: int

  @property
  def num_examples(self) -> int:
    return self.end_index - self.start_index

  @property
  def shard_split(self) -> str:
    return f'{self.hf_split}[{self.start_index}:{self.end_index}]'


@dataclasses.dataclass(frozen=True)
class _ShardInfo:
  """Information about a shard after it is generated.

  _ShardSpec is the input to the shard generation. This is the output.

  Attributes:
    num_bytes: Actual number of bytes in the shard.
    num_examples: Actual number of examples in the shard.
    num_exceptions: Number of exceptions during retrieval.
  """

  num_bytes: int
  num_examples: int
  num_exceptions: int


def _write_shard(
    shard_spec: _ShardSpec,
    hf_builder,
    example_writer,
    features: feature_lib.FeaturesDict,
    ignore_hf_errors: bool,
) -> _ShardInfo:
  """Writes shard to the file.

  Args:
    shard_spec: Shard spec.
    hf_builder: HuggingFace dataset builder.
    example_writer: Example writer.
    features: TFDS features dict.
    ignore_hf_errors: Whether to silence and log Hugging Face errors during
      retrieval.

  Returns:
    A _ShardInfo containing the actual shard information.
  """
  serialized_info = features.get_serialized_info()
  serializer = example_serializer.ExampleSerializer(serialized_info)
  num_bytes = 0
  num_exceptions = 0

  def get_serialized_examples_iter():
    nonlocal num_bytes
    nonlocal num_exceptions
    dataset = hf_builder.as_dataset(
        split=shard_spec.shard_split, run_post_process=False
    )
    for i in range(shard_spec.num_examples):
      try:
        hf_value = dataset[i]
      except Exception:  # pylint: disable=broad-exception-caught
        num_exceptions += 1
        if ignore_hf_errors:
          logging.exception('Ignoring Hugging Face error')
          continue
        else:
          raise
      example = conversion_utils.to_tfds_value(hf_value, features)
      encoded_example = features.encode_example(example)
      serialized_example = serializer.serialize_example(encoded_example)
      num_bytes += len(serialized_example)
      yield serialized_example

  example_writer.write(
      os.fspath(shard_spec.path),
      tqdm_utils.tqdm(
          enumerate(get_serialized_examples_iter()),
          desc=f'Writing {shard_spec.path} examples...',
          unit=' examples',
          total=shard_spec.num_examples,
          leave=False,
          mininterval=1.0,
      ),
  )

  return _ShardInfo(
      num_bytes=num_bytes,
      num_examples=shard_spec.num_examples - num_exceptions,
      num_exceptions=num_exceptions,
  )


class HuggingfaceDatasetBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
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
      file_format: Optional[Union[str, file_adapters.FileFormat]] = None,
      hf_repo_id: str,
      hf_config: Optional[str] = None,
      ignore_verifications: bool = False,
      data_dir: Optional[epath.PathLike] = None,
      hf_hub_token: Optional[str] = None,
      hf_num_proc: Optional[int] = None,
      tfds_num_proc: Optional[int] = None,
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
    self._tfds_num_proc = tfds_num_proc
    self._verification_mode = (
        'no_checks' if ignore_verifications else 'all_checks'
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

  @property
  def builder_config(self) -> Optional[Any]:
    return self._converted_builder_config

  def _create_builder_config(
      self, builder_config, version
  ) -> Optional[dataset_builder.BuilderConfig]:
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
    return (
        'WARNING: This dataset is gated. Before using it, make sure to sign'
        f' the conditions at: {self.homepage}. Important: access requests are'
        ' always granted to individual users rather than to entire'
        ' organizations.'
    )

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
      ds_description = self._gated_text + '\n' + ds_description
      ds_license = ds_license + ' ' + self._gated_dataset_warning
    return dataset_info_lib.DatasetInfo(
        builder=self,
        description=ds_description,
        features=huggingface_utils.convert_hf_features(self._hf_features()),
        citation=self._get_text_field('citation'),
        license=ds_license,
        supervised_keys=_extract_supervised_keys(self._hf_info),
        homepage=self.homepage,
    )

  def _split_generators(
      self, dl_manager: download.DownloadManager
  ) -> Dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    raise NotImplementedError('This method should not be called.')

  def _generate_examples(self, data) -> split_builder_lib.SplitGenerator:
    raise NotImplementedError('This method should not be called.')

  def _generate_splits(
      self,
      dl_manager: download.DownloadManager,
      download_config: download.DownloadConfig,
  ) -> Sequence[splits_lib.SplitInfo]:
    """Prepares the dataset by writing to shards directly."""
    del dl_manager, download_config  # Unused.
    self._hf_download_and_prepare()

    shard_specs_by_split: dict[str, Sequence[_ShardSpec]] = {}
    for hf_split, hf_split_info in self._hf_info.splits.items():
      split = conversion_utils.to_tfds_name(hf_split)
      shard_specs_by_split[split] = self._compute_shard_specs(
          hf_split_info, split
      )

    shard_infos_by_split = self._write_shards(shard_specs_by_split)
    split_infos: list[splits_lib.SplitInfo] = []
    for split, shard_infos in shard_infos_by_split.items():
      shard_lengths = [shard_info.num_examples for shard_info in shard_infos]
      num_bytes = sum(shard_info.num_bytes for shard_info in shard_infos)
      split_infos.append(
          splits_lib.SplitInfo(
              name=split,
              shard_lengths=shard_lengths,
              num_bytes=num_bytes,
              filename_template=self._get_filename_template(split),
          )
      )
    return split_infos

  def _compute_shard_specs(
      self, hf_split_info: hf_datasets.SplitInfo, split: str
  ) -> Sequence[_ShardSpec]:
    """Returns specs for evenly spread shards.

    Args:
      hf_split_info: HuggingFace split info.
      split: TFDS split name.
    """
    # HF split size is good enough for estimating the number of shards.
    num_shards = shard_utils.ShardConfig.calculate_number_shards(
        total_size=hf_split_info.num_bytes,
        num_examples=hf_split_info.num_examples,
        uses_precise_sharding=False,
    )
    filename_template = self._get_filename_template(split)
    shard_boundaries = shard_utils.get_shard_boundaries(
        num_examples=hf_split_info.num_examples, number_of_shards=num_shards
    )

    prev_shard_boundary = 0
    shard_specs: list[_ShardSpec] = []

    for shard_index, shard_boundary in enumerate(shard_boundaries):
      shard_specs.append(
          _ShardSpec(
              path=filename_template.sharded_filepath(
                  shard_index=shard_index, num_shards=len(shard_boundaries)
              ),
              hf_split=hf_split_info.name,
              split=split,
              start_index=prev_shard_boundary,
              end_index=shard_boundary,
          )
      )
      prev_shard_boundary = shard_boundary

    return shard_specs

  def _write_shards(
      self,
      shard_specs_by_split: Mapping[str, Sequence[_ShardSpec]],
  ) -> Mapping[str, Sequence[_ShardInfo]]:
    """Writes shards to files.

    Args:
      shard_specs_by_split: Shard specs by split name.

    Returns:
      Shard sizes in bytes.
    """
    shard_specs = list(itertools.chain(*shard_specs_by_split.values()))
    shard_specs = tqdm_utils.tqdm(
        shard_specs,
        desc='Writing shards...',
        unit=' shards',
        total=len(shard_specs),
        leave=False,
    )
    write_shard = functools.partial(
        _write_shard,
        hf_builder=self._hf_builder,
        example_writer=self._example_writer(),
        features=self.info.features,
        ignore_hf_errors=self._ignore_hf_errors,
    )

    if self._tfds_num_proc is None:
      shard_infos = list(map(write_shard, shard_specs))
    else:
      with multiprocessing.Pool(processes=self._tfds_num_proc) as pool:
        shard_infos = pool.map(write_shard, shard_specs)

    shard_idx = 0
    shard_infos_by_split: dict[str, Sequence[_ShardInfo]] = {}
    for split, shard_specs in shard_specs_by_split.items():
      shard_infos_by_split[split] = shard_infos[
          shard_idx : shard_idx + len(shard_specs)
      ]
      shard_idx += len(shard_specs)
    expected_num_examples = sum(spec.num_examples for spec in shard_specs)
    if self._ignore_hf_errors and expected_num_examples > 0:
      num_exceptions = sum(info.num_exceptions for info in shard_infos)
      percentage_exceptions = num_exceptions / expected_num_examples * 100
      logging.info(
          'Got %d exceptions (%.2f%%) during Hugging Face generation',
          num_exceptions,
          percentage_exceptions,
      )
    return shard_infos_by_split

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
    name: str, config: Optional[str] = None, **builder_kwargs
) -> HuggingfaceDatasetBuilder:
  hf_repo_id = huggingface_utils.to_huggingface_name(name)
  return HuggingfaceDatasetBuilder(
      hf_repo_id=hf_repo_id, hf_config=config, **builder_kwargs
  )


def login_to_hf(hf_hub_token: Optional[str] = None):
  """Logs in to Hugging Face Hub with the token as arg or env variable."""
  hf_hub_token = hf_hub_token or os.environ.get('HUGGING_FACE_HUB_TOKEN')
  if hf_hub_token is not None:
    huggingface_hub.login(token=hf_hub_token)

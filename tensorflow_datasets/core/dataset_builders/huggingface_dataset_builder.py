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

"""Dataset builder for Huggingface datasets.

Instead of changing the Huggingface dataset builder code to directly construct a
TFDS dataset, here we first download and prepare a Huggingface dataset and use
the resulting dataset to create a new TFDS dataset. This is to support
Huggingface community datasets that are hosted on external repositories.

Furthermore, this also enables creating datasets based on datasets in
Huggingface.
"""

from __future__ import annotations

import datetime
import functools
import io
import itertools
import multiprocessing
import os
from typing import Any, Dict, Mapping, Optional, Tuple, Type, Union

from absl import logging
from etils import epath
import numpy as np
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

_IMAGE_ENCODING_FORMAT = "png"
_EMPTY_SPLIT_WARNING_MSG = "%s split doesn't have any examples"


def _convert_to_np_dtype(dtype: str) -> Type[np.generic]:
  """Returns the `np.dtype` scalar feature."""
  str2val = {
      "bool": np.bool_,
      "bool_": np.bool_,
      "float": np.float32,
      "double": np.float64,
      "large_string": np.object_,
      "utf8": np.object_,
      "string": np.object_,
  }
  if dtype in str2val:
    return str2val[dtype]
  elif hasattr(np, dtype):
    return getattr(np, dtype)
  elif dtype.startswith("timestamp"):
    # Timestamps are converted to seconds since UNIX epoch.
    return np.int64
  elif hasattr(tf.dtypes, dtype):
    return getattr(tf.dtypes, dtype)
  else:
    raise ValueError(
        f"Unrecognized type {dtype}. Please open an issue if you think "
        "this is a bug."
    )


def extract_features(hf_features) -> feature_lib.FeatureConnector:
  """Converts Huggingface feature spec to TFDS feature spec."""
  hf_datasets = lazy_imports_lib.lazy_imports.datasets
  if isinstance(hf_features, (hf_datasets.Features, dict)):
    return feature_lib.FeaturesDict(
        {
            name: extract_features(hf_inner_feature)
            for name, hf_inner_feature in hf_features.items()
        }
    )
  if isinstance(hf_features, hf_datasets.Sequence):
    return feature_lib.Sequence(feature=extract_features(hf_features.feature))
  if isinstance(hf_features, list):
    if len(hf_features) != 1:
      raise ValueError(f"List {hf_features} should have a length of 1.")
    return feature_lib.Sequence(feature=extract_features(hf_features[0]))
  if isinstance(hf_features, hf_datasets.Value):
    return feature_lib.Scalar(dtype=_convert_to_np_dtype(hf_features.dtype))
  if isinstance(hf_features, hf_datasets.ClassLabel):
    if hf_features.names:
      return feature_lib.ClassLabel(names=hf_features.names)
    if hf_features.names_file:
      return feature_lib.ClassLabel(names_file=hf_features.names_file)
    if hf_features.num_classes:
      return feature_lib.ClassLabel(num_classes=hf_features.num_classes)
  if isinstance(hf_features, hf_datasets.Translation):
    return feature_lib.Translation(
        languages=hf_features.languages,
    )
  if isinstance(hf_features, hf_datasets.TranslationVariableLanguages):
    return feature_lib.TranslationVariableLanguages(
        languages=hf_features.languages,
    )
  if isinstance(hf_features, hf_datasets.Image):
    return feature_lib.Image(encoding_format=_IMAGE_ENCODING_FORMAT)
  if isinstance(hf_features, hf_datasets.Audio):
    return feature_lib.Audio(sample_rate=hf_features.sampling_rate)
  raise ValueError(f"Type {type(hf_features)} is not supported.")


def from_hf_to_tfds(hf_name: str) -> str:
  """Converts Huggingface dataset name to a TFDS compatible name.

  Huggingface dataset names can contain characters that are not supported in
  TFDS. For example, in Huggingface a dataset name like `a/b` is supported,
  while in TFDS `b` would be parsed as the config.

  Examples:
  - `hf_name='codeparrot/github-code'` becomes `codeparrot__github_code`.

  Arguments:
    hf_name: the dataset name in Huggingface.

  Returns:
    the TFDS compatible dataset name.
  """
  return hf_name.replace("-", "_").replace(".", "_").replace("/", "__").lower()


def _from_tfds_to_hf(tfds_name: str) -> str:
  """Finds the original HF repo ID.

  As TFDS doesn't support case-sensitive names, we list all HF datasets and pick
  the dataset that has a case-insensitive match.

  Args:
    tfds_name: the dataset name in TFDS.

  Returns:
    the HF dataset name.

  Raises:
    Exception: if the name doesn't correspond to any existing dataset.
  """
  hf_datasets = lazy_imports_lib.lazy_imports.datasets
  hf_names = hf_datasets.list_datasets()
  for hf_name in hf_names:
    if from_hf_to_tfds(hf_name) == tfds_name.lower():
      return hf_name
  raise registered.DatasetNotFoundError(
      f'"{tfds_name}" is not listed in Hugging Face datasets.'
  )


def convert_config_name(hf_config: Optional[str]) -> Optional[str]:
  if hf_config is None:
    return hf_config
  return hf_config.lower().replace(",", "_")


def _convert_value(hf_value: Any, feature: feature_lib.FeatureConnector) -> Any:
  """Converts a Huggingface value to a TFDS compatible value."""
  # See the docstring of _default_value for explanations.
  if hf_value is None:
    return _default_value(feature)
  if isinstance(hf_value, datetime.datetime):
    return int(hf_value.timestamp())
  elif isinstance(feature, feature_lib.ClassLabel):
    return hf_value
  elif isinstance(feature, feature_lib.Scalar):
    return hf_value
  elif isinstance(feature, feature_lib.Translation):
    if isinstance(hf_value, dict):
      # Replaces `None` values with the default value.
      return {
          key: value if value is not None else _default_value(feature[key])
          for key, value in hf_value.items()
      }
  elif isinstance(feature, feature_lib.FeaturesDict):
    if isinstance(hf_value, dict):
      return {k: _convert_value(v, feature[k]) for k, v in hf_value.items()}
    raise ValueError(f"The feature is {feature}, but the value is: {hf_value}")
  elif isinstance(feature, feature_lib.Sequence):
    if isinstance(hf_value, dict):
      # Should be a dict of lists:
      return {
          k: [_convert_value(el, feature.feature[k]) for el in v]
          for k, v in hf_value.items()
      }
    if isinstance(hf_value, list):
      return [_convert_value(v, feature.feature) for v in hf_value]
    else:
      return [hf_value]
  elif isinstance(feature, feature_lib.Audio):
    assert isinstance(hf_value, dict), f"Audio {hf_value} should be a dict"
    if "array" in hf_value:
      sample_rate = feature.sample_rate
      # Hugging Face uses float, TFDS uses integers.
      return [int(s * sample_rate) for s in hf_value["array"]]
    if "path" in hf_value:
      path = epath.Path(hf_value["path"])
      if path.exists():
        return path
    else:
      raise ValueError(f"{hf_value} is not a valid audio feature.")
  elif isinstance(hf_value, lazy_imports_lib.lazy_imports.PIL_Image.Image):
    buffer = io.BytesIO()
    if hf_value.mode == "CMYK":
      # Convert CMYK images to RGB.
      hf_value = hf_value.convert("RGB")
    hf_value.save(fp=buffer, format=_IMAGE_ENCODING_FORMAT)
    return buffer.getvalue()
  elif isinstance(feature, feature_lib.Tensor):
    return hf_value
  raise ValueError(
      f"Type {type(hf_value)} of value {hf_value} "
      f"for feature {type(feature)} is not supported."
  )


def _convert_example(
    index: int,
    example: Mapping[str, Any],
    features: feature_lib.FeaturesDict,
) -> Tuple[int, Mapping[str, Any]]:
  """Converts an example from Huggingface format to TFDS format."""
  converted_example = {
      name: _convert_value(value, features[name])
      for name, value in example.items()
  }
  return index, converted_example


def _extract_supervised_keys(hf_info):
  if hf_info.supervised_keys is not None:
    sk_input = hf_info.supervised_keys.input
    sk_output = hf_info.supervised_keys.output
    if sk_input is not None and sk_output is not None:
      return (sk_input, sk_output)
  return None


def _default_value(
    feature: feature_lib.FeatureConnector,
) -> Union[bytes, int, bool, float]:
  """Returns the default value for a feature.

  Hugging Face is loose as far as typing is concerned. It accepts None values.
  As long as `tfds.features.Optional` does not exist, we default to a constant
  default value.

  For int and float, we do not return 0 or -1, but rather -inf, as 0 or -1 can
  be contained in the values of the dataset. In practice, you can compare your
  value to:

  ```
  np.iinfo(np.int32).min  # for integers
  np.finfo(np.float32).min  # for floats
  ...
  ```

  Args:
    feature: the TFDS feature from which we want the default value.

  Returns:
    The default value.
  """
  if isinstance(feature, feature_lib.FeaturesDict):
    return {
        name: _default_value(sub_feature)
        for name, sub_feature in feature.items()
    }
  elif isinstance(feature, feature_lib.Sequence):
    return []
  elif dtype_utils.is_string(feature.np_dtype):
    return b""
  elif dtype_utils.is_integer(feature.np_dtype):
    return np.iinfo(feature.np_dtype).min
  elif dtype_utils.is_floating(feature.np_dtype):
    return np.finfo(feature.np_dtype).min
  elif dtype_utils.is_bool(feature.np_dtype):
    return False
  raise ValueError(f"Could not get default value for {feature}")


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

  VERSION = utils.Version("1.0.0")  # This will be replaced in __init__.

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
      **config_kwargs,
  ):
    self._hf_repo_id = hf_repo_id
    self._hf_config = hf_config
    self.config_kwargs = config_kwargs
    tfds_config = convert_config_name(hf_config)
    hf_datasets = lazy_imports_lib.lazy_imports.datasets
    self._hf_builder = hf_datasets.load_dataset_builder(
        self._hf_repo_id, self._hf_config, **self.config_kwargs
    )
    self._hf_info = self._hf_builder.info
    version = str(self._hf_info.version or self._hf_builder.VERSION or "1.0.0")
    self.VERSION = utils.Version(version)  # pylint: disable=invalid-name
    if self._hf_config:
      self._converted_builder_config = dataset_builder.BuilderConfig(
          name=tfds_config,
          version=self.VERSION,
          description=self._hf_info.description,
      )
    else:
      self._converted_builder_config = None
    self.name = from_hf_to_tfds(hf_repo_id)
    self._hf_hub_token = hf_hub_token
    self._hf_num_proc = hf_num_proc
    self._tfds_num_proc = tfds_num_proc
    self._verification_mode = (
        "all_checks" if ignore_verifications else "no_checks"
    )
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
      self, builder_config
  ) -> Optional[dataset_builder.BuilderConfig]:
    return self._converted_builder_config

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
    ds = self._download_and_prepare_for_hf()
    for split in ds.values():
      return split.info

  @py_utils.memoize()
  def _info(self) -> dataset_info_lib.DatasetInfo:
    return dataset_info_lib.DatasetInfo(
        builder=self,
        description=self._hf_info.description,
        features=extract_features(self._hf_features()),
        citation=self._hf_info.citation,
        license=self._hf_info.license,
        supervised_keys=_extract_supervised_keys(self._hf_info),
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
    dataset_info = self._info()
    if self._tfds_num_proc is None:
      for index, example in enumerate(data):
        yield _convert_example(index, example, dataset_info.features)
    else:
      with multiprocessing.Pool(processes=self._tfds_num_proc) as pool:
        examples = pool.starmap(
            functools.partial(_convert_example, features=dataset_info.features),
            enumerate(data),
        )
        yield from examples


def builder(
    name: str, config: Optional[str] = None, **builder_kwargs
) -> HuggingfaceDatasetBuilder:
  hf_repo_id = _from_tfds_to_hf(name)
  return HuggingfaceDatasetBuilder(
      hf_repo_id=hf_repo_id, hf_config=config, **builder_kwargs
  )


def login_to_hf(hf_hub_token: Optional[str] = None):
  """Logs in to Hugging Face Hub with the token as arg or env variable."""
  hf_hub_token = hf_hub_token or os.environ.get("HUGGING_FACE_HUB_TOKEN")
  if hf_hub_token is not None:
    huggingface_hub = lazy_imports_lib.lazy_imports.huggingface_hub
    huggingface_hub.login(token=hf_hub_token)

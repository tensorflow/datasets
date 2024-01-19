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

"""Format-specific dataset builders for CoNLL-like formatted data.

It contains a ConllBuilderConfig and a ConllDatasetBuilder which are used to
initialize TFDS datasets based on CoNLL-like formatted data.

Typical usage example:
class MyConllDataset(tfds.dataset_builders.ConllDatasetBuilder):
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [conll_lib.CONLL_2003_CONFIG]

  def _info(self) -> tfds.core.DatasetInfo:
    ...

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    ...
"""

import collections
from collections.abc import Sequence
from typing import Optional, Union

from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features.features_dict import FeaturesDict


# TODO(b/241346210): Should update ConllBuilderConfig to @dataclasses.dataclass.
class ConllBuilderConfig(dataset_builder.BuilderConfig):
  """Base class for CoNLL-like formatted data configuration.

  Attributes:
    separator: The separator used for splitting feature columns in the input
      lines. For CoNLL-formatted data, this is usually a tab or a space.
    ordered_features: An OrderedDict specifying the features names and their
      type, in the same order as they appear as columns in the input lines.
  """

  def __init__(
      self,
      *,
      separator: str,
      ordered_features: collections.OrderedDict[
          str, feature_lib.FeatureConnector
      ],
      **kwargs,
  ):
    """Initializes the builder config for Conll datasets.

    Args:
      separator: The separator used for splitting feature columns in the input
        lines. For CoNLL-formatted data, this is usually a tab or a space.
      ordered_features: An OrderedDict specifying the features names and their
        type, in the same order as they appear as columns in the input lines.
      **kwargs: keyword arguments forwarded to super.
    """
    super(ConllBuilderConfig, self).__init__(**kwargs)
    self.separator = separator
    self.ordered_features = ordered_features

  @property
  def features_dict(self) -> FeaturesDict:
    return FeaturesDict(self.ordered_features)


class ConllDatasetBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """Base class for CoNLL-like formatted datasets.

  It provides functionalities to ease the processing of CoNLL-like datasets.
  Users can overwrite `_generate_examples` to customize the pipeline.
  """

  BUILDER_CONFIGS: Sequence[ConllBuilderConfig] = []

  @property
  def builder_config(self) -> ConllBuilderConfig:
    """`tfds.core.BuilderConfig` for this builder."""
    return self._builder_config  # pytype: disable=bad-return-type  # always-use-return-annotations

  def create_dataset_info(
      self,
      description: Optional[str] = None,
      supervised_keys: Optional[dataset_info.SupervisedKeysType] = None,
      homepage: Optional[str] = None,
      citation: Optional[str] = None,
  ) -> dataset_info.DatasetInfo:
    """Initializes `dataset_info.DatasetInfo` for Conll datasets.

    Args:
      description: [DEPRECATED] A short, markdown-formatted description of the
        dataset. Prefer placing description in `README.md` file.
      supervised_keys:  Specifies the input structure for supervised learning,
        if applicable for the dataset, used with "as_supervised". Typically this
        is a `(input_key, target_key)` tuple.
      homepage: The homepage of the dataset, if applicable for this dataset.
      citation: [DEPRECATED] The citation to use for this dataset, if applicable
        for this dataset. Prefer placing citations in `CITATIONS.bib` file.

    Returns:
      `dataset_info.DatasetInfo` for Conll datasets, populated with the values
      from the provided arguments.
    """
    return self.dataset_info_from_configs(
        description=description,
        features=self.builder_config.features_dict,
        supervised_keys=supervised_keys,
        homepage=homepage,
        citation=citation,
    )

  def _generate_examples(
      self,
      filepaths: Union[epath.PathLike, list[epath.PathLike]],
  ) -> split_builder_lib.SplitGenerator:
    """Processes CoNLL-like datasets and generate examples.

    Args:
      filepaths: The filepaths of the input data. Could be a list of paths for
        multiple input files, or a single path.

    Yields:
      Generated examples.
    """
    path = filepaths if isinstance(filepaths, list) else [filepaths]

    input_sequences = {feature: [] for feature in self.info.features}

    example_id = 0
    for filepath in path:
      with epath.Path(filepath).open() as f:
        for line in f:
          if line.startswith("-DOCSTART-") or line == "\n" or not line:
            if input_sequences["tokens"]:
              yield example_id, input_sequences
              example_id += 1
              input_sequences = {feature: [] for feature in self.info.features}
          else:
            splits = line.split(self.builder_config.separator)
            if len(splits) != len(self.builder_config.ordered_features):
              raise ValueError(
                  f"Mismatch in the number of features found in line: {line}\n"
                  f"Should be {len(self.builder_config.ordered_features)}, "
                  f"but found {len(splits)}"
              )
            for index, feature in enumerate(
                self.builder_config.ordered_features.keys()
            ):
              input_sequences[feature].append(splits[index].rstrip())

      # Last example from file.
      yield example_id, input_sequences

      # Initializing a new empty example in case of multiple filepaths in path.
      example_id += 1
      input_sequences = {feature: [] for feature in self.info.features}

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

"""Format-specific dataset builders for CoNLL-like formatted data.

It contains a ConllBuilderConfig and a ConllDatasetBuilder which are used to
initialize TFDS datasets based on CoNLL-like formatted data.
"""
from typing import Callable, List, Mapping, Optional, OrderedDict, Sequence, Union

from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import split_builder as split_builder_lib
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features.features_dict import FeaturesDict


def get_conllu_example(
    sentence, example_id, features
) -> Mapping[str, Union[str, Sequence[str]]]:
  """Processes a conllu-annotated sentence into an example to be serialized.

  Args:
    sentence: the annotated sentence parsed with the conllu library.
    example_id: the example_id of the example, which will be used if the `idx`
      feature is present but not defined in the annotated sentence.
    features: the features defined in the output example.

  Returns:
    An example to be serialized.
  """
  example = {}

  for feature in features:
    # Use the idx parsed from the data, example_id if not available.
    if feature == "idx":
      idx = sentence.metadata.get("sent_id", example_id)
      example["idx"] = idx

    # CoNNL-U format stores tokens using the `form` tag.
    elif feature == "tokens":
      example["tokens"] = [token["form"] for token in sentence]

    # CoNNL-U format stores lemmas using the `lemma` tag.
    elif feature == "lemmas":
      example["lemmas"] = [token["lemma"] for token in sentence]

    elif feature == "text":
      if "text" in sentence.metadata:
        text = sentence.metadata["text"]
      else:
        text = " ".join(example["tokens"])
      example["text"] = text

    # All other features are Sequences whose feature name corresponds to
    # the respective tag name in the annotations generated with the
    # conllu library.
    else:
      # UPOS are stored as ClassLabels and are therefore not converted
      # into strings.
      # Future features might follow the same principle, therefore we
      # check for list membership.
      if feature in ["upos"]:
        example[feature] = [token[feature] for token in sentence]
      else:
        example[feature] = [str(token[feature]) for token in sentence]

  return example


def get_xtreme_pos_example(
    sentence, example_id, features
) -> Mapping[str, Union[str, Sequence[str]]]:
  """Processes an annotated sentence into an example for the xtreme_pos dataset.

  This function adds a further check ensuring that, at a given position in a
  sentence, both the token and the upos label are not empty.
  This is done for consistency with the xtreme implementation in other
  libraries, such as HuggingFace (rf. line 955):
  https://github.com/huggingface/datasets/blob/e6f1352fe19679de897f3d962e616936a17094f5/datasets/xtreme/xtreme.py

  Args:
    sentence: the annotated sentence parsed with the conllu library.
    example_id: the example_id of the example, which will be used if the `idx`
      feature is present but not defined in the annotated sentence.
    features: the features defined in the output example.

  Returns:
    An example to be serialized.
  """
  del example_id
  example = {feature: [] for feature in features}
  for token in sentence:
    if token["form"] != "_" and token["upos"] != "_":
      example["tokens"].append(token["form"])
      example["upos"].append(token["upos"])
  return example


# TODO(b/241346210): Should update ConllUBuilderConfig to @dataclasses.dataclass
class ConllUBuilderConfig(dataset_builder.BuilderConfig):
  """Base class for CoNLL-U formatted data configuration.

  Attributes:
    features: An OrderedDict specifying the features names and their type.
    language: The language of the data used to generate the ConllUBuilderConfig.
  """

  def __init__(
      self,
      *,
      features: OrderedDict[str, feature_lib.FeatureConnector],
      language: str,
      **kwargs,
  ):
    """Initializes the builder config for Conll-U formatted datasets.

    Args:
      features: An OrderedDict specifying the features names and their type.
      language: The language of the data used to generate the
        ConllUBuilderConfig.
      **kwargs: keyword arguments forwarded to super.
    """
    super(ConllUBuilderConfig, self).__init__(**kwargs)
    self.features = features
    self.language = language

  @property
  def features_dict(self) -> FeaturesDict:
    return FeaturesDict(self.features)


class ConllUDatasetBuilder(
    dataset_builder.GeneratorBasedBuilder, skip_registration=True
):
  """Base class for CoNLL-like formatted datasets.

  It provides functionalities to ease the processing of CoNLL-like datasets.
  Users can overwrite `_generate_examples` to customize the pipeline.
  """

  BUILDER_CONFIGS: Sequence[ConllUBuilderConfig] = []

  @property
  def builder_config(self) -> ConllUBuilderConfig:
    """`tfds.core.BuilderConfig` for this builder."""
    return self._builder_config

  def create_dataset_info(
      self,
      description: Optional[str] = None,
      supervised_keys: Optional[dataset_info.SupervisedKeysType] = None,
      homepage: Optional[str] = None,
      citation: Optional[str] = None,
  ) -> dataset_info.DatasetInfo:
    """Initializes `dataset_info.DatasetInfo` for Conll-U datasets.

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
      `dataset_info.DatasetInfo` for Conll-U datasets, populated with the values
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
      filepaths: Union[epath.PathLike, List[epath.PathLike]],
      process_example_fn: Callable[
          ..., Mapping[str, Union[str, Sequence[str]]]
      ] = get_conllu_example,
  ) -> split_builder_lib.SplitGenerator:
    """Processes CoNLL-U formatted datasets and generate examples.

    Args:
      filepaths: The filepaths of the input data. Could be a list of paths for
        multiple input files, or a single path.
      process_example_fn: The function used to process a conllu-annotated
        sentence into an example to be serialized. Defaults to
        get_conllu_example.

    Yields:
      Generated examples.
    """
    conllu = lazy_imports_lib.lazy_imports.conllu
    path = filepaths if isinstance(filepaths, list) else [filepaths]

    example_id = 0
    for filepath in path:
      with epath.Path(filepath).open() as data_file:
        annotated_sentences = list(conllu.parse_incr(data_file))
        for sentence in annotated_sentences:
          example = process_example_fn(
              sentence=sentence,
              example_id=example_id,
              features=self.builder_config.features,
          )
          yield example_id, example

          example_id += 1

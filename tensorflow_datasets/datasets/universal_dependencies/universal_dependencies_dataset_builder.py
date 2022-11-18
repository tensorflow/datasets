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

"""universal_dependencies dataset."""

from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib
from tensorflow_datasets.datasets.universal_dependencies import universal_dependencies_utils as ud_utils
import tensorflow_datasets.public_api as tfds

_DATA_URL = "https://raw.githubusercontent.com/UniversalDependencies/"


class Builder(tfds.dataset_builders.ConllUDatasetBuilder):
  """DatasetBuilder for universal_dependencies dataset."""
  BUILDER_CONFIGS = []
  for language in ud_utils.LANGS:
    BUILDER_CONFIGS.append(
        conllu_lib.get_universal_morphology_config(
            language=language,
            description=ud_utils.DESCRIPTIONS[language],
            features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES))

  VERSION = tfds.core.Version("1.0.1")
  RELEASE_NOTES = {
      "1.0.1":
          "Updated config names.",
      "1.0.0":
          "Initial release, which corresponds to Universal Dependencies 2.10.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        homepage="https://universaldependencies.org/",
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = {}
    for split, split_paths in ud_utils.UD_FILEPATHS[
        self.builder_config.language].items():
      paths[split] = ud_utils.prepare_ud_filepaths(
          path_prefix=_DATA_URL, filepaths=split_paths)

    paths_per_split = dl_manager.download_and_extract(paths)

    return {
        split: self._generate_examples(filepaths=split_paths)
        for split, split_paths in paths_per_split.items()
    }

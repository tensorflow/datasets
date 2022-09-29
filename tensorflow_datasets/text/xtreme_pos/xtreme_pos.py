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

"""xtreme_pos dataset."""
import os

import tensorflow as tf
from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder
from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Universal Dependencies (UD) is a framework for consistent annotation of grammar
(parts of speech, morphological features, and syntactic dependencies) across
different human languages. UD is an open community effort with over 200
contributors producing more than 100 treebanks in over 70 languages. If you’re
new to UD, you should start by reading the first part of the Short Introduction
and then browsing the annotation guidelines.
"""

_CITATION = """
@article{nivre2018universal,
  title={Universal Dependencies 2.2},
  author={Nivre, Joakim and Abrams, Mitchell and Agi{\'c}, {\v{Z}}eljko
  and Ahrenberg, Lars and Antonsen, Lene and Aranzabe, Maria Jesus and
  Arutie, Gashaw and Asahara, Masayuki and Ateyah, Luma and Attia,
  Mohammed and others},
  year={2018}
}
"""

_LANGS = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "he": "Hebrew",
    "hi": "Hindi",
    "hu": "Hungarian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "kk": "Kazakh",
    "ko": "Korean",
    "mr": "Marathi",
    "nl": "Dutch",
    "pt": "Portuguese",
    "ru": "Russian",
    "ta": "Tagalog",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Tamil",
    "tr": "Turkish",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "yo": "Yoruba",
    "zh": "Chinese"
}

_DATA_URLS = "https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3105/ud-treebanks-v2.5.tgz"


class XtremePos(tfds.dataset_builders.ConllUDatasetBuilder):
  """DatasetBuilder for xtreme_pos dataset."""

  BUILDER_CONFIGS = []
  for language in _LANGS:
    BUILDER_CONFIGS.append(
        conllu_lib.get_universal_morphology_config(
            language=language,
            features=conllu_lib.XTREME_POS_FEATURES,
            name=f"xtreme_pos_{language}"))

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        description=_DESCRIPTION,
        homepage="https://universaldependencies.org/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download_and_extract(_DATA_URLS)
    subpath = os.path.join(dl_dir, "ud-treebanks-v2.5")
    lang = _LANGS[self.builder_config.language]
    data_dir = os.path.join(subpath, "*_" + lang + "*")
    folders = sorted(tf.io.gfile.glob(data_dir))

    if lang == "Kazakh":
      paths = {"train": [], "test": []}
      for split in paths:
        for folder in folders:
          for file in sorted(tf.io.gfile.listdir(folder)):
            if split in file and file.endswith(".conllu"):
              paths[split].append(os.path.join(folder, file))

    elif lang in ["Tagalog", "Thai", "Yoruba"]:
      paths = {"test": []}
      for folder in folders:
        for file in sorted(tf.io.gfile.listdir(folder)):
          if "test" in file and file.endswith(".conllu"):
            paths["test"].append(os.path.join(folder, file))

    else:
      paths = {"train": [], "dev": [], "test": []}
      for split in paths:
        # We exclude Arabic-NYUAD which does not contains any words, only `_`.
        for folder in folders:
          for file in sorted(tf.io.gfile.listdir(folder)):
            if split in file and file.endswith(
                ".conllu") and "NYUAD" not in folder:
              paths[split].append(os.path.join(folder, file))

    return {  # pylint:disable=g-complex-comprehension
        split: self._generate_examples(
            filepaths=split_files,
            process_example_fn=conllu_dataset_builder.get_xtreme_pos_example)
        for split, split_files in paths.items()
    }

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

"""MLQA: Multilingual Question Answering Dataset."""

import os
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

LANGUAGES = ["ar", "de", "en", "es", "hi", "vi", "zh"]

_DOWNLOAD_URL = "https://dl.fbaipublicfiles.com/MLQA/MLQA_V1.zip"


class MlqaConfig(tfds.core.BuilderConfig):
  """BuilderConfig for MLQA."""

  def __init__(self, language, **kwargs):
    """BuilderConfig for MLQA.

    Args:
      language: string, a valid language code.
      **kwargs: keyword arguments forwarded to super.
    """
    super(MlqaConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs
    )
    self.language = language


class Builder(tfds.core.GeneratorBasedBuilder):
  """MLQA: Multilingual Question Answering Dataset."""

  BUILDER_CONFIGS = [
      MlqaConfig(  # pylint:disable=g-complex-comprehension
          name=lang,
          language=lang,
          description=("MLQA '{}' dev and test splits.").format(lang),
      )
      for lang in LANGUAGES
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=qa_utils.squadlike_features(),
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        homepage="https://github.com/facebookresearch/MLQA",
    )

  def _split_generators(self, dl_manager):
    lang = self.builder_config.language
    filepaths = dl_manager.download_and_extract({
        "test": _DOWNLOAD_URL,
        "validation": _DOWNLOAD_URL,
    })
    filepaths["test"] = os.path.join(
        filepaths["test"],
        "MLQA_V1",
        "test",
        "test-context-{0}-question-{0}.json".format(lang),
    )
    filepaths["validation"] = os.path.join(
        filepaths["validation"],
        "MLQA_V1",
        "dev",
        "dev-context-{0}-question-{0}.json".format(lang),
    )
    return [
        tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
            name=split, gen_kwargs={"filepath": path}
        )
        for split, path in filepaths.items()
    ]

  def _generate_examples(self, filepath):
    return qa_utils.generate_squadlike_examples(filepath)

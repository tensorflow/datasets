# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""XQuAD: Cross-lingual Question Answering Dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_CITATION = """\
@article{Artetxe:etal:2019,
      author    = {Mikel Artetxe and Sebastian Ruder and Dani Yogatama},
      title     = {On the cross-lingual transferability of monolingual representations},
      journal   = {CoRR},
      volume    = {abs/1910.11856},
      year      = {2019},
      archivePrefix = {arXiv},
      eprint    = {1910.11856}
}
"""

_DESCRIPTION = """\
XQuAD (Cross-lingual Question Answering Dataset) is a benchmark dataset for \
evaluating cross-lingual question answering performance. The dataset consists \
of a subset of 240 paragraphs and 1190 question-answer pairs from the \
development set of SQuAD v1.1 (Rajpurkar et al., 2016) together with their \
professional translations into ten languages: Spanish, German, Greek, Russian, \
Turkish, Arabic, Vietnamese, Thai, Chinese, and Hindi. Consequently, the \
dataset is entirely parallel across 11 languages. \
\
To run XQuAD in the default zero-shot setting, use the SQuAD v1.1 training and \
validation data here: https://www.tensorflow.org/datasets/catalog/squad

We also include "translate-train", "translate-dev", and "translate-test" \
splits for each non-English language from XTREME (Hu et al., 2020). These can \
be used to run XQuAD in the "translate-train" or "translate-test" settings.
"""


LANGUAGES = ["ar", "de", "el", "en", "es", "hi", "ru", "th", "tr", "vi", "zh"]

_URL_FORMAT = "https://github.com/deepmind/xquad/raw/master/xquad.{lang}.json"
_XTREME_SQUAD_URL_FORMAT = "https://storage.googleapis.com/xtreme_translations/SQuAD/translate-{split}/squad.translate.{split}.en-{lang}.json"
_XTREME_XQUAD_URL_FORMAT = "https://storage.googleapis.com/xtreme_translations/XQuAD/translate-test/xquad.translate.test.{lang}-en.json"


class XquadConfig(tfds.core.BuilderConfig):
  """BuilderConfig for XQuAD."""

  def __init__(self, language, **kwargs):
    """BuilderConfig for XQuAD.

    Args:
      language: string, a valid language code.
      **kwargs: keyword arguments forwarded to super.
    """
    super(XquadConfig, self).__init__(
        version=tfds.core.Version("2.0.0"), **kwargs)
    self.language = language


class Xquad(tfds.core.GeneratorBasedBuilder):
  """XQuAD: Cross-lingual Question Answering Dataset."""

  BUILDER_CONFIGS = [
      XquadConfig(  # pylint:disable=g-complex-comprehension
          name=lang,
          language=lang,
          description=("XQuAD '{}' test split, with machine-translated "
                       "translate-train/translate-dev/translate-test splits "
                       "from XTREME (Hu et al., 2020).").format(lang),
      ) for lang in LANGUAGES if lang != "en"
  ] + [
      XquadConfig(  # pylint:disable=g-complex-comprehension
          name="en",
          language="en",
          description="XQuAD 'en' test split.",
      )
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=qa_utils.SQUADLIKE_FEATURES,
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        homepage="https://github.com/deepmind/xquad",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    lang = self.builder_config.language

    if lang == "en":
      filepaths = dl_manager.download_and_extract(
          {
              "test": _URL_FORMAT.format(lang=lang),
          }
      )
    else:
      filepaths = dl_manager.download_and_extract(
          {
              "test": _URL_FORMAT.format(lang=lang),
              "translate-train": _XTREME_SQUAD_URL_FORMAT.format(
                  split="train", lang=lang),
              "translate-dev": _XTREME_SQUAD_URL_FORMAT.format(
                  split="dev", lang=lang),
              "translate-test": _XTREME_XQUAD_URL_FORMAT.format(lang=lang),
          }
      )

    return [
        tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
            name=split,
            gen_kwargs={"filepath": path})
        for split, path in filepaths.items()
    ]

  def _generate_examples(self, filepath):
    return qa_utils.generate_squadlike_examples(filepath)

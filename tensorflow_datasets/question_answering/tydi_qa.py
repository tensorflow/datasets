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

"""TyDi QA: Information-Seeking QA in Typologically Diverse Languages."""

# TODO(adarob): Add primary tasks (SelectP and MinSpan).

import os

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.question_answering import qa_utils

_CITATION = """\
@article{tydiqa,
   title = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
  author = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
    year = {2020},
 journal = {Transactions of the Association for Computational Linguistics}
}
"""

_DESCRIPTION = """\
TyDi QA is a question answering dataset covering 11 typologically diverse \
languages with 204K question-answer pairs. The languages of TyDi QA are \
diverse with regard to their typology -- the set of linguistic features that \
each language expresses -- such that we expect models performing well on this \
set to generalize across a large number of the languages in the world. It \
contains language phenomena that would not be found in English-only corpora. \
To provide a realistic information-seeking task and avoid priming effects, \
questions are written by people who want to know the answer, but don't know \
the answer yet, (unlike SQuAD and its descendents) and the data is collected \
directly in each language without the use of translation (unlike MLQA and \
XQuAD).

IMPORTANT:  Please choose your training split carefully.

Training splits:

'train': This is the GoldP task from the original TyDi QA paper \
[https://arxiv.org/abs/2003.05002] that has original-language labeled \
training data.

'translate-train-*': These splits are the automatic translations from English \
to each target language used in the translate-train baselines in the XTREME \
paper [https://arxiv.org/abs/2003.11080]. This purposefully ignores the \
non-English TyDiQA-GoldP training data to simulate the transfer learning \
scenario where original-language data is not available and system builders \
must rely on labeled English data plus existing machine translation systems.

Typically, you should use EITHER the train or translate-train split, but not both.
"""

LANGUAGES = {
    "ar": "arabic",
    "bn": "bengali",
    "en": "english",
    "fi": "finnish",
    "id": "indonesian",
    "ko": "korean",
    "ru": "russian",
    "sw": "swahili",
    "te": "telugu",
}

_GOLD_URL_PREFIX = "https://storage.googleapis.com/tydiqa/v1.1/tydiqa-goldp-v1.1-"
_GOLD_TRANSLATE_URL_FORMAT = "https://storage.googleapis.com/xtreme_translations/TyDiQA-GoldP/translate-train/tydiqa.translate.train.en-{lang_iso}.json"


class TydiQAConfig(tfds.core.BuilderConfig):
  """BuilderConfig for TydiQa."""


class TydiQA(tfds.core.GeneratorBasedBuilder):
  """TyDi QA: Information-Seeking QA in Typologically Diverse Languages."""

  BUILDER_CONFIGS = [
      TydiQAConfig(
          name="goldp",
          description="Gold passage (GoldP) task (https://github.com/google-research-datasets/tydiqa/tree/master/gold_passage_baseline)."
      ),
  ]

  VERSION = tfds.core.Version("3.0.0")
  RELEASE_NOTES = {
      "3.0.0":
          "Fixes issue with a number of examples where answer spans are "
          "misaligned due to context white-space removal. This change impacts "
          "roughly 25% of train and dev examples."
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=qa_utils.squadlike_features(),
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        homepage="https://github.com/google-research-datasets/tydiqa",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    urls_to_download = {
        "train": _GOLD_URL_PREFIX + "train.json",
        "validation": _GOLD_URL_PREFIX + "dev.json",
        "lang-validation": _GOLD_URL_PREFIX + "dev.tgz",
    }
    for lang_iso in LANGUAGES:
      if lang_iso == "en":
        continue
      urls_to_download[
          f"translate-train-{lang_iso}"] = _GOLD_TRANSLATE_URL_FORMAT.format(
              lang_iso=lang_iso)
    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepath": downloaded_files["train"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": downloaded_files["validation"]}),
    ] + [
        tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
            name=f"validation-{lang_iso}",
            gen_kwargs={
                "filepath":
                os.path.join(downloaded_files["lang-validation"],
                             f"tydiqa-goldp-v1.1-dev/tydiqa-goldp-dev-{lang_name}.json")
            })
        for lang_iso, lang_name in LANGUAGES.items()
    ] + [
        tfds.core.SplitGenerator(  # pylint:disable=g-complex-comprehension
            name=f"translate-train-{lang_iso}",
            gen_kwargs={
                "filepath": downloaded_files[f"translate-train-{lang_iso}"]
                })
        for lang_iso, lang_name in LANGUAGES.items() if lang_iso != "en"
    ]

  def _generate_examples(self, filepath):
    return qa_utils.generate_squadlike_examples(filepath)

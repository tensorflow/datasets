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

"""tatoeba dataset."""
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This data is extracted from the Tatoeba corpus, dated Saturday 2018/11/17.

For each languages, we have selected 1000 English sentences and their
translations, if available. Please check this paper for a description of the
languages, their families and  scripts as well as baseline results.

Please note that the English sentences are not identical for all language pairs.
This means that the results are not directly comparable across languages.
"""

_CITATION = """
@article{tatoeba,
          title={Massively Multilingual Sentence Embeddings for Zero-Shot
                   Cross-Lingual Transfer and Beyond},
          author={Mikel, Artetxe and Holger, Schwenk,},
          journal={arXiv:1812.10464v2},
          year={2018}
}

@InProceedings{TIEDEMANN12.463,
  author = {J{\"o}rg}rg Tiedemann},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {Proceedings of the Eight International Conference on Language Resources and Evaluation (LREC'12)},
  year = {2012},
  month = {may},
  date = {23-25},
  address = {Istanbul, Turkey},
  editor = {Nicoletta Calzolari (Conference Chair) and Khalid Choukri and Thierry Declerck and Mehmet Ugur Dogan and Bente Maegaard and Joseph Mariani and Jan Odijk and Stelios Piperidis},
  publisher = {European Language Resources Association (ELRA)},
  isbn = {978-2-9517408-7-7},
  language = {english}
}
"""

_LANGS = {
    "af": "afr",
    "ar": "ara",
    "bg": "bul",
    "bn": "ben",
    "de": "deu",
    "el": "ell",
    "es": "spa",
    "et": "est",
    "eu": "eus",
    "fa": "pes",
    "fi": "fin",
    "fr": "fra",
    "he": "heb",
    "hi": "hin",
    "hu": "hun",
    "id": "ind",
    "it": "ita",
    "ja": "jpn",
    "jv": "jav",
    "ka": "kat",
    "kk": "kaz",
    "ko": "kor",
    "ml": "mal",
    "mr": "mar",
    "nl": "nld",
    "pt": "por",
    "ru": "rus",
    "sw": "swh",
    "ta": "tam",
    "te": "tel",
    "th": "tha",
    "tl": "tgl",
    "tr": "tur",
    "ur": "urd",
    "vi": "vie",
    "zh": "cmn",
}

_DATA_URLS = "https://raw.githubusercontent.com/facebookresearch/LASER/main/data/tatoeba/v1"


class TatoebaConfig(tfds.core.BuilderConfig):
  """Configuration Class for Tatoeba."""

  def __init__(self, *, language, **kwargs):
    if language not in _LANGS:
      raise ValueError("language must be one of {}".format(list(_LANGS.keys())))

    super(TatoebaConfig, self).__init__(**kwargs)
    self.language = language


class Tatoeba(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for tatoeba dataset."""
  BUILDER_CONFIGS = [
      TatoebaConfig(  # pylint: disable=g-complex-comprehension
          name="tatoeba_" + language,
          language=language,
      ) for language in _LANGS.keys()
  ]

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "source_sentence": tfds.features.Text(),
            "target_sentence": tfds.features.Text(),
            "source_language": tfds.features.Text(),
            "target_language": tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage="http://opus.nlpl.eu/Tatoeba.php",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    lang = _LANGS[self.builder_config.language]

    tatoeba_source_path = os.path.join(
        _DATA_URLS, "tatoeba.{lang}-eng.{lang}".format(lang=lang))
    tatoeba_eng_path = os.path.join(_DATA_URLS,
                                    "tatoeba.{}-eng.eng".format(lang))

    archive = dl_manager.download_and_extract({
        "tatoeba_source_data": tatoeba_source_path,
        "tatoeba_eng_data": tatoeba_eng_path
    })

    return {
        "train":
            self._generate_examples(
                source_file=archive["tatoeba_source_data"],
                target_file=archive["tatoeba_eng_data"]),
    }

  def _generate_examples(self, source_file, target_file):
    """Yields examples."""
    source_sentences = []
    target_sentences = []
    with tf.io.gfile.GFile(source_file, "rb") as f1:
      for row in f1:
        source_sentences.append(row)
    with tf.io.gfile.GFile(target_file, "rb") as f2:
      for row in f2:
        target_sentences.append(row)
    for i in range(len(source_sentences)):
      yield i, {
          "source_sentence": source_sentences[i],
          "target_sentence": target_sentences[i],
          "source_language": self.builder_config.language,
          "target_language": "en",
      }

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

"""opus dataset."""

import os
from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Tiedemann2012ParallelData,
  author = {Tiedemann, J},
  title = {Parallel Data, Tools and Interfaces in OPUS},
  booktitle = {LREC}
  year = {2012}}
"""

_DESCRIPTION = """
OPUS is a collection of translated texts from the web.

Create your own config to choose which data / language pair to load.

```
config = tfds.translate.opus.OpusConfig(
    version=tfds.core.Version('0.1.0'),
    language_pair=("de", "en"),
    subsets=["GNOME", "EMEA"]
)
builder = tfds.builder("opus", config=config)
```
"""


class SubDataset():
  """Class to keep track of information on a sub-dataset of OPUS."""

  def __init__(self, name, description, homepage, url, languages):
    """Sub-dataset of OPUS.

    Args:
      name: `string`, a unique dataset identifier.
      description: `string`, a description of the dataset.
      homepage: `string`, homepage of the dataset.
      url: `string`, download url for the dataset.
      languages: `<list>(string)`, a list of supported languages.
    """
    self.name = name
    self.description = description
    self.homepage = homepage
    self.url = url

    sorted_languages = sorted(languages)
    language_pairs = []
    for idx, source in enumerate(sorted_languages):
      for target in sorted_languages[idx + 1:]:
        language_pairs.append((source, target))

    self.language_pairs = language_pairs

DATASET_MAP = {ds.name: ds for ds in [  # pylint:disable=g-complex-comprehension
    # pylint:disable=line-too-long
    SubDataset(
        name="EMEA",
        description="A parallel corpus made out of PDF documents from the European Medicines Agency.",
        homepage="http://opus.nlpl.eu/EMEA.php",
        url="http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/",
        languages=["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hu", "it", "lt", "lv", "mt", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
    ),
    SubDataset(
        name="JRC-Acquis",
        description="A collection of legislative text of the European Union and currently comprises selected texts written between the 1950s and now.",
        homepage="http://opus.nlpl.eu/JRC-Acquis.php",
        url="http://opus.nlpl.eu/download.php?f=JRC-Acquis/",
        languages=["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hu", "it", "lt", "lv", "mt", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]
    ),
    SubDataset(
        name="Tanzil",
        description="A collection of Quran translations compiled by the Tanzil project.",
        homepage="http://opus.nlpl.eu/Tanzil.php",
        url="http://opus.nlpl.eu/download.php?f=Tanzil/v1/moses/",
        languages=["am", "ar", "az", "bg", "bn", "bs", "cs", "de", "dv", "en", "es", "fa", "fr", "ha", "hi", "id", "it", "ja", "ko", "ku", "ml", "ms", "nl", "no", "pl", "pt", "ro", "ru", "sd", "so", "sq", "sv", "sw", "ta", "tg", "th", "tr", "tt", "ug", "ur", "uz", "zh"]
    ),
    SubDataset(
        name="GNOME",
        description="A parallel corpus of GNOME localization files. Source: https://l10n.gnome.org",
        homepage="http://opus.nlpl.eu/GNOME.php",
        url="http://opus.nlpl.eu/download.php?f=GNOME/v1/moses/",
        languages=["af", "am", "an", "ang", "ar", "ar_TN", "ara", "as", "ast", "az", "az_IR", "bal", "be", "bem", "bg", "bg_BG", "bn", "bn_IN", "bo", "br", "brx", "bs", "ca", "cat", "crh", "cs", "csb", "cy", "da", "da_DK", "de", "de_CH", "dv", "dz", "el", "en", "en_AU", "en_CA", "en_GB", "en_NZ", "en_US", "en_ZA", "eo", "es", "es_AR", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_ES", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PE", "es_PR", "es_SV", "es_UY", "es_VE", "et", "eu", "fa", "fa_IR", "fi", "fo", "foo", "fr", "fur", "fy", "ga", "gd", "gl", "gn", "gr", "gu", "gv", "ha", "he", "hi", "hi_IN", "hr", "hu", "hy", "ia", "id", "ig", "io", "is", "it", "it_IT", "ja", "jbo", "ka", "kg", "kk", "km", "kn", "ko", "kr", "ks", "ku", "ky", "la", "lg", "li", "lo", "lt", "lv", "mai", "mg", "mi", "mk", "ml", "mn", "mr", "ms", "ms_MY", "mt", "mus", "my", "nb", "nb_NO", "nds", "ne", "nhn", "nl", "nn", "nn_NO", "no", "no_nb", "nqo", "nr", "nso", "oc", "or", "os", "pa", "pl", "ps", "pt", "pt_BR", "pt_PT", "quz", "ro", "ru", "rw", "si", "sk", "sl", "so", "sq", "sr", "sr_ME", "st", "sv", "sw", "szl", "ta", "te", "tg", "tg_TJ", "th", "tk", "tl", "tl_PH", "tmp", "tr", "tr_TR", "ts", "tt", "ug", "uk", "ur", "ur_PK", "uz", "vi", "vi_VN", "wa", "xh", "yi", "yo", "zh_CN", "zh_HK", "zh_TW", "zu"]
    ),
    SubDataset(
        name="KDE4",
        description="A parallel corpus of KDE4 localization files (v.2).",
        homepage="http://opus.nlpl.eu/KDE4.php",
        url="http://opus.nlpl.eu/download.php?f=KDE4/v2/moses/",
        languages=["af", "ar", "as", "ast", "be", "bg", "bn", "bn_IN", "br", "ca", "crh", "cs", "csb", "cy", "da", "de", "el", "en", "en_GB", "eo", "es", "et", "eu", "fa", "fi", "fr", "fy", "ga", "gl", "gu", "ha", "he", "hi", "hne", "hr", "hsb", "hu", "hy", "id", "is", "it", "ja", "ka", "kk", "km", "kn", "ko", "ku", "lb", "lt", "lv", "mai", "mk", "ml", "mr", "ms", "mt", "nb", "nds", "ne", "nl", "nn", "nso", "oc", "or", "pa", "pl", "ps", "pt", "pt_BR", "ro", "ru", "rw", "se", "si", "sk", "sl", "sr", "sv", "ta", "te", "tg", "th", "tr", "uk", "uz", "vi", "wa", "xh", "zh_CN", "zh_HK", "zh_TW"]
    ),
    SubDataset(
        name="PHP",
        description="A parallel corpus originally extracted from http://se.php.net/download-docs.php.",
        homepage="http://opus.nlpl.eu/PHP.php",
        url="http://opus.nlpl.eu/download.php?f=PHP/v1/moses/",
        languages=["cs", "de", "en", "es", "fi", "fr", "he", "hu", "it", "ja", "ko", "nl", "pl", "pt_BR", "ro", "ru", "sk", "sl", "sv", "tr", "tw", "zh", "zh_TW"]
    ),
    SubDataset(
        name="Ubuntu",
        description="A parallel corpus of Ubuntu localization files. Source: https://translations.launchpad.net",
        homepage="http://opus.nlpl.eu/Ubuntu.php",
        url="http://opus.nlpl.eu/download.php?f=Ubuntu/v14.10/moses/",
        languages=["ace", "af", "ak", "am", "an", "ang", "ar", "ar_SY", "ary", "as", "ast", "az", "ba", "bal", "be", "bem", "ber", "bg", "bho", "bn", "bn_IN", "bo", "br", "brx", "bs", "bua", "byn", "ca", "ce", "ceb", "chr", "ckb", "co", "crh", "cs", "csb", "cv", "cy", "da", "de", "de_AT", "de_DE", "dsb", "dv", "dz", "el", "en", "en_AU", "en_CA", "en_GB", "en_NZ", "en_US", "eo", "es", "es_AR", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_ES", "es_GT", "es_HN", "es_MX", "es_NI", "es_PA", "es_PE", "es_PR", "es_SV", "es_UY", "es_VE", "et", "eu", "fa", "fa_AF", "ff", "fi", "fil", "fo", "fr", "fr_CA", "fr_FR", "frm", "frp", "fur", "fy", "ga", "gd", "gl", "gn", "grc", "gu", "guc", "gv", "ha", "haw", "he", "hi", "hil", "hne", "hr", "hsb", "ht", "hu", "hy", "ia", "id", "ig", "io", "is", "it", "iu", "ja", "jbo", "jv", "ka", "kab", "kg", "kk", "kl", "km", "kn", "ko", "kok", "ks", "ksh", "ku", "kw", "ky", "la", "lb", "lg", "li", "lij", "lld", "ln", "lo", "lt", "ltg", "lv", "mai", "mg", "mh", "mhr", "mi", "miq", "mk", "ml", "mn", "mo", "mr", "ms", "mt", "mus", "my", "nan", "nap", "nb", "nds", "ne", "nhn", "nl", "nl_NL", "nn", "no", "nso", "ny", "oc", "oj", "om", "or", "os", "pa", "pam", "pap", "pl", "pms", "pmy", "ps", "pt", "pt_BR", "pt_PT", "qu", "rm", "ro", "rom", "ru", "rw", "sa", "sc", "sco", "sd", "se", "shn", "shs", "si", "sk", "sl", "sm", "sml", "sn", "so", "son", "sq", "sr", "st", "sv", "sw", "syr", "szl", "ta", "ta_LK", "te", "tet", "tg", "th", "ti", "tk", "tl", "tlh", "tr", "trv", "ts", "tt", "ug", "uk", "ur", "uz", "ve", "vec", "vi", "wa", "wae", "wo", "xal", "xh", "yi", "yo", "zh", "zh_CN", "zh_HK", "zh_TW", "zu", "zza"]
    ),
    SubDataset(
        name="OpenOffice",
        description="A collection of documents from http://www.openoffice.org/.",
        homepage="http://opus.nlpl.eu/OpenOffice-v2.php",
        url="http://opus.nlpl.eu/download.php?f=OpenOffice/v2/moses/",
        languages=["de", "en", "es", "fr", "jp", "sv"]
    ),
    SubDataset(
        name="OpenSubtitles",
        description="A new collection of translated movie subtitles from http://www.opensubtitles.org/",
        homepage="http://opus.nlpl.eu/OpenSubtitles-v2018.php",
        url="http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/moses/",
        languages=["af", "ar", "bg", "bn", "br", "bs", "ca", "cs", "da", "de", "el", "en", "eo", "es", "et", "eu", "fa", "fi", "fr", "gl", "he", "hi", "hr", "hu", "hy", "id", "is", "it", "ja", "ka", "kk", "ko", "lt", "lv", "mk", "ml", "ms", "nl", "no", "pl", "pt", "pt_br", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "ta", "te", "th", "tl", "tr", "uk", "ur", "vi", "ze_en", "ze_zh", "zh_cn", "zh_tw"]
    )
]}


class OpusConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Opus."""

  def __init__(self, *, language_pair, subsets, **kwargs):
    """BuilderConfig for Opus.

    Args:
      language_pair: `(string, string)`, pair of languages used for translation.
        Should contain 2 letter coded strings (e.g. "de", "en")
      subsets: `<list>(string)`, list of the subdatasets to use.
      **kwargs: keyword arguments forwarded to super.
    """
    sorted_language_pair = sorted(language_pair)
    name = kwargs.get("name", "%s-%s for %s" % (
        sorted_language_pair[0], sorted_language_pair[1], ", ".join(subsets)))

    description = name + " documents"

    super(OpusConfig, self).__init__(
        description=description, **dict(kwargs, name=name))

    self.language_pair = sorted_language_pair
    self.subsets = subsets


class Opus(tfds.core.GeneratorBasedBuilder):
  """OPUS is a collection of translated texts from the web."""

  _KK_SUBSETS = [
      ("medical", ["EMEA"]),
      ("law", ["JRC-Acquis"]),
      ("koran", ["Tanzil"]),
      ("IT", ["GNOME", "KDE4", "PHP", "Ubuntu", "OpenOffice"]),
      ("subtitles", ["OpenSubtitles"])
  ]

  """The following configurations reproduce the evaluation tasks from "Six
  Challenges for Neural Machine Translation" by Philipp Koehn and Rebecca
  Knowles (2017) https://www.aclweb.org/anthology/W17-3204.pdf"""
  BUILDER_CONFIGS = [
      OpusConfig(  # pylint:disable=g-complex-comprehension
          version=tfds.core.Version("0.1.0"),
          language_pair=("de", "en"),
          subsets=subsets,
          name=name
      ) for name, subsets in _KK_SUBSETS
  ]

  @property
  def subsets(self):
    # Return only the datasets that exist for the language pair.
    source, target = self.builder_config.language_pair
    filtered_subsets = []
    for dataset in [DATASET_MAP[name] for name in self.builder_config.subsets]:
      if (source, target) in dataset.language_pairs:
        filtered_subsets.append(dataset)

    return filtered_subsets

  def _info(self):
    src, target = self.builder_config.language_pair
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(
            languages=self.builder_config.language_pair),
        supervised_keys=(src, target),
        homepage="http://opus.nlpl.eu/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    source, target = self.builder_config.language_pair
    file_ext = "%s-%s"%(source, target)

    subsets = []
    for item in self.subsets:
      dl_dir = dl_manager.download_and_extract(
          os.path.join(item.url, "%s.txt.zip"%file_ext))
      source_file = os.path.join(
          dl_dir, "%s.%s.%s"%(item.name, file_ext, source))
      target_file = os.path.join(
          dl_dir, "%s.%s.%s"%(item.name, file_ext, target))
      subsets.append({
          "name": item.name,
          "source_file": source_file,
          "target_file": target_file
      })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"subsets": subsets}
        )
    ]

  def _generate_examples(self, subsets):
    source, target = self.builder_config.language_pair

    for item in subsets:
      logging.info("Generating examples from: %s", item["name"])
      source_file = item["source_file"]
      target_file = item["target_file"]

      gens = [_gen_line(source_file), _gen_line(target_file)]
      for idx, (source_sent, target_sent) in enumerate(zip(*gens)):
        result = {source: source_sent, target: target_sent}
        if all(result.values()):
          key = "%s/%d"%(item["name"], idx)
          yield key, result


def _gen_line(filename):
  """Returns sentences from an OPUS data file."""
  with tf.io.gfile.GFile(filename) as f:
    for line in f:
      yield line

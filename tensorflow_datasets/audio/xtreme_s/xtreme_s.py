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

# coding=utf-8
#  Copyright 2022 The TensorFlow Authors
#  Copyright 2022 The HuggingFace Dataset Authors
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
"""Data for the XTREME-S Benchmark.

This corresponds to XTREME-S on HugginFace, defined at:
https://huggingface.co/datasets/google/xtreme_s/blob/main/xtreme_s.py
"""

import collections
import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{conneau2022xtreme,
  title={XTREME-S: Evaluating Cross-lingual Speech Representations},
  author={Conneau, Alexis and Bapna, Ankur and Zhang, Yu and Ma, Min and von Platen, Patrick and Lozhkov, Anton and Cherry, Colin and Jia, Ye and Rivera, Clara and Kale, Mihir and others},
  journal={arXiv preprint arXiv:2203.10752},
  year={2022}
}
"""

_DESCRIPTION = """\
XTREME-S covers four task families: speech recognition, classification, speech-to-text translation and retrieval. Covering 102
languages from 10+ language families, 3 different domains and 4
task families, XTREME-S aims to simplify multilingual speech
representation evaluation, as well as catalyze research in “universal” speech representation learning.

In this version, only the FLEURS dataset is provided, which covers speech
recognition and speech-to-text translation.
"""

# Full English name to language subtag.
_FLEURS_LANG_TO_ID = collections.OrderedDict([
    ("Afrikaans", "af"), ("Amharic", "am"), ("Arabic", "ar"),
    ("Armenian", "hy"), ("Assamese", "as"), ("Asturian", "ast"),
    ("Azerbaijani", "az"), ("Belarusian", "be"), ("Bengali", "bn"),
    ("Bosnian", "bs"), ("Bulgarian", "bg"), ("Burmese", "my"),
    ("Catalan", "ca"), ("Cebuano", "ceb"), ("Mandarin Chinese", "cmn_hans"),
    ("Cantonese Chinese", "yue_hant"), ("Croatian", "hr"), ("Czech", "cs"),
    ("Danish", "da"), ("Dutch", "nl"), ("English", "en"), ("Estonian", "et"),
    ("Filipino", "fil"), ("Finnish", "fi"), ("French", "fr"), ("Fula", "ff"),
    ("Galician", "gl"), ("Ganda", "lg"), ("Georgian", "ka"), ("German", "de"),
    ("Greek", "el"), ("Gujarati", "gu"), ("Hausa", "ha"), ("Hebrew", "he"),
    ("Hindi", "hi"), ("Hungarian", "hu"), ("Icelandic", "is"), ("Igbo", "ig"),
    ("Indonesian", "id"), ("Irish", "ga"), ("Italian", "it"),
    ("Japanese", "ja"), ("Javanese", "jv"), ("Kabuverdianu", "kea"),
    ("Kamba", "kam"), ("Kannada", "kn"), ("Kazakh", "kk"), ("Khmer", "km"),
    ("Korean", "ko"), ("Kyrgyz", "ky"), ("Lao", "lo"), ("Latvian", "lv"),
    ("Lingala", "ln"), ("Lithuanian", "lt"), ("Luo", "luo"),
    ("Luxembourgish", "lb"), ("Macedonian", "mk"), ("Malay", "ms"),
    ("Malayalam", "ml"), ("Maltese", "mt"), ("Maori", "mi"), ("Marathi", "mr"),
    ("Mongolian", "mn"), ("Nepali", "ne"), ("Northern-Sotho", "nso"),
    ("Norwegian", "nb"), ("Nyanja", "ny"), ("Occitan", "oc"), ("Oriya", "or"),
    ("Oromo", "om"), ("Pashto", "ps"), ("Persian", "fa"), ("Polish", "pl"),
    ("Portuguese", "pt"), ("Punjabi", "pa"), ("Romanian", "ro"),
    ("Russian", "ru"), ("Serbian", "sr"), ("Shona", "sn"), ("Sindhi", "sd"),
    ("Slovak", "sk"), ("Slovenian", "sl"), ("Somali", "so"),
    ("Sorani-Kurdish", "ckb"), ("Spanish", "es"), ("Swahili", "sw"),
    ("Swedish", "sv"), ("Tajik", "tg"), ("Tamil", "ta"), ("Telugu", "te"),
    ("Thai", "th"), ("Turkish", "tr"), ("Ukrainian", "uk"), ("Umbundu", "umb"),
    ("Urdu", "ur"), ("Uzbek", "uz"), ("Vietnamese", "vi"), ("Welsh", "cy"),
    ("Wolof", "wo"), ("Xhosa", "xh"), ("Yoruba", "yo"), ("Zulu", "zu")
])

# Short name (language subtag) to full English name.
_FLEURS_LANG_SHORT_TO_LONG = {v: k for k, v in _FLEURS_LANG_TO_ID.items()}

# Language codes, lowercase, underscore-separated versions of BCP-47 tags,
# including language and region subtags, and sometimes script subtags.
_FLEURS_LANG = sorted([
    "af_za", "am_et", "ar_eg", "as_in", "ast_es", "az_az", "be_by", "bn_in",
    "bs_ba", "ca_es", "ceb_ph", "cmn_hans_cn", "yue_hant_hk", "cs_cz", "cy_gb",
    "da_dk", "de_de", "el_gr", "en_us", "es_419", "et_ee", "fa_ir", "ff_sn",
    "fi_fi", "fil_ph", "fr_fr", "ga_ie", "gl_es", "gu_in", "ha_ng", "he_il",
    "hi_in", "hr_hr", "hu_hu", "hy_am", "id_id", "ig_ng", "is_is", "it_it",
    "ja_jp", "jv_id", "ka_ge", "kam_ke", "kea_cv", "kk_kz", "km_kh", "kn_in",
    "ko_kr", "ckb_iq", "ky_kg", "lb_lu", "lg_ug", "ln_cd", "lo_la", "lt_lt",
    "luo_ke", "lv_lv", "mi_nz", "mk_mk", "ml_in", "mn_mn", "mr_in", "ms_my",
    "mt_mt", "my_mm", "nb_no", "ne_np", "nl_nl", "nso_za", "ny_mw", "oc_fr",
    "om_et", "or_in", "pa_in", "pl_pl", "ps_af", "pt_br", "ro_ro", "ru_ru",
    "bg_bg", "sd_in", "sk_sk", "sl_si", "sn_zw", "so_so", "sr_rs", "sv_se",
    "sw_ke", "ta_in", "te_in", "tg_tj", "th_th", "tr_tr", "uk_ua", "umb_ao",
    "ur_pk", "uz_uz", "vi_vn", "wo_sn", "xh_za", "yo_ng", "zu_za"
])

# Full English name to language code.
_FLEURS_LONG_TO_LANG = {
    _FLEURS_LANG_SHORT_TO_LONG["_".join(k.split("_")[:-1]) or k]: k
    for k in _FLEURS_LANG
}

# Language code to full English name.
_FLEURS_LANG_TO_LONG = {v: k for k, v in _FLEURS_LONG_TO_LANG.items()}

_FLEURS_GROUP_TO_LONG = collections.OrderedDict({
    "western_european_we": [
        "Asturian", "Bosnian", "Catalan", "Croatian", "Danish", "Dutch",
        "English", "Finnish", "French", "Galician", "German", "Greek",
        "Hungarian", "Icelandic", "Irish", "Italian", "Kabuverdianu",
        "Luxembourgish", "Maltese", "Norwegian", "Occitan", "Portuguese",
        "Spanish", "Swedish", "Welsh"
    ],
    "eastern_european_ee": [
        "Armenian", "Belarusian", "Bulgarian", "Czech", "Estonian", "Georgian",
        "Latvian", "Lithuanian", "Macedonian", "Polish", "Romanian", "Russian",
        "Serbian", "Slovak", "Slovenian", "Ukrainian"
    ],
    "central_asia_middle_north_african_cmn": [
        "Arabic", "Azerbaijani", "Hebrew", "Kazakh", "Kyrgyz", "Mongolian",
        "Pashto", "Persian", "Sorani-Kurdish", "Tajik", "Turkish", "Uzbek"
    ],
    "sub_saharan_african_ssa": [
        "Afrikaans", "Amharic", "Fula", "Ganda", "Hausa", "Igbo", "Kamba",
        "Lingala", "Luo", "Northern-Sotho", "Nyanja", "Oromo", "Shona",
        "Somali", "Swahili", "Umbundu", "Wolof", "Xhosa", "Yoruba", "Zulu"
    ],
    "south_asian_sa": [
        "Assamese", "Bengali", "Gujarati", "Hindi", "Kannada", "Malayalam",
        "Marathi", "Nepali", "Oriya", "Punjabi", "Sindhi", "Tamil", "Telugu",
        "Urdu"
    ],
    "south_east_asian_sea": [
        "Burmese", "Cebuano", "Filipino", "Indonesian", "Javanese", "Khmer",
        "Lao", "Malay", "Maori", "Thai", "Vietnamese"
    ],
    "chinese_japanase_korean_cjk": [
        "Mandarin Chinese", "Cantonese Chinese", "Japanese", "Korean"
    ],
})

# Full English name to group name.
_FLEURS_LONG_TO_GROUP = {  # pylint: disable=g-complex-comprehension
    a: k for k, v in _FLEURS_GROUP_TO_LONG.items() for a in v
}

# Language code to group name.
_FLEURS_LANG_TO_GROUP = {
    _FLEURS_LONG_TO_LANG[k]: v for k, v in _FLEURS_LONG_TO_GROUP.items()
}

_ALL_DATASET_CONFIGS = {
    "fleurs": _FLEURS_LANG,
}

_ALL_CONFIGS = []  # e.g. mls.en, covost.en.sv, ...
for sub_data, langs in _ALL_DATASET_CONFIGS.items():
  for lang in langs:
    _ALL_CONFIGS.append(f"{sub_data}.{lang}")

# add "all" for all datasets except 'BABEL'
_ALL_CONFIGS += [
    "fleurs.all",
]

_DESCRIPTIONS = {
    "fleurs": "FLEURS is the speech version of the FLORES machine translation"
              " benchmark, covering 2000 n-way parallel sentences in n=102"
              " languages.",
}

_CITATIONS = {
    "fleurs":
        """\
@article{fleurs2022arxiv,
  title = {FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech},
  author = {Conneau, Alexis and Ma, Min and Khanuja, Simran and Zhang, Yu and Axelrod, Vera and Dalmia, Siddharth and Riesa, Jason and Rivera, Clara and Bapna, Ankur},
  journal={arXiv preprint arXiv:2205.12446},
  url = {https://arxiv.org/abs/2205.12446},
  year = {2022},
}""",
}

_HOMEPAGE_URLS = {
    "fleurs": "https://arxiv.org/abs/2205.12446",
}

_DATA_URLS = {
    "fleurs": [
        "https://storage.googleapis.com/xtreme_translations/FLEURS102/{}.tar.gz"
    ],
}


class XtremeSConfig(tfds.core.BuilderConfig):
  """BuilderConfig for XTREME-S."""

  def __init__(self, name, dataset_name, lang_name, description, citation,
               homepage, data_urls):
    super().__init__(
        name=name,
        version=tfds.core.Version("2.0.0"),
        release_notes={
            "2.0.0":
                "Initial release on TFDS, FLEURS-only. Named to match version"
                " 2.0.0 on huggingface which has the same FLEURS data ("
                " https://huggingface.co/datasets/google/xtreme_s)."
        },
        description=self.description,
    )
    self.name = name
    self.dataset_name = dataset_name
    self.lang_name = lang_name
    self.description = description
    self.citation = citation
    self.homepage = homepage
    self.data_urls = data_urls


def _build_config(name):
  dataset_name = name.split(".")[0]
  lang_name = ".".join(name.split(".")[1:])

  return XtremeSConfig(
      name=name,
      dataset_name=dataset_name,
      lang_name=lang_name,
      description=_DESCRIPTIONS[dataset_name],
      citation=_CITATIONS[dataset_name],
      homepage=_HOMEPAGE_URLS[dataset_name],
      data_urls=_DATA_URLS[dataset_name],
  )


class XtremeS(tfds.core.GeneratorBasedBuilder):
  """XTREME-S Benchmark datasets."""

  DEFAULT_WRITER_BATCH_SIZE = 1000
  BUILDER_CONFIGS = [_build_config(name) for name in _ALL_CONFIGS]

  def _info(self):
    languages = _ALL_DATASET_CONFIGS[self.builder_config.dataset_name]

    if self.builder_config.dataset_name == "fleurs":
      features = tfds.features.FeaturesDict({
          "id":
              tfds.features.Scalar(
                  tf.dtypes.int32,
                  doc="Source text identifier, consistent across all languages"
                  " to keep n-way parallelism of translations. Since each"
                  " transcription may be spoken by multiple speakers,"
                  " within each language multiple examples will also share"
                  " the same id."),
          "num_samples":
              tfds.features.Scalar(
                  tf.dtypes.int32, doc="Total number of frames in the audio"),
          "path":
              tf.dtypes.string,
          "audio":
              tfds.features.Audio(sample_rate=16_000),
          "transcription":
              tfds.features.Text(doc="Normalized transcription."),
          "raw_transcription":
              tfds.features.Text(doc="Raw Transcription from FLoRes."),
          "gender":
              tfds.features.ClassLabel(names=["male", "female", "other"]),
          "lang_id":
              tfds.features.ClassLabel(names=languages),
          "language":
              tfds.features.Text(
                  doc="Language encoded as lowercase, underscore-separated"
                  "version of a BCP-47 tag."),
          "lang_group_id":
              tfds.features.ClassLabel(
                  names=list(_FLEURS_GROUP_TO_LONG.keys())),
      })

      return tfds.core.DatasetInfo(
          builder=self,
          description=self.builder_config.description + "\n" + _DESCRIPTION,
          features=features,
          supervised_keys=("audio", "transcription"),
          homepage=self.builder_config.homepage,
          citation=self.builder_config.citation + "\n" + _CITATION,
      )

  def _split_generators(self, *args, **kwargs):
    if self.builder_config.dataset_name == "fleurs":
      return self._fleurs_split_generators(*args, **kwargs)

  def _generate_examples(self, *args, **kwargs):
    if self.builder_config.dataset_name == "fleurs":
      yield from self._fleurs_generate_examples(*args, **kwargs)

  def _fleurs_split_generators(self, dl_manager):
    data_url_format = self.builder_config.data_urls[0]

    if self.builder_config.lang_name == "all":
      data_urls = {l: data_url_format.format(l) for l in _FLEURS_LANG}
    else:
      data_urls = {
          self.builder_config.lang_name:
              data_url_format.format(self.builder_config.lang_name)
      }

    archive_path = dl_manager.download_and_extract(data_urls)
    audio_paths = {
        l: os.path.join(v, l, "audio") for l, v in archive_path.items()
    }
    text_paths = {l: os.path.join(v, l) for l, v in archive_path.items()}

    def create_split_generator(split: str,
                               file_prefix: str) -> tfds.core.SplitGenerator:
      return tfds.core.SplitGenerator(
          name=split,
          gen_kwargs={
              "audio_path": {
                  l: os.path.join(v, file_prefix)
                  for l, v in audio_paths.items()
              },
              "text_path": {
                  l: os.path.join(v, f"{file_prefix}.tsv")
                  for l, v in text_paths.items()
              },
          },
      )

    return [
        create_split_generator(
            split=tfds.core.Split.TRAIN, file_prefix="train"),
        create_split_generator(
            split=tfds.core.Split.VALIDATION, file_prefix="dev"),
        create_split_generator(split=tfds.core.Split.TEST, file_prefix="test"),
    ]

  def _fleurs_generate_examples(self, audio_path, text_path):
    key = 0

    gender_to_id = {"MALE": 0, "FEMALE": 1, "OTHER": 2}

    for lang_id in text_path.keys():
      text_file = text_path[lang_id]
      audio_dir = audio_path[lang_id]

      with tf.io.gfile.GFile(text_file, "r") as f:
        lines = f.readlines()
        for line in lines:
          (
              index,
              file_name,
              raw_transcription,
              transcription,
              _,  # character transcription
              num_samples,
              gender,
          ) = line.strip().split("\t")

          lang_group = _FLEURS_LANG_TO_GROUP[lang_id]

          yield key, {
              "id":
                  int(index),
              "path":
                  os.path.join(audio_dir, file_name),
              "audio":
                  os.path.join(audio_dir, file_name),
              "raw_transcription":
                  raw_transcription,
              "transcription":
                  transcription,
              "num_samples":
                  int(num_samples),
              "gender":
                  gender_to_id[gender],
              "lang_id":
                  _FLEURS_LANG.index(lang_id),
              "language":
                  _FLEURS_LANG_TO_LONG[lang_id],
              "lang_group_id":
                  list(_FLEURS_GROUP_TO_LONG.keys()).index(lang_group),
          }
          key += 1

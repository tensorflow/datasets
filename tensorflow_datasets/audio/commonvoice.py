# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Mozilla Common Voice Dataset."""

import collections
import csv
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-6.1-2020-12-11/{}.tar.gz"
_SPLITS = {
    tfds.Split.TRAIN: "train",
    tfds.Split.TEST: "test",
    tfds.Split.VALIDATION: "validated"
}
_GENDER_CLASSES = ["male", "female", "other"]

# OrderedDict to keep collection order constant (en is the default config)
_LANGUAGE_ACCENTS = collections.OrderedDict([
    ("en", [
        "african","australia","bermuda","canada","england","hongkong","indian",
        "ireland","malaysia","newzealand","philippines","scotland","singapore",
        "southatlandtic","us","wales"
    ]),
    ("de", [
        "austria","belgium","brazil","bulgaria","canada","czechia","denmark",
        "finland","france","germany","greece","hungary","italy","kazakhstan",
        "liechtenstein","lithuania","luxembourg","namibia","netherlands",
        "paraguay","poland","romania","russia","slovakia","slovenia",
        "switzerland","turkey","united_kingdom","united_states"

    ]),
   ("fr", [
          "algeria","andorra","austria","belgium","benin","burkina_faso",
          "burundi","cameroon","canada","central_african_republic","chad",
          "comoros","congo_brazzaville","congo_kinshasa","cote_d_ivoire",
          "cyprus","djibouti","equatorial_guinea","france","french_guiana",
          "french_polynesia","gabon","germany","greece","guadeloupe",
          "guinea","haiti","hungary","ireland","italy","lebanon","luxembourg",
          "madagascar","mali","malta","martinique","mauritania","mauritius",
          "mayotte","monaco","morocco","netherlands","new_caledonia","niger",
          "portugal","reunion","romania","rwanda","senegal","seychelles",
          "st_barthelemy","st_martin","st_pierre_et_miquelon","switzerland",
          "syria","togo","tunisia","united_kingdom","united_states","vanuatu",
          "wallis_et_futuna"

    ]),
    ("cy", ["united_kingdom", "other"]),
    ("br", ["gwenedeg","kerneveg","leoneg","tregerieg"]),
    ("cv", []),
    ("tr", ["other"]),
    ("tt", []),
    ("ky", ["other"]),
    ("ga-IE", [ "connachta", "ulaidh","mumhain","other"]),
    ("kab", ["other"]),
    ("ca",
     ["northwestern", "central", "other","valencian","balearic","northern"]),
    ("zh-TW", 
    [
        "changhua_county","chiayi_city","chiayi_county","hong_kong",
        "hsinchu_city","hsinchu_county","hualien_county","kaohsiung_city",
        "keelung_city","kinmen_county","lienchiang_county","miaoli_county",
        "nantou_county","new_taipei_city","penghu_county","pingtung_county",
        "taichung_city","tainan_city","taipei_city","taitung_county",
        "taoyuan_city","yilan_county","yunlin_county"
    ]),
    ("sl", ["other"]),
    ("it", ["other"]),
    ("nl", [
            "aruba","belgium","curacao","france","germany","indonesia","namibia",
            "netherlands","sint_maarten","south_africa","suriname"]),
    ("cnh", ["other"]),
    ("eo", ["internacia", "other"]),
    ("id",[])
])


class CommonVoiceConfig(tfds.core.BuilderConfig):
  """Configuration Class for Mozilla CommonVoice Dataset."""

  def __init__(self, *, language, accents=None, **kwargs):
    """Constructs CommonVoiceConfig.
    Args:
     language: `str`, one of [ca, nl, br, de, sl, cy, en, kab, tt, zh-TW, eo,
       it, fr, ga-IE, tr, ky, cnh, cv]. Language Code of the Dataset to be used.
     accents: `list[str]`, labels for the accents of the language
     **kwargs: keywords arguments forwarded to super
    """
    if language not in _LANGUAGE_ACCENTS:
      raise ValueError("language must be one of {}. Not: {}".format(
          list(_LANGUAGE_ACCENTS.keys()), language))
    self.language = language
    self.accents = accents

    kwargs.setdefault("name", language)
    kwargs.setdefault("description", "Language Code: %s" % language)
    kwargs.setdefault("version", tfds.core.Version("1.0.0"))
    super(CommonVoiceConfig, self).__init__(**kwargs)


class CommonVoice(tfds.core.GeneratorBasedBuilder):
  """Mozilla Common Voice Dataset."""
  BUILDER_CONFIGS = [
      CommonVoiceConfig(language=l, accents=a)
      for l, a in _LANGUAGE_ACCENTS.items()
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        description=("Mozilla Common Voice Dataset"),
        builder=self,
        features=tfds.features.FeaturesDict({
            "client_id":
                tfds.features.Text(),
            "upvotes":
                tf.int32,
            "downvotes":
                tf.int32,
            "age":
                tfds.features.Text(),
            "gender":
                tfds.features.ClassLabel(names=_GENDER_CLASSES),
            "accent":
                tfds.features.ClassLabel(names=self.builder_config.accents),
            "sentence":
                tfds.features.Text(),
            "voice":
                tfds.features.Audio(),
        }),
        homepage="https://voice.mozilla.org/en/datasets",
    )

  def _split_generators(self, dl_manager):
    dl_path = dl_manager.download_and_extract(
        _DOWNLOAD_URL.format(self.builder_config.language))
    dl_path=os.path.join(dl_path,"cv-corpus-6.1-2020-12-11")
    dl_path=os.path.join(dl_path,self.builder_config.language)
    clip_folder = os.path.join(dl_path, "clips")
    return [
        tfds.core.SplitGenerator(  # pylint: disable=g-complex-comprehension
            name=k,
            gen_kwargs={
                "audio_path": clip_folder,
                "label_path": os.path.join(dl_path, "%s.tsv" % v)
            },
        ) for k, v in _SPLITS.items()
    ]

  def _generate_examples(self, audio_path, label_path):
    """Generate Voice samples and statements given the data paths.
    
    Args:
      audio_path: str, path to audio storage folder
      label_path: str, path to the label files
    Yields:
      example: The example `dict`
    """
    with tf.io.gfile.GFile(label_path) as file_:
      dataset = csv.DictReader(file_, delimiter="\t")
      for i, row in enumerate(dataset):
        file_path = os.path.join(audio_path, "%s" % row["path"])
        if tf.io.gfile.exists(file_path):
          yield i, {
              "client_id": row["client_id"],
              "voice": file_path,
              "sentence": row["sentence"],
              "upvotes": int(row["up_votes"]) if row["up_votes"] else 0,
              "downvotes": int(row["down_votes"]) if row["down_votes"] else 0,
              "age": row["age"],
              "gender": row["gender"] if row["gender"] else -1,
              "accent": row["accent"] if row["accent"] else -1
          }
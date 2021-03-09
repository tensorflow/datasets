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

"""wikiann dataset."""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
WikiANN (sometimes called PAN-X) is a multilingual named entity recognition \
dataset consisting of Wikipedia articles annotated with LOC (location), PER \
(person), and ORG (organisation) tags in the IOB2 format. This version \
corresponds to the balanced train, dev, and test splits of Rahimi et al. \
(2019), which supports 176 of the 282 languages from the original WikiANN \
corpus.
"""

_CITATION = """
@inproceedings{rahimi-etal-2019-massively,
    title = "Massively Multilingual Transfer for {NER}",
    author = "Rahimi, Afshin  and
      Li, Yuan  and
      Cohn, Trevor",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association \
    for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-1015",
    pages = "151--164",
}
"""

URL = "https://www.dropbox.com/s/12h3qqog6q4bjve/panx_dataset.tar?dl=1"

LANGS = [
    "ace", "af", "als", "am", "ang", "an", "arc", "ar", "arz", "as", "ast",
    "ay", "az", "bar", "ba", "bat-smg", "be", "be-x-old", "bg", "bh", "bn",
    "bo", "br", "bs", "ca", "cbk-zam", "cdo", "ceb", "ce", "ckb", "co", "crh",
    "csb", "cs", "cv", "cy", "da", "de", "diq", "dv", "el", "eml", "en", "eo",
    "es", "et", "eu", "ext", "fa", "fi", "fiu-vro", "fo", "frr", "fr", "fur",
    "fy", "gan", "ga", "gd", "gl", "gn", "gu", "hak", "he", "hi", "hr", "hsb",
    "hu", "hy", "ia", "id", "ig", "ilo", "io", "is", "it", "ja", "jbo", "jv",
    "ka", "kk", "km", "kn", "ko", "ksh", "ku", "ky", "la", "lb", "lij", "li",
    "lmo", "ln", "lt", "lv", "map-bms", "mg", "mhr", "min", "mi", "mk", "ml",
    "mn", "mr", "ms", "mt", "mwl", "my", "mzn", "nap", "nds", "ne", "nl", "nn",
    "no", "nov", "oc", "or", "os", "pa", "pdc", "pl", "pms", "pnb", "ps", "pt",
    "qu", "rm", "ro", "ru", "rw", "sah", "sa", "scn", "sco", "sd", "sh",
    "simple", "si", "sk", "sl", "so", "sq", "sr", "su", "sv", "sw", "szl", "ta",
    "te", "tg", "th", "tk", "tl", "tr", "tt", "ug", "uk", "ur", "uz", "vec",
    "vep", "vi", "vls", "vo", "war", "wa", "wuu", "xmf", "yi", "yo", "zea",
    "zh-classical", "zh-min-nan", "zh", "zh-yue"
]


class WikiannConfig(tfds.core.BuilderConfig):
  """ConfigurationClass for wikiann dataset."""

  def __init__(self, *, language, **kwargs):
    if language not in LANGS:
      raise ValueError("language must be one of {}".format(list(LANGS)))

    super(WikiannConfig, self).__init__(**kwargs)
    self.language = language


class Wikiann(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wikiann dataset."""

  BUILDER_CONFIGS = [
      WikiannConfig(  # pylint: disable=g-complex-comprehension
          name=language,
          description=("Wikiann {} train/dev/test splits".format(language)),
          version="1.0.0",
          language=language,
      ) for language in LANGS
  ]

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = tfds.features.FeaturesDict({
        "tokens":
            tfds.features.Sequence(tfds.features.Text()),
        "tags":
            tfds.features.Sequence(
                tfds.features.ClassLabel(names=[
                    "O",
                    "B-PER",
                    "I-PER",
                    "B-ORG",
                    "I-ORG",
                    "B-LOC",
                    "I-LOC",
                ])),
        "langs":
            tfds.features.Sequence(tfds.features.Text()),
    })
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        supervised_keys=None,
        homepage="https://github.com/afshinrahimi/mmner",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(URL)
    subpath = dl_manager.extract(
        os.path.join(path, self.builder_config.language + ".tar.gz"))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"filepath": os.path.join(subpath, "dev")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"filepath": os.path.join(subpath, "test")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"filepath": os.path.join(subpath, "train")},
        ),
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""

    key = 1
    with tf.io.gfile.GFile(filepath, "r") as f:
      tokens = []
      tags = []
      langs = []
      for line in f:
        if line.startswith("-DOCSTART-") or line == "" or line == "\n":
          if tokens:
            yield key, {"tokens": tokens, "tags": tags, "langs": langs}
            key += 1
            tokens = []
            tags = []
            langs = []
        else:
          # wikiann data is tab separated
          splits = line.split("\t")
          # strip out language prefix
          langs.append(splits[0].split(":")[0])
          tokens.append(":".join(splits[0].split(":")[1:]))
          if len(splits) > 1:
            tags.append(splits[-1].replace("\n", ""))
          else:
            # examples have no label in test set
            tags.append("O")
      if tokens:
        yield key, {"tokens": tokens, "tags": tags, "langs": langs}

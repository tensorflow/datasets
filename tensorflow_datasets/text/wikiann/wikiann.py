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

"""wikiann dataset."""

import os
import tensorflow as tf
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


def tags_to_spans(tags):
  """Convert tags to spans."""
  spans = set()
  span_start = 0
  span_end = 0
  active_conll_tag = None
  for index, string_tag in enumerate(tags):
    # Actual BIO tag.
    bio_tag = string_tag[0]
    assert bio_tag in ["B", "I", "O"], "Invalid Tag"
    conll_tag = string_tag[2:]
    if bio_tag == "O":
      # The span has ended.
      if active_conll_tag:
        spans.add((active_conll_tag, (span_start, span_end)))
      active_conll_tag = None
      # We don't care about tags we are
      # told to ignore, so we do nothing.
      continue
    elif bio_tag == "B":
      # We are entering a new span; reset indices and active tag to new span.
      if active_conll_tag:
        spans.add((active_conll_tag, (span_start, span_end)))
      active_conll_tag = conll_tag
      span_start = index
      span_end = index
    elif bio_tag == "I" and conll_tag == active_conll_tag:
      # We're inside a span.
      span_end += 1
    else:
      # This is the case the bio label is an "I", but either:
      # 1) the span hasn't started - i.e. an ill formed span.
      # 2) We have IOB1 tagging scheme.
      # We'll process the previous span if it exists, but also include this
      # span. This is important, because otherwise, a model may get a perfect
      # F1 score whilst still including false positive ill-formed spans.
      if active_conll_tag:
        spans.add((active_conll_tag, (span_start, span_end)))
      active_conll_tag = conll_tag
      span_start = index
      span_end = index
  # Last token might have been a part of a valid span.
  if active_conll_tag:
    spans.add((active_conll_tag, (span_start, span_end)))
  # Return sorted list of spans
  return sorted(list(spans), key=lambda x: x[1][0])


def get_spans(tokens, tags):
  """Convert tags to textspans."""
  spans = tags_to_spans(tags)
  text_spans = [
      x[0] + ": " + " ".join([tokens[i]
                              for i in range(x[1][0], x[1][1] + 1)])
      for x in spans
  ]
  if not text_spans:
    text_spans = ["None"]
  return text_spans


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
        "spans":
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
    """Reads line by line format of the NER dataset and generates examples.

    Input Format:

    en:rick  B-PER
    en:and  O
    en:morty  B-PER
    en:are  O
    en:cool  O
    en:.  O

    Output Format:

    {
    'tokens': ["rick", "and", "morty", "are", "cool", "."],
    'tags': ["B-PER", "O" , "B-PER", "O", "O", "O"],
    'langs': ["en", "en", "en", "en", "en", "en"]
    'spans': ["PER: rick", "PER: morty"]
    }

    Args:
      filepath: Path to file with line by line NER format.

    Yields:
      Examples with the format listed above.

    """

    key = 1
    with tf.io.gfile.GFile(filepath, "r") as f:
      tokens = []
      tags = []
      langs = []
      for line in f:
        line = line.rstrip()
        # pylint: disable=g-explicit-bool-comparison
        if line.startswith("-DOCSTART-") or line == "":
          if tokens:
            spans = get_spans(tokens, tags)
            yield key, {
                "tokens": tokens,
                "tags": tags,
                "langs": langs,
                "spans": spans
            }
            key += 1
            tokens = []
            tags = []
            langs = []
        else:
          # wikiann data is tab separated
          fields = line.split("\t")
          # strip out language prefix
          langs.append(fields[0].split(":")[0])
          tokens.append(":".join(fields[0].split(":")[1:]))
          if len(fields) > 1:
            tags.append(fields[-1])
          else:
            # examples have no label in test set
            tags.append("O")
      if tokens:
        spans = get_spans(tokens, tags)
        yield key, {
            "tokens": tokens,
            "tags": tags,
            "langs": langs,
            "spans": spans
        }

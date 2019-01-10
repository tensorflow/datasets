# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""WMT: Translate dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import json
import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Translate dataset based on the data from statmt.org.
"""

# Tuple that describes a single pair of files with matching translations.
# language_to_file is the map from language (2 letter string: example 'en')
# to the file path in the extracted directory.
TranslateData = collections.namedtuple("TranslateData",
                                       ["url", "language_to_file"])

TRANSLATE_DATASETS = {
    "wmt10_giga_fren_enfr": TranslateData(
        url="http://www.statmt.org/wmt10/training-giga-fren.tar",
        language_to_file={
            "en": "giga-fren.release2.fixed.en.gz",
            "fr": "giga-fren.release2.fixed.fr.gz",
        }),
    "wmt13_commoncrawl_ende": TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        language_to_file={
            "en": "commoncrawl.de-en.en",
            "de": "commoncrawl.de-en.de",
        }),
    "wmt13_commoncrawl_enfr": TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-commoncrawl.tgz",
        language_to_file={
            "en": "commoncrawl.fr-en.en",
            "fr": "commoncrawl.fr-en.fr",
        }),

    "wmt13_europarl_ende": TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        language_to_file={
            "en": "training/europarl-v7.de-en.en",
            "de": "training/europarl-v7.de-en.de",
        }),
    "wmt13_europarl_enfr": TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-europarl-v7.tgz",
        language_to_file={
            "en": "training/europarl-v7.fr-en.en",
            "fr": "training/europarl-v7.fr-en.fr",
        }),
    "wmt13_undoc_enfr": TranslateData(
        url="http://www.statmt.org/wmt13/training-parallel-un.tgz",
        language_to_file={
            "en": "un/undoc.2000.fr-en.en",
            "fr": "un/undoc.2000.fr-en.fr",
        }),
    "wmt14_news_commentary_enfr": TranslateData(
        url="http://www.statmt.org/wmt14/training-parallel-nc-v9.tgz",
        language_to_file={
            "en": "training/news-commentary-v9.fr-en.en",
            "fr": "training/news-commentary-v9.fr-en.fr",
        }),
    "wmt17_newstest": TranslateData(
        url="http://data.statmt.org/wmt17/translation-task/dev.tgz",
        language_to_file={
            "en": "dev/newstest2013.en",
            "de": "dev/newstest2013.de",
            "fr": "dev/newstest2013.fr",
        }),
    "wmt18_news_commentary_ende": TranslateData(
        url="http://data.statmt.org/wmt18/translation-task/training-parallel-nc-v13.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "training-parallel-nc-v13/news-commentary-v13.de-en.en",
            "de": "training-parallel-nc-v13/news-commentary-v13.de-en.de",
        }),
    "opennmt_1M_enfr_train": TranslateData(
        url="https://s3.amazonaws.com/opennmt-trainingdata/baseline-1M-enfr.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "baseline-1M-enfr/baseline-1M_train.en",
            "fr": "baseline-1M-enfr/baseline-1M_train.fr",
        }),
    "opennmt_1M_enfr_valid": TranslateData(
        url="https://s3.amazonaws.com/opennmt-trainingdata/baseline-1M-enfr.tgz",  # pylint: disable=line-too-long
        language_to_file={
            "en": "baseline-1M-enfr/baseline-1M_valid.en",
            "fr": "baseline-1M-enfr/baseline-1M_valid.fr",
        }),
}


class WMTConfig(tfds.core.BuilderConfig):
  """BuilderConfig for WMT."""

  # TODO(tfds): figure out if we want to share vocab between src/target.
  @api_utils.disallow_positional_args
  def __init__(self,
               text_encoder_config=None,
               language_pair=(None, None),
               data=None,
               name_suffix=None,
               **kwargs):
    """BuilderConfig for WMT.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      language_pair: pair of languages that will be used for translation. Should
                 contain 2 letter coded strings. For example: ("en", "de").
      data: data used for this training. It should be in the dictionary format,
        with keys matching "train", "test", "dev". Each entry should be a list
        of strings that are indexes into the TRANSLATE_DATASETS map.
      name_suffix: name that should be appended to the dataset name at the end.
      **kwargs: keyword arguments forwarded to super.
    """
    encoder_name = (
        text_encoder_config.name if text_encoder_config else "plain_text")
    name = "%s%s_%s" % (language_pair[0], language_pair[1], encoder_name)
    if name_suffix:
      name += "_%s" % name_suffix

    description = (
        "Translation dataset from %s to %s, uses encoder %s. It uses the "
        "following data files (see the code for exact contents): %s.") % (
            language_pair[0], language_pair[1], encoder_name,
            json.dumps(data, sort_keys=True))

    super(WMTConfig, self).__init__(
        name=name, description=description, **kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())

    self.language_pair = language_pair
    self.data = data


# Datasets used by T2T code for en-de translation.
T2T_ENDE_TRAIN = [
    "wmt18_news_commentary_ende", "wmt13_commoncrawl_ende",
    "wmt13_europarl_ende"
]
T2T_ENDE_TEST = ["wmt17_newstest"]

T2T_ENFR_TRAIN_SMALL = ["opennmt_1M_enfr_train"]
T2T_ENFR_TEST_SMALL = ["opennmt_1M_enfr_valid"]

T2T_ENFR_TRAIN_LARGE = ["wmt13_commoncrawl_enfr", "wmt13_europarl_enfr",
                        "wmt14_news_commentary_enfr",
                        # TODO(b/119253909): figure out if we need this
                        # as a part of the train set (as it has data
                        # in a different file format).
                        # "wmt10_giga_fren_enfr",
                        "wmt13_undoc_enfr"]
T2T_ENFR_TEST_LARGE = ["wmt17_newstest"]


class TranslateWmt(tfds.core.GeneratorBasedBuilder):
  """WMT translation dataset."""
  _URL = "http://www.statmt.org/wmt18/"

  BUILDER_CONFIGS = [
      WMTConfig(
          language_pair=("en", "de"),
          version="0.0.1",
          name_suffix="t2t",
          data={
              "train": T2T_ENDE_TRAIN,
              "test": T2T_ENDE_TEST,
              "dev": []
          }),
      WMTConfig(
          language_pair=("en", "de"),
          version="0.0.1",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t",
          data={
              "train": T2T_ENDE_TRAIN,
              "test": T2T_ENDE_TEST,
              "dev": []
          }),
      # EN-FR translations (matching the data used by Tensor2Tensor library).
      WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.1",
          name_suffix="t2t_small",
          data={
              "train": T2T_ENFR_TRAIN_SMALL,
              "test": T2T_ENFR_TEST_SMALL,
              "dev": []
          }),
      WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.1",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t_small",
          data={
              "train": T2T_ENFR_TRAIN_SMALL,
              "test": T2T_ENFR_TEST_SMALL,
              "dev": []
          }),
      WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.1",
          name_suffix="t2t_large",
          data={
              "train": T2T_ENFR_TRAIN_LARGE,
              "test": T2T_ENFR_TEST_LARGE,
              "dev": []
          }),
      WMTConfig(
          language_pair=("en", "fr"),
          version="0.0.1",
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              name="subwords8k",
              vocab_size=2**13),
          name_suffix="t2t_large",
          data={
              "train": T2T_ENFR_TRAIN_LARGE,
              "test": T2T_ENFR_TEST_LARGE,
              "dev": []
          }),
  ]

  def _info(self):
    src, target = self.builder_config.language_pair
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            src:
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            target:
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
        }),
        # No default supervised_keys (as we have to pass both question
        # and context as input).
        supervised_keys=None,
        urls=["http://www.statmt.org/wmt18/"],
        # TODO(tfds): Add the citations for all corpi (Europarl, etc.)
    )

  def _vocab_text_gen(self, files, language):
    for ex in self._generate_examples(files):
      yield ex[language]

  def _split_generators(self, dl_manager):
    urls_to_download = {}
    for split in ["train", "test", "dev"]:
      urls_to_download.update({
          "%s_%d" % (split, i): TRANSLATE_DATASETS[entry].url
          for i, entry in enumerate(self.builder_config.data[split])
      })

    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    # Dictionary with file locations for each split.
    # Inside it contains a list of pairs of files with matching sentences.
    files = {}
    for split in ["train", "test", "dev"]:
      files[split] = []
      for i, entry in enumerate(self.builder_config.data[split]):
        files[split].append((os.path.join(
            downloaded_files["%s_%d" % (split, i)],
            TRANSLATE_DATASETS[entry].language_to_file[
                self.builder_config.language_pair[0]]),
                             os.path.join(
                                 downloaded_files["%s_%d" % (split, i)],
                                 TRANSLATE_DATASETS[entry].language_to_file[
                                     self.builder_config.language_pair[1]])))

    # Generate vocabulary from training data if SubwordTextEncoder configured
    for language in self.builder_config.language_pair:
      self.info.features[language].maybe_build_from_corpus(
          self._vocab_text_gen(files["train"], language))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={"files": files["train"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={"files": files["dev"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs={"files": files["test"]}),
    ]

  def _generate_examples(self, files):
    """This function returns the examples in the raw (text) form."""
    for entry in files:
      with tf.gfile.Open(entry[0]) as f:
        lang1_sentences = f.read().split("\n")
      with tf.gfile.Open(entry[1]) as f:
        lang2_sentences = f.read().split("\n")

      assert len(lang1_sentences) == len(
          lang2_sentences), "Sizes do not match: %d vs %d for %s vs %s." % (
              len(lang1_sentences), len(lang2_sentences), entry[0], entry[1])
      # Skip the last entry (it is usually ('', '') due to the end of file)
      for l1, l2 in zip(lang1_sentences, lang2_sentences):
        result = {
            self.builder_config.language_pair[0]: l1,
            self.builder_config.language_pair[1]: l2
        }
        # Make sure that both translations are non-empty.
        if all(result.values()):
          yield result

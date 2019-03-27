# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

import abc
import collections
import json
import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Translate dataset based on the data from statmt.org.
"""

_CITATION = """\
@InProceedings{bojar-EtAl:2018:WMT1,
  author    = {Bojar, Ond\v{r}ej  and  Federmann, Christian  and  Fishel, Mark
    and Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and
    Koehn, Philipp  and  Monz, Christof},
  title     = {Findings of the 2018 Conference on Machine Translation (WMT18)},
  booktitle = {Proceedings of the Third Conference on Machine Translation,
    Volume 2: Shared Task Papers},
  month     = {October},
  year      = {2018},
  address   = {Belgium, Brussels},
  publisher = {Association for Computational Linguistics},
  pages     = {272--307},
  url       = {http://www.aclweb.org/anthology/W18-6401}
}
"""

# Tuple that describes a single pair of files with matching translations.
# language_to_file is the map from language (2 letter string: example 'en')
# to the file path in the extracted directory.
TranslateData = collections.namedtuple("TranslateData",
                                       ["url", "language_to_file"])


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
        of strings that are indexes into the self.translate_datasets map.
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


class WmtTranslate(tfds.core.GeneratorBasedBuilder):
  """WMT translation dataset."""
  _URL = "http://www.statmt.org/wmt18/"
  IN_DEVELOPMENT = True

  @abc.abstractproperty
  def translate_datasets(self):
    """Datasets used in this class."""
    raise NotImplementedError

  def _info(self):
    src, target = self.builder_config.language_pair
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(
            languages=self.builder_config.language_pair,
            encoder_config=self.builder_config.text_encoder_config),
        supervised_keys=(src, target),
        urls=["http://www.statmt.org/wmt18/"],
        citation=_CITATION,
    )

  def _vocab_text_gen(self, files, language):
    for ex in self._generate_examples(files):
      yield ex[language]

  def _split_generators(self, dl_manager):
    urls_to_download = {}
    for split in ["train", "dev"]:
      urls_to_download.update({
          "%s_%d" % (split, i): self.translate_datasets[entry].url
          for i, entry in enumerate(self.builder_config.data[split])
      })

    downloaded_files = dl_manager.download_and_extract(urls_to_download)

    # Dictionary with file locations for each split.
    # Inside it contains a list of pairs of files with matching sentences.
    files = {}
    for split in ["train", "dev"]:
      files[split] = []
      for i, entry in enumerate(self.builder_config.data[split]):
        path = os.path.join(
            downloaded_files["%s_%d" % (split, i)],
            self.translate_datasets[entry].language_to_file[
                self.builder_config.language_pair[1]])
        files[split].append((os.path.join(
            downloaded_files["%s_%d" % (split, i)],
            self.translate_datasets[entry].language_to_file[
                self.builder_config.language_pair[0]]), path))

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
    ]

  def _generate_examples(self, files):
    """This function returns the examples in the raw (text) form."""
    for entry in files:
      with tf.io.gfile.GFile(entry[0]) as f:
        lang1_sentences = f.read().split("\n")
      with tf.io.gfile.GFile(entry[1]) as f:
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

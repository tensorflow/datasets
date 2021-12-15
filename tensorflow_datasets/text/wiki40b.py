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

"""Wiki40B: A clean Wikipedia dataset for 40+ languages."""

import os

from absl import logging

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{49029,
title = {Wiki-40B: Multilingual Language Model Dataset},
author = {Mandy Guo and Zihang Dai and Denny Vrandecic and Rami Al-Rfou},
year = {2020},
booktitle	= {LREC 2020}
}
"""

_DESCRIPTION = """
Clean-up text for 40+ Wikipedia languages editions of pages
correspond to entities. The datasets have train/dev/test splits per language.
The dataset is cleaned up by page filtering to remove disambiguation pages,
redirect pages, deleted pages, and non-entity pages. Each example contains the
wikidata id of the entity, and the full Wikipedia article after page processing
that removes non-content sections and structured objects. The language models
trained on this corpus - including 41 monolingual models, and 2 multilingual
models - can be found at https://tfhub.dev/google/collections/wiki40b-lm/1.
"""

_LICENSE = """
This work is licensed under the Creative Commons Attribution-ShareAlike
3.0 Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
"""

_URL = "https://research.google/pubs/pub49029/"

_DATA_DIRECTORY = tfds.core.gcs_path("downloads/wiki40b/tfrecord_prod")

WIKIPEDIA_LANGUAGES = [
    "en", "ar", "zh-cn", "zh-tw", "nl", "fr", "de", "it", "ja", "ko", "pl",
    "pt", "ru", "es", "th", "tr", "bg", "ca", "cs", "da", "el", "et", "fa",
    "fi", "he", "hi", "hr", "hu", "id", "lt", "lv", "ms", "no", "ro", "sk",
    "sl", "sr", "sv", "tl", "uk", "vi"
]


class Wiki40bConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Wiki40B."""

  def __init__(self, *, language=None, **kwargs):
    """BuilderConfig for Wiki40B.

    Args:
      language: string, the language code for the Wiki40B dataset to use.
      **kwargs: keyword arguments forwarded to super.
    """
    super(Wiki40bConfig, self).__init__(
        name=language,
        description="Wiki40B dataset for {}.".format(language),
        **kwargs)
    self.language = language


_VERSION = tfds.core.Version("1.3.0")


class Wiki40b(tfds.core.BeamBasedBuilder):
  """Wiki40B: A Clean Wikipedia Dataset for Mutlilingual Language Modeling."""

  BUILDER_CONFIGS = [
      Wiki40bConfig(  # pylint:disable=g-complex-comprehension
          version=_VERSION,
          language=lang,
      ) for lang in WIKIPEDIA_LANGUAGES
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "wikidata_id": tfds.features.Text(),
            "text": tfds.features.Text(),
            "version_id": tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage=_URL,
        citation=_CITATION,
        license=_LICENSE,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    del dl_manager  # Unused

    lang = self._builder_config.language

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "filepaths":
                    os.path.join(_DATA_DIRECTORY, "train",
                                 "{}_examples-*".format(lang))
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "filepaths":
                    os.path.join(_DATA_DIRECTORY, "dev",
                                 "{}_examples-*".format(lang))
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "filepaths":
                    os.path.join(_DATA_DIRECTORY, "test",
                                 "{}_examples-*".format(lang))
            }),
    ]

  def _build_pcollection(self, pipeline, filepaths):
    """Build PCollection of examples."""
    beam = tfds.core.lazy_imports.apache_beam
    logging.info("generating examples from = %s", filepaths)

    def _extract_content(example):
      """Extracts content from a TFExample."""
      wikidata_id = example.features.feature["wikidata_id"].bytes_list.value[
          0].decode("utf-8")
      text = example.features.feature["text"].bytes_list.value[0].decode(
          "utf-8")
      version_id = example.features.feature["version_id"].bytes_list.value[
          0].decode("utf-8")

      # wikidata_id could be duplicated with different texts.
      yield wikidata_id + text, {
          "wikidata_id": wikidata_id,
          "text": text,
          "version_id": version_id,
      }

    return (pipeline
            | beam.io.ReadFromTFRecord(
                filepaths, coder=beam.coders.ProtoCoder(tf.train.Example))
            | beam.FlatMap(_extract_content))

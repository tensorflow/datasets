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

# Lint as: python3
"""opus dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
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
"""

_LANGUAGES = ["de", "en", "es"]

class SubDataset(object):
  def __init__(self, name, url, languages, filename):
    self.name = name
    self.url = url
    self.filename = filename

    language_pairs = []
    for idx, source in enumerate(languages):
      for target in languages[idx + 1:]:
        language_pairs.append((source, target))

    self.language_pairs = language_pairs

DATASET_MAP = {ds.name: ds for ds in [
  SubDataset(
    name="medical", 
    url="http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/",
    languages=["de", "en", "es"], 
    filename="EMEA"
  ),
  SubDataset(
    name="law",
    url="http://opus.nlpl.eu/download.php?f=JRC-Acquis/",
    languages=["de", "en", "es"],
    filename="JRC-Acquis"
  )
]}

class OpusConfig(tfds.core.BuilderConfig):
  @tfds.core.disallow_positional_args
  def __init__(self, language_pair, subsets, **kwargs):
    """BuilderConfig for Opus.

    Args:
      language_pair: pair of languages that will be used for translation. Should contain 2 letter coded strings (e.g. "en", "de")
      subsets: list[str]. List of the subsets to use
      **kwargs: keyword arguments forwarded to super.
    """
    name = "%s-%s" % (language_pair[0], language_pair[1])
    description = name + " documents"

    super(OpusConfig, self).__init__(name=name, description=description, **kwargs)
    self.language_pair = language_pair
    self.subsets = subsets

class Opus(tfds.core.GeneratorBasedBuilder):
  """OPUS is a collection of translated texts from the web.
  """

  @property
  def subsets(self):
    # return only the datasets that exist for the language pair for each builder config
    source, target = self.builder_config.language_pair
    filtered_subsets = []
    for dataset in [DATASET_MAP[name] for name in self.builder_config.subsets]:
      if (source, target) in dataset.language_pairs:
        filtered_subsets.append(dataset)

    return filtered_subsets

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(languages=self.builder_config.language_pair),
        supervised_keys=self.builder_config.language_pair,
        homepage='http://opus.nlpl.eu/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    source, target = self.builder_config.language_pair
    file_ext = "%s-%s"%(source, target)

    subsets = []

    for item in self.subsets:
      dl_dir = dl_manager.download_and_extract(os.path.join(item.url, "%s.txt.zip"%file_ext))
      subsets.append({
        "name": item.name,
        "source_file": os.path.join(dl_dir, "%s.%s.%s"%(item.filename, file_ext, source)),
        "target_file": os.path.join(dl_dir, "%s.%s.%s"%(item.filename, file_ext, target))
      })

    return [
      tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={ "subsets": subsets }
        )
    ]

  def _generate_examples(self, subsets):
    for item in subsets:
      source_file = item["source_file"]
      target_file = item["target_file"]

      with tf.io.gfile.GFile(source_file) as f:
        source_sentences = f.read().split("\n")
      with tf.io.gfile.GFile(target_file) as f:
        target_sentences = f.read().split("\n")

      source, target = self.builder_config.language_pair
      for idx, (source_sentence, target_sentence) in enumerate(zip(source_sentences, target_sentences)):
        result = {source: source_sentence, target: target_sentence}
        if all(result.values()):
          key = "%s/%d"%(item["name"], idx)
          yield key, result


"""medical dataset."""

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
This is a parallel corpus made out of PDF documents from the European Medicines Agency. 
"""

_LANGUAGES = ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hu", "it", "lt", "lv", "mt", "nl", "pl", "pt", "ro", "sk", "sl", "sv"]

_DATA_URL = "http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/"


class MedicalConfig(tfds.core.BuilderConfig):
  @tfds.core.disallow_positional_args
  def __init__(self, language_pair=(None, None), **kwargs):
    name = "%s_%s" % (language_pair[0], language_pair[1])
    super(MedicalConfig, self).__init__(name=name, description=name + " documents", **kwargs)
    self.language_pair = language_pair


class Medical(tfds.core.GeneratorBasedBuilder):
  language_pairs = []
  for idx, l1 in enumerate(_LANGUAGES):
    for l2 in _LANGUAGES[idx + 1:]:
      language_pairs.append((l1, l2))

  BUILDER_CONFIGS = [
    MedicalConfig(language_pair=pair, version="0.1.0") for pair in language_pairs
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(languages=self.builder_config.language_pair),
        supervised_keys=self.builder_config.language_pair,
        homepage='http://opus.nlpl.eu/EMEA.php',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    l1, l2 = self.builder_config.language_pair
    file_ext = "%s-%s"%(l1, l2)

    dl_dir = dl_manager.download_and_extract(os.path.join(_DATA_URL, "%s.txt.zip"%file_ext))
    
    l1_file = os.path.join(dl_dir, "EMEA.%s.%s"%(file_ext, l1))
    l2_file = os.path.join(dl_dir, "EMEA.%s.%s"%(file_ext, l2))

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"l1_file": l1_file, "l2_file": l2_file},
        ),
    ]

  def _generate_examples(self, l1_file, l2_file):
    with tf.io.gfile.GFile(l1_file) as f:
      l1_sentences = f.read().split("\n")
    with tf.io.gfile.GFile(l2_file) as f:
      l2_sentences = f.read().split("\n")

    l1, l2 = self.builder_config.language_pair
    for idx, (source, target) in enumerate(zip(l1_sentences, l2_sentences)):
      result = {l1: source, l2: target}
      if all(result.values()):
        yield idx, result

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

_VALID_LANGUAGE_PAIRS = (
    ("en", "de"),
)

_DATA_URL = "http://opus.nlpl.eu/download.php?f=EMEA/v3/moses/de-en.txt.zip"


class MedicalConfig(tfds.core.BuilderConfig):
  @tfds.core.disallow_positional_args
  def __init__(self, language_pair=(None, None), **kwargs):
    name = "%s_to_%s" % (language_pair[0], language_pair[1])
    description = "description"
    super(MedicalConfig, self).__init__(name=name, description=description, **kwargs)
    self.language_pair = language_pair


class Medical(tfds.core.GeneratorBasedBuilder):
  """Parallel corpus made out of PDF documents from the European Medicines Agency. """

  BUILDER_CONFIGS = [
    MedicalConfig(language_pair=pair, version="0.1.0") for pair in _VALID_LANGUAGE_PAIRS
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.Translation(languages=self.builder_config.language_pair),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=self.builder_config.language_pair,
        # Homepage of the dataset for documentation
        homepage='http://opus.nlpl.eu/EMEA.php',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(medical): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    source, target = self.builder_config.language_pair
    dl_dir = dl_manager.download_and_extract(_DATA_URL)

    l1_file = os.path.join(dl_dir, "EMEA.de-en.de")
    l2_file = os.path.join(dl_dir, "EMEA.de-en.en")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"l1_file": l1_file, "l2_file": l2_file},
        ),
    ]

  def _generate_examples(self, l1_file, l2_file):
    """Yields examples."""
    with tf.io.gfile.GFile(l1_file) as f:
      l1_sentences = f.read().split("\n")
    with tf.io.gfile.GFile(l2_file) as f:
      l2_sentences = f.read().split("\n")

    l1, l2 = self.builder_config.language_pair
    for idx, (source, target) in enumerate(zip(l1_sentences, l2_sentences)):
      result = {l1: source, l2: target}
      if all(result.values()):
        yield idx, result

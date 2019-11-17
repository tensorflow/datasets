"""TODO(bbbp): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds

# TODO(bbbp): BibTeX citation
_CITATION = """
"""

# TODO(bbbp):
_DESCRIPTION = """
"""


class Bbbp(tfds.core.GeneratorBasedBuilder):
  """TODO(bbbp): Short description of my dataset."""

  # TODO(bbbp): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(bbbp): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(bbbp): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={},
        ),
    ]

  def _generate_examples(self):
    """Yields examples."""
    # TODO(bbbp): Yields (key, example) tuples from the dataset
    yield 'key', {}


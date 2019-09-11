"""TODO(my_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds

# TODO(my_dataset): BibTeX citation
_CITATION = """
"""

# TODO(my_dataset):
_DESCRIPTION = """
"""


class MyDataset(tfds.core.GeneratorBasedBuilder):
  """TODO(my_dataset): Short description of my dataset."""

  # TODO(my_dataset): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(isic): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image()     # These are the features of your dataset like images, labels ...
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        urls=[],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(isic): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs

    dl_paths = dl_manager.download_and_extract({
      'train': 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_Input.zip',
      'train_csv': 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_GroundTruth.csv',
      'train_metadata_csv': 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Training_GroundTruth.csv',
      'test': 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Test_Input.zip',
      'test_csv_metadata': 'https://s3.amazonaws.com/isic-challenge-2019/ISIC_2019_Test_Metadata.csv'
    })

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'images_dir_path': dl_paths['train'],
                'metadata': dl_paths['train_metadata_csv']
                'labels': dl_paths['train_csv']
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={
                'images_dir_path': dl_paths['test'],
                'metadata': dl_paths['test_metadata_csv']
                'labels': dl_paths['test_csv']            },
        ),
    ]

  def _generate_examples(self):
    """Yields examples."""
    # TODO(my_dataset): Yields (key, example) tuples from the dataset
    yield 'key', {}

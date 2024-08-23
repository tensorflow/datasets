"""pklot dataset."""

import os
from itertools import chain
from pathlib import Path

import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This database contains 12,417 images (1280X720) captured from two different parking lots (parking1 and parking2) in sunny, cloudy and rainy days. The first parking lot has two different capture angles (parking1a and parking 1b).

The images are organised into three directories (parking1a, parking1b and parking2). Each directory contains three subdirectories for different weather conditions (cloudy, rainy and sunny). Inside of each subdirectory the images are organised by acquisition date.

Each image of the database has a XML file associated including the coordinates of all the parking spaces and its label (occupied/vacant). By using the XML files to segment the parking space, you will be able to get around 695,900 images of parking spaces.

More info about the database can be found in this readme file.
"""

_CITATION = """
Almeida, P., Oliveira, L. S., Silva Jr, E., Britto Jr, A., Koerich, A., PKLot - A robust dataset for parking lot classification, Expert Systems with Applications, 42(11):4937-4949, 2015.
"""

_EMPTY_LABEL = "Empty"
_OCCUPIED_LABEL = "Occupied"
_EMPTY_LABEL_DIR_NAME = _EMPTY_LABEL
_OCCUPIED_LABEL_DIR_NAME = _OCCUPIED_LABEL
_LABEL_DIR_NAME_TO_LABEL_MAP = {
    _EMPTY_LABEL_DIR_NAME: _EMPTY_LABEL,
    _OCCUPIED_LABEL_DIR_NAME: _OCCUPIED_LABEL
}


class Pklot(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for pklot dataset."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {
                # These are the features of your dataset like images, labels ...
                "image":
                    tfds.features.Image(shape=(None, None, 3)),
                "label":
                    tfds.features.ClassLabel(
                        names=[_EMPTY_LABEL, _OCCUPIED_LABEL]
                    ),
            }
        ),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=("image", "label"),  # Set to `None` to disable
        homepage="https://web.inf.ufpr.br/vri/databases/parking-lot-database/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        "http://www.inf.ufpr.br/vri/databases/PKLot.tar.gz"
    ) / "PKLot" / "PKLotSegmented"
    return {
        "train":
            chain(
                self._generate_examples(path, "UFPR04"),
                self._generate_examples(path, "UFPR05"),
            ),
        "test":
            self._generate_examples(path, "PUC"),
    }

  def _generate_examples(self, path: Path, subdir: str):
    """Yields examples."""
    for weather_dir_entry in os.scandir(path / subdir):
      if not weather_dir_entry.is_dir():
        continue

      for date_dir_entry in os.scandir(weather_dir_entry):
        if not date_dir_entry.is_dir():
          continue

        key_prefix = subdir + "_" + weather_dir_entry.name + "_" + date_dir_entry.name + "_"

        for label_dir_entry in os.scandir(date_dir_entry):
          if not label_dir_entry.is_dir():
            continue

          for jpg_file_entry in os.scandir(label_dir_entry):
            yield key_prefix + label_dir_entry.name + "_" + jpg_file_entry.name, {
                "image": jpg_file_entry.path,
                "label": _LABEL_DIR_NAME_TO_LABEL_MAP[label_dir_entry.name]
            }

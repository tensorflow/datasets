"""pklot dataset."""

import os
import pathlib
import platform
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


# NOTE: this is a workaround for glob failing on Windows with long paths
# even if long paths support is enabled
# https://stackoverflow.com/a/57502760
def _fix_windows_long_path(path):
  normalized = os.fspath(path.resolve())
  if not normalized.startswith("\\\\?\\"):
    normalized = "\\\\?\\" + normalized
  return pathlib.Path(normalized)


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
                "image": tfds.features.Image(shape=(None, None, 3)),
                "label": tfds.features.ClassLabel(names=["Empty", "Occupied"]),
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
    )
    if platform.system() == "Windows":
      path = _fix_windows_long_path(path)
    return {
        "train":
            chain(
                self._generate_examples(
                    path / "PKLot" / "PKLotSegmented" / "UFPR04"
                ),
                self._generate_examples(
                    path / "PKLot" / "PKLotSegmented" / "UFPR05"
                ),
            ),
        "test":
            self._generate_examples(path / "PKLot" / "PKLotSegmented" / "PUC"),
    }

  def _generate_examples(self, path: Path):
    """Yields examples."""
    for img_path in path.rglob("*.jpg"):
      yield "_".join(img_path.parts[-5:]), {
          "image": img_path,
          "label": "Empty" if img_path.parent.name[0] == "E" else "Occupied",
      }

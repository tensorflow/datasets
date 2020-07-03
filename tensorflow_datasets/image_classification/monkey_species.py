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
"""10 Money Species is an image classification dataset containing JPG images
(rescaled to 256x256 color images) of 10 monkey species.

NOTE: this dataset requires additional kaggle authentication.
Please look at: https://www.kaggle.com/docs/api

Information about the dataset:
Label, Latin Name           , Common Name              , Train Ex, Validation Ex
n0   , alouatta_palliata	  , mantled_howler           , 131     , 26
n1   , erythrocebus_patas	  , patas_monkey             , 139     , 28
n2   , cacajao_calvus	      , bald_uakari              , 137     , 27
n3   , macaca_fuscata	      , japanese_macaque         , 152     , 30
n4   , cebuella_pygmea	    , pygmy_marmoset           , 131     , 26
n5   , cebus_capucinus	    , white_headed_capuchin    , 141     , 28
n6   , mico_argentatus	    , silvery_marmoset         , 132     , 26
n7   , saimiri_sciureus	    , common_squirrel_monkey   , 142     , 28
n8   , aotus_nigriceps	    , black_headed_night_monkey, 133     , 27
n9   , trachypithecus_johnii, nilgiri_langur           , 132     , 26
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {monkey_species,
    author = "Mario Loaiciga, Romain Renard, Gustavo Montoya, Jacky Zhang, Sofia Loaiciga",
    title  = "10 Monkey Species dataset",
    month  = "jan",
    year   = "2018",
    url    = "https://www.kaggle.com/slothkong/10-monkey-species"
}
"""

_DESCRIPTION = """
10 Money Species is an image classification dataset containing JPG images
(rescaled to 256x256 color images) of 10 monkey species.

NOTE: this dataset requires additional kaggle authentication.
Please look at: https://www.kaggle.com/docs/api

Information about the dataset:
Label, Latin Name           , Common Name              , Train Ex, Validation Ex
n0   , alouatta_palliata	  , mantled_howler           , 131     , 26
n1   , erythrocebus_patas	  , patas_monkey             , 139     , 28
n2   , cacajao_calvus	      , bald_uakari              , 137     , 27
n3   , macaca_fuscata	      , japanese_macaque         , 152     , 30
n4   , cebuella_pygmea	    , pygmy_marmoset           , 131     , 26
n5   , cebus_capucinus	    , white_headed_capuchin    , 141     , 28
n6   , mico_argentatus	    , silvery_marmoset         , 132     , 26
n7   , saimiri_sciureus	    , common_squirrel_monkey   , 142     , 28
n8   , aotus_nigriceps	    , black_headed_night_monkey, 133     , 27
n9   , trachypithecus_johnii, nilgiri_langur           , 132     , 26
"""

_DOWNLOAD_URL = "slothkong/10-monkey-species"
_MONKEY_IMAGE_CHANNELS = 3
_MONKEY_IMAGE_SHAPE = (None, None, _MONKEY_IMAGE_CHANNELS)
_MONKEY_NUM_CLASSES = 10

_TRAIN_DIR = "training"
_VALIDATION_DIR = "validation"

_MONKEY_SPECIES_MAP = {
    "n0": {"latin": "alouatta_palliata", "common": "mantled_howler"},
    "n1": {"latin": "erythrocebus_patas", "common": "patas_monkey"},
    "n2": {"latin": "cacajao_calvus", "common": "bald_uakari"},
    "n3": {"latin": "macaca_fuscata", "common": "japanese_macaque"},
    "n4": {"latin": "cebuella_pygmea", "common": "pygmy_marmoset"},
    "n5": {"latin": "cebus_capucinus", "common": "white_headed_capuchin"},
    "n6": {"latin": "mico_argentatus", "common": "silvery_marmoset"},
    "n7": {"latin": "saimiri_sciureus", "common": "common_squirrel_monkey"},
    "n8": {"latin": "aotus_nigriceps", "common": "black_headed_night_monkey"},
    "n9": {"latin": "trachypithecus_johnii", "common": "nilgiri_langur"}
}

class MonkeySpecies(tfds.core.GeneratorBasedBuilder):
  """10 Monkey Species dataset."""

  VERSION = tfds.core.Version("0.1.0")

  def _info(self):
    """
    Returns basic information about the dataset.

    Returns:
      tfds.core.DatasetInfo.
    """
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "latin_name": tfds.features.Text(),
            "common_name": tfds.features.Text(),
            "image": tfds.features.Image(shape=_MONKEY_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(
                num_classes=_MONKEY_NUM_CLASSES),
        }),
        supervised_keys=("image", "label"),
        homepage="https://www.kaggle.com/slothkong/10-monkey-species",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Return the train and validation splits of the 10 Monkey Species dataset.

    Args:
      dl_manager: Download manager object.

    Returns:
      Train and validation splits."""
    # Download the full 10 Monkey Species dataset
    path = dl_manager.download_kaggle_data(_DOWNLOAD_URL)
    # monkey_species provides TRAIN and VALIDATION splits, not a TEST
    # split, so we only write the TRAIN and VALIDATION splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                data_path=os.path.join(path, _TRAIN_DIR, _TRAIN_DIR),
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs=dict(
                data_path=os.path.join(path, _VALIDATION_DIR, _VALIDATION_DIR),
            )),
    ]

  def _generate_examples(self, data_path):
    """Generate the 10 Monkey Species dataset data.

    Args:
      data_path: Path to the location of extracted dataset.

    Returns:
      Record with image file object along with its associated label.
    """
    for label in range(_MONKEY_NUM_CLASSES):
      label_dir = "n" + str(label)
      label_path = os.path.join(data_path, label_dir)
      images = list(tf.io.gfile.glob(label_path + "*.jpg"))
      for image in images:
        data = tf.io.gfile.GFile(image, "rb")
        record = {
            "latin_name": _MONKEY_SPECIES_MAP[label_dir]["latin"],
            "common_name": _MONKEY_SPECIES_MAP[label_dir]["common"],
            "image": data,
            "label": label,
        }
        yield image, record

# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Wine quality dataset."""

from __future__ import annotations

import csv

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@ONLINE {cortezpaulo;cerdeiraantonio;almeidafernando;matostelmo;reisjose1999,
    author = "Cortez, Paulo; Cerdeira, Antonio; Almeida,Fernando;  Matos, Telmo;  Reis, Jose",
    title  = "Modeling wine preferences by data mining from physicochemical properties.",
    year   = "2009",
    url    = "https://archive.ics.uci.edu/ml/datasets/wine+quality"
}
"""

_DESCRIPTION = """
Two datasets were created, using red and white wine samples.
The inputs include objective tests (e.g. PH values) and the output is based on sensory data
(median of at least 3 evaluations made by wine experts).
Each expert graded the wine quality
between 0 (very bad) and 10 (very excellent).
Several data mining methods were applied to model
these datasets under a regression approach. The support vector machine model achieved the
best results. Several metrics were computed: MAD, confusion matrix for a fixed error tolerance (T),
etc. Also, we plot the relative importances of the input variables (as measured by a sensitivity
analysis procedure).

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine.
For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].
Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables
are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

Number of Instances: red wine - 1599; white wine - 4898

Input variables (based on physicochemical tests):

1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol

Output variable (based on sensory data):

12. quality (score between 0 and 10)

"""

_DOWNLOAD_URL_WHITE_WINES = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
_DOWNLOAD_URL_RED_WINES = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
_HOMEPAGE_URL = "https://archive.ics.uci.edu/ml/datasets/wine+quality"


class WineQualityConfig(tfds.core.BuilderConfig):
  """Config for Wine Quality."""

  def __init__(self, *, dl_url, **kwargs):
    super(WineQualityConfig, self).__init__(version="1.0.0", **kwargs)
    self.dl_url = dl_url


class WineQuality(tfds.core.GeneratorBasedBuilder):
  """Wine Quality Dataset."""

  BUILDER_CONFIGS = [
      WineQualityConfig(
          name="white",
          description="White Wine",
          dl_url=_DOWNLOAD_URL_WHITE_WINES,
      ),
      WineQualityConfig(
          name="red",
          description="Red Wine",
          dl_url=_DOWNLOAD_URL_RED_WINES,
      ),
  ]

  def _info(self):
    features_dict = {
        "fixed acidity": tf.float32,
        "volatile acidity": tf.float32,
        "citric acid": tf.float32,
        "residual sugar": tf.float32,
        "chlorides": tf.float32,
        "free sulfur dioxide": tf.float32,
        "total sulfur dioxide": tf.float32,
        "density": tf.float32,
        "pH": tf.float32,
        "sulphates": tf.float64,
        "alcohol": tf.float32,
    }

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "quality": np.int32,
            "features": features_dict,
        }),
        supervised_keys=("features", "quality"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_path = dl_manager.download({"train": self.builder_config.dl_url})

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"file_path": file_path["train"]},
        ),
    ]

  def _generate_examples(self, file_path):
    """Yields examples.

    Args:
       file_path: Path of the downloaded csv file

    Yields:
       Next examples
    """

    with epath.Path(file_path).open() as f:
      reader = csv.DictReader(f, delimiter=";")
      for index, row in enumerate(reader):
        key = index
        example = {
            "quality": row.pop("quality"),
            "features": {name: value for name, value in row.items()},
        }
        yield key, example

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

"""simPTE dataset."""

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """

Full name: Simulations for Personalized Treatment Effects
Generated with the R's Uplift package: https://rdrr.io/cran/uplift/man/sim_pte.html
The package could be downloaded here: https://cran.r-project.org/src/contrib/Archive/uplift/

Dataset generated in R version 4.1.2 with following code:

  library(uplift)

  set.seed(123)

  train <- sim_pte(n = 1000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)
  test <- sim_pte(n = 2000, p = 20, rho = 0, sigma = sqrt(2), beta.den = 4)

  train$treat <- ifelse(train$treat == 1, 2, 1)
  test$treat <- ifelse(test$treat == 1, 2, 1)

  train$y <- ifelse(train$y == 1, 2, 1)
  test$y <- ifelse(test$y == 1, 2, 1)

  train$ts = NULL
  test$ts = NULL


Parameters:
  n = number of samples
  p = number of predictors
  ro = covariance between predictors
  sigma = mutiplier of the error term
  beta.den = beta is mutiplied by 1/beta.den

Creator: Leo Guelman leo.guelman@gmail.com

"""

_CITATION = """
@misc{https://doi.org/10.48550/arxiv.1212.2995,
  doi = {10.48550/ARXIV.1212.2995},
  url = {https://arxiv.org/abs/1212.2995},
  author = {Tian, Lu and Alizadeh, Ash and Gentles, Andrew and Tibshirani, Robert},
  keywords = {Methodology (stat.ME), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {A Simple Method for Detecting Interactions between a Treatment and a Large Number of Covariates},
  publisher = {arXiv},
  year = {2012},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

"""


class Simpte(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for simPTE dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """
    Please download training data: sim_pte_train.csv and test data:
    sim_pte_test.csv to ~/tensorflow_datasets/downloads/manual/.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'y': tf.int32,
            'treat': tf.int32,
            'X1': tf.float32,
            'X2': tf.float32,
            'X3': tf.float32,
            'X4': tf.float32,
            'X5': tf.float32,
            'X6': tf.float32,
            'X7': tf.float32,
            'X8': tf.float32,
            'X9': tf.float32,
            'X10': tf.float32,
            'X11': tf.float32,
            'X12': tf.float32,
            'X13': tf.float32,
            'X14': tf.float32,
            'X15': tf.float32,
            'X16': tf.float32,
            'X17': tf.float32,
            'X18': tf.float32,
            'X19': tf.float32,
            'X20': tf.float32,
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=({
            'X1': 'X1',
            'X2': 'X2',
            'X3': 'X3',
            'X4': 'X4',
            'X5': 'X5',
            'X6': 'X6',
            'X7': 'X7',
            'X8': 'X8',
            'X9': 'X9',
            'X10': 'X10',
            'X11': 'X11',
            'X12': 'X12',
            'X13': 'X13',
            'X14': 'X14',
            'X15': 'X15',
            'X16': 'X16',
            'X17': 'X17',
            'X18': 'X18',
            'X19': 'X19',
            'X20': 'X20',
            'treat': 'treat',
        }, 'y'),
        homepage='https://rdrr.io/cran/uplift/man/sim_pte.html',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    train_path = dl_manager.manual_dir / 'sim_pte_train.csv'
    test_path = dl_manager.manual_dir / 'sim_pte_test.csv'

    return {
        'train': self._generate_examples(train_path),
        'test': self._generate_examples(test_path)
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:
      index = 0
      for row in csv.DictReader(f):
        # And yield (key, feature_dict)
        yield index, {
            'X1': row['X1'],
            'X2': row['X2'],
            'X3': row['X3'],
            'X4': row['X4'],
            'X5': row['X5'],
            'X6': row['X6'],
            'X7': row['X7'],
            'X8': row['X8'],
            'X9': row['X9'],
            'X10': row['X10'],
            'X11': row['X11'],
            'X12': row['X12'],
            'X13': row['X13'],
            'X14': row['X14'],
            'X15': row['X15'],
            'X16': row['X16'],
            'X17': row['X17'],
            'X18': row['X18'],
            'X19': row['X19'],
            'X20': row['X20'],
            'treat': row['treat'],
            'y': row['y']
        }
        index += 1

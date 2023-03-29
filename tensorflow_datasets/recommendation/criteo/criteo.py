# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Criteo dataset."""

from __future__ import annotations

import csv

import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """

# Criteo Uplift Modeling Dataset
This dataset is released along with the paper:
“A Large Scale Benchmark for Uplift Modeling”
Eustache Diemert, Artem Betlei, Christophe Renaudin; (Criteo AI Lab), Massih-Reza Amini (LIG, Grenoble INP)

This work was published in: AdKDD 2018 Workshop, in conjunction with KDD 2018.

### Data description
This dataset is constructed by assembling data resulting from several incrementality tests, a particular randomized trial procedure where a random part of the population is prevented from being targeted by advertising. it consists of 25M rows, each one representing a user with 11 features, a treatment indicator and 2 labels (visits and conversions).

### Fields
Here is a detailed description of the fields (they are comma-separated in the file):

- f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11: feature values (dense, float)
- treatment: treatment group (1 = treated, 0 = control)
- conversion: whether a conversion occured for this user (binary, label)
- visit: whether a visit occured for this user (binary, label)
- exposure: treatment effect, whether the user has been effectively exposed (binary)

### Key figures

- Format: CSV
- Size: 459MB (compressed)
- Rows: 25,309,483
- Average Visit Rate: .04132
- Average Conversion Rate: .00229
- Treatment Ratio: .846

### Tasks

The dataset was collected and prepared with uplift prediction in mind as the main task. Additionally we can foresee related usages such as but not limited to:

- benchmark for causal inference
- uplift modeling
- interactions between features and treatment
- heterogeneity of treatment
- benchmark for observational causality methods

"""

_CITATION = """
@inproceedings{Diemert2018,
author = {{Diemert Eustache, Betlei Artem} and Renaudin, Christophe and Massih-Reza, Amini},
title={A Large Scale Benchmark for Uplift Modeling},
publisher = {ACM},
booktitle = {Proceedings of the AdKDD and TargetAd Workshop, KDD, London,United Kingdom, August, 20, 2018},
year = {2018}
}
"""


class Criteo(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for criteo dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.1': 'Fixed parsing of fields `conversion`, `visit` and `exposure`.',
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'f0': np.float32,
            'f1': np.float32,
            'f2': np.float32,
            'f3': np.float32,
            'f4': np.float32,
            'f5': np.float32,
            'f6': np.float32,
            'f7': np.float32,
            'f8': np.float32,
            'f9': np.float32,
            'f10': np.float32,
            'f11': np.float32,
            'treatment': np.int64,
            'conversion': np.bool_,
            'visit': np.bool_,
            'exposure': np.bool_,
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=(
            {
                'f0': 'f0',
                'f1': 'f1',
                'f2': 'f2',
                'f3': 'f3',
                'f4': 'f4',
                'f5': 'f5',
                'f6': 'f6',
                'f7': 'f7',
                'f8': 'f8',
                'f9': 'f9',
                'f10': 'f10',
                'f11': 'f11',
                'treatment': 'treatment',
                'exposure': 'exposure',
            },
            'visit',
        ),
        homepage='https://ailab.criteo.com/criteo-uplift-prediction-dataset/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        'http://go.criteo.net/criteo-research-uplift-v2.1.csv.gz'
    )

    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with path.open() as f:
      index = 0
      for row in csv.DictReader(f):
        # And yield (key, feature_dict)
        yield index, {
            'f0': row['f0'],
            'f1': row['f1'],
            'f2': row['f2'],
            'f3': row['f3'],
            'f4': row['f4'],
            'f5': row['f5'],
            'f6': row['f6'],
            'f7': row['f7'],
            'f8': row['f8'],
            'f9': row['f9'],
            'f10': row['f10'],
            'f11': row['f11'],
            'treatment': row['treatment'],
            'conversion': int(row['conversion']),
            'visit': int(row['visit']),
            'exposure': int(row['exposure']),
        }
        index += 1

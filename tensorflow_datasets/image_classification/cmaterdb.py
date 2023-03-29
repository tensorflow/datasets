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

"""CMATERdb dataset."""

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# CMATERdb constants
_CMATERDB_IMAGE_SIZE = 32
_CMATERDB_IMAGE_SHAPE = (_CMATERDB_IMAGE_SIZE, _CMATERDB_IMAGE_SIZE, 3)
# GitHub npz mirror of https://code.google.com/archive/p/cmaterdb/
_CMATERDB_TRAINING_URL = (
    "https://raw.githubusercontent.com/prabhuomkar/CMATERdb/master/"
    "datasets/{type}-numerals/training-images.npz"
)
_CMATERDB_TESTING_URL = (
    "https://raw.githubusercontent.com/prabhuomkar/CMATERdb/master/"
    "datasets/{type}-numerals/testing-images.npz"
)

_CITATION = """\
@article{Das:2012:GAB:2161007.2161320,
  author = {Das, Nibaran and Sarkar, Ram and Basu, Subhadip and Kundu, Mahantapas 
            and Nasipuri, Mita and Basu, Dipak Kumar},
  title = {A Genetic Algorithm Based Region Sampling for Selection of Local Features 
          in Handwritten Digit Recognition Application},
  journal = {Appl. Soft Comput.},
  issue_date = {May, 2012},
  volume = {12},
  number = {5},
  month = may,
  year = {2012},
  issn = {1568-4946},
  pages = {1592--1606},
  numpages = {15},
  url = {http://dx.doi.org/10.1016/j.asoc.2011.11.030},
  doi = {10.1016/j.asoc.2011.11.030},
  acmid = {2161320},
  publisher = {Elsevier Science Publishers B. V.},
  address = {Amsterdam, The Netherlands, The Netherlands},
  keywords = {Feature selection, Genetic algorithm, N-Quality consensus, 
  Optimal local regions, Region sampling, Variable sized local regions},
}
@article{Das:2012:SFC:2240301.2240421,
  author = {Das, Nibaran and Reddy, Jagan Mohan and Sarkar, Ram and Basu, Subhadip and Kundu, 
            Mahantapas and Nasipuri, Mita and Basu, Dipak Kumar},
  title = {A Statistical-topological Feature Combination for Recognition of Handwritten Numerals},
  journal = {Appl. Soft Comput.},
  issue_date = {August, 2012},
  volume = {12},
  number = {8},
  month = aug,
  year = {2012},
  issn = {1568-4946},
  pages = {2486--2495},
  numpages = {10},
  url = {http://dx.doi.org/10.1016/j.asoc.2012.03.039},
  doi = {10.1016/j.asoc.2012.03.039},
  acmid = {2240421},
  publisher = {Elsevier Science Publishers B. V.},
  address = {Amsterdam, The Netherlands, The Netherlands},
  keywords = {Character recognition, Feature combination, MPCA, PCA, SVM, Statistical, Topological},
}
"""

_DESCRIPTION = """\
This dataset contains images of -
  Handwritten Bangla numerals - balanced dataset of total 6000 Bangla numerals (32x32 RGB coloured, 6000 images), each having 600 images per class(per digit). 
  Handwritten Devanagari numerals - balanced dataset of total 3000 Devanagari numerals (32x32 RGB coloured, 3000 images), each having 300 images per class(per digit). 
  Handwritten Telugu numerals - balanced dataset of total 3000 Telugu numerals (32x32 RGB coloured, 3000 images), each having 300 images per class(per digit). 

CMATERdb is the pattern recognition database repository created at the 'Center for Microprocessor Applications for Training Education and Research' (CMATER) research lab, Jadavpur University, India.
"""


class CmaterdbConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CMATERdb Config."""


class Cmaterdb(tfds.core.GeneratorBasedBuilder):
  """CMATERdb dataset."""

  BUILDER_CONFIGS = [
      CmaterdbConfig(
          name="bangla",
          description="CMATERdb Bangla Numerals",
          version="1.0.0",
      ),
      CmaterdbConfig(
          name="devanagari",
          description="CMATERdb Devangari Numerals",
          version="1.0.0",
      ),
      CmaterdbConfig(
          name="telugu",
          description="CMATERdb Telugu Numerals",
          version="1.0.0",
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_CMATERDB_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(num_classes=10),
        }),
        supervised_keys=("image", "label"),
        homepage="https://code.google.com/archive/p/cmaterdb/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # Download the CMATERdb dataset by mentioned numeral
    train_path, test_path = dl_manager.download([
        _CMATERDB_TRAINING_URL.format(type=self.builder_config.name),
        _CMATERDB_TESTING_URL.format(type=self.builder_config.name),
    ])

    # CMATERdb (mirrored) provides TRAIN and TEST splits,
    # not a VALIDATION split, so we only
    # write the TRAIN and TEST splits to disk.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(data_path=train_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(data_path=test_path),
        ),
    ]

  def _generate_examples(self, data_path):
    """Generate CMATERdb examples as dicts.

    Args:
      data_path (str): Path to the data files

    Yields:
      Generator yielding the next examples
    """
    with tf.io.gfile.GFile(data_path, mode="rb") as f:
      data = np.load(f)

    data = list(zip(data["images"], data["labels"]))
    for index, (image, label) in enumerate(data):
      yield index, {
          "image": image,
          "label": label,
      }

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
"""BBBP(Blood-brain barrier penetration) dataset."""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

BBBP_URL = "https://s3-us-west-1.amazonaws.com/deepchem.io/datasets/molnet_publish/bbbp.zip"

_CITATION = """\
@article{doi:10.1021/ci300124c,
author = {Martins, Ines Filipa and Teixeira, Ana L. and Pinheiro, Luis and Falcao, Andre O.},
title = {A Bayesian Approach to in Silico Blood-Brain Barrier Penetration Modeling},
journal = {Journal of Chemical Information and Modeling},
volume = {52},
number = {6},
pages = {1686-1697},
year = {2012},
doi = {10.1021/ci300124c},
    note ={PMID: 22612593},
URL = {
        https://doi.org/10.1021/ci300124c

},
eprint = {
        https://doi.org/10.1021/ci300124c

}
}
"""

_DESCRIPTION = """\
The Blood-brain barrier penetration (BBBP) dataset is extracted from a study on
the modeling and prediction of the barrier permeability. As a membrane separating
circulating blood and brain extracellular fluid, the blood-brain barrier blocks
most drugs, hormones and neurotransmitters. Thus penetration of the barrier forms
a long-standing issue in development of drugs targeting central nervous system.
This dataset includes binary labels for over 2000 compounds on their permeability
properties.

The data file contains a csv table, in which columns below are used:
     "name" - Name of the compound
     "smiles" - SMILES representation of the molecular structure
     "p_np" - Binary labels for penetration/non-penetration

"""

FEATURES = tfds.features.FeaturesDict({
    'name': tf.string,
    'p_np': tfds.features.ClassLabel(num_classes=2)
})


class BBBP(tfds.core.GeneratorBasedBuilder):
  """BBBP dataset."""
  NUM_CLASSES = 3
  VERSION = tfds.core.Version('0.0.1')

  def _info(self):
    """This contains the general information about the dataset"""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'smiles': tf.string,
            'features': FEATURES
        }),
        supervised_keys=("features", "smiles"),
        homepage="http://moleculenet.ai/datasets-1",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Generate Splits"""
    bbbp_path = dl_manager.download_and_extract(BBBP_URL)
    csv_path = os.path.join(bbbp_path, "BBBP.csv")
    all_lines = tf.io.gfile.GFile(csv_path).read().split("\n")[1:-1]
    all_lines = [','.join(line.split(',')[1:])[:-1].replace('"', '')
                 for line in all_lines]

        # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "records": all_lines,
            }
        ),
    ]

  def _generate_examples(self, records):
    """Generate examples given the extracted records"""
    for i, row in enumerate(records):
      elems = row.split(",")
      features = {'name': ','.join(elems[:-2]), 'p_np': elems[-2]}
      yield i, {
          "features": features,
          "smiles": elems[-1],
      }

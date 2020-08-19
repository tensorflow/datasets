"""
Blood-brain barrier permeability (BBBP) dataset from MoleculeNet.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{wu2017moleculenet,
    title={MoleculeNet: A Benchmark for Molecular Machine Learning},
    author={Zhenqin Wu and Bharath Ramsundar and Evan N. Feinberg and Joseph Gomes and Caleb Geniesse and Aneesh S. Pappu and Karl Leswing and Vijay Pande},
    year={2017},
    eprint={1703.00564},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""

_DESCRIPTION = """
Blood-brain barrier permeability (BBBP) of 2000 compounds extracted from a study on the modeling and
prediction of the barrier permeability. As a membrane separating circulating blood and brain
extracellular fluid, the blood-brain barrier blocks most drugs, hormones and neurotransmitters.
Thus penetration of the barrier forms a long-standing issue in development of drugs targeting
central nervous system.
"""

_URL = "https://s3-us-west-1.amazonaws.com/deepchem.io/datasets/molnet_publish/bbbp.zip"
_FILE_NAME = "BBBP.csv"

class Bbbp(tfds.core.GeneratorBasedBuilder):
  """
  Blood-brain barrier permeability (BBBP) dataset from MoleculeNet.
  """

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "name": tfds.features.Text(),
            "smiles": tfds.features.Text(),
            "p_np": tfds.features.ClassLabel(num_classes=2)
        }),
        supervised_keys=("smiles", "p_np"),
        homepage="http://moleculenet.ai/datasets-1",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract(_URL)
    dataset_csv_path = os.path.join(extracted_path, _FILE_NAME),

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "dataset_csv_path": dataset_csv_path,
                "bounds": (0, 1641)
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "dataset_csv_path": dataset_csv_path,
                "bounds": (1641, 1847)
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "dataset_csv_path": dataset_csv_path,
                "bounds": (1847, 2053)
            },
        ),
    ]

  def _generate_examples(self, dataset_csv_path, bounds):
    with tf.io.gfile.GFile(dataset_csv_path[0]) as f:
      raw_data = csv.DictReader(f)

      for i, row in enumerate(raw_data[bounds[0]:bounds[1]]):
        yield i, {
            "name": row["name"],
            "p_np": int(row["p_np"]),
            "smiles": row["smiles"]
        }

"""BBBP(Blood-brain Barrier Penetration)  dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{wu2018moleculenet,
  title={MoleculeNet: a benchmark for molecular machine learning},
  author={Wu, Zhenqin and Ramsundar, Bharath and Feinberg, Evan N and Gomes, Joseph and Geniesse, Caleb and Pappu, 
          Aneesh S and Leswing, Karl and Pande, Vijay},
  journal={Chemical science},
  volume={9},
  number={2},
  pages={513--530},
  year={2018},
  publisher={Royal Society of Chemistry}
}
"""

_DESCRIPTION = """\
The Blood-brain barrier penetration (BBBP) dataset comes from a recent study 52 on the modeling and prediction of 
the barrier permeability. As a membrane separating circulating blood and brain extracellular fluid, the  blood-brain 
barrier blocks most drugs, hormones and neurotransmitters. Thus penetration of the barrier forms a long-standing issue 
in development of drugs targeting central nervous system. This dataset includes binary labels for over 2000 compounds 
on their permeability properties. Scaffold splitting is also recommended for this well-defined target.

Original Download URL: http://deepchem.io.s3-website-us-west-1.amazonaws.com/datasets/BBBP.csv
"""

_URL_ = "http://moleculenet.ai/datasets-1"
_DOWNLOAD_URL = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/modified_bbbp.csv"

""" Split URLs """
_RAND_TRAIN = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/random_train_bbbp.csv"
_RAND_TEST = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/random_test_bbbp.csv"
_SCAFF_TRAIN = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/scaffold_train_bbbp.csv"
_SCAFF_VALID = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/scaffold_valid_bbbp.csv"
_SCAFF_TEST = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/scaffold_test_bbbp.csv"
_SCAFF_TOTAL = "https://raw.githubusercontent.com/SoojungYang/ChemDatasetSplitter/master/bbbp/total_scaffold_bbbp.csv"


class Bbbp(tfds.core.GeneratorBasedBuilder):
    """Predict Blood-brain barrier penetration in binary classification."""
    # TODO(bbbp): Set up version.s
    VERSION = tfds.core.Version('0.1.0')

    def _info(self):
        # TODO(bbbp): Specifies the tfds.core.DatasetInfo object
        return tfds.core.DatasetInfo(
            builder=self,
            description=_DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "smile": tfds.features.Text(),
                "label":  tfds.features.ClassLabel(names=["0", "1"]),
            }),
            supervised_keys=("smile", "label"),
            homepage=_URL_,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        """
        TOTAL 2039 samples. 
        11 samples that are unable to be converted to 'mols' were removed from original dataset.
        ALL: total 2039 samples.  
        
        1) Random split samples (seed=123, ratio=8:2)
        TRAIN: randomly split bbbp for training (1631 samples)
        TEST: randomly split bbbp for test (408 samples)
        
        2) Scaffold split samples
        scaffold_train: choose samples from the largest scaffold sets (1631 samples)
        scaffold_valid: choose samples from the largest scaffold sets after train set (204 samples)
        scaffold_test: choose the remaining samples as test set (204 samples)
        scaffold: total samples, but sorted by the size of the scaffold set, from the largest to the smallest (2039 samples)
        """

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={"file": dl_manager.download(_RAND_TRAIN)},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={"file": dl_manager.download(_RAND_TEST)},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split('scaffold_train'),
                gen_kwargs={"file": dl_manager.download(_SCAFF_TRAIN)},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split('scaffold_validation'),
                gen_kwargs={"file": dl_manager.download(_SCAFF_VALID)},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split('scaffold_test'),
                gen_kwargs={"file": dl_manager.download(_SCAFF_TEST)},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split('scaffold'),
                gen_kwargs={"file": dl_manager.download(_SCAFF_TOTAL)},
            ),
        ]

    def _generate_examples(self, file):
        """Yields examples."""
        with tf.io.gfile.GFile(file) as f:
            reader = csv.DictReader(f)
            for _, row in enumerate(reader):
                yield row['num'], {
                    'smile': row['smiles'],
                    'label': row['p_np'],
                }

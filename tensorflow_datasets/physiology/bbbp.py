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
"""

_URL_ = "http://moleculenet.ai/datasets-1"
_DOWNLOAD_URL = "http://deepchem.io.s3-website-us-west-1.amazonaws.com/datasets/BBBP.csv"


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
        file = dl_manager.download(_DOWNLOAD_URL)
        """Returns SplitGenerators."""

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={"file": file},
            ),
            tfds.core.SplitGenerator(
                name=tfds.Split.TEST,
                gen_kwargs={"file": file},
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

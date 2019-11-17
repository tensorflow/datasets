"""BBBP(Blood-brain Barrier Penetration)  dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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


class Bbbp(tfds.core.GeneratorBasedBuilder):
  """TODO(bbbp): Short description of my dataset."""

  # TODO(bbbp): Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # TODO(bbbp): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        homepage='http://moleculenet.ai/datasets-1',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # TODO(bbbp): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={},
        ),
    ]

  def _generate_examples(self):
    """Yields examples."""
    # TODO(bbbp): Yields (key, example) tuples from the dataset
    yield 'key', {}


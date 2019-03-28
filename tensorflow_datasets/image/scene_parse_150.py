"""MIT Scene Parsing Benchmark (SceneParse150)"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds

# BibTeX citation
_CITATION = """
@inproceedings{zhou2017scene,
    title={Scene Parsing through ADE20K Dataset},
    author={Zhou, Bolei and Zhao, Hang and Puig, Xavier and Fidler, Sanja and Barriuso, Adela and Torralba, Antonio},
    booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
    year={2017}
}
@article{zhou2016semantic,
  title={Semantic understanding of scenes through the ade20k dataset},
  author={Zhou, Bolei and Zhao, Hang and Puig, Xavier and Fidler, Sanja and Barriuso, Adela and Torralba, Antonio},
  journal={arXiv preprint arXiv:1608.05442},
  year={2016}
}
"""


_DESCRIPTION = """
Scene parsing is to segment and parse an image into different image regions associated with semantic categories, such as sky, road, person, and bed. MIT Scene Parsing Benchmark (SceneParse150) provides a standard training and evaluation platform for the algorithms of scene parsing. 
"""

_TRAIN_URL = "http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip"
_TEST_URL  = "http://data.csail.mit.edu/places/ADEchallenge/release_test.zip" 

_IMAGE_SIZE = 256

_IMAGE_SHAPE = ( _IMAGE_SIZE, _IMAGE_SIZE, 3 )


class SceneParse150(tfds.core.GeneratorBasedBuilder):
  """MIT Scene Parsing Benchmark dataset"""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    # TODO(scene_parse_150): Specifies the tfds.core.DatasetInfo object
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
        urls=["http://sceneparsing.csail.mit.edu/"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    # TODO(scene_parse_150): Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # TODO(scene_parse_150): Tune the number of shards such that each shard
            # is < 4 GB.
            num_shards=10,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={},
        ),
    ]

  def _generate_examples(self):
    # TODO(scene_parse_150): Yields examples from the dataset
    yield {}


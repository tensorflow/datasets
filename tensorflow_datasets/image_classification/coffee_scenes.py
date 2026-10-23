"""coffee_scenes dataset."""
from pathlib import Path
import csv
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
 Brazildam dataset consists of multispectral images of ore tailings dams 
 throughout Brazil.
 This dataset is a composition of scenes taken by SPOT sensor in 2005 
 over four counties in the State of Minas Gerais, Brazil:
 Arceburgo, Guaranesia, Guaxupé and Monte Santo. 
 It has many intraclass variance caused by different crop management 
 techniques. Also this dataset includes scenes with different plant ages
 and/or with spectral distortions caused by shadows.
 The whole image set of each country was partitioned into multiple tiles of
 64 x 64 pixels.The identification of coffee crops (i.e. ground-truth 
 annotation) was performed manually by agricultural researches.
"""

_CITATION = """
 @inproceedings{penatti2015deep,
	title={Do deep features generalize from everyday objects to remote sensing and aerial scenes domains?},
	author={Penatti, Ot{\'a}vio AB and Nogueira, Keiller and Dos Santos, Jefersson A},
	booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition workshops},
	pages={44--51},
	year={2015}
}
"""

class CoffeeScenes(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for coffee_scenes dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(64, 64, 3)),
            'label': tfds.features.ClassLabel(names=['noncoffee','coffee']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'), 
        homepage='http://www.patreo.dcc.ufmg.br/2017/11/12/brazilian-coffee-scenes-dataset/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract('http://www.patreo.dcc.ufmg.br/wp-content/uploads/2017/11/brazilian_coffee_dataset.zip')

    return {
        'fold1': self._generate_examples(path / 'brazilian_coffee_scenes/fold1'),
        'fold2': self._generate_examples(path / 'brazilian_coffee_scenes/fold2'),
        'fold3': self._generate_examples(path / 'brazilian_coffee_scenes/fold3'),
        'fold4': self._generate_examples(path / 'brazilian_coffee_scenes/fold4'),
        'fold5': self._generate_examples(path / 'brazilian_coffee_scenes/fold5'),
    }


  def _generate_examples(self, path):
    """Yields examples."""
    with open(str(path)+".txt", mode='r') as reader:
      rd=csv.reader(reader, delimiter='.')
      for r in rd:
        x_name=r[1]+"."+r[2]+"."+r[3]+"."+r[4]+"."+r[5]+".jpg"
        yield x_name, {'image': path / x_name, 'label': r[0],}


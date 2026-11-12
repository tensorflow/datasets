"""kaokore dataset."""

import csv
import tensorflow_datasets.public_api as tfds
import tensorflow.compat.v2 as tf

_DESCRIPTION = """
KaoKore is a novel dataset of face images from Japanese illustrations along with multiple labels for each face, derived from the Collection of Facial Expressions.
"""

_CITATION = """\
@misc{tian2020kaokore,
  title={KaoKore: A Pre-modern Japanese Art Facial Expression Dataset},
  author={Yingtao Tian and Chikahiko Suzuki and Tarin Clanuwat and Mikel Bober-Irizar and Alex Lamb and Asanobu Kitamoto},
  year={2020},
  eprint={2002.08595},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
"""

_URL = 'https://raw.githubusercontent.com/rois-codh/kaokore/9acba43d89f2a32a0b126f1aae3603da6f56345f/dataset_v1.2'
_IMAGE_SIZE = 256
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)
_LABELS = {
  'gender': ['male', 'female'],
  'status': ['noble', 'warrior', 'incarnation', 'commoner'],
}


class Kaokore(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for kaokore dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
    '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
    tfds.core.BuilderConfig(
      name='gender',
      description='Use gender label.',
      version=tfds.core.Version('1.0.0'),
    ),
    tfds.core.BuilderConfig(
      name='status',
      description='Use status label.',
      version=tfds.core.Version('1.0.0'),
    ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict(
        {
          'image': tfds.features.Image(shape=_IMAGE_SHAPE),
          'label': tfds.features.ClassLabel(
            names=_LABELS[self.builder_config.name]
          ),
        }
      ),
      supervised_keys=('image', 'label'),
      homepage='http://codh.rois.ac.jp/face/dataset',
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    paths = dl_manager.download(
      {'labels.csv': _URL + '/labels.csv', 'urls.txt': _URL + '/urls.txt'}
    )

    urls = {}
    with tf.io.gfile.GFile(paths['urls.txt']) as f:
      for i, url in enumerate(f):
        urls['{:08d}.jpg'.format(i)] = url.strip()
    paths.update(dl_manager.download(urls))

    sets = {'train': {}, 'dev': {}, 'test': {}}
    label = self.builder_config.name
    with tf.io.gfile.GFile(paths['labels.csv']) as f:
      reader = csv.DictReader(f)
      for row in reader:
        sets[row['set']][row['image']] = int(row[label])

    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        gen_kwargs={'labels': sets['train'], 'paths': paths},
      ),
      tfds.core.SplitGenerator(
        name=tfds.Split.VALIDATION,
        gen_kwargs={'labels': sets['dev'], 'paths': paths},
      ),
      tfds.core.SplitGenerator(
        name=tfds.Split.TEST,
        gen_kwargs={'labels': sets['test'], 'paths': paths},
      ),
    ]

  def _generate_examples(self, labels, paths):
    for name, label in labels.items():
      yield name, {'image': paths[name], 'label': label}

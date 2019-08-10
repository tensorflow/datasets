'''Cityscapes Datasets.'''

import os
import re
import abc

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import api_utils

_CITATION = '''\
@inproceedings{Cordts2016Cityscapes,
  title={The Cityscapes Dataset for Semantic Urban Scene Understanding},
  author={Cordts, Marius and Omran, Mohamed and Ramos, Sebastian and Rehfeld, Timo and Enzweiler, Markus and Benenson, Rodrigo and Franke, Uwe and Roth, Stefan and Schiele, Bernt},
  booktitle={Proc. of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2016}
}
'''

_DESCRIPTION = '''\
  Cityscapes is a dataset consisting of diverse urban street scenes and dense pixel-level
  annotations taken across 50 different cities at varying times of the year. The label
  annotations span across 30 (34 including ignored indices) distinct classes of objects
  commonly encountered in driving scenes. Detailed label information may be found here:
  https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99

  The dataset consists of 5000 annotated image, label pairs at 1024 * 2048 resolution
  pre-split into training (2975) validation (500) and test (1525) sets.

  Cityscapes also provides an additional dataset subset (accessible via 'cityscapes/coarse')
  consisting of coarse labels for training and validation splits as well as 19998 images
  in a new 'train_extra' split which may be useful for data-heavy applications.

  WARNING: this dataset requires users to setup a login and password in order to get the files.
'''

# TODO add instance ids (might need to import cityScapesScripts)


class CityscapesConfig(tfds.core.BuilderConfig):
  '''BuilderConfig for Cityscapes'''

  @api_utils.disallow_positional_args
  def __init__(self, fine_grain=True, **kwargs):
    ''' BuilderConfig for Cityscapes
    Args:
      fine_grain: boolean switch to choose between coarse or fine grain labels
      **kwargs: keyword arguments forwarded to super.
    '''
    super().__init__(**kwargs)
    self.fine_grain = fine_grain

    # Setup zip and root dir names
    self.zip_root = {
      'images': ('leftImg8bit_trainvaltest.zip', 'leftImg8bit'),
      'labels': ('gtFine_trainvaltest.zip', 'gtFine') if fine_grain else
                ('gtCoarse.zip', 'gtCoarse'),
    }

    # Add coarse grain split
    if not fine_grain:
      self.zip_root['images_extra'] = ('leftImg8bit_trainextra.zip', 'leftImg8bit')

    # Setup suffix
    self.label_suffix = 'gtFine_labelIds' if fine_grain else 'gtCoarse_labelIds'
      
class Cityscapes(tfds.core.GeneratorBasedBuilder):
  '''Base class for Cityscapes datasets'''

  BUILDER_CONFIGS = [
      CityscapesConfig(
          name='fine',
          description='Cityscapes subset with fine grain labels.',
          version="0.1.0",
          fine_grain=True,
      ),
      CityscapesConfig(
          name='coarse',
          description='Cityscapes split with coarse grain labels.\nRequires additional download.',
          version="0.1.0",
          fine_grain=False,
      ),
  ]

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(1024, 2048, 3), encoding_format='png'),
            'label': tfds.features.Image(shape=(1024, 2048, 1), encoding_format='png'),
            'image_id': tfds.features.Text(),
        }),
        supervised_keys=('image', 'label'),
        urls=['https://www.cityscapes-dataset.com', 'https://github.com/mcordts/cityscapesScripts'],
        citation=_CITATION,
    )
  
  def _split_generators(self, dl_manager):

    paths = {}
    for split, (zip_file, zip_root) in self.builder_config.zip_root.items():
      paths[split] = os.path.join(dl_manager.manual_dir, zip_file)

    if any(not os.path.exists(z) for z in paths.values()):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join(paths.values())
      raise AssertionError(msg)

    for split, (_, zip_root) in self.builder_config.zip_root.items():
      paths[split] = os.path.join(dl_manager.extract(paths[split]), zip_root)

    ''' num_shards calculations:
    - instance size = image + label = 1024 * 2048 * 3 + 1024 * 2048 * 1 bytes = 8MB
    - max shard size = 4GB
    - max instances per shard = 4GB / 8MB = 512
    - shard sizes:
      - train: 2975 / 512 = 6
      - valid: 500 / 512 = 1
      - test: 1525 / 512 = 3
      - train_extra: 19998 / 512 = 40
    '''

    splits = [
      tfds.core.SplitGenerator(
          name=tfds.Split.TRAIN,
          num_shards=6,
          gen_kwargs={
              'images_path': os.path.join(paths['images'], 'train'),
              'labels_path': os.path.join(paths['labels'], 'train')
          },
      ),
      tfds.core.SplitGenerator(
          name=tfds.Split.VALIDATION,
          num_shards=1,
          gen_kwargs={
              'images_path': os.path.join(paths['images'], 'val'),
              'labels_path': os.path.join(paths['labels'], 'val')
          },
      ),
    ]

    # cityscapes coarse has no test split but instead has a train_extra split
    if self.builder_config.fine_grain:
      splits.append(tfds.core.SplitGenerator(
          name=tfds.Split.TEST,
          num_shards=3,
          gen_kwargs={
              'images_path': os.path.join(paths['images'], 'test'),
              'labels_path': os.path.join(paths['labels'], 'test')
          },
      ))
    else:
      splits.append(tfds.core.SplitGenerator(
          name='train_extra',
          num_shards=40,
          gen_kwargs={
              'images_path': os.path.join(paths['images_extra'], 'train_extra'),
              'labels_path': os.path.join(paths['labels'], 'train_extra'),
          },
      ))
    return splits

  def _generate_examples(self, images_path, labels_path):
    for city_id in tf.io.gfile.listdir(images_path):
      city_images_path = os.path.join(images_path, city_id)
      city_labels_path = os.path.join(labels_path, city_id)

      for image_file in tf.io.gfile.listdir(city_images_path):
        image_id = _image_id(image_file)
        image_path = os.path.join(city_images_path, image_file)
        label_path = os.path.join(
            city_labels_path, f'{image_id}_{self.builder_config.label_suffix}.png')

        features = {
            'image': image_path,
            'label': label_path,
            'image_id': image_id
        }
        yield image_id, features

# Helper functions

IMAGE_FILE_RE = re.compile(r'([a-z\-]+)_(\d+)_(\d+)_leftImg8bit\.png')

def _image_id(image_file):
  '''Returns the id of an image file. Used to associate an image file
  with its corresponding label.
  Example:
    'bonn_000001_000019_leftImg8bit' -> 'bonn_000001_000019'
  '''
  match = IMAGE_FILE_RE.match(image_file)
  return f'{match.group(1)}_{match.group(2)}_{match.group(3)}'

# pylint: disable=bad-indentation

'''Cityscapes Datasets.'''

import os
import re

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

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
  annotations span across 30 (34 including ingore indices) distinct classes of objects
  commonly encountered in driving scenes. Detailed label information may be found here:
  https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py#L52-L99

  The dataset consists of 5000 annotated image, label pairs at 1024 * 2048 resolution
  pre-split into training (2975) validation (500) and test (1525) sets.

  Cityscapes also provides an additional dataset (accessible via 'cityscapes_extra')
  consisting of coarse labels for training and validation splits as well as 19998 images
  in a new 'train_extra' split which may be useful for data-heavy applications.
'''

# TODO add instance ids (might need to import cityScapesScripts)

class CityscapesCore(tfds.core.GeneratorBasedBuilder):
  '''Base for cityscapes datasets'''

  VERSION = tfds.core.Version('2.0.0')

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
        urls=["https://www.cityscapes-dataset.com", "https://github.com/mcordts/cityscapesScripts"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    raise NotImplementedError

  def _generate_examples(self, images_path, labels_path):
    for city_id in tf.io.gfile.listdir(images_path):
      city_images_path = os.path.join(images_path, city_id)
      city_labels_path = os.path.join(labels_path, city_id)

      for image_file in tf.io.gfile.listdir(city_images_path):
        image_id = _image_id(image_file)
        image_path = os.path.join(city_images_path, image_file)
        label_path = os.path.join(
            city_labels_path, f'{image_id}_{self.__class__.CITYSCAPES_LABEL_SUFFIX}.png')

        yield {
            'image': image_path,
            'label': label_path,
            'image_id': image_id
        }


class Cityscapes(CityscapesCore):
  '''Cityscapes with fine labels.'''

  CITYSCAPES_LABEL_SUFFIX = 'gtFine_labelIds'

  def _split_generators(self, dl_manager):
    paths = {
        'images': os.path.join(dl_manager.manual_dir, 'leftImg8bit_trainvaltest.zip'),
        'labels': os.path.join(dl_manager.manual_dir, 'gtFine_trainvaltest.zip'),
    }

    if any(not os.path.exists(p) for p in paths.values()):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join(paths.values())
      raise AssertionError(msg)

    paths['images'] = os.path.join(dl_manager.extract(paths['images']), 'leftImg8bit')
    paths['labels'] = os.path.join(dl_manager.extract(paths['labels']), 'gtFine')

    # Number of shards calculations:
    # Max shard size = 4GB
    # Instance size = image + label = 1024 * 2048 * 3 + 1024 * 2048 * 4 bytes = 8MB
    # Max instances per shard = 4GB / 8MB = 512
    # Split shards = 2975 / 512 = 6, 500 / 512 = 1, 1525 / 512 = 3
    return [
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
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=3,
            gen_kwargs={
                'images_path': os.path.join(paths['images'], 'test'),
                'labels_path': os.path.join(paths['labels'], 'test')
            },
        ),
    ]

class CityscapesCoarse(CityscapesCore):
  '''Cityscapes with coarse labels and train_extra split.'''

  CITYSCAPES_LABEL_SUFFIX = 'gtCoarse_labelIds'

  def _split_generators(self, dl_manager):
    paths = {
        'images': os.path.join(dl_manager.manual_dir, 'leftImg8bit_trainvaltest.zip'),
        'images_extra': os.path.join(dl_manager.manual_dir, 'leftImg8bit_trainextra.zip'),
        'labels': os.path.join(dl_manager.manual_dir, 'gtCoarse.zip'),
    }

    if any(not os.path.exists(p) for p in paths.values()):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join(paths.values())
      raise AssertionError(msg)

    paths['images'] = os.path.join(dl_manager.extract(paths['images']), 'leftImg8bit')
    paths['images_extra'] = os.path.join(dl_manager.extract(paths['images_extra']), 'leftImg8bit')
    paths['labels'] = os.path.join(dl_manager.extract(paths['labels']), 'gtCoarse')

    # Number of shards calculations (see Cityscapes class for details)
    # Max instances per shard = 4GB / 8MB = 512
    # Split shards = ceil(2975 / 512) = 6, ceil(19998 / 512) = 40, ceil(1525 / 512) = 3
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=6,
            gen_kwargs={
                'images_path': os.path.join(paths['images'], 'train'),
                'labels_path': os.path.join(paths['labels'], 'train'),
            },
        ),
        tfds.core.SplitGenerator(
            name='train_extra',
            num_shards=40,
            gen_kwargs={
                'images_path': os.path.join(paths['images_extra'], 'train_extra'),
                'labels_path': os.path.join(paths['labels'], 'train_extra'),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=1,
            gen_kwargs={
                'images_path': os.path.join(paths['images'], 'val'),
                'labels_path': os.path.join(paths['labels'], 'val'),
            },
        ),
    ]

# Helper functions

IMAGE_FILE_RE = re.compile(r'([a-z\-]+)_(\d+)_(\d+)_leftImg8bit\.png')

def _image_id(image_file):
  match = IMAGE_FILE_RE.match(image_file)
  return f'{match.group(1)}_{match.group(2)}_{match.group(3)}'

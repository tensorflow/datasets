# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""DomainNet dataset."""
import dataclasses
import os
from typing import Any, Dict, Iterator, Optional, Text, Tuple

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The DomainNet dataset consists of images from six distinct domains, including
photos (real), painting, clipart, quickdraw, infograph and sketch. Per domain
there are 48K - 172K images (600K in total) categorized into 345 classes.

In this TFDS version of DomainNet the cleaned version is used.
"""

_HOMEPAGE = 'http://ai.bu.edu/DomainNet/'
_CITATION = """\
@inproceedings{peng2019moment,
  title={Moment matching for multi-source domain adaptation},
  author={Peng, Xingchao and Bai, Qinxun and Xia, Xide and Huang, Zijun and Saenko, Kate and Wang, Bo},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={1406--1415},
  year={2019}
}
"""

_CLASS_NAMES = [
    'aircraft_carrier',
    'airplane',
    'alarm_clock',
    'ambulance',
    'angel',
    'animal_migration',
    'ant',
    'anvil',
    'apple',
    'arm',
    'asparagus',
    'axe',
    'backpack',
    'banana',
    'bandage',
    'barn',
    'baseball',
    'baseball_bat',
    'basket',
    'basketball',
    'bat',
    'bathtub',
    'beach',
    'bear',
    'beard',
    'bed',
    'bee',
    'belt',
    'bench',
    'bicycle',
    'binoculars',
    'bird',
    'birthday_cake',
    'blackberry',
    'blueberry',
    'book',
    'boomerang',
    'bottlecap',
    'bowtie',
    'bracelet',
    'brain',
    'bread',
    'bridge',
    'broccoli',
    'broom',
    'bucket',
    'bulldozer',
    'bus',
    'bush',
    'butterfly',
    'cactus',
    'cake',
    'calculator',
    'calendar',
    'camel',
    'camera',
    'camouflage',
    'campfire',
    'candle',
    'cannon',
    'canoe',
    'car',
    'carrot',
    'castle',
    'cat',
    'ceiling_fan',
    'cello',
    'cell_phone',
    'chair',
    'chandelier',
    'church',
    'circle',
    'clarinet',
    'clock',
    'cloud',
    'coffee_cup',
    'compass',
    'computer',
    'cookie',
    'cooler',
    'couch',
    'cow',
    'crab',
    'crayon',
    'crocodile',
    'crown',
    'cruise_ship',
    'cup',
    'diamond',
    'dishwasher',
    'diving_board',
    'dog',
    'dolphin',
    'donut',
    'door',
    'dragon',
    'dresser',
    'drill',
    'drums',
    'duck',
    'dumbbell',
    'ear',
    'elbow',
    'elephant',
    'envelope',
    'eraser',
    'eye',
    'eyeglasses',
    'face',
    'fan',
    'feather',
    'fence',
    'finger',
    'fire_hydrant',
    'fireplace',
    'firetruck',
    'fish',
    'flamingo',
    'flashlight',
    'flip_flops',
    'floor_lamp',
    'flower',
    'flying_saucer',
    'foot',
    'fork',
    'frog',
    'frying_pan',
    'garden',
    'garden_hose',
    'giraffe',
    'goatee',
    'golf_club',
    'grapes',
    'grass',
    'guitar',
    'hamburger',
    'hammer',
    'hand',
    'harp',
    'hat',
    'headphones',
    'hedgehog',
    'helicopter',
    'helmet',
    'hexagon',
    'hockey_puck',
    'hockey_stick',
    'horse',
    'hospital',
    'hot_air_balloon',
    'hot_dog',
    'hot_tub',
    'hourglass',
    'house',
    'house_plant',
    'hurricane',
    'ice_cream',
    'jacket',
    'jail',
    'kangaroo',
    'key',
    'keyboard',
    'knee',
    'knife',
    'ladder',
    'lantern',
    'laptop',
    'leaf',
    'leg',
    'light_bulb',
    'lighter',
    'lighthouse',
    'lightning',
    'line',
    'lion',
    'lipstick',
    'lobster',
    'lollipop',
    'mailbox',
    'map',
    'marker',
    'matches',
    'megaphone',
    'mermaid',
    'microphone',
    'microwave',
    'monkey',
    'moon',
    'mosquito',
    'motorbike',
    'mountain',
    'mouse',
    'moustache',
    'mouth',
    'mug',
    'mushroom',
    'nail',
    'necklace',
    'nose',
    'ocean',
    'octagon',
    'octopus',
    'onion',
    'oven',
    'owl',
    'paintbrush',
    'paint_can',
    'palm_tree',
    'panda',
    'pants',
    'paper_clip',
    'parachute',
    'parrot',
    'passport',
    'peanut',
    'pear',
    'peas',
    'pencil',
    'penguin',
    'piano',
    'pickup_truck',
    'picture_frame',
    'pig',
    'pillow',
    'pineapple',
    'pizza',
    'pliers',
    'police_car',
    'pond',
    'pool',
    'popsicle',
    'postcard',
    'potato',
    'power_outlet',
    'purse',
    'rabbit',
    'raccoon',
    'radio',
    'rain',
    'rainbow',
    'rake',
    'remote_control',
    'rhinoceros',
    'rifle',
    'river',
    'roller_coaster',
    'rollerskates',
    'sailboat',
    'sandwich',
    'saw',
    'saxophone',
    'school_bus',
    'scissors',
    'scorpion',
    'screwdriver',
    'sea_turtle',
    'see_saw',
    'shark',
    'sheep',
    'shoe',
    'shorts',
    'shovel',
    'sink',
    'skateboard',
    'skull',
    'skyscraper',
    'sleeping_bag',
    'smiley_face',
    'snail',
    'snake',
    'snorkel',
    'snowflake',
    'snowman',
    'soccer_ball',
    'sock',
    'speedboat',
    'spider',
    'spoon',
    'spreadsheet',
    'square',
    'squiggle',
    'squirrel',
    'stairs',
    'star',
    'steak',
    'stereo',
    'stethoscope',
    'stitches',
    'stop_sign',
    'stove',
    'strawberry',
    'streetlight',
    'string_bean',
    'submarine',
    'suitcase',
    'sun',
    'swan',
    'sweater',
    'swing_set',
    'sword',
    'syringe',
    'table',
    'teapot',
    'teddy-bear',
    'telephone',
    'television',
    'tennis_racquet',
    'tent',
    'The_Eiffel_Tower',
    'The_Great_Wall_of_China',
    'The_Mona_Lisa',
    'tiger',
    'toaster',
    'toe',
    'toilet',
    'tooth',
    'toothbrush',
    'toothpaste',
    'tornado',
    'tractor',
    'traffic_light',
    'train',
    'tree',
    'triangle',
    'trombone',
    'truck',
    'trumpet',
    't-shirt',
    'umbrella',
    'underwear',
    'van',
    'vase',
    'violin',
    'washing_machine',
    'watermelon',
    'waterslide',
    'whale',
    'wheel',
    'windmill',
    'wine_bottle',
    'wine_glass',
    'wristwatch',
    'yoga',
    'zebra',
    'zigzag',
]


@dataclasses.dataclass
class DomainnetConfig(tfds.core.BuilderConfig):
  name: Text
  img_url: Optional[Text] = None


class Domainnet(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for domainnet dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  BUILDER_CONFIGS = [
      DomainnetConfig(name='real', img_url='real.zip'),
      DomainnetConfig(name='painting', img_url='groundtruth/painting.zip'),
      DomainnetConfig(name='clipart', img_url='groundtruth/clipart.zip'),
      DomainnetConfig(name='quickdraw', img_url='quickdraw.zip'),
      DomainnetConfig(name='infograph', img_url='infograph.zip'),
      DomainnetConfig(name='sketch', img_url='sketch.zip'),
  ]

  _BASE_URL = 'http://csr.bu.edu/ftp/visda/2019/multi-source'

  img_path: Any
  splits: Dict[str, Any]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        citation=_CITATION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(None, None, 3)),
            'label': tfds.features.ClassLabel(names=_CLASS_NAMES),
        }),
        homepage=_HOMEPAGE,
        supervised_keys=('image', 'label'),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    img_download_url = f'{self._BASE_URL}/{self.builder_config.img_url}'
    self.img_path = dl_manager.download_and_extract(img_download_url)

    domain = self.builder_config.name
    train_split_url = f'{self._BASE_URL}/domainnet/txt/{domain}_train.txt'
    test_split_url = f'{self._BASE_URL}/domainnet/txt/{domain}_test.txt'

    self.splits = dl_manager.download(
        {'train': train_split_url, 'test': test_split_url}
    )

    return {
        'train': self._generate_examples(split='train'),
        'test': self._generate_examples(split='test'),
    }

  def _generate_examples(
      self, split: Text = 'train'
  ) -> Iterator[Tuple[Text, Dict[Text, Any]]]:
    """Generator of examples for each split."""
    with tf.io.gfile.GFile(self.splits[split]) as split_file:  # pytype: disable=attribute-error  # gen-stub-imports
      for i, img_class_line in enumerate(split_file.read().split('\n')):
        if not img_class_line:
          continue
        key = f'{self.builder_config.name}_{split}_{i:08d}'

        example_path, example_class = img_class_line.split(' ')
        example_fullpath = os.path.join(self.img_path, example_path)  # pytype: disable=attribute-error  # gen-stub-imports

        yield key, {'image': example_fullpath, 'label': int(example_class)}

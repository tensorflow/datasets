# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Dataset class for Cars196 Dataset."""
import os

import six.moves.urllib as urllib
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = 'http://ai.stanford.edu/~jkrause/car196/'
_EXTRA_URL = 'https://ai.stanford.edu/~jkrause/cars/car_devkit.tgz'

_DESCRIPTION = (
    'The Cars dataset contains 16,185 images of 196 classes of cars. The data '
    'is split into 8,144 training images and 8,041 testing images, where each '
    'class has been split roughly in a 50-50 split. Classes are typically at '
    'the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 '
    'coupe.')

_NAMES = [
    'AM General Hummer SUV 2000',
    'Acura RL Sedan 2012',
    'Acura TL Sedan 2012',
    'Acura TL Type-S 2008',
    'Acura TSX Sedan 2012',
    'Acura Integra Type R 2001',
    'Acura ZDX Hatchback 2012',
    'Aston Martin V8 Vantage Convertible 2012',
    'Aston Martin V8 Vantage Coupe 2012',
    'Aston Martin Virage Convertible 2012',
    'Aston Martin Virage Coupe 2012',
    'Audi RS 4 Convertible 2008',
    'Audi A5 Coupe 2012',
    'Audi TTS Coupe 2012',
    'Audi R8 Coupe 2012',
    'Audi V8 Sedan 1994',
    'Audi 100 Sedan 1994',
    'Audi 100 Wagon 1994',
    'Audi TT Hatchback 2011',
    'Audi S6 Sedan 2011',
    'Audi S5 Convertible 2012',
    'Audi S5 Coupe 2012',
    'Audi S4 Sedan 2012',
    'Audi S4 Sedan 2007',
    'Audi TT RS Coupe 2012',
    'BMW ActiveHybrid 5 Sedan 2012',
    'BMW 1 Series Convertible 2012',
    'BMW 1 Series Coupe 2012',
    'BMW 3 Series Sedan 2012',
    'BMW 3 Series Wagon 2012',
    'BMW 6 Series Convertible 2007',
    'BMW X5 SUV 2007',
    'BMW X6 SUV 2012',
    'BMW M3 Coupe 2012',
    'BMW M5 Sedan 2010',
    'BMW M6 Convertible 2010',
    'BMW X3 SUV 2012',
    'BMW Z4 Convertible 2012',
    'Bentley Continental Supersports Conv. Convertible 2012',
    'Bentley Arnage Sedan 2009',
    'Bentley Mulsanne Sedan 2011',
    'Bentley Continental GT Coupe 2012',
    'Bentley Continental GT Coupe 2007',
    'Bentley Continental Flying Spur Sedan 2007',
    'Bugatti Veyron 16.4 Convertible 2009',
    'Bugatti Veyron 16.4 Coupe 2009',
    'Buick Regal GS 2012',
    'Buick Rainier SUV 2007',
    'Buick Verano Sedan 2012',
    'Buick Enclave SUV 2012',
    'Cadillac CTS-V Sedan 2012',
    'Cadillac SRX SUV 2012',
    'Cadillac Escalade EXT Crew Cab 2007',
    'Chevrolet Silverado 1500 Hybrid Crew Cab 2012',
    'Chevrolet Corvette Convertible 2012',
    'Chevrolet Corvette ZR1 2012',
    'Chevrolet Corvette Ron Fellows Edition Z06 2007',
    'Chevrolet Traverse SUV 2012',
    'Chevrolet Camaro Convertible 2012',
    'Chevrolet HHR SS 2010',
    'Chevrolet Impala Sedan 2007',
    'Chevrolet Tahoe Hybrid SUV 2012',
    'Chevrolet Sonic Sedan 2012',
    'Chevrolet Express Cargo Van 2007',
    'Chevrolet Avalanche Crew Cab 2012',
    'Chevrolet Cobalt SS 2010',
    'Chevrolet Malibu Hybrid Sedan 2010',
    'Chevrolet TrailBlazer SS 2009',
    'Chevrolet Silverado 2500HD Regular Cab 2012',
    'Chevrolet Silverado 1500 Classic Extended Cab 2007',
    'Chevrolet Express Van 2007',
    'Chevrolet Monte Carlo Coupe 2007',
    'Chevrolet Malibu Sedan 2007',
    'Chevrolet Silverado 1500 Extended Cab 2012',
    'Chevrolet Silverado 1500 Regular Cab 2012',
    'Chrysler Aspen SUV 2009',
    'Chrysler Sebring Convertible 2010',
    'Chrysler Town and Country Minivan 2012',
    'Chrysler 300 SRT-8 2010',
    'Chrysler Crossfire Convertible 2008',
    'Chrysler PT Cruiser Convertible 2008',
    'Daewoo Nubira Wagon 2002',
    'Dodge Caliber Wagon 2012',
    'Dodge Caliber Wagon 2007',
    'Dodge Caravan Minivan 1997',
    'Dodge Ram Pickup 3500 Crew Cab 2010',
    'Dodge Ram Pickup 3500 Quad Cab 2009',
    'Dodge Sprinter Cargo Van 2009',
    'Dodge Journey SUV 2012',
    'Dodge Dakota Crew Cab 2010',
    'Dodge Dakota Club Cab 2007',
    'Dodge Magnum Wagon 2008',
    'Dodge Challenger SRT8 2011',
    'Dodge Durango SUV 2012',
    'Dodge Durango SUV 2007',
    'Dodge Charger Sedan 2012',
    'Dodge Charger SRT-8 2009',
    'Eagle Talon Hatchback 1998',
    'FIAT 500 Abarth 2012',
    'FIAT 500 Convertible 2012',
    'Ferrari FF Coupe 2012',
    'Ferrari California Convertible 2012',
    'Ferrari 458 Italia Convertible 2012',
    'Ferrari 458 Italia Coupe 2012',
    'Fisker Karma Sedan 2012',
    'Ford F-450 Super Duty Crew Cab 2012',
    'Ford Mustang Convertible 2007',
    'Ford Freestar Minivan 2007',
    'Ford Expedition EL SUV 2009',
    'Ford Edge SUV 2012',
    'Ford Ranger SuperCab 2011',
    'Ford GT Coupe 2006',
    'Ford F-150 Regular Cab 2012',
    'Ford F-150 Regular Cab 2007',
    'Ford Focus Sedan 2007',
    'Ford E-Series Wagon Van 2012',
    'Ford Fiesta Sedan 2012',
    'GMC Terrain SUV 2012',
    'GMC Savana Van 2012',
    'GMC Yukon Hybrid SUV 2012',
    'GMC Acadia SUV 2012',
    'GMC Canyon Extended Cab 2012',
    'Geo Metro Convertible 1993',
    'HUMMER H3T Crew Cab 2010',
    'HUMMER H2 SUT Crew Cab 2009',
    'Honda Odyssey Minivan 2012',
    'Honda Odyssey Minivan 2007',
    'Honda Accord Coupe 2012',
    'Honda Accord Sedan 2012',
    'Hyundai Veloster Hatchback 2012',
    'Hyundai Santa Fe SUV 2012',
    'Hyundai Tucson SUV 2012',
    'Hyundai Veracruz SUV 2012',
    'Hyundai Sonata Hybrid Sedan 2012',
    'Hyundai Elantra Sedan 2007',
    'Hyundai Accent Sedan 2012',
    'Hyundai Genesis Sedan 2012',
    'Hyundai Sonata Sedan 2012',
    'Hyundai Elantra Touring Hatchback 2012',
    'Hyundai Azera Sedan 2012',
    'Infiniti G Coupe IPL 2012',
    'Infiniti QX56 SUV 2011',
    'Isuzu Ascender SUV 2008',
    'Jaguar XK XKR 2012',
    'Jeep Patriot SUV 2012',
    'Jeep Wrangler SUV 2012',
    'Jeep Liberty SUV 2012',
    'Jeep Grand Cherokee SUV 2012',
    'Jeep Compass SUV 2012',
    'Lamborghini Reventon Coupe 2008',
    'Lamborghini Aventador Coupe 2012',
    'Lamborghini Gallardo LP 570-4 Superleggera 2012',
    'Lamborghini Diablo Coupe 2001',
    'Land Rover Range Rover SUV 2012',
    'Land Rover LR2 SUV 2012',
    'Lincoln Town Car Sedan 2011',
    'MINI Cooper Roadster Convertible 2012',
    'Maybach Landaulet Convertible 2012',
    'Mazda Tribute SUV 2011',
    'McLaren MP4-12C Coupe 2012',
    'Mercedes-Benz 300-Class Convertible 1993',
    'Mercedes-Benz C-Class Sedan 2012',
    'Mercedes-Benz SL-Class Coupe 2009',
    'Mercedes-Benz E-Class Sedan 2012',
    'Mercedes-Benz S-Class Sedan 2012',
    'Mercedes-Benz Sprinter Van 2012',
    'Mitsubishi Lancer Sedan 2012',
    'Nissan Leaf Hatchback 2012',
    'Nissan NV Passenger Van 2012',
    'Nissan Juke Hatchback 2012',
    'Nissan 240SX Coupe 1998',
    'Plymouth Neon Coupe 1999',
    'Porsche Panamera Sedan 2012',
    'Ram C/V Cargo Van Minivan 2012',
    'Rolls-Royce Phantom Drophead Coupe Convertible 2012',
    'Rolls-Royce Ghost Sedan 2012',
    'Rolls-Royce Phantom Sedan 2012',
    'Scion xD Hatchback 2012',
    'Spyker C8 Convertible 2009',
    'Spyker C8 Coupe 2009',
    'Suzuki Aerio Sedan 2007',
    'Suzuki Kizashi Sedan 2012',
    'Suzuki SX4 Hatchback 2012',
    'Suzuki SX4 Sedan 2012',
    'Tesla Model S Sedan 2012',
    'Toyota Sequoia SUV 2012',
    'Toyota Camry Sedan 2012',
    'Toyota Corolla Sedan 2012',
    'Toyota 4Runner SUV 2012',
    'Volkswagen Golf Hatchback 2012',
    'Volkswagen Golf Hatchback 1991',
    'Volkswagen Beetle Hatchback 2012',
    'Volvo C30 Hatchback 2012',
    'Volvo 240 Sedan 1993',
    'Volvo XC90 SUV 2007',
    'smart fortwo Convertible 2012',
]

_CITATION = """\

    @inproceedings{KrauseStarkDengFei-Fei_3DRR2013,
  title = {3D Object Representations for Fine-Grained Categorization},
  booktitle = {4th International IEEE Workshop on  3D Representation and Recognition (3dRR-13)},
  year = {2013},
  address = {Sydney, Australia},
  author = {Jonathan Krause and Michael Stark and Jia Deng and Li Fei-Fei}
  }

"""


class Cars196(tfds.core.GeneratorBasedBuilder):
  """Car Images dataset."""

  VERSION = tfds.core.Version('2.1.0')
  SUPPORTED_VERSIONS = [
      tfds.core.Version('2.1.0'),
  ]

  RELEASE_NOTES = {
      '2.0.0': 'Initial release',
      '2.0.1': 'Website URL update',
      '2.1.0': 'Fixing bug https://github.com/tensorflow/datasets/issues/3927',
  }

  def _info(self):
    """Define the dataset info."""
    features_dict = {
        'image': tfds.features.Image(),
        'label': tfds.features.ClassLabel(names=_NAMES),
        'bbox': tfds.features.BBoxFeature(),
    }
    if self.version > '2.0.0':
      features_dict['id'] = tfds.features.Text()
    return tfds.core.DatasetInfo(
        builder=self,
        description=(_DESCRIPTION),
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=('image', 'label'),
        homepage='https://ai.stanford.edu/~jkrause/cars/car_dataset.html',
        citation=_CITATION)

  def _split_generators(self, dl_manager):
    """Define the train and test split."""
    output_files = dl_manager.download_and_extract({
        'train':
            urllib.parse.urljoin(_URL, 'cars_train.tgz'),
        'test':
            urllib.parse.urljoin(_URL, 'cars_test.tgz'),
        'extra':
            _EXTRA_URL,
        'test_annos':
            urllib.parse.urljoin(_URL, 'cars_test_annos_withlabels.mat'),
    })

    return [
        tfds.core.SplitGenerator(
            name='train',
            gen_kwargs={
                'split_name':
                    'train',
                'data_dir_path':
                    os.path.join(output_files['train'], 'cars_train'),
                'data_annotations_path':
                    os.path.join(output_files['extra'],
                                 os.path.join('devkit',
                                              'cars_train_annos.mat')),
            },
        ),
        tfds.core.SplitGenerator(
            name='test',
            gen_kwargs={
                'split_name':
                    'test',
                'data_dir_path':
                    os.path.join(output_files['test'], 'cars_test'),
                'data_annotations_path':
                    output_files['test_annos'],
            },
        ),
    ]

  def _generate_examples(self, split_name, data_dir_path,
                         data_annotations_path):
    """Generate training and testing samples."""

    image_dict = self.returnImageDict(data_dir_path)
    bbox_dict = self.returnBbox(data_annotations_path, image_dict)
    with tf.io.gfile.GFile(data_annotations_path, 'rb') as f:
      mat = tfds.core.lazy_imports.scipy.io.loadmat(f)
    for example in mat['annotations'][0]:
      image_name = example[-1].item().split('.')[0]
      label = _NAMES[example[4].item() - 1]
      image = image_dict[image_name]
      bbox = bbox_dict[image_name]
      features = {
          'label': label,
          'image': image,
          'bbox': bbox,
      }
      if self.version > '2.0.0':
        features['id'] = image_name
      yield image_name, features

  def returnImageDict(self, path):
    return {
        filename.split('.')[0]: os.path.join(path, filename)
        for filename in tf.io.gfile.listdir(path)
    }

  def returnBbox(self, filename, image_dict):
    bbox_dict = {}
    with tf.io.gfile.GFile(filename, 'rb') as f:
      data = tfds.core.lazy_imports.scipy.io.loadmat(f)
    for example in data['annotations'][0]:
      image_name = example[-1].item().split('.')[0]
      ymin = float(example[1].item())
      xmin = float(example[0].item())
      ymax = float(example[3].item())
      xmax = float(example[2].item())
      with tf.io.gfile.GFile(image_dict[image_name], 'rb') as fp:
        img = tfds.core.lazy_imports.PIL_Image.open(fp)
        width, height = img.size
      bbox_dict[image_name] = tfds.features.BBox(ymin / height, xmin / width,
                                                 ymax / height, xmax / width)
    return bbox_dict

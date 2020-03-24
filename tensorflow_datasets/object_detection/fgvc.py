# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""FGVC Aircraft Dataset."""

import os
import tensorflow_datasets.public_api as tfds

_PROJECT_URL = 'http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/'

_DATASET_URL = 'http://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/archives/fgvc-aircraft-2013b.tar.gz'

_CITATION = """
@techreport{maji13fine-grained,
   title         = {Fine-Grained Visual Classification of Aircraft},
   author        = {S. Maji and J. Kannala and E. Rahtu
                    and M. Blaschko and A. Vedaldi},
   year          = {2013},
   archivePrefix = {arXiv},
   eprint        = {1306.5151},
   primaryClass  = "cs-cv",
}
"""

_DESCRIPTION = """
The dataset contains 10,200 images of aircraft, with 100 images for each of 102
different aircraft model variants, most of which are airplanes. The (main)
aircraft in each image is annotated with a tight bounding box and a
hierarchical airplane model label.

Aircraft models are organized in a four-levels hierarchy. The four levels,
from finer to coarser, are:

1)   Model, e.g. Boeing 737-76J. Since certain models are nearly visually
     indistinguishable, this level is not used in the evaluation.
2)   Variant, e.g. Boeing 737-700. A variant collapses all the models that are
     visually indistinguishable into one class. The dataset comprises 102
     different variants.
3)   Family, e.g. Boeing 737. The dataset comprises 70 different families.
4)   Manufacturer, e.g. Boeing. The dataset comprises 41 different
     manufacturers.
"""


def convert_to_string(d):
  return d


FAMILIES = ['A300', 'A310', 'A320', 'A330', 'A340', 'A380', 'ATR-42', 'ATR-72',
            'An-12', 'BAE 146', 'BAE-125', 'Beechcraft 1900', 'Boeing 707',
            'Boeing 717', 'Boeing 727', 'Boeing 737', 'Boeing 747',
            'Boeing 757', 'Boeing 767', 'Boeing 777', 'C-130', 'C-47',
            'CRJ-200', 'CRJ-700', 'Cessna 172', 'Cessna 208',
            'Cessna Citation', 'Challenger 600', 'DC-10', 'DC-3', 'DC-6',
            'DC-8', 'DC-9', 'DH-82', 'DHC-1', 'DHC-6', 'DR-400', 'Dash 8',
            'Dornier 328', 'EMB-120', 'Embraer E-Jet', 'Embraer ERJ 145',
            'Embraer Legacy 600', 'Eurofighter Typhoon', 'F-16', 'F/A-18',
            'Falcon 2000', 'Falcon 900', 'Fokker 100', 'Fokker 50',
            'Fokker 70', 'Global Express', 'Gulfstream', 'Hawk T1', 'Il-76',
            'King Air', 'L-1011', 'MD-11', 'MD-80', 'MD-90', 'Metroliner',
            'PA-28', 'SR-20', 'Saab 2000', 'Saab 340', 'Spitfire', 'Tornado',
            'Tu-134', 'Tu-154', 'Yak-42']


MANUFACTURERS = ['ATR', 'Airbus', 'Antonov', 'Beechcraft', 'Boeing',
                 'Bombardier Aerospace', 'British Aerospace', 'Canadair',
                 'Cessna', 'Cirrus Aircraft', 'Dassault Aviation', 'Dornier',
                 'Douglas Aircraft Company', 'Embraer', 'Eurofighter',
                 'Fairchild', 'Fokker', 'Gulfstream Aerospace', 'Ilyushin',
                 'Lockheed Corporation', 'Lockheed Martin',
                 'McDonnell Douglas', 'Panavia', 'Piper', 'Robin', 'Saab',
                 'Supermarine', 'Tupolev', 'Yakovlev', 'de Havilland']


VARIANTS = ['707-320', '727-200', '737-200', '737-300', '737-400', '737-500',
            '737-600', '737-700', '737-800', '737-900', '747-100', '747-200',
            '747-300', '747-400', '757-200', '757-300', '767-200', '767-300',
            '767-400', '777-200', '777-300', 'A300B4', 'A310', 'A318', 'A319',
            'A320', 'A321', 'A330-200', 'A330-300', 'A340-200', 'A340-300',
            'A340-500', 'A340-600', 'A380', 'ATR-42', 'ATR-72', 'An-12',
            'BAE 146-200', 'BAE 146-300', 'BAE-125', 'Beechcraft 1900',
            'Boeing 717', 'C-130', 'C-47', 'CRJ-200', 'CRJ-700', 'CRJ-900',
            'Cessna 172', 'Cessna 208', 'Cessna 525', 'Cessna 560',
            'Challenger 600', 'DC-10', 'DC-3', 'DC-6', 'DC-8', 'DC-9-30',
            'DH-82', 'DHC-1', 'DHC-6', 'DHC-8-100', 'DHC-8-300', 'DR-400',
            'Dornier 328', 'E-170', 'E-190', 'E-195', 'EMB-120', 'ERJ 135',
            'ERJ 145', 'Embraer Legacy 600', 'Eurofighter Typhoon', 'F-16A/B',
            'F/A-18', 'Falcon 2000', 'Falcon 900', 'Fokker 100', 'Fokker 50',
            'Fokker 70', 'Global Express', 'Gulfstream IV', 'Gulfstream V',
            'Hawk T1', 'Il-76', 'L-1011', 'MD-11', 'MD-80', 'MD-87', 'MD-90',
            'Metroliner', 'Model B200', 'PA-28', 'SR-20', 'Saab 2000',
            'Saab 340', 'Spitfire', 'Tornado', 'Tu-134', 'Tu-154', 'Yak-42']

FEATURES_DICT = {
    'image': tfds.features.Image(encoding_format='jpeg'),
    'image_predictions': tfds.features.Sequence({
        'bbox': tfds.features.BBoxFeature(),
        'family': tfds.features.ClassLabel(names=FAMILIES),
        'manufacturer': tfds.features.ClassLabel(names=MANUFACTURERS),
        'variant': tfds.features.ClassLabel(names=VARIANTS)
        })
    }


class FGVC(tfds.core.GeneratorBasedBuilder):
  """FGVC Aircraft Dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(FEATURES_DICT),
        homepage=_PROJECT_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_dirs = dl_manager.download_and_extract(_DATASET_URL)
    extracted_dirs = os.path.join(extracted_dirs, 'fgvc-aircraft-2013b')
    extracted_dirs = os.path.join(extracted_dirs, 'data')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'split': 'train',
                'extracted_dirs': extracted_dirs
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'split': 'val',
                'extracted_dirs': extracted_dirs
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'split': 'test',
                'extracted_dirs': extracted_dirs
            })
    ]

  def _generate_examples(self, split, extracted_dirs):
    """Yields examples."""
    filenames = open(os.path.join(extracted_dirs,
                                  'images_{}.txt'.format(split))).readlines()
    filenames = [filename.strip() + '.jpg' for filename in filenames]

    families = open(os.path.join(extracted_dirs,
                                 'images_family_{}.txt'
                                 .format(split))).readlines()
    families = [' '.join(family.strip().split()[1:]) for family in families]

    manufacturers = open(os.path.join(extracted_dirs,
                                      'images_manufacturer_{}.txt'
                                      .format(split))).readlines()

    manufacturers = [' '.join(manufacturer.strip().split()[1:])
                     for manufacturer in manufacturers]

    variants = open(os.path.join(extracted_dirs,
                                 'images_variant_{}.txt'
                                 .format(split))).readlines()
    variants = [' '.join(variant.strip().split()[1:]) for variant in variants]

    bounding_boxes = open(os.path.join(extracted_dirs,
                                       'images_box.txt')).readlines()
    bounding_boxes = [box.strip().split() for box in bounding_boxes]
    bboxes = {}
    for box in bounding_boxes:
      bboxes[box[0]] = box[1:]

    for i, filename in enumerate(filenames):
      full_path = os.path.join(extracted_dirs, 'images/') + filename
      family = families[i]
      manufacturer = manufacturers[i]
      variant = variants[i]
      xmin, ymin, xmax, ymax = list(map(int, bboxes[filename.split('.')[0]]))
      image = tfds.core.lazy_imports.PIL_Image.open(full_path)
      width, height = image.size
      ymin = ymin / height
      xmin = xmin / width
      ymax = ymax / height
      xmax = xmax / width
      predictions = [{
          'bbox': tfds.features.BBox(
              ymin=ymin,
              xmin=xmin,
              ymax=ymax,
              xmax=xmax),
          'family': convert_to_string(family),
          'manufacturer': convert_to_string(manufacturer),
          'variant': convert_to_string(variant)
          }]
      record = {'image': full_path,
                'image_predictions': predictions}
      yield filename, record

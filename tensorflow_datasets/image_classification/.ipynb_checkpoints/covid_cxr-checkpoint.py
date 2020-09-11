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

"""covid_cxr dataset."""

import tensorflow_datasets.public_api as tfds
import os

_CITATION = """
Wang, Linda, et al. COVID-Net: A Tailored Deep Convolutional Neural Network ... 2020, arxiv.org/pdf/2003.09871.pdf. 
"""

# TODO(covid_cxr):
_DESCRIPTION = """
Dataset with radiography images belonging to three different classes 
    - normal
    - pneumonia
    - COVID - 19
                    
"""

# _TRAIN_URL = 'https://drive.google.com/uc?export=download&id=1FE57dEo6xKK9goxd8trERz_Y_vdP3GCX'
# _TEST_URL = 'https://drive.google.com/uc?export=download&id=12sq9rO5nSgl-fmWD2KtHocU2xUyX38qP'

_TEST_224_URL       = 'https://drive.google.com/uc?export=download&id=1ZzrVZlDSzzHew92lWF5VWoabXQXeeZh2'
_TEST_480_URL       = 'https://drive.google.com/uc?export=download&id=1WDoHmfsrSGivArnZoLujUEbJBsFEnOid'
_TEST_ORIGINAL_URL  = 'https://drive.google.com/uc?export=download&id=1Wq5fqLkzfDDv4iEF5MTyBAbp50Bz1RHl'

_TRAIN_224_URL      = 'https://drive.google.com/uc?export=download&id=1LsC-a1Ig5sUmFbWFg2sus9XB-Ex8bkC_'
_TRAIN_480_URL      = 'https://drive.google.com/uc?export=download&id=1slHH_yHdiiHc0q5OTL7txcG47HA-yjfQ'
_TRAIN_ORIGINAL_URL = 'https://drive.google.com/uc?export=download&id=1FrxYfLLg1FDOUzvGyZBnVt5vwGAErjtN'

_DATA_OPTIONS = ['original', 480, 224]

class CovidCxrConfig(tfds.core.BuilderConfig):
  """BuilderConfig for covid_cxr."""

  def __init__(self, resolution, **kwargs):
    """BuilderConfig
    Args:
      resolution: Resolution of the image. Values supported: original, 480, 224
      **kwargs: keyword arguments forwarded to super.
    """
    if resolution not in _DATA_OPTIONS:
        raise ValueError('selection must be one of %s' % _DATA_OPTIONS)
        
    v2 = tfds.core.Version(
        '2.0.0', 'New split API (https://tensorflow.org/datasets/splits)')
    
    super(CovidCxrConfig, self).__init__(version = v2, 
                                name = '%s' % resolution, 
                                description = 'Covid-19 Chest X-ray images in %s x %s resolution' % (resolution, resolution),
                                **kwargs)
    self.resolution = resolution
    
class CovidCxr(tfds.core.GeneratorBasedBuilder):
  """TODO(covid_cxr): Chest X-ray images of COVID-19, normal, and pneumonia patients."""

  VERSION = tfds.core.Version('0.1.0')
    
  BUILDER_CONFIGS = [
      CovidCxrConfig(resolution='original'),
      CovidCxrConfig(resolution=480),
      CovidCxrConfig(resolution=224),
  ]

  def _info(self):
    if self.builder_config.resolution == 'original':
        shape_res = None
    elif self.builder_config.resolution == 480:
        shape_res = (self.builder_config.resolution, self.builder_config.resolution, 3)
    elif self.builder_config.resolution == 224:
        shape_res = (self.builder_config.resolution, self.builder_config.resolution, 3)
        
    return tfds.core.DatasetInfo(
        builder = self,
        description = _DESCRIPTION,
        
        features = tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape = shape_res, 
                                         dtype = 'uint8', 
                                         encoding_format = 'png'),
            
            "label": tfds.features.ClassLabel(
                names = ["COVID-19", "normal", "pneumonia"]),
        }),

        supervised_keys = ('image', 'label'),
        
        homepage = 'https://github.com/lindawangg/COVID-Net',
        citation = _CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    
    if self.builder_config.resolution == 'original':
        train_path, test_path = dl_manager.download([_TRAIN_ORIGINAL_URL, _TEST_ORIGINAL_URL])
    elif self.builder_config.resolution == 480:
        train_path, test_path = dl_manager.download([_TRAIN_480_URL, _TEST_480_URL])
    elif self.builder_config.resolution == 224:
        train_path, test_path = dl_manager.download([_TRAIN_224_URL, _TEST_224_URL])
        
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "archive": dl_manager.iter_archive(train_path),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "archive": dl_manager.iter_archive(test_path),
            }),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""

    for fname, fobj in archive:
            image_dir, image_file = os.path.split(fname)
            d = os.path.basename(image_dir)
            record = {"image": fobj, "label": d}
            yield "%s/%s" % (image_file, d), record


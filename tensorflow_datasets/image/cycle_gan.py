# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""CycleGAN dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds


_DL_URL = "https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/"
_DL_URLS = {
    "ae_photos": _DL_URL + "ae_photos.zip",
    "apple2orange": _DL_URL + "apple2orange.zip",
    "summer2winter_yosemite": _DL_URL + "summer2winter_yosemite.zip",
    "horse2zebra": _DL_URL + "horse2zebra.zip",
    "monet2photo": _DL_URL + "monet2photo.zip",
    "cezanne2photo": _DL_URL + "cezanne2photo.zip",
    "ukiyoe2photo": _DL_URL + "ukiyoe2photo.zip",
    "vangogh2photo": _DL_URL + "vangogh2photo.zip",
    "maps": _DL_URL + "maps.zip",
    "cityscapes": _DL_URL + "cityscapes.zip",
    "facades": _DL_URL + "facades.zip",
    "iphone2dslr_flower": _DL_URL + "iphone2dslr_flower.zip",
}

_DATA_OPTIONS = ["ae_photos", "apple2orange", "summer2winter_yosemite", "horse2zebra", "monet2photo", "cezanne2photo", "ukiyoe2photo", "vangogh2photo", "maps", "cityscapes", "facades", "iphone2dslr_flower"]


class CycleGANConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CycleGAN.""" 
  
  @api_utils.disallow_positional_args
  def __init__(self, data=None, **kwargs):
    """Constructs a CycleGANConfig. 
    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)
  
    super(CycleGANConfig, self).__init__(**kwargs)
    self.data = data

    
class CycleGAN(tfds.core.GeneratorBasedBuilder):
  """CycleGAN dataset."""
  
  VERSION = tfds.core.Version("2.0.0")
  
  BUILDER_CONFIGS = [
      CycleGANConfig(
          name="facades",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="facades",
      ),
      CycleGANConfig(
          name="horse2zebra",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="horse2zebra",
      ),
      CycleGANConfig(
          name="ae_photos",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="ae_photos",
      ),  
      CycleGANConfig(
          name="apple2orange",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="apple2orange",
      ),
      CycleGANConfig(
          name="summer2winter_yosemite",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB",
          version=VERSION, 
          data="summer2winter_yosemite",
      ),
      CycleGANConfig(
          name="monet2photo",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="monet2photo",
      ),
      CycleGANConfig(
          name="cezanne2photo",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="cezanne2photo",
      ),
      CycleGANConfig(
          name="ukiyoe2photo",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="ukiyoe2photo",
      ),
      CycleGANConfig(
          name="vangogh2photo",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="vangogh2photo",
      ),
      CycleGANConfig(
          name="maps",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="maps",
      ),
      CycleGANConfig(
          name="cityscapes",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="cityscapes",
      ),
      CycleGANConfig(
          name="iphone2dslr_flower",
          description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB", 
          version=VERSION,
          data="iphone2dslr_flower", 
      ),             
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A dataset consisting of (trainA and testA) images of typeA and (trainB and testB) images of typeB",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=["A", "B"]), 
        }),
        supervised_keys=("image", "label"),
        urls=["https://people.eecs.berkeley.edu/~taesung_park/CycleGAN/datasets/"],
    )

  def _split_generators(self, dl_manager):
    url = _DL_URLS[self.builder_config.name]
    data_dirs = dl_manager.download_and_extract(url) 
    print(data_dirs)
    path_to_dataset = data_dirs + "/" + tf.io.gfile.listdir(data_dirs)[0]
    print(path_to_dataset)
    trainA_files = tf.io.gfile.glob(os.path.join(path_to_dataset, 'trainA'))
    trainB_files = tf.io.gfile.glob(os.path.join(path_to_dataset, 'trainB'))
    testA_files = tf.io.gfile.glob(os.path.join(path_to_dataset, 'testA'))
    testB_files = tf.io.gfile.glob(os.path.join(path_to_dataset, 'testB'))
    
    return [
        tfds.core.SplitGenerator(
            name="trainA",
            num_shards=10,
            gen_kwargs={"files": trainA_files,
                        "label": "A",
            }
        ),
        tfds.core.SplitGenerator(
            name="trainB",
            num_shards=10,
            gen_kwargs={"files": trainB_files,
                        "label": "B",
            }
        ),
        tfds.core.SplitGenerator(
            name="testA",
            num_shards=1,
            gen_kwargs={"files": testA_files,
                        "label": "A",
            }
        ),
        tfds.core.SplitGenerator(
            name="testB",
            num_shards=1,
            gen_kwargs={"files": testB_files,
                        "label": "B",
            }
        ),
    ]

  def _generate_examples(self, files, label): 
    path=files[0]+"/"
    images=tf.io.gfile.listdir(path)  

    for image in images:
      yield{
          "image": path+"/"+image,
          "label": label,
      }
      




# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Remote Sensing Image Scene Classification (RESISC45) Dataset."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{Cheng_2017,
   title={Remote Sensing Image Scene Classification: Benchmark and State of the Art},
   volume={105},
   ISSN={1558-2256},
   url={http://dx.doi.org/10.1109/JPROC.2017.2675998},
   DOI={10.1109/jproc.2017.2675998},
   number={10},
   journal={Proceedings of the IEEE},
   publisher={Institute of Electrical and Electronics Engineers (IEEE)},
   author={Cheng, Gong and Han, Junwei and Lu, Xiaoqiang},
   year={2017},
   month={Oct},
   pages={1865-1883}
}"""

_DESCRIPTION = """\
RESISC45 dataset is a publicly available benchmark for Remote Sensing Image
Scene Classification (RESISC), created by Northwestern Polytechnical University
(NWPU). This dataset contains 31,500 images, covering 45 scene classes with 700
images in each class."""

_LABELS = [
    'airplane', 'airport', 'baseball_diamond', 'basketball_court', 'beach',
    'bridge', 'chaparral', 'church', 'circular_farmland', 'cloud',
    'commercial_area', 'dense_residential', 'desert', 'forest', 'freeway',
    'golf_course', 'ground_track_field', 'harbor', 'industrial_area',
    'intersection', 'island', 'lake', 'meadow', 'medium_residential',
    'mobile_home_park', 'mountain', 'overpass', 'palace', 'parking_lot',
    'railway', 'railway_station', 'rectangular_farmland', 'river', 'roundabout',
    'runway', 'sea_ice', 'ship', 'snowberg', 'sparse_residential', 'stadium',
    'storage_tank', 'tennis_court', 'terrace', 'thermal_power_station',
    'wetland'
]

_URL = 'http://www.escience.cn/people/JunweiHan/NWPU-RESISC45.html'


class Resisc45(tfds.core.GeneratorBasedBuilder):
  """NWPU Remote Sensing Image Scene Classification (RESISC) Dataset."""

  VERSION = tfds.core.Version('3.0.0')

  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Dataset can be downloaded from OneDrive:
  https://1drv.ms/u/s!AmgKYzARBl5ca3HNaHIlzp_IXjs
  After downloading the rar file, please extract it to the manual_dir.
  """

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=[256, 256, 3]),
            'label': tfds.features.ClassLabel(names=_LABELS),
            'filename': tfds.features.Text(),
        }),
        supervised_keys=('image', 'label'),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = os.path.join(dl_manager.manual_dir, 'NWPU-RESISC45')
    if not tf.io.gfile.exists(path):
      raise AssertionError('You must download the dataset manually from {}, '
                           'extract it, and place it in {}.'.format(
                               _URL, dl_manager.manual_dir))
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'path': path},
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    for label in tf.io.gfile.listdir(path):
      for filename in tf.io.gfile.glob(os.path.join(path, label, '*.jpg')):
        example = {
            'image': filename,
            'label': label,
            'filename': os.path.basename(filename)
        }
        yield f'{label}_{os.path.basename(filename)}', example

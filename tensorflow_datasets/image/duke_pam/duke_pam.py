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
"""TFDS Duke PAM Dataset"""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@dataset{anthony_dispirito_iii_2020_4042171,
  author       = {Anthony DiSpirito III},
  title        = {Duke PAM Dataset},
  month        = sep,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.4042171},
  url          = {https://doi.org/10.5281/zenodo.4042171}
}
"""

_DESCRIPTION = """\
Duke PAM is a photoacoustic microscopy (PAM) dataset collected at Duke
University with the optical resolution PAM system described in (M. Chen et al.,
"Simultaneous photoacoustic imaging of intravascular and tissue oxygenation,"
Optics Letters, vol. 44, no. 15, pp. 3773-3776, 2019.) at a wavelength of
532 nm. This dataset is composed of primarily mouse brain microvasculature
images, with a few images of mouse ear and tumors. Although collected in 3-D,
for the purposes of viewing, collection, and storage, the images have been
projected into 2-D using maximum amplitude projection (MAP). These data were
collected with support from the National Institutes of Health (R01 EB028143,
R01 NS111039, R01 NS115581, R21 EB027304, R43 CA243822, R43 CA239830,
R44 HL138185); Duke MEDx Basic Science Grant; Duke Center for Genomic and
Computational Biology Faculty Research Grant; Duke Institute of Brain Science
Incubator Award; American Heart Association Collaborative Sciences Award
(18CSA34080277).
"""

_DATASET_URL = 'https://zenodo.org/record/4042171/files'
_GITHUB_URL = 'https://github.com/axd465/pam_dataset'

_DATA_OPTIONS = {'clean': f'The clean dataset config consists of maximum \
                           amplitude projection PAM images that have been \
                           post-processed according to typical lab standards. \
                           The post processing method can be found at \
                           ({_GITHUB_URL}). This post-processing enhances \
                           image contrast and helps remove some noise. The \
                           images of the clean config have multiple different \
                           image sizes.Each image dimension is greater than or \
                           equal to 128 pixels.',
                 'patches': 'The patches dataset config consists of maximum \
                             amplitude projection PAM images that have been \
                             post-processed according to typical lab \
                             standards. This post-processing enhances image \
                             contrast and helps remove some noise. To \
                             standardize image size, the patches config has \
                             divided each PAM image into non-overlapping \
                             patches of size 128 x 128.',
                 'raw': 'The raw dataset config consists of maximum amplitude \
                         projection PAM images acquired at 532 nm that have \
                         been converted from Matlab structs stored as \
                         .mat files to float32 .tif images. This raw dataset \
                         differs from the clean dataset as the images have \
                         not been post-processed. Unlike the patches dataset, \
                         the images are of varying sizes. Each image dimension \
                         is greater than or equal to 128 pixels.'}

class DukePAMConfig(tfds.core.BuilderConfig):
  """BuilderConfig for DukePAM Dataset."""
  def __init__(self, *, data=None, **kwargs):
    """
    Constructs a DukePAMConfig.
    Args:
      data(str): Specified Heavy Config, one of `_DATA_OPTIONS`.
      kwargs(str): keyword arguments forwarded to super.
    Raises:
      ValueError: raises a ValueError if the user inputs an invalid
                  Heavy Config (not in _DATA_OPTIONS).
    """
    if data not in _DATA_OPTIONS:
      raise ValueError('data must be one of %s' % list(_DATA_OPTIONS))

    super(DukePAMConfig, self).__init__(**kwargs)
    self.data = data


# pylint: disable=invalid-name
class DukePAM(tfds.core.GeneratorBasedBuilder):
  """Defines DukePAM Dataset Builder Object."""
  VERSION = tfds.core.Version('0.1.0')
  # pylint: disable=g-complex-comprehension
  BUILDER_CONFIGS = [
      DukePAMConfig(name=config_name,
                    description=
                    f'A dataset consisting of Train and Validation \
                    images of {config_name} images. \
                    {_DATA_OPTIONS[config_name]}',
                    version=tfds.core.Version('0.1.0'),
                    data=config_name,) for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    """
    Specifies the tfds.core.DatasetInfo object.
    Returns:
      object: Contains `tfds.core.DatasetInfo` object specifying
              the Heavy Config.
    """
    if self.builder_config.name == 'patches':
      dataset_info = tfds.core.DatasetInfo(
          builder=self,
          description=_DESCRIPTION,
          features=tfds.features.FeaturesDict({
              'image': tfds.features.Image(shape=(128, 128, 1),
                                           encoding_format='jpeg')
          }),
          supervised_keys=None,
          # Homepage of the dataset for documentation
          homepage=_DATASET_URL,
          citation=_CITATION,
      )
    elif self.builder_config.name == 'clean':
      dataset_info = tfds.core.DatasetInfo(
          builder=self,
          description=_DESCRIPTION,
          features=tfds.features.FeaturesDict({
              'image': tfds.features.Image(shape=(None, None, 1),
                                           encoding_format='jpeg')
          }),
          supervised_keys=None,
          # Homepage of the dataset for documentation
          homepage=_DATASET_URL,
          citation=_CITATION,
      )
    elif self.builder_config.name == 'raw':
      dataset_info = tfds.core.DatasetInfo(
          builder=self,
          description=_DESCRIPTION,
          features=tfds.features.FeaturesDict({
              'image': tfds.features.Image(shape=(None, None, 1),
                                           encoding_format='png',
                                           dtype=tf.uint16)
          }),
          supervised_keys=None,
          # Homepage of the dataset for documentation
          homepage=_DATASET_URL,
          citation=_CITATION,
      )
    return dataset_info
  def _split_generators(self, dl_manager):
    """
    Returns SplitGenerators.
    Args:
      dl_manager(tfds.download.DownloadManager): Object used to download
                                                 and extract data from the URL.
    Returns:
      tuple: Tuple with Train and Valid `tfds.core.SplitGenerator` objects.
    """
    train_url = f'{_DATASET_URL}/{self.builder_config.name}' + \
                 '_train.zip?download=1'
    valid_url = f'{_DATASET_URL}/{self.builder_config.name}' + \
                 '_valid.zip?download=1'
    data_dirs = dl_manager.download_and_extract({
        f'{self.builder_config.name}_train': train_url,
        f'{self.builder_config.name}_valid': valid_url,
    })
    train_key = f'{self.builder_config.name}_train'
    valid_key = f'{self.builder_config.name}_valid'
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'images_dir_path': data_dirs[train_key],
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'images_dir_path': data_dirs[valid_key],
            }),
    ]

  def _generate_examples(self, images_dir_path):
    """
    Yields examples.
    Args:
      images_dir_path(str): Contains the path to the downloaded
                            images directory.
    Yields:
      str, dict(str): The filename and a dict with the next
                      downloaded image path.
    """
    for filename in tf.io.gfile.listdir(images_dir_path):
      image_path = os.path.join(images_dir_path, filename)
      yield filename, {'image': image_path}

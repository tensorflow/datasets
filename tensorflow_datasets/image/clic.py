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

"""CLIC dataset."""

import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{CLIC2020,
  title = {Workshop and Challenge on Learned Image Compression (CLIC2020)},
  author = {George Toderici, Wenzhe Shi, Radu Timofte, Lucas Theis,
            Johannes Balle, Eirikur Agustsson, Nick Johnston, Fabian Mentzer},
  url = {http://www.compression.cc},
  year={2020},
  organization={CVPR}
}
"""

_DESCRIPTION = """
CLIC is a dataset for the Challenge on Learned Image Compression 2020 lossy
image compression track. These images contain a mix of the professional and
mobile datasets used to train and benchmark rate-distortion performance. The
dataset contains both RGB and grayscale images. This may require special
handling if a grayscale image is processed as a 1 channel Tensor and a 3 channel
Tensor is expected.

This dataset does *NOT* contain the data from the P-Frame challenge (YUV image
frames).
"""

CLIC_MOBILE_TRAIN = 'https://data.vision.ee.ethz.ch/cvl/clic/mobile_train_2020.zip'
CLIC_PROFESSIONAL_TRAIN = 'https://data.vision.ee.ethz.ch/cvl/clic/professional_train_2020.zip'
CLIC_MOBILE_VALIDATION = 'https://data.vision.ee.ethz.ch/cvl/clic/mobile_valid_2020.zip'
CLIC_PROFESSIONAL_VALIDATION = 'https://data.vision.ee.ethz.ch/cvl/clic/professional_valid_2020.zip'
CLIC_MOBILE_TEST = 'https://data.vision.ee.ethz.ch/cvl/clic/test/CLIC2020Mobile_test.zip'
CLIC_PROFESSIONAL_TEST = 'https://data.vision.ee.ethz.ch/cvl/clic/test/CLIC2020Professional_test.zip'


class CLIC(tfds.core.GeneratorBasedBuilder):
  """CLIC dataset."""

  # We set the version based on the conference year. The 3rd CLIC was held in
  # 2020 and we are using this lossy image dataset.
  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(),
        }),
        homepage='https://www.compression.cc/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    downloaded_dirs = dl_manager.download_and_extract({
        'mobile_train': CLIC_MOBILE_TRAIN,
        'prof_train': CLIC_PROFESSIONAL_TRAIN,
        'mobile_val': CLIC_MOBILE_VALIDATION,
        'prof_val': CLIC_PROFESSIONAL_VALIDATION,
        'mobile_test': CLIC_MOBILE_TEST,
        'prof_test': CLIC_PROFESSIONAL_TEST,
    })

    train_dirs = {k: v for k, v in downloaded_dirs.items() if 'train' in k}
    val_dirs = {k: v for k, v in downloaded_dirs.items() if 'val' in k}
    test_dirs = {k: v for k, v in downloaded_dirs.items() if 'test' in k}
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={
                'download_path': train_dirs,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION, gen_kwargs={
                'download_path': val_dirs,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, gen_kwargs={
                'download_path': test_dirs,
            })
    ]

  def _generate_examples(self, download_path):
    """Yields examples."""
    for _, path in download_path.items():
      for root, _, files in tf.io.gfile.walk(path):
        for file_path in files:
          # Select only png files.
          if file_path.endswith('.png'):
            yield file_path, {
                'image': os.path.join(root, file_path),
            }

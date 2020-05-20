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
"""Dataset class for Malaria dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import fnmatch
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://ceb.nlm.nih.gov/proj/malaria/cell_images.zip"

_DESCRIPTION = ("""The Malaria dataset contains a total of 27,558 cell images
with equal instances of parasitized and uninfected cells from the thin blood 
smear slide images of segmented cells.""")

_NAMES = ["parasitized", "uninfected"]

_IMAGE_SHAPE = (None, None, 3)

_CITATION = """\
 @article{rajaraman2018pre,
  title={Pre-trained convolutional neural networks as feature extractors toward 
  improved malaria parasite detection in thin blood smear images},
  author={Rajaraman, Sivaramakrishnan and Antani, Sameer K and Poostchi, Mahdieh
  and Silamut, Kamolrat and Hossain, Md A and Maude, Richard J and Jaeger, 
  Stefan and Thoma, George R},
  journal={PeerJ},
  volume={6},
  pages={e4568},
  year={2018},
  publisher={PeerJ Inc.}
}
"""


class Malaria(tfds.core.GeneratorBasedBuilder):
  """Malaria Cell Image Dataset Class."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    """Define Dataset Info."""

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names=_NAMES),
        }),
        supervised_keys=("image", "label"),
        homepage="https://lhncbc.nlm.nih.gov/publication/pub9932",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Define Splits."""

    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_dir_path": os.path.join(path, "cell_images"),
            },
        ),
    ]

  def _generate_examples(self, data_dir_path):
    """Generate images and labels for splits."""
    folder_names = ["Parasitized", "Uninfected"]

    for folder in folder_names:
      folder_path = os.path.join(data_dir_path, folder)
      for file_name in tf.io.gfile.listdir(folder_path):
        if fnmatch.fnmatch(file_name, "*.png"):
          image = os.path.join(folder_path, file_name)
          label = folder.lower()
          image_id = "%s_%s" % (folder, file_name)
          yield image_id, {"image": image, "label": label}

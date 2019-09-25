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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import fnmatch
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "http://people.duke.edu/~kk349/bbbc.zip"

_CITATION = """\
 @misc{ljosa_sokolnicki_carpenter_2012,
  title={Annotated high-throughput microscopy image sets for validation},
  author={Ljosa, Vebjorn and Sokolnicki, Katherine L and Carpenter, Anne E},
  url={https://www.nature.com/articles/nmeth.2083},
  journal={Nature News},
  publisher={Nature Publishing Group},
  year={2012},
  month={Jun}
}
"""

_DESCRIPTION = """The original data set contains 1364 images and
consists of two classes of uninfected cells(red blood cells and leukocytes) and
four classes of infected cells(gametocytes, rings, schizonts, and trophozoites).
The Malaria dataset contains a total of 74,211 cell images and we have removed 414 cell images
because annotators marked the cells as difficult as it was not clearly in one of the cell classes.
Fianlly malaria_bbbc data set contains 73,797 cells.
This data set is extremly skewed toward uninfected cases, so we did not divide original data to train and test sets
so that the user can try in their own way to deal with this problem.
"""

_NAMES = ["gametocyte", "leukocyte", "red blood cell", "ring", "schizont", "trophozoite"]

_IMAGE_SHAPE = (None, None, 3)


class MalariaBbbc(tfds.core.GeneratorBasedBuilder):
  """malaria_bbbc dataset."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "label": tfds.features.ClassLabel(names=_NAMES),
        }),
        supervised_keys=("image", "label"),
        urls=[_URL],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Define Splits."""

    path = dl_manager.download_and_extract(_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_dir_path": os.path.join(path, "bbbc"),
            },
        ),
    ]

  def _generate_examples(self, data_dir_path):
    """Generate images and labels for splits."""
    folder_names = ["gametocyte", "leukocyte", "red blood cell", "ring", "schizont", "trophozoite"]

    for folder in folder_names:
      folder_path = os.path.join(data_dir_path, folder)
      for file_name in tf.io.gfile.listdir(folder_path):
        if fnmatch.fnmatch(file_name, "*.png"):
          image = os.path.join(folder_path, file_name)
          label = folder.lower()
          image_id = "%s_%s" % (folder, file_name)
          yield image_id, {"image": image, "label": label}

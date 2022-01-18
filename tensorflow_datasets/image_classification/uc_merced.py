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

"""UC Merced: Small remote sensing dataset for land use classification."""

import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@InProceedings{Nilsback08,
   author = "Yang, Yi and Newsam, Shawn",
   title = "Bag-Of-Visual-Words and Spatial Extensions for Land-Use Classification",
   booktitle = "ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (ACM GIS)",
   year = "2010",
}"""

_DESCRIPTION = """\
UC Merced is a 21 class land use remote sensing image dataset, with 100 images
per class. The images were manually extracted from large images from the USGS
National Map Urban Area Imagery collection for various urban areas around the
country. The pixel resolution of this public domain imagery is 0.3 m.

While most images are 256x256 pixels, there are 44 images with different shape.
"""

_URL = "http://weegee.vision.ucmerced.edu/datasets/landuse.html"

_LABELS = [
    "agricultural",
    "airplane",
    "baseballdiamond",
    "beach",
    "buildings",
    "chaparral",
    "denseresidential",
    "forest",
    "freeway",
    "golfcourse",
    "harbor",
    "intersection",
    "mediumresidential",
    "mobilehomepark",
    "overpass",
    "parkinglot",
    "river",
    "runway",
    "sparseresidential",
    "storagetanks",
    "tenniscourt",
]

_ZIP_URL = "http://weegee.vision.ucmerced.edu/datasets/UCMerced_LandUse.zip"
_ZIP_SUBDIR = "UCMerced_LandUse/Images"


class UcMerced(tfds.core.GeneratorBasedBuilder):
  """Small 21 class remote sensing land use classification dataset."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(names=_LABELS),
            "filename": tfds.features.Text(),
        }),
        supervised_keys=("image", "label"),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(_ZIP_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(path, _ZIP_SUBDIR)},
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    for label in tf.io.gfile.listdir(path):
      for filename in tf.io.gfile.glob(os.path.join(path, label, "*.tif")):
        image = _load_tif(filename)
        filename = os.path.basename(filename)
        record = {
            "image": image,
            "label": label,
            "filename": filename,
        }
        yield filename, record


def _load_tif(path):
  with tf.io.gfile.GFile(path, "rb") as fp:
    image = tfds.core.lazy_imports.PIL_Image.open(fp)
  return np.array(image)

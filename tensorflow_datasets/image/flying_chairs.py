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

"""Flying Chairs dataset for Optical Flow"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core.download import DownloadManager

_CITATION = r"""@InProceedings{DFIB15,
  author    = "A. Dosovitskiy and P. Fischer and E. Ilg and P. H{\"a}usser and
  C. Haz{\i}rba{\c{s}} and V. Golkov and P. v.d. Smagt and D. Cremers and T. Brox",
  title     = "FlowNet: Learning Optical Flow with Convolutional Networks",
  booktitle = "IEEE International Conference on Computer Vision (ICCV)",
  month     = " ",
  year      = "2015",
  url       = "http://lmb.informatik.uni-freiburg.de/Publications/2015/DFIB15"
}"""

_DESCRIPTION = """The Flying Chairs are a synthetic dataset with optical flow ground truth. It
consists of 22872 image pairs and corresponding flow fields. Images show renderings of 3D chair
models moving in front of random backgrounds from Flickr. Motions of both the chairs and the
background are purely planar.

This dataset has been used for training convolutional networks in the ICCV 2015 paper
FlowNet: Learning Optical Flow with Convolutional Networks."""

_URL_SPLIT_ROOT = "http://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs/"
_URL_SPLIT_FILE = "FlyingChairs_train_val.txt"
_URL_DATA_ROOT = "http://lmb.informatik.uni-freiburg.de/data/FlyingChairs/"
_URL_DATA_ZIP = "FlyingChairs.zip"

_WIDTH, _HEIGHT, _CHANNELS = 512, 384, 3


class FlyingChairs(tfds.core.GeneratorBasedBuilder):
  """Supervised Optical Flow dataset from the Freiburg Computer Vision group"""

  VERSION = tfds.core.Version('1.0.0')
  DATA_DIR = "FlyingChairs_release/data"

  SPLIT_TAG_TRAIN = 1
  SPLIT_TAG_VALIDATION = 2

  def _info(self):
    """Builds `tfds.core.DatasetInfo`"""
    image_feature_connector = tfds.features.Image(
        shape=(_HEIGHT, _WIDTH, _CHANNELS))  # RGB images

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image_pair": tfds.features.FeaturesDict({
                "image_one": image_feature_connector,
                "image_two": image_feature_connector,
            }),
            #  The flow field has a (x,y) velocity vector for every pixel in the image.
            "flow": tfds.features.Tensor(shape=(_HEIGHT, _WIDTH, 2),
                                         dtype=tf.float32)
        }),
        supervised_keys=("image_pair", "flow"),
        homepage='https://lmb.informatik.uni-freiburg.de/resources/datasets/FlyingChairs.en.html',
        citation=_CITATION)

  def _split_generators(self, dl_manager: DownloadManager):
    """Returns SplitGenerators."""

    # Download
    path_data_dir, path_split_file = dl_manager.download_and_extract([
        os.path.join(_URL_DATA_ROOT, _URL_DATA_ZIP),
        os.path.join(_URL_SPLIT_ROOT, _URL_SPLIT_FILE)])

    # Sparse splits
    split_map = self._parse_split_file(path_split_file)
    train_map = [i for i, e in enumerate(split_map)
                 if e == self.SPLIT_TAG_TRAIN]
    validation_map = [i for i, e in enumerate(split_map)
                      if e == self.SPLIT_TAG_VALIDATION]

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"split_ids": train_map,
                        "extraction_dir": path_data_dir},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"split_ids": validation_map,
                        "extraction_dir": path_data_dir},
        ),
    ]

  def _parse_split_file(self, file_path):
    """Reads numbers from the test-validation split .txt file."""

    with tf.io.gfile.GFile(file_path) as f:
      lines = f.readlines()
      splits = [None] * (len(lines) + 1)

      for i, line in enumerate(lines, start=1):
        v = line.strip()
        if v == '':
          continue

        assert v.isdigit()
        v = int(v)

        assert v in (self.SPLIT_TAG_TRAIN, self.SPLIT_TAG_VALIDATION), \
            "The parsed numbers in this file did not match the known" \
            " separation tags."

        splits[i] = int(v)

    return splits

  def _read_flow(self, path):
    """Reads a .flo file"""

    with tf.io.gfile.GFile(path, "rb") as f:
      header = f.read(4)

      if header.decode("utf-8") != 'PIEH':
        raise Exception('Flow file header does not contain PIEH.')

      contents = np.frombuffer(f.read(4 * _WIDTH * _HEIGHT * 2),
                               dtype=np.float32)
      flow = np.resize(contents, (_HEIGHT, _WIDTH, 2))

    return flow

  def _read_image(self, path):
    with tf.io.gfile.GFile(path, "rb") as f:
      image = tfds.core.lazy_imports.PIL_Image.open(f)

    return np.array(image)

  def _generate_examples(self, split_ids, extraction_dir):
    """Yields examples."""
    data_dir = os.path.join(extraction_dir, self.DATA_DIR)

    for img_number in split_ids:
      im1_path = "%s/%s_img1.ppm" % (data_dir, str(img_number).zfill(5))
      im1 = self._read_image(im1_path)

      im2_path = "%s/%s_img2.ppm" % (data_dir, str(img_number).zfill(5))
      im2 = self._read_image(im2_path)

      flow_path = "%s/%s_flow.flo" % (data_dir, str(img_number).zfill(5))
      flow = self._read_flow(flow_path)

      yield img_number, dict(image_pair=dict(image_one=im1, image_two=im2),
                             flow=flow)

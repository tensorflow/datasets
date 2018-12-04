# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""CelebA dataset.

Large-scale CelebFaces Attributes (CelebA) Dataset

Deep Learning Face Attributes in the Wild
Ziwei Liu and Ping Luo and Xiaogang Wang and Xiaoou Tang
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

IMG_ALIGNED_DATA = ("https://drive.google.com/uc?export=download&"
                    "id=0B7EVK8r0v71pZjFTYXZWM3FlRnM")
EVAL_LIST = ("https://drive.google.com/uc?export=download&"
             "id=0B7EVK8r0v71pY0NSMzRuSXJEVkk")
# Landmark coordinates: left_eye, right_eye etc.
LANDMARKS_DATA = ("https://drive.google.com/uc?export=download&"
                  "id=0B7EVK8r0v71pd0FJY3Blby1HUTQ")

# Attributes in the image (Eyeglasses, Mustache etc).
ATTR_DATA = ("https://drive.google.com/uc?export=download&"
             "id=0B7EVK8r0v71pblRyaVFSWGxPY0U")

LANDMARK_HEADINGS = ("lefteye_x lefteye_y righteye_x righteye_y "
                     "nose_x nose_y leftmouth_x leftmouth_y rightmouth_x "
                     "rightmouth_y").split()
ATTR_HEADINGS = (
    "5_o_Clock_Shadow Arched_Eyebrows Attractive Bags_Under_Eyes Bald Bangs "
    "Big_Lips Big_Nose Black_Hair Blond_Hair Blurry Brown_Hair "
    "Bushy_Eyebrows Chubby Double_Chin Eyeglasses Goatee Gray_Hair "
    "Heavy_Makeup High_Cheekbones Male Mouth_Slightly_Open Mustache "
    "Narrow_Eyes No_Beard Oval_Face Pale_Skin Pointy_Nose Receding_Hairline "
    "Rosy_Cheeks Sideburns Smiling Straight_Hair Wavy_Hair Wearing_Earrings "
    "Wearing_Hat Wearing_Lipstick Wearing_Necklace Wearing_Necktie Young"
).split()


class CelebA(tfds.core.GeneratorBasedDatasetBuilder):
  """CelebA dataset. Aligned and cropped. With metadata."""

  def _info(self):
    return tfds.core.DatasetInfo(
        name=self.name,
        description=("Large-scale CelebFaces Attributes, CelebA."
                     "Set of ~30k celebrities pictures. "
                     "These pictures are cropped."),
        version="0.2.0",
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(
                    shape=(218, 178, 3), encoding_format="jpeg"),
            "landmarks": {name: tf.int64 for name in LANDMARK_HEADINGS},
            # Attributes could be some special MultiLabel FeatureConnector
            "attributes": {
                name: tf.bool for name in ATTR_HEADINGS
            },
        }),
        urls=["http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html"],
        size_in_bytes=2 * tfds.units.GiB,
        citation="Ziwei Liu and Ping Luo and Xiaogang Wang and Xiaoou Tang "
        "Deep Learning Face Attributes in the Wild "
        "ICCV 2015")

  def _split_generators(self, dl_manager):
    # TODO(b/120128659): pass the map directly to download_and_extract
    #                    after this is supported by the test framework.
    extracted_dirs = {
        key: dl_manager.download_and_extract(path) for key, path in {
            "img_align_celeba": IMG_ALIGNED_DATA,
            "list_eval_partition": EVAL_LIST,
            "list_attr_celeba": ATTR_DATA,
            "landmarks_celeba": LANDMARKS_DATA
        }.items()
    }
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs={
                "file_id": 0,
                "extracted_dirs": extracted_dirs,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=4,
            gen_kwargs={
                "file_id": 1,
                "extracted_dirs": extracted_dirs,
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=4,
            gen_kwargs={
                "file_id": 2,
                "extracted_dirs": extracted_dirs,
            })
    ]

  def _process_celeba_config_file(self, file_path):
    """Unpack the celeba config file.

    The file starts with the number of lines, and a header.
    Afterwards, there is a configuration for each file: one per line.

    Args:
      file_path: Path to the file with the configuration.

    Returns:
      keys: names of the attributes
      values: map from the file name to the list of attribute values for
              this file.
    """
    with tf.gfile.Open(file_path) as f:
      data_raw = f.read()
    lines = data_raw.split("\n")

    keys = lines[1].strip().split()
    values = {}
    # Go over each line (skip the last one, as it is empty).
    for line in lines[2:-1]:
      row_values = line.strip().split()
      # Each row start with the 'file_name' and then space-separated values.
      values[row_values[0]] = [int(v) for v in row_values[1:]]
    return keys, values

  def _generate_examples(self, file_id, extracted_dirs):
    filedir = os.path.join(extracted_dirs["img_align_celeba"],
                           "img_align_celeba")

    img_list_path = os.path.join(extracted_dirs["list_eval_partition"],
                                 "list_eval_partition.txt")
    landmarks_path = os.path.join(extracted_dirs["landmarks_celeba"],
                                  "list_landmarks_align_celeba.txt")
    attr_path = os.path.join(extracted_dirs["list_attr_celeba"],
                             "list_attr_celeba.txt")

    with tf.gfile.Open(img_list_path) as f:
      files = [
          line.split()[0]
          for line in f.readlines()
          if int(line.split()[1]) == file_id
      ]

    attributes = self._process_celeba_config_file(attr_path)
    landmarks = self._process_celeba_config_file(landmarks_path)

    for file_name in files:
      path = os.path.join(filedir, file_name)

      yield self.info.features.encode_example({
          "image": path,
          "landmarks": {
              k: v for k, v in zip(landmarks[0], landmarks[1][file_name])
          },
          "attributes": {
              k: v for k, v in zip(attributes[0], attributes[1][file_name])
          },
      })

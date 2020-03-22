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
"""Imagewoof Dataset"""
# gfile cannot be imported directly `from tensorflow.io import gfile`
import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


_IMAGEWOOF_URL = "https://s3.amazonaws.com/fast-ai-imageclas/imagewoof2.tgz"

_CITATION = """
@misc{imagewoof,
  author    = "Jeremy Howard",
  title     = "Imagewoof",
  url       = "https://github.com/fastai/imagenette/"
}
"""

_DESCRIPTION = """\
Imagewoof is a subset of 10 classes from Imagenet that aren't so easy to
classify, since they're all dog breeds. The breeds are: Australian terrier,
Border terrier, Samoyed, Beagle, Shih-Tzu, English foxhound, Rhodesian
ridgeback, Dingo, Golden retriever, Old English sheepdog.
"""

lbl_dict = {
    'n02093754': 'Australian terrier',
    'n02089973': 'Border terrier',
    'n02099601': 'Samoyed',
    'n02087394': 'Beagle',
    'n02105641': 'Shih-Tzu',
    'n02096294': 'English foxhound',
    'n02088364': 'Rhodesian ridgeback',
    'n02115641': 'Dingo',
    'n02111889': 'Golden retriever',
    'n02086240': 'Old English sheepdog'
}


class Imagewoof(tfds.core.GeneratorBasedBuilder):
  """Imagewoof Dataset"""
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(
                names=['Australian terrier', 'Border terrier', 'Samoyed',
                       'Beagle', 'Shih-Tzu', 'English foxhound',
                       'Rhodesian ridgeback', 'Dingo', 'Golden retriever',
                       'Old English sheepdog']),
        }),
        supervised_keys=("image", "label"),
        homepage="https://github.com/fastai/imagenette",
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    """Generate Splits"""
    extracted_path = dl_manager.download_and_extract(_IMAGEWOOF_URL)
    extracted_path = os.path.join(extracted_path, 'imagewoof2')
    # Specify the splits
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "train"),
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "images_dir_path": os.path.join(extracted_path, "val"),
            }),
        ]

  def _generate_examples(self, images_dir_path):
    """Generate examples given the image directory path"""
    count = 0
    for image_folder in tf.io.gfile.listdir(images_dir_path):
      for image_file in tf.io.gfile.listdir(os.path.join(images_dir_path,
                                                         image_folder)):
        yield count, {
            'image': '{}/{}/{}'.format(images_dir_path, image_folder,
                                       image_file),
            'label': lbl_dict[image_folder]
        }
        count += 1

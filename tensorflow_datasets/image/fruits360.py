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

"""Fruits-360: A dataset of images containing fruits.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow.python.framework import errors
import tensorflow_datasets.public_api as tfds

from tensorflow_datasets.core import api_utils

_CITATION = """\
@article{article,
author = {Mureșan, Horea and Oltean, Mihai},
year = {2018},
month = {06},
pages = {26-42},
title = {Fruit recognition from images using deep learning},
volume = {10},
journal = {Acta Universitatis Sapientiae, Informatica},
doi = {10.2478/ausi-2018-0002}
}
"""

_DESCRIPTION = """\
A large set of fruits on a white background.

Note that the dataset is frequently updated independent of TensorFlow Datasets. To use a different version of the \
dataset, create a custom `tfds.image.fruits360.Fruits360Config`. 

```python
config = tfds.image.fruits360.Fruits360Config(
    name="2019.08.14.0",
    ref="3a2533e",
    num_classes=118
)
builder = tfds.builder("fruits360", config=config)
```
"""
_IMAGE_SIZE = 100
_IMAGE_SHAPE = (_IMAGE_SIZE, _IMAGE_SIZE, 3)


class Fruits360Config(tfds.core.BuilderConfig):
  """BuilderConfig for Fruits360."""

  @api_utils.disallow_positional_args
  def __init__(self,
               name=None,
               ref=None,
               num_classes=None,
               **kwargs):
    """BuilderConfig for Fruits360.

    Args:
      name: The name of the
      ref: The git reference (either commit or branch) for the dataset version (string).
      num_classes: The number of classes present in the dataset (int).
      **kwargs: keyword arguments forwarded to super.
    """
    self.url = "https://github.com/Horea94/Fruit-Images-Dataset/archive/{}.tar.gz".format(ref)
    self.num_classes = num_classes
    super(Fruits360Config, self).__init__(name=name, **kwargs)


class Fruits360(tfds.core.GeneratorBasedBuilder):
  """Fruits 360 dataset."""

  VERSION = tfds.core.Version("1.0.0", experiments={tfds.core.Experiment.S3: True})
  BUILDER_CONFIGS = [
      Fruits360Config(name="2019.08.14.0", ref="3a2533e", num_classes=118)
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(shape=_IMAGE_SHAPE),
            "image/filename": tfds.features.Text(),
            "label": tfds.features.ClassLabel(num_classes=self.builder_config.num_classes)
        }),
        supervised_keys=("image", "label"),
        urls=["https://www.kaggle.com/moltean/fruits"],
        citation=_CITATION
    )

  def _split_generators(self, dl_manager):
    resource = tfds.download.Resource(url=self.builder_config.url, extract_method=tfds.download.ExtractMethod.TAR_GZ)
    download_path = dl_manager.download_and_extract(resource)
    sub = tf.io.gfile.listdir(download_path)[0]
    root_path = os.path.join(download_path, sub)
    train_path = os.path.join(root_path, "Training")
    test_path = os.path.join(root_path, "Test")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=1,
            gen_kwargs=dict(split_dir=train_path),
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=1,
            gen_kwargs=dict(split_dir=test_path),
        ),
    ]

  def _generate_examples(self, split_dir):
    """Generate fruit examples given a base path.
    Args:
      split_dir: path to the directory where the images are stored (in their respective class folders)
    Yields:
      The image path and its label.
    """
    class_names = sorted(tf.io.gfile.listdir(split_dir))
    for class_name in class_names:
      class_dir = os.path.join(split_dir, class_name)
      try:
        filenames = sorted(tf.io.gfile.listdir(class_dir))
      except errors.NotFoundError:
        continue

      for filename in filenames:
        image_path = os.path.join(class_dir, filename)
        yield "%s/%s" % (class_name, filename), {
            "image": image_path,
            "image/filename": filename,
            "label": class_name,
        }

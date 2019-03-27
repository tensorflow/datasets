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

"""Utility library to generate dataset-like files."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import random
import tempfile

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import utils

MIN_HEIGHT_WIDTH = 10
MAX_HEIGHT_WIDTH = 15
CHANNELS_NB = 3


def get_random_picture(height=None, width=None):
  """Returns random picture as np.ndarray (int)."""
  height = height or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  width = width or random.randrange(MIN_HEIGHT_WIDTH, MAX_HEIGHT_WIDTH)
  return np.random.randint(
      256, size=(height, width, CHANNELS_NB), dtype=np.uint8)


def get_random_jpeg(height=None, width=None):
  """Returns path to JPEG picture."""
  image = get_random_picture(height, width)
  jpeg = tf.image.encode_jpeg(image)
  with utils.nogpu_session() as sess:
    res = sess.run(jpeg)
  fobj = tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.JPEG')
  fobj.write(res)
  fobj.close()
  return fobj.name


def get_random_png(height=None, width=None):
  """Returns path to PNG picture."""
  image = get_random_picture(height, width)
  png = tf.image.encode_png(image)
  with utils.nogpu_session() as sess:
    res = sess.run(png)
  fobj = tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.PNG')
  fobj.write(res)
  fobj.close()
  return fobj.name

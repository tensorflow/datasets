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

"""Video Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow_datasets.core.features import feature

# TODO(tfds): Support more formats (gifs, mp4,...)
# TODO(tfds): Better internal encoding (ex: png instead of storing raw tensor
# values)


class Video(feature.Tensor):
  """Feature which encode/decode a video.

  Video: The image connector accepts as input:
    * uint8 array representing an video.

  Output:
    video: tf.Tensor of type tf.uint8 and shape [num_frames, height, width, 3]

  Example:
    * In the DatasetInfo object:
      features=features.FeatureDict({
          'video': features.Video(shape=(None, 64, 64, 3)),
      })

    * During generation:
      yield self.info.features.encode_example({
          'input': np.ones(shape=(128, 64, 64, 3), dtype=np.uint8),
      })
  """

  def __init__(self, shape):
    """Construct the connector.

    Args:
      shape: tuple of ints, the shape of the video (num_frames, height, width,
        channels=3).

    Raises:
      ValueError: If the shape is invalid
    """
    shape = tuple(shape)
    if len(shape) != 4:
      raise ValueError('Video shape should be of rank 4')
    super(Video, self).__init__(shape=shape, dtype=tf.uint8)

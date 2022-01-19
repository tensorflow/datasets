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

"""Tests for tensorflow_datasets.core.features.image_feature."""

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features as features_lib


class LabeledImageFeatureTest(testing.FeatureExpectationsTestCase):

  def test_images(self):
    rng = np.random.default_rng()
    img = rng.integers(256, size=(28, 28, 1), dtype=np.uint8)

    self.assertFeature(
        feature=features_lib.LabeledImage(
            labels=['background', 'car', 'truck'],
            shape=(28, 28, 1),
        ),
        shape=(28, 28, 1),
        dtype=tf.uint8,
        tests=[
            # Numpy array
            testing.FeatureExpectationItem(
                value=img,
                expected=img,
            ),
        ],
        test_attributes=dict(
            num_classes=3,
            names=['background', 'car', 'truck'],
            _use_colormap=True,
        ),
    )

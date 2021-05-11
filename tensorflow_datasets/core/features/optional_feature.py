# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Optional feature."""

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core import utils


class Optional(feature.FeatureConnector):
    """Optional `FeatureConnector` for wrapping other features.

    `Optional` defines a wrapper for any other `tfds.features.FeatureConnector`.
    At generation time, the user can even pass `None` as a suitable value to
    the Optional feature

    NOTE: `Optional` does not support Nested features in itself. However, it
    can be achieved by wrapping a `tfds.features.Sequence` feature.

    During `_generate_examples` the Optional feature can take as input:

      * Any type of input supported by the wrapped feature
      * `None` to denote absence of any input

    Example:
    At construction time:
    ```python
    features=features.FeatureDict({
        'image': features.Optional(features.Image()),
        'label': features.Optional(features.ClassLabel()),
    })
    ```

    At generation time:
    ```python
    yield{
        'image': 'path/to/image.jpg',
        'label': None
    }
    ```
    """

    def __init__(self, feature):
        """Construct the Optional connector

        Args:
          feature: `tfds.features` feature to wrap
        """
        #Convert primitive datatypes to tensor, raise error for invalid feature.
        #Like tf.int32 -> Tensor(shape=(), dtype=tf.int32)
        self._feature = to_feature(feature)

    @property
    def feature(self):
        """The wrapped feature."""
        return self._feature

    def get_tensor_info(self):
        """See base class for details."""
        return self.feature.get_tensor_info()

    def get_serialized_info(self):
        """See base class for details."""
        return self.feature.get_serialized_info()

    def encode_example(self, data):
        if data is None:
            return 'OptionalNone'
        else:
            return self.feature.encode_example(data)

    def decode_example(self, tfdata):
        """Decode example based on whether it is a None value or a valid one."""
        def is_none():
            return tf.experimental.Optional.empty(
                tf.TensorSpec(shape=(28,28,1), dtype=self.feature._dtype, name=None)
            )
        def is_valid():
            return tf.experimental.Optional.from_value(
                self.feature.decode_example(tfdata)
                )
        result = tf.cond(tf.math.equal(tfdata, 'OptionalNone'), is_none, is_valid)
        return result

def to_feature(value):
  """Convert the given value to Feature if necessary."""
  if isinstance(value, feature.FeatureConnector):
    return value
  elif utils.is_dtype(value):  # tf.int32, tf.string,...
    return feature.Tensor(shape=(), dtype=tf.as_dtype(value))
  else:
    raise ValueError('Feature not supported with `Optional`: {}'.format(value))

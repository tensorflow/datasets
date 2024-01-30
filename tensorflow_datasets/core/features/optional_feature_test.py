# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for optional_feature."""

from absl.testing import parameterized
import numpy as np
from tensorflow_datasets import testing
from tensorflow_datasets.core import features


class ScalarFeatureTest(
    parameterized.TestCase, testing.FeatureExpectationsTestCase
):

  @parameterized.parameters(
      (np.int64, 42, 42),
      (np.int64, None, testing.TestValue.NONE),
      (np.str_, 'foo', 'foo'),
      (np.str_, None, testing.TestValue.NONE),
  )
  def test_scalar(self, dtype, value, expected_np):
    self.assertFeature(
        feature=features.Optional(
            features.Scalar(dtype=dtype, doc='Some description')
        ),
        shape=(),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=value,
                raise_cls=NotImplementedError,
                raise_msg='supports tfds.data_source',
            ),
            testing.FeatureExpectationItem(
                value=value,
                expected_np=expected_np,
            ),
        ],
    )

  def test_dict(self):
    self.assertFeature(
        feature=features.FeaturesDict({'a': features.Optional(np.int32)}),
        shape={'a': ()},
        dtype={'a': np.int32},
        tests=[
            testing.FeatureExpectationItem(
                value={'a': None},
                raise_cls=NotImplementedError,
                raise_msg='supports tfds.data_source',
            ),
            testing.FeatureExpectationItem(
                value={'a': None},
                expected_np={'a': None},
            ),
            # You cannot ommit the key, you do have to specify {'a': None}.
            testing.FeatureExpectationItem(
                value={},
                raise_cls_np=RuntimeError,
                raise_msg="'a'",
            ),
        ],
    )


if __name__ == '__main__':
  testing.test_main()

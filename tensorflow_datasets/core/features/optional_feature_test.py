# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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
      (np.int64, 42, 42, 42),
      (np.int64, None, -9223372036854775808, testing.TestValue.NONE),
      (np.str_, 'foo', 'foo', 'foo'),
      (np.str_, None, '', testing.TestValue.NONE),
  )
  def test_scalar(self, dtype, value, expected, expected_np):
    self.assertFeature(
        feature=features.Scalar(
            dtype=dtype, doc='Some description', optional=True
        ),
        shape=(),
        dtype=dtype,
        tests=[
            testing.FeatureExpectationItem(
                value=value,
                expected=expected,
                expected_np=expected_np,
            ),
        ],
    )

  def test_dict(self):
    self.assertFeature(
        feature=features.FeaturesDict(
            {'a': features.Scalar(np.int32, optional=True)}
        ),
        shape={'a': ()},
        dtype={'a': np.int32},
        tests=[
            testing.FeatureExpectationItem(
                value={'a': None},
                expected={'a': -2147483648},
                expected_np={'a': None},
            ),
            # You cannot ommit the key, you do have to specify {'a': None}.
            testing.FeatureExpectationItem(
                value={},
                raise_cls=RuntimeError,
                raise_cls_np=RuntimeError,
                raise_msg="'a'",
            ),
        ],
    )

  def test_raise_error_if_feature_is_not_optional(self):
    self.assertFeature(
        feature=features.FeaturesDict({'a': np.int32}),
        shape={'a': ()},
        dtype={'a': np.int32},
        tests=[
            testing.FeatureExpectationItem(
                value={'a': None},
                raise_cls=TypeError,
                raise_cls_np=TypeError,
                raise_msg="not 'NoneType'",
            ),
        ],
    )


if __name__ == '__main__':
  testing.test_main()

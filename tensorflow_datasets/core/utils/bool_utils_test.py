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

import pytest
from tensorflow_datasets.core.utils import bool_utils


@pytest.mark.parametrize(
    ['string', 'result'],
    [
        (True, True),
        (False, False),
        # In `wit_kaggle` dataset
        ('true', True),
        (' true  ', True),
        ('false', False),
        ('  false ', False),
        # In `gap` dataset
        ('TRUE', True),
        ('FALSE', False),
        # In `kddcup99`/`duke_ultrasound_dataset_builder` datasets
        (0, False),
        ('0', False),
        (1, True),
        ('1', True),
    ],
)
def test_parse_bool_success(string, result):
  assert bool_utils.parse_bool(string) == result


@pytest.mark.parametrize(
    ['string', 'exception'],
    [
        ('_true', 'Cannot convert "_true" to bool'),
        ('2', 'Cannot convert "2" to bool'),
    ],
)
def test_parse_bool_exception(string, exception):
  with pytest.raises(Exception, match=exception):
    bool_utils.parse_bool(string)

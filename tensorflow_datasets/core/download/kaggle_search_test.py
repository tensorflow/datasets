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

"""Tests for Kaggle API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

from tensorflow_datasets import testing
from tensorflow_datasets.core.download import kaggle_search


class KaggleSearchTest(testing.TestCase):

  def test_kaggle_search(self):
    searcher = kaggle_search.KaggleSearch(search='career-con-2019')
    reg = re.compile(r'\s+')
    output = """refdeadlinecategoryrewardteamCountuserHasEntered
    ------------------------------------------------------------
    --------------career-con-20192019-04-1123:59:00RecruitmentSwag1478False """
    self.assertEqual(reg.sub('', searcher.searching), reg.sub('', output))


if __name__ == "__main__":
  testing.test_main()
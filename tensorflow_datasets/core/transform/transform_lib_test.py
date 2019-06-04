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

"""Tests for tensorflow_datasets.core.api_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

from tensorflow_datasets import testing
from tensorflow_datasets.core.transform import transform_lib


class TransformLibTest(testing.TestCase):

  def test_transform(self):

    Foo = collections.namedtuple("Foo", ["a", "b"])  # pylint: disable=invalid-name

    def delete_b(ex):
      del ex["b"]
      return ex

    def increment(val):
      return val * 10

    data = {
        "a": 1,
        "b": 2,
        "c": (3, 4),
        "d": {
            "f": 6,
        },
        "g": collections.OrderedDict([
            ("h", 7),
            ("i", 8),
        ]),
        "j": Foo(9, 1),
    }

    out_data = transform_lib.partial_map_nested([
        delete_b,  # operates on the whole dictionary
        {
            "a": increment,
            # second element has 2 transforms applied to it
            # None in a tuple means pass-through (i.e. identity)
            "c": (None, [increment, increment]),
            # missing keys are passed through (i.e. identity)
        },
        {
            "a": increment,
            "d": {
                "f": [increment, increment],
            },
            "g": {
                "i": increment,
            },
            "j": (None, increment),
        },
    ], data)

    self.assertEqual(out_data, {
        "a": 100,
        "c": (3, 400),
        "d": {
            "f": 600,
        },
        "g": collections.OrderedDict([
            ("h", 7),
            ("i", 80),
        ]),
        "j": Foo(9, 10),
    })


if __name__ == "__main__":
  testing.test_main()

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

"""Tests for tensorflow_datasets.core.units."""
from tensorflow_datasets import testing
from tensorflow_datasets.core import units


class UnitsTest(testing.TestCase):

  def test_none(self):
    self.assertEqual("Unknown size", units._size_str(None))

  def test_normal_sizes(self):
    self.assertEqual("1.50 PiB", units._size_str(1.5 * units.PiB))
    self.assertEqual("1.50 TiB", units._size_str(1.5 * units.TiB))
    self.assertEqual("1.50 GiB", units._size_str(1.5 * units.GiB))
    self.assertEqual("1.50 MiB", units._size_str(1.5 * units.MiB))
    self.assertEqual("1.50 KiB", units._size_str(1.5 * units.KiB))

  def test_bytes(self):
    self.assertEqual("150 bytes", units._size_str(150))

  def test_size(self):
    self.assertEqual(repr(units.Size()), "Unknown size")
    self.assertEqual(repr(units.Size(150)), "150 bytes")
    self.assertEqual(repr(units.Size(1.5 * units.GiB)), "1.50 GiB")
    self.assertEqual(repr(units.Size(150) + 150), "300 bytes")
    self.assertEqual(repr(units.Size(300) - 150), "150 bytes")
    self.assertEqual(str(units.Size()), "Unknown size")
    self.assertEqual(str(units.Size(150)), "150 bytes")
    x = units.Size(300)
    x += 300
    self.assertEqual(repr(x), "600 bytes")


if __name__ == "__main__":
  testing.test_main()

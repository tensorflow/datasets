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

"""Tests for tensorflow_datasets.core.lazy_imports."""

from absl.testing import parameterized
import tensorflow_datasets as tfds
from tensorflow_datasets import testing


class LazyImportsTest(testing.TestCase, parameterized.TestCase):

  # The following deps are not in the test list because the datasets that
  # require them need to have their tests run in isolation:
  # * crepe (NSynth)
  # * librosa (NSynth)
  @parameterized.parameters(
      "bs4",
      "cv2",
      "gcld3",
      "gcsfs_store",
      "langdetect",
      "lxml",
      "matplotlib",
      "mwparserfromhell",
      "nltk",
      "os",
      "pandas",
      "pretty_midi",
      "pycocotools",
      "pydub",
      "scipy",
      "skimage",
      "tifffile",
      "tldextract",
      "zarr",
  )
  def test_import(self, module_name):
    getattr(tfds.core.lazy_imports, module_name)

  def test_bad_import(self):
    with self.assertRaisesWithPredicateMatch(
        ModuleNotFoundError, "extras_require"
    ):
      _ = tfds.core.lazy_imports.test_foo


if __name__ == "__main__":
  testing.test_main()

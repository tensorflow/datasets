# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Tests for tensorflow_datasets.core.lazy_imports."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import parameterized
import six
import tensorflow_datasets as tfds
from tensorflow_datasets import testing


class LazyImportsTest(testing.TestCase, parameterized.TestCase):

  # The following deps are not in the test list because the datasets that
  # require them need to have their tests run in isolation:
  # * crepe (NSynth)
  # * librosa (NSynth)
  @parameterized.parameters(
      "cv2",
      "langdetect",
      "matplotlib",
      "mwparserfromhell",
      "nltk",
      "os",
      "pandas",
      "pretty_midi",
      "pydub",
      "scipy",
      "skimage",
      "tldextract",
  )
  def test_import(self, module_name):
    if module_name == "nltk" and six.PY2:  # sklearn do not support Python2
      return
    # TODO(rsepassi): Re-enable skimage on Py3 (b/129964829)
    if module_name == "skimage" and six.PY3:
      return
    getattr(tfds.core.lazy_imports, module_name)

  def test_bad_import(self):
    with self.assertRaisesWithPredicateMatch(ImportError, "extras_require"):
      _ = tfds.core.lazy_imports.test_foo

  # pylint: disable=import-outside-toplevel, protected-access, unused-import
  def test_lazy_import_context_manager(self):
    with tfds.core.try_import():
      import pandas
      import matplotlib.pyplot as plt

    self.assertTrue(hasattr(pandas, "read_csv"))
    self.assertTrue(hasattr(plt, "figure"))

  def test_import_without_context_manager(self):
    import nltk
    self.assertTrue(hasattr(nltk, 'tokenize'))

    tfds.core.lazy_imports_lib._ALLOWED_LAZY_DEPS.append("valid_module")
    with self.assertRaisesWithPredicateMatch(ImportError,
                                             "No module named 'valid_module'"):
      import valid_module

    tfds.core.lazy_imports_lib._ALLOWED_LAZY_DEPS.remove("valid_module")

  def test_lazy_import_context_manager_errors(self):
    with self.assertRaisesWithPredicateMatch(ImportError, "_ALLOWED_LAZY_DEPS"):
      with tfds.core.try_import():
        import fake_module

    tfds.core.lazy_imports_lib._ALLOWED_LAZY_DEPS.append("new_module")
    with tfds.core.try_import():
      import new_module

    with self.assertRaisesWithPredicateMatch(ImportError, "extras_require"):
      new_module.some_function()

    tfds.core.lazy_imports_lib._ALLOWED_LAZY_DEPS.remove("new_module")
  # pylint: enable=import-outside-toplevel, protected-access, unused-import


if __name__ == "__main__":
  testing.test_main()

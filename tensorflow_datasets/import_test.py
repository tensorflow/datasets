# coding=utf-8
# Copyright 2026 The TensorFlow Datasets Authors.
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

"""Test import."""

import os
import subprocess
import sys
import tensorflow_datasets as tfds


class ImportTest(tfds.testing.TestCase):

  def test_import(self):
    pass

  def test_gcs_prefer_fsspec_true(self):
    env = os.environ.copy()
    env['GCS_PREFER_FSSPEC'] = 'true'
    env.pop('EPATH_PREFER_FSSPEC', None)

    code = """
import os
import tensorflow_datasets as tfds
from etils import epath
print("EPATH_PREFER_FSSPEC:", os.environ.get('EPATH_PREFER_FSSPEC'))
p = epath.Path('gs://dummy-bucket/file.txt')
print("BACKEND:", type(p._backend).__name__)
"""
    result = subprocess.run(
        [sys.executable, '-c', code],
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    self.assertIn("EPATH_PREFER_FSSPEC: true", result.stdout)
    self.assertIn("BACKEND: _FileSystemSpecBackend", result.stdout)

  def test_gcs_prefer_fsspec_false(self):
    env = os.environ.copy()
    env.pop('GCS_PREFER_FSSPEC', None)
    env.pop('EPATH_PREFER_FSSPEC', None)

    code = """
import os
import tensorflow_datasets as tfds
from etils import epath
print("EPATH_PREFER_FSSPEC:", os.environ.get('EPATH_PREFER_FSSPEC'))
p = epath.Path('gs://dummy-bucket/file.txt')
print("BACKEND:", type(p._backend).__name__)
"""
    result = subprocess.run(
        [sys.executable, '-c', code],
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    self.assertIn("EPATH_PREFER_FSSPEC: None", result.stdout)
    self.assertIn("BACKEND: _TfBackend", result.stdout)


if __name__ == '__main__':
  tfds.testing.test_main()

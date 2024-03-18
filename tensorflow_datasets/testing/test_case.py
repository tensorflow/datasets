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

"""Base TestCase to use test_data."""

import contextlib
import os
import tempfile
from unittest import mock

from absl import logging
from tensorflow_datasets import setup_teardown
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.testing import test_case_in_context
from tensorflow_datasets.testing import test_utils


class TestCase(test_case_in_context.TestCaseInContext, tf.test.TestCase):
  """Base TestCase to be used for all tests.

  `test_data` class attribute: path to the directory with test data.
  `tmp_dir` attribute: path to temp directory reset before every test.
  """

  # By default, tests globally applied fixture to disable GCS, Github API,...
  # If set, do not apply the given global fixtures
  DO_NOT_APPLY_FIXTURES = []

  @classmethod
  def _context_managers(cls):
    context_managers = []
    for fixture in setup_teardown.GLOBAL_FIXTURES:
      if fixture in cls.DO_NOT_APPLY_FIXTURES:
        continue
      context_managers.append(contextlib.contextmanager(fixture)())
    if test_utils.disable_gcs_access not in cls.DO_NOT_APPLY_FIXTURES:
      context_managers.append(test_utils.disable_gcs_access())
    return context_managers

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.test_data = os.path.join(os.path.dirname(__file__), "test_data")

  def setUp(self):
    super().setUp()
    # get_temp_dir is actually the same for all tests, so create a temp sub-dir.
    self.tmp_dir = tempfile.mkdtemp(dir=tf.compat.v1.test.get_temp_dir())

  @contextlib.contextmanager
  def assertLogs(self, text, level="info"):
    with mock.patch.object(logging, level) as mock_log:
      yield
      concat_logs = ""
      for log_call in mock_log.call_args_list:
        args = log_call[0]
        base, args = args[0], args[1:]
        log_text = base % tuple(args)
        concat_logs += " " + log_text
      self.assertIn(text, concat_logs)

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

"""Base TestCase to run inside context managers."""

from collections.abc import Sequence
import contextlib
from typing import Any, ContextManager
import unittest


class TestCaseInContext(unittest.TestCase):
  """Base TestCase for running tests inside the given contexts.

  It ensures that all contexts are entered before any test starts and are exited
  upon all tests completion.
  """

  @classmethod
  def _context_managers(cls) -> Sequence[ContextManager[Any]]:
    """Returns a list of context managers automatically applied to all tests."""
    raise NotImplementedError

  @classmethod
  def setUpClass(cls):
    super().setUpClass()

    # Keep track of all entered contexts
    cls._stack = contextlib.ExitStack()
    for cm in cls._context_managers():
      cls._stack.enter_context(cm)

  @classmethod
  def tearDownClass(cls):
    # Exit all contexts in the reverse order
    cls._stack.close()
    super().tearDownClass()

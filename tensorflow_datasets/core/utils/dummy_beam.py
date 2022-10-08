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
"""Utilities for beam wrapper."""

import types

_MSG = ("Failed importing {name}. Please install {name}."
        " Using pip install {name}")

class Empty(): # pylint: disable=too-few-public-methods
    """Empty class for beam API."""
    def __call__(self, *args, **kwargs):
        return None

class DummyBeam(types.ModuleType): # pylint: disable=too-few-public-methods
    """Dummy class.
    Raise:
      ImportError, when calling beam API and apache_beam was not installed.
    """
    DoFn = Empty
    Pipeline = Empty

    def __init__(self):
        self.module_name = "apache_beam"

    def __getattribute__(self, _):
        if getattr(DummyBeam, _, None) is Empty:
            _name = super().__getattribute__('module_name')
            err_msg = _MSG.format(name=_name)
            raise ImportError(err_msg)

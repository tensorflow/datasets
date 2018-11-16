# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""API utilities."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import inspect

import six
import wrapt

__all__ = [
    "disallow_positional_args"
]

REQUIRED_ARG = object()
_POSITIONAL_ARG_ERR_MSG = (
    "Please use keyword arguments and not positional arguments. This enables "
    "more flexible API development. Thank you!\n"
    "Positional arguments passed to fn %s: %s.")


@wrapt.decorator
def disallow_positional_args(fn, instance, args, kwargs):
  """Requires function to be called using keyword arguments."""
  ismethod = instance is not None
  _check_no_positional(fn, args, ismethod)
  _check_required(fn, kwargs)
  return fn(*args, **kwargs)


def _check_no_positional(fn, args, is_method=False):
  offset = int(is_method)
  if args:
    arg_names = getargspec(fn).args[offset:offset + len(args)]
    raise ValueError(_POSITIONAL_ARG_ERR_MSG % (fn.__name__, str(arg_names)))


def _required_args(fn):
  """Returns arguments of fn with default=REQUIRED_ARG."""
  spec = getargspec(fn)
  if not spec.defaults:
    return []

  required_args = []
  arg_names = spec.args[-len(spec.defaults):]
  for name, val in zip(arg_names, spec.defaults):
    if val is REQUIRED_ARG:
      required_args.append(name)
  return required_args


def _check_required(fn, kwargs):
  required_args = _required_args(fn)
  for arg in required_args:
    if arg not in kwargs:
      raise ValueError("Argument %s is required." % arg)


def getargspec(fn):
  if six.PY3:
    spec = inspect.getfullargspec(fn)
  else:
    spec = inspect.getargspec(fn)
  return spec

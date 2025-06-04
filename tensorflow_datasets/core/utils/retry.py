# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""To add retry logic to operations suceptible to transient failures."""

import random
import time
from typing import Callable, ParamSpec, TypeVar

from absl import logging
from tensorflow_datasets.core import constants


P = ParamSpec("P")
T = TypeVar("T")


def retry(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
  """Returns a decorator that retries the function."""
  # We purposely don't use flags, as this code might be run before flags are
  # parsed.
  tries = constants.TFDS_RETRY_TRIES
  delay = constants.TFDS_RETRY_INITIAL_DELAY
  multiplier = constants.TFDS_RETRY_DELAY_MULTIPLIER
  noise = constants.TFDS_RETRY_NOISE
  msg_substrings = constants.TFDS_RETRY_MSG_SUBSTRINGS
  for trial in range(1, tries + 1):
    try:
      return func(*args, **kwargs)
    except BaseException as err:  # pylint: disable=broad-except
      if trial >= tries:
        raise err
      msg = str(err)
      for msg_substring in msg_substrings:
        if msg_substring in msg:
          break
      else:
        raise err
      delay = delay + random.uniform(0, noise)
      logging.warning("%s, retrying in %s seconds...", msg, delay)
      time.sleep(delay)
      delay *= multiplier

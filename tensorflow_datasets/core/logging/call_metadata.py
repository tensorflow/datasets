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

"""To associate metadata with TFDS calls."""

import enum
import threading
import time
from typing import Dict, Optional, Tuple

# Maps thread_id to "Session ID", if any.
_THREAD_TO_SESSIONID: Dict[int, int] = {}

_NEXT_SESSION_ID = 1
_NEXT_SESSION_ID_LOCK = threading.Lock()


class Status(enum.Enum):
  UNKNOWN = 0
  SUCCESS = 1
  ERROR = 2


def _get_session_id(thread_id: int) -> Tuple[int, bool]:
  """Returns (session_id, direct_call) tuple."""
  session_id = _THREAD_TO_SESSIONID.get(thread_id, None)
  if session_id:
    direct_call = False
  else:
    direct_call = True
    with _NEXT_SESSION_ID_LOCK:
      global _NEXT_SESSION_ID
      session_id = _NEXT_SESSION_ID
      _THREAD_TO_SESSIONID[thread_id] = session_id
      _NEXT_SESSION_ID += 1
  return session_id, direct_call


class CallMetadata:
  """Represents metadata associated with call.

  Object must be initialized just before the call, on same thread.
  """

  # The start and end times of the event (microseconds since Epoch).
  start_time_micros: Optional[int]
  end_time_micros: Optional[int]

  # The status (success or error) of the call.
  status: Status

  # Thread in which the call was made.
  thread_id: int

  # A unique number within the scope of the process to identify the session.
  # A session starts with a TFDS call (eg: `tfds.load(...)` and is propagated
  # through the stack to possibly other TFDS calls (eg: `tfds.dataset(...)`)
  # which the end-user did not call directly.
  session_id: int

  # Whether the operation was directly triggered by the user, ie: it is the
  # first operation of the session.
  direct_call: bool


  def __init__(self):
    self.status = Status.UNKNOWN
    self.thread_id = threading.get_ident()
    self.session_id, self.direct_call = _get_session_id(self.thread_id)
    self.start_time_micros = int(time.time() * 1e6)

  def mark_end(self):
    self.end_time_micros = int(time.time() * 1e6)
    if self.status == Status.UNKNOWN:
      self.status = Status.SUCCESS
    if self.direct_call:
      _THREAD_TO_SESSIONID.pop(self.thread_id)

  def mark_error(self):
    self.status = Status.ERROR

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

"""Download backend interface."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class DownloadBackendAbc(object):
  """Download backend interface.

  Download backend is the object containing code specific to the deployment
  platform (local or cloud).
  """

  @abc.abstractmethod
  def download(self, download_trial):
    """Download the given url (thread-safe)."""
    raise NotImplementedError('Abstract method.')

  @abc.abstractmethod
  def extract_gzip(self, src, dst):
    """Extract the given file."""
    raise NotImplementedError('Abstract method.')

  @abc.abstractmethod
  def extract_zip(self, src, dst):
    """Extract the given file."""
    raise NotImplementedError('Abstract method.')

  @abc.abstractmethod
  def extract_tar(self, src, dst):
    """Extract the given file."""
    raise NotImplementedError('Abstract method.')

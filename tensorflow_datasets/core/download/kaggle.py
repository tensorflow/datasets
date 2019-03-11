# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Data downloads using the Kaggle CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess as sp

from absl import logging
import tensorflow as tf

from tensorflow_datasets.core import utils

_ERR_MSG = """\
To download Kaggle data through TFDS, follow the instructions to install the \
kaggle API and get API credentials:
https://github.com/Kaggle/kaggle-api#installation

Additionally, you must join the competition through the Kaggle competition's \
website:
https://www.kaggle.com/c/%s
"""

_NOT_FOUND_ERR_MSG = """\
Competition %s not found. Please ensure you have spelled the competition name \
correctly.
"""


class KaggleFile(object):
  """Represents a Kaggle competition file."""
  _URL_PREFIX = "kaggle://"

  def __init__(self, competition_name, filename):
    self._competition_name = competition_name
    self._filename = filename

  @property
  def competition(self):
    return self._competition_name

  @property
  def filename(self):
    return self._filename

  @classmethod
  def from_url(cls, url):
    if not KaggleFile.is_kaggle_url(url):
      raise TypeError("Not a valid kaggle URL")
    competition_name, filename = url[len(cls._URL_PREFIX):].split("/", 1)
    return cls(competition_name, filename)

  @staticmethod
  def is_kaggle_url(url):
    return url.startswith(KaggleFile._URL_PREFIX)

  def to_url(self):
    return "%s%s/%s" % (self._URL_PREFIX, self._competition_name,
                        self._filename)


class KaggleCompetitionDownloader(object):
  """Downloader for a Kaggle competition.

  Usage:

  ```
  downloader = KaggleCompetitionDownloader(competition_name)
  for fname in downloader.competition_files:
    downloader.download_file(fname, make_file_output_path(fname))
  ```
  """

  def __init__(self, competition_name):
    self._competition_name = competition_name

  @utils.memoized_property
  def competition_files(self):
    """List of competition files."""
    command = [
        "kaggle",
        "competitions",
        "files",
        "-v",
        self._competition_name,
    ]
    output = _run_kaggle_command(command, self._competition_name)
    return sorted([
        line.split(",")[0] for line in output.split("\n")[1:] if line
    ])

  @utils.memoized_property
  def competition_urls(self):
    """Returns 'kaggle://' urls."""
    return [
        KaggleFile(self._competition_name, fname).to_url()
        for fname in self.competition_files  # pylint: disable=not-an-iterable
    ]

  def download_file(self, fname, output_dir):
    """Downloads competition file to output_dir."""
    if fname not in self.competition_files:  # pylint: disable=unsupported-membership-test
      raise ValueError("%s is not one of the competition's "
                       "files: %s" % (fname, self.competition_files))
    command = [
        "kaggle",
        "competitions",
        "download",
        "--file",
        fname,
        "--path",
        output_dir,
        "-c",
        self._competition_name,
    ]
    _run_kaggle_command(command, self._competition_name)
    return os.path.join(output_dir, fname)


def _run_kaggle_command(command_args, competition_name):
  """Run kaggle command with subprocess."""
  try:
    output = sp.check_output(command_args)
    return tf.compat.as_text(output)
  except sp.CalledProcessError as err:
    output = err.output
    _log_command_output(output, error=True)
    if output.startswith(b"404"):
      logging.error(_NOT_FOUND_ERR_MSG, competition_name)
      raise
    logging.error(_ERR_MSG, competition_name)
    raise


def _log_command_output(output, error=False):
  log = logging.error if error else logging.info
  log("kaggle command output:\n%s", tf.compat.as_text(output))

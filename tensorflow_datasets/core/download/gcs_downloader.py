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

import subprocess as sp

import re
from absl import logging
import tensorflow as tf

from urllib.parse import urlparse

_URL_PREFIX = "gs://"

_GS_URL = re.compile(r'^https://storage\.googleapis\.com/')


def is_gs_url(url):
    """Check if the url is gcs url"""
    return url.startswith(_URL_PREFIX) or _GS_URL.match(url)


def url_path_parser(url):
    """Parse the url path"""
    return urlparse(url).path


def api_to_gs_path_converter(url):
    """Convert the gcs url to gsutil url."""
    return "gs:/" + url_path_parser(url)


def _run_gsutil_command(command_args):
    """Run gsutil command on subprocess."""
    output = sp.check_output(command_args)
    return tf.compat.as_text(output)


def _log_command_output(output, error=False):
    log = logging.error if error else logging.info
    log("Gsutil command output:\n%s", tf.compat.as_text(output))


def gs_downloader(url, destination_path):
    """Download google cloud storage files."""
    if _GS_URL.match(url):
        url = api_to_gs_path_converter(url)
    _run_gsutil_command(["gsutil", "cp", "-r", url, destination_path])


_url = "https://.googleapis.com/laurencemoroney-blog.appspot.com/rps-test-set.zip"


# TODO(us) Error handling
# TODO(us) Checksum validation
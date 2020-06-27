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
"""Data downloads using the Kaggle CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import subprocess as sp
import zipfile

from absl import logging
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import resource

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

KaggleType = collections.namedtuple(
    "KaggleType",
    ["prefix", "download_cmd", "dl_flag"])

_KAGGLE_TYPES = {
    "dataset": KaggleType(
        prefix="dataset",
        download_cmd="datasets",
        dl_flag="-d"),
    "competition": KaggleType(
        prefix="competition",
        download_cmd="competitions",
        dl_flag="-c")
}


def _get_kaggle_type(competition_or_dataset):
  if "/" in competition_or_dataset:
    return _KAGGLE_TYPES["dataset"]
  return _KAGGLE_TYPES["competition"]


def _kaggle_dir_name(competition_or_dataset):
  """Returns name of dir where the dataset is to be downloaded."""
  return competition_or_dataset.replace("/", "_")


def _get_kaggle_url(competition_or_dataset):
  """Returns 'kaggle.com' urls."""
  return "%s/%s" % ("kaggle.com", competition_or_dataset)


def _log_command_output(output, error=False):
  log = logging.error if error else logging.info
  log("kaggle command output:\n%s", tf.compat.as_text(output))


def _run_kaggle_command(command_args, competition_or_dataset):
  """Run kaggle command with subprocess."""
  try:
    output = sp.check_output(command_args)
    return tf.compat.as_text(output)
  except sp.CalledProcessError as err:
    output = err.output
    _log_command_output(output, error=True)
    if output.startswith(b"404"):
      logging.error(_NOT_FOUND_ERR_MSG, competition_or_dataset)
      raise
    logging.error(_ERR_MSG, competition_or_dataset)
    raise
  except FileNotFoundError as err:
    raise FileNotFoundError(_ERR_MSG % competition_or_dataset +
                            "\nOriginal exception: {}".format(err))


def _download_competition_or_dataset(competition_or_dataset, output_dir):
  """Downloads kaggle data to output_dir"""
  kaggle_type = _get_kaggle_type(competition_or_dataset)
  command = ["kaggle",
             kaggle_type.download_cmd,
             "download",
             kaggle_type.dl_flag,
             competition_or_dataset,
             "-p",
             output_dir]
  _run_kaggle_command(command, competition_or_dataset)
  downloads = tf.io.gfile.listdir(output_dir)
  for download in downloads:
    fpath = os.path.join(output_dir, download)
    if zipfile.is_zipfile(fpath):
      ext = extractor.get_extractor()
      with ext.tqdm():
        ext.extract(fpath, resource.ExtractMethod.ZIP, output_dir).get()


def kaggle_download(competition_or_dataset, download_dir):
  """Downloads competition file to output_dir."""
  kaggle_dir = _kaggle_dir_name(competition_or_dataset)
  download_path = os.path.join(download_dir, kaggle_dir)
  # If the dataset has already been downloaded, return the path to it.
  if os.path.isdir(download_path):
    logging.info('Dataset %s already downloaded: reusing %s.',
                 competition_or_dataset, download_path)
    return download_path
  # Otherwise, download the dataset.
  with utils.incomplete_dir(download_path) as tmp_data_dir:
    logging.info('Downloading %s into %s...', competition_or_dataset,
                 tmp_data_dir)
    _download_competition_or_dataset(competition_or_dataset, tmp_data_dir)
  return download_path

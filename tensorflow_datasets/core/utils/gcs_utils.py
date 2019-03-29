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

"""Utilities for accessing TFDS GCS buckets."""

import os
import posixpath
from xml.etree import ElementTree

import requests
import tensorflow as tf

from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils

GCS_URL = "http://storage.googleapis.com"

# for dataset_info/
GCS_DATASET_INFO_URL = posixpath.join(GCS_URL, "tfds-data")
GCS_DATASET_INFO_PATH = "dataset_info"


def is_gcs_dataset_accessible(relative_data_dir):
  return tf.io.gfile.exists(os.path.join(
      constants.GCS_DATA_DIR,
      relative_data_dir,
      "dataset_info.json"))


def download_gcs_info_file(path, out_fname=None):
  """Download a file from GCS, optionally to a file."""
  url = posixpath.join(GCS_DATASET_INFO_URL, path)
  stream = bool(out_fname)
  resp = requests.get(url, stream=stream)
  if not resp.ok:
    raise ValueError("GCS bucket inaccessible")
  if out_fname:
    with tf.io.gfile.GFile(out_fname, "wb") as f:
      for chunk in resp.iter_content(1024):
        f.write(chunk)
  else:
    return resp.content


@utils.memoize()
def gcs_info_files():
  top_level_xml_str = download_gcs_info_file("")
  xml_root = ElementTree.fromstring(top_level_xml_str)
  filenames = [el[0].text for el in xml_root if el.tag.endswith("Contents")]
  return filenames


def gcs_dataset_info_files(dataset_dir):
  """Return paths to GCS files in the given dataset directory."""
  prefix = posixpath.join(GCS_DATASET_INFO_PATH, dataset_dir, "")
  # Filter for this dataset
  filenames = [el for el in gcs_info_files()
               if el.startswith(prefix) and len(el) > len(prefix)]
  return filenames

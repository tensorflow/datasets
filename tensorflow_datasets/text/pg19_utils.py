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
"""Utilities for generating the PG-19 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import posixpath
from xml.etree import ElementTree
import requests

GCS_URL = 'https://storage.googleapis.com'
BUCKET = posixpath.join(GCS_URL, 'deepmind-gutenberg')

def gcs_files(url, prefix_filter=None, marker=None):
  """Get files from GCS."""
  if prefix_filter:
    url += '?prefix={}'.format(prefix_filter)
  if marker:
    url += '&marker={}'.format(marker)
  resp = requests.get(url)
  if not resp.ok:
    raise ValueError('GCS bucket inaccessible')
  return resp.content


def get_all_files_name(prefix_filter=None):
  """Get all files from GCS"""
  top_level_xml_str = gcs_files(BUCKET, prefix_filter=prefix_filter)
  xml_root = ElementTree.fromstring(top_level_xml_str)
  filenames = [el[0].text for el in xml_root if el.tag.endswith('Contents')]
  next_marker = xml_root[3]

  while next_marker.text != 'false':
    top_level_xml_str = gcs_files(BUCKET,
                                  prefix_filter=prefix_filter,
                                  marker=xml_root[3].text)
    xml_root = ElementTree.fromstring(top_level_xml_str)
    filenames.extend([
        el[0].text for el in xml_root
        if el.tag.endswith('Contents')
        ])
    next_marker = xml_root[3]
  return filenames[:-1]


def get_urls(filenames):
  """Build URL from filenames from GCS"""
  return [posixpath.join(BUCKET, filename) for filename in filenames]

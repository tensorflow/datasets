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

r"""Script to create the checksums file of a dataset.

This script is meant to be used by the creator of a DatasetBuilder.

Once the DatasetBuilder has been written and run at least once, and files have
been downloaded, run this script to create the file associating URLs and
checksums.

Example of usage:

$ scripts/create_checksum_file --dest_dir=url_checksums --dataset=mnist

See documentation at:
https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md#enabling-downloads-validation

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import json
import os
import re

from absl import app
from absl import flags
import tensorflow as tf

from tensorflow_datasets.core.download import checksums_file
from tensorflow_datasets.core.download import util

flags.DEFINE_string('dataset', None, 'Name of dataset.')
flags.DEFINE_string('dest_dir', 'url_checksums',
                    'Path to directory in which to write the checksums file .')
flags.DEFINE_string('downloads_path',
                    os.path.join('~', 'tensorflow_datasets', 'downloads'),
                    'Path to downloads directory.')
flags.DEFINE_string('extracts_path',
                    os.path.join('~', 'tensorflow_datasets', 'extracted'),
                    'Path to extractions directory.')

FLAGS = flags.FLAGS


def _rename(old_path, new_path):
  print('mv %s %s' % (old_path, new_path))
  tf.gfile.Rename(old_path, new_path, overwrite=True)


def _write_checksums(dataset_name, out_path, downloads_path):
  """Write url->checksum csv file, return mapping."""
  url_to_checksum = {}
  info_fnames = [fname for fname in tf.gfile.ListDirectory(downloads_path)
                 if fname.endswith('.INFO')]
  for info_fname in info_fnames:
    with tf.gfile.Open(os.path.join(downloads_path, info_fname)) as info_f:
      info = json.load(info_f)
    if dataset_name not in info['dataset_names']:
      continue
    fname = info_fname[:-len('.INFO')]
    path = os.path.join(downloads_path, fname)
    if not tf.gfile.Exists(path):
      continue
    sha256 = util.read_checksum_digest(path, hashlib.sha256)
    for url in info['urls']:
      if url in info and url_to_checksum[url] != sha256:
        msg = ('URL %s is associated with two sha256 checksums: %s (old) and '
               '%s (actual). Please check the INFO files %s.' % (
                   url, url_to_checksum[url], sha256, info_fnames))
        raise AssertionError(msg)
      url_to_checksum[url] = sha256
  if not url_to_checksum:
    print('No files downloaded by %s could be found in %s.' % (
        dataset_name, downloads_path))
    return
  print('Writing url->checksum associations to %s...' % out_path)
  checksums_file.dump(out_path, url_to_checksum)
  return url_to_checksum


def _move_already_downloaded_extracted_files(url_to_checksum, downloads_path,
                                             extracts_path):
  """Move already downloaded files to new filenames using checksums."""
  url_to_methods = {}  # url_checksum -> methods, filled by following block:
  for fname in tf.gfile.ListDirectory(extracts_path):
    res = re.match(r'(\d+)\.url\.([a-f0-9]{64})', fname)
    if res:
      extraction_method = res.group(1)
      url_checksum = res.group(2)
      url_to_methods.setdefault(url_checksum, []).append(extraction_method)

  for url, checksum in url_to_checksum.items():
    url_checksum = hashlib.sha256(url.encode('utf8')).hexdigest()
    # Downloaded file + INFO file
    old_path = os.path.join(downloads_path, 'url.' + url_checksum)
    if tf.gfile.Exists(old_path):
      new_path = os.path.join(downloads_path, checksum)
      _rename(old_path, new_path)
      _rename(old_path + '.INFO', new_path + '.INFO')
    # Extracted files:
    for method in url_to_methods.get(url_checksum, []):
      old_path = os.path.join(extracts_path, '%s.url.%s' % (method,
                                                            url_checksum))
      new_path = os.path.join(extracts_path, '%s.%s' % (method, checksum))
      _rename(old_path, new_path)


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  dataset = FLAGS.dataset
  checksums_path = os.path.join(os.path.expanduser(FLAGS.dest_dir),
                                '%s.csv' % dataset)
  downloads_path = os.path.expanduser(FLAGS.downloads_path)
  extracts_path = os.path.expanduser(FLAGS.extracts_path)
  url_to_checksum = _write_checksums(dataset, checksums_path, downloads_path)
  if url_to_checksum:
    _move_already_downloaded_extracted_files(
        url_to_checksum, downloads_path, extracts_path)


if __name__ == '__main__':
  flags.mark_flag_as_required('dataset')
  app.run(main)

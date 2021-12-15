# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Copy the info files from placer to GCS bucket.
"""

import os

from absl import app
from absl import flags
from absl import logging
import tensorflow as tf

import tensorflow_datasets as tfds

flags.DEFINE_boolean('dry_run', True, 'If True, just print, do nothing.')
flags.DEFINE_boolean('overwrite', False, 'If True, overwrites the data.')
flags.DEFINE_string(
    'from_directory', tfds.core.constants.DATA_DIR,
    'Where to get the info files from (datasets/ dir on placer).')
flags.DEFINE_string('to_directory', None,
                    'Path where dataset info files will be copied.')

FLAGS = flags.FLAGS


def _copy_metadata(from_dir, to_dir):
  """Copy the info files from within `from_dir` to `to_dir`."""
  if not FLAGS.dry_run:
    tf.io.gfile.makedirs(to_dir)
  for fname in tfds.core.utils.list_info_files(from_dir):
    from_path = os.path.join(from_dir, fname)
    to_path = os.path.join(to_dir, fname)
    logging.info('cp %s %s', from_path, to_path)
    if not FLAGS.dry_run:
      tf.io.gfile.copy(from_path, to_path, overwrite=True)


def copy(from_dir: tfds.core.PathLike, to_dir: tfds.core.PathLike) -> None:
  """Copy the info files from within `from_dir` to `to_dir`."""
  for full_name in tfds.core.load.list_full_names():
    from_full_name_dir = os.path.join(from_dir, full_name)
    to_full_name_dir = os.path.join(to_dir, full_name)

    # Skip if the dataset isn't generated or that metadata are already copied
    if not tf.io.gfile.exists(from_full_name_dir):
      logging.info('Skipping %s (not found)', from_full_name_dir)
      continue
    if tf.io.gfile.exists(to_full_name_dir) and not FLAGS.overwrite:
      logging.info('Skipping %s (already exists)', to_full_name_dir)
      continue

    _copy_metadata(from_dir=from_full_name_dir, to_dir=to_full_name_dir)


def main(_):
  copy(
      FLAGS.from_directory,
      FLAGS.to_directory or tfds.core.gcs_path('dataset_info'),
  )


if __name__ == '__main__':
  app.run(main)

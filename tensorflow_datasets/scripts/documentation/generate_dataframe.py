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

r"""Script which generates datasets dataframes.
"""

import functools
import multiprocessing
import os
from typing import List, Optional

from absl import app
from absl import flags
from absl import logging

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import script_utils


WORKER_COUNT_DATASETS = 10

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'datasets', None,
    'Comma separated list of datasets to generates. None for all datasets.')
flags.DEFINE_string(
    'dst_dir', tfds.core.gcs_path('visualization/dataframe'),
    'Destination dir to save the dataframe html.')
flags.DEFINE_boolean(
    'overwrite', False, 'If True, overwrite the existing visualizations.')


@script_utils.log_exception
def _generate_single_dataframe(full_name: str, dst_dir: str) -> None:
  """Save the generated dataframe HTML for the dataset in dst_dir.

  Args:
    full_name: Name of the dataset to build `dataset`, `dataset/config`.
    dst_dir: Destination where the dataset will be saved (as
      `dataset-config-version`)
  """
  dst_filename = full_name.replace('/', '-') + '.html'
  dst_path = os.path.join(dst_dir, dst_filename)
  # If the html already exists, skip the html generation
  if not FLAGS.overwrite and tf.io.gfile.exists(dst_path):
    logging.info(f'Skipping dataframe for {full_name} (already exists)')
    return

  logging.info(f'Generating dataframe for {full_name}...')
  # Load the dataset.
  builder_name, _, version = full_name.rpartition('/')
  builder = tfds.builder(f'{builder_name}:{version}')
  split_names = list(builder.info.splits.keys())
  if not split_names:
    logging.info(f'Dataset `{full_name}` not generated.')
    return
  elif 'train' in split_names:
    split = 'train'
  else:
    split = split_names[0]
  ds = builder.as_dataset(split=split, shuffle_files=False)

  if not tf.io.gfile.exists(dst_dir):
    tf.io.gfile.makedirs(dst_dir)
  try:
    df = tfds.as_dataframe(ds.take(10), builder.info)
  except Exception:  # pylint: disable=broad-except
    logging.info(f'Dataframe not supported for dataset `{full_name}`')
    return

  tf.io.write_file(dst_path, df._repr_html_())


def generate_dataframe(
    datasets: Optional[List[str]] = None,
    *,
    dst_dir: str,
) -> None:
  """Generate dataframe HTML for datasets.

  Args:
    datasets: List of all `dataset` names to generate. If None, dataframes
      for all available datasets will be generated.
    dst_dir: Directory where the dataframe is saved.
  """
  full_names = script_utils.get_full_names(datasets)
  generate_fn = functools.partial(
      _generate_single_dataframe, dst_dir=dst_dir)
  logging.info(f'Generate dataframes for {len(full_names)} builders')
  with multiprocessing.Pool(WORKER_COUNT_DATASETS) as tpool:
    tpool.map(generate_fn, full_names)


def main(_):
  """Main script."""
  datasets = FLAGS.datasets.split(',') if FLAGS.datasets else None
  generate_dataframe(datasets, dst_dir=FLAGS.dst_dir)


if __name__ == '__main__':
  flags.mark_flags_as_required(['dst_dir'])
  app.run(main)

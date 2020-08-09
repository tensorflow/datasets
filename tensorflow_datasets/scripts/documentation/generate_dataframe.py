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
import itertools
import multiprocessing
import os
import tempfile
import traceback
from typing import List, Optional

from absl import app
from absl import flags
from absl import logging

import matplotlib.pyplot as plt
from matplotlib.image import imsave

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core.visualization import visualizer


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


# pylint: disable=logging-format-interpolation,logging-not-lazy


def _log_exception(fn):
  """Logs the exceptions from a `ThreadPoolExecutor`."""

  @functools.wraps(fn)
  def decorated(*args, **kwargs):
    try:
      return fn(*args, **kwargs)
    except Exception:  # pylint: disable=broad-except
      err_str = traceback.format_exc()
      logging.error(f'Exception occurred for {args}, {kwargs}:\n' + err_str)
      raise

  return decorated


@_log_exception
def _generate_single_dataframe(full_name: str, dst_dir: str) -> None:
  """Save the generated dataframe HTML for the dataset in dst_dir.

  Args:
    full_name: Name of the dataset to build `dataset`, `dataset/config`.
    dst_dir: Destination where the dataset will be saved (as
      `dataset-config-version`)
  """
  dst = full_name.replace('/', '-')
  dst_filename = dst + '.html'
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

  # Add audio, image, and video to html
  audio_keys = visualizer.extract_keys(
      builder.info.features, features_lib.Audio)
  image_keys = visualizer.extract_keys(
      builder.info.features, features_lib.Image)
  video_keys = visualizer.extract_keys(
      builder.info.features, features_lib.Video)

  def generate_audio_html(audio_key, audio_idx, audio_arr, audio_rate):
    dst_audio_path = dst + '-' + audio_key + '-' + str(audio_idx) + '.wav'
    lazy_imports_lib.lazy_imports.scipy.io.wavfile.write(
        dst_audio_path, audio_rate, audio_arr)
    return '<audio src="' + dst_audio_path + '" controls type="audio/wav" />'

  def generate_image_html(image_key, image_idx, image_arr):
    dst_image_path = dst + '-' + image_key + '-' + str(image_idx) + '.png'
    lazy_imports_lib.lazy_imports.matplotlib.image.imsave(
        dst_image_path, image_arr)
    return '<img src="' + dst_image_path + '" width="100" />'

  def generate_video_html(video_key, video_idx, video_arr, audio_rate):
    dst_audio_path = dst + '-' + audio_key + '-' + str(audio_idx) + '.wav'
    lazy_imports_lib.lazy_imports.scipy.io.wavfile.write(
        dst_audio_path, audio_rate, audio_arr)
    return '<audio src="' + dst_audio_path + '" controls type="audio/wav" />'

  for idx in range(df.shape[0]):
    for key in audio_keys:
      df[key][idx] = generate_audio_html(
          key, idx, df[key][idx], builder.info.features[key].sample_rate)
    for key in image_keys:
      df[key][idx] = generate_image_html(key, idx, df[key][idx])






  # `savefig` do not support GCS, so first save the image locally.
  with tempfile.TemporaryDirectory() as tmp_dir:
    tmp_path = os.path.join(tmp_dir, dst_filename)
    figure.savefig(tmp_path)
    tf.io.gfile.copy(tmp_path, dst_path, overwrite=FLAGS.overwrite)
  plt.close(figure)


def _get_full_names(datasets: Optional[List[str]] = None) -> List[str]:
  """List all builder names `ds/version` and `ds/config/version` to generate.

  Args:
    datasets: List of datasets from which get the builder names.

  Returns:
    builder_names: The builder names.
  """
  if datasets is None:
    return tfds.core.registered.list_full_names(
        current_version_only=True,
    )
  else:
    builder_names = list(itertools.chain.from_iterable([
        tfds.core.registered.single_full_names(builder_name)
        for builder_name in datasets
    ]))
    return builder_names


def generate_visualization(
    datasets: Optional[List[str]] = None,
    *,
    dst_dir: str,
) -> None:
  """Generate Visualization for datasets.

  Args:
    datasets: List of all `dataset` names to generate. If None, visualization
      for all available datasets will be generated.
    dst_dir: Directory where saving the images.
  """
  full_names = _get_full_names(datasets)
  generate_fn = functools.partial(
      _generate_single_visualization, dst_dir=dst_dir)
  logging.info(f'Generate figures for {len(full_names)} builders')
  with multiprocessing.Pool(WORKER_COUNT_DATASETS) as tpool:
    tpool.map(generate_fn, full_names)


def main(_):
  """Main script."""
  datasets = FLAGS.datasets.split(',') if FLAGS.datasets else None
  generate_visualization(datasets, dst_dir=FLAGS.dst_dir)


if __name__ == '__main__':
  flags.mark_flags_as_required(['dst_dir'])
  app.run(main)

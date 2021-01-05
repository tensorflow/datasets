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

r"""Script which generates datasets figures.
"""

import functools
import os
import tempfile

from absl import flags

import matplotlib
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import script_utils

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'datasets', None,
    'Comma separated list of datasets to generates. None for all datasets.')
flags.DEFINE_string(
    'dst_dir', None, 'Destination dir to save the images.')
flags.DEFINE_boolean(
    'overwrite', False, 'If True, overwrite the existing visualizations.')


def _save_fig(dst_path: str, figure: matplotlib.figure.Figure) -> None:
  """Save the generated figures for the dataset in dst_dir."""
  # `savefig` do not support GCS, so first save the image locally.
  with tempfile.TemporaryDirectory() as tmp_dir:
    tmp_path = os.path.join(tmp_dir, 'tmp.png')
    figure.savefig(tmp_path)
    tf.io.gfile.copy(tmp_path, dst_path, overwrite=FLAGS.overwrite)
  plt.close(figure)


def main(_):
  """Main script."""
  datasets = FLAGS.datasets.split(',') if FLAGS.datasets else None
  generate_and_save_figure_fn = functools.partial(
      script_utils.generate_and_save_artifact,
      dst_dir=FLAGS.dst_dir or tfds.core.gcs_path('visualization/fig'),
      overwrite=FLAGS.overwrite,
      file_extension='.png',
      get_artifact_fn=tfds.show_examples,
      save_artifact_fn=_save_fig,
  )
  script_utils.multi_process_map(
      worker_fn=generate_and_save_figure_fn,
      datasets=datasets,
  )


if __name__ == '__main__':
  script_utils.multi_process_run(main)

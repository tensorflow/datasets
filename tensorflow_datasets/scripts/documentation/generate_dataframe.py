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

r"""Script which generates datasets dataframes HTML.

"""

import functools

from absl import app
from absl import flags
import pandas

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import script_utils

FLAGS = flags.FLAGS

flags.DEFINE_string(
    'datasets', None,
    'Comma separated list of datasets to generates. None for all datasets.')
flags.DEFINE_string(
    'dst_dir', None, 'Destination dir to save the dataframe html.')
flags.DEFINE_boolean(
    'overwrite', False, 'If True, overwrite the existing visualizations.')


def _save_html(dst_path: str, df: pandas.DataFrame) -> None:
  with tf.io.gfile.GFile(dst_path, 'w') as f:
    f.write(df._repr_html_())  # pylint: disable=protected-access


def main(_):
  """Main script."""
  datasets = FLAGS.datasets.split(',') if FLAGS.datasets else None
  generate_and_save_dataframe_fn = functools.partial(
      script_utils.generate_and_save_artifact,
      dst_dir=FLAGS.dst_dir or tfds.core.gcs_path('visualization/dataframe'),
      overwrite=FLAGS.overwrite,
      file_extension='.html',
      get_artifact_fn=tfds.as_dataframe,
      save_artifact_fn=_save_html,
  )
  script_utils.multi_thread_map(
      worker_fn=generate_and_save_dataframe_fn,
      datasets=datasets,
  )


if __name__ == '__main__':
  app.run(main)

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
"""Script to generate datasets figures and save them
  in docs/catalog/images/ directory.

Args:
  data_name: name of the dataset, for which figures to be generated.
"""

import os
from absl import app
from absl import flags
from concurrent import futures

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import registered

WORKER_COUNT_DATASETS = 200

FLAGS = flags.FLAGS
FIG_DIR = os.path.join('..', 'docs', 'catalog', 'images')
flags.DEFINE_string('dst_dir', tfds.core.get_tfds_path(FIG_DIR),
                    'Path to tensorflow_datasets/docs/catalog/images')

def generate_single_visualization(data_name):
    """Save the generated figures for the dataset in dst_dir.

    Args:
      data_name: name of the dataset with or without config for which
      generate figure.
    """
    print("Generating examples %s..." % data_name)
    builder = tfds.builder(data_name)
    split = list(builder.info.splits.keys())[0]
    data, data_info = tfds.load(data_name, split=split, with_info=True)

    if not tf.io.gfile.exists(FLAGS.dst_dir):
        tf.io.gfile.mkdir(FLAGS.dst_dir)
    suffix = data_name.replace("/", "-")
    data_path = os.path.join(FLAGS.dst_dir, suffix+ ".png")
    try:
        figure = tfds.show_examples(data_info, data)
        figure.savefig(data_path)
    except ValueError:
        print("Visualisation not supported for dataset `{}`".format(data_name))


def get_config_names(datasets=None):
    """List all dataset names with or without config.

    Args:
        datasets: list of datasets for which to generate figures.
              If None, then all available datasets will be used.

    Returns:
        List of dataset names with or without config.
    """
    dataset_config_list = []
    if not datasets:
        dataset_config_list = [x for x in registered.list_config_names()]
        return dataset_config_list
    else:
        for data_name in datasets:
          builder = tfds.builder(data_name)
          if builder.BUILDER_CONFIGS:
            for config in builder.BUILDER_CONFIGS:
                dataset_config_list.append(os.path.join(builder.name, config.name))
          else:
              dataset_config_list.append(builder.name)
    return dataset_config_list


def generate_visualization(datasets=None):
    """Generate Visualization for datasets.

    Args:
        datasets: list of datasets for which to generate figures.
              If None, then all available datasets will be used.
    """
    dataset_config_list = get_config_names(datasets)
    with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_DATASETS) as tpool:
        builder_examples = tpool.map(generate_single_visualization, dataset_config_list)

def main(_):
    """Main script."""
    generate_visualization()

if __name__ == "__main__":
    app.run(main)

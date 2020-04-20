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

import tensorflow as tf
import tensorflow_datasets as tfds

FIG_DIR = os.path.join('..', 'docs', 'catalog', 'images')
FULL_PATH = tfds.core.get_tfds_path(FIG_DIR)

def generate_vizz(data_name):
    """Save the generated figures for the dataset
    Args:
      data_name: name of the dataset
    """
    try:
        print("Generating examples...")
        builder = tfds.builder(data_name)
        builder.download_and_prepare()
        split = list(builder.info.splits.keys())[0]
        data, data_info = tfds.load(data_name, split=split, with_info=True)
        figure = tfds.show_examples(data_info, data)
        suffix = data_name.replace("\\", "/").replace("/", "_")
        data_path = os.path.join(FULL_PATH, suffix+ ".jpg")

        if not tf.io.gfile.exists(FULL_PATH):
            tf.io.gfile.mkdir(FULL_PATH)
        figure.savefig(data_path, optimize=True, quality=70)

    except ValueError:
        config_name = os.path.split(data_info.full_name)[-2]
        print("Visualisation not supported for dataset `{}`".format(config_name))


def main(_):
    """Main script."""
    generate_vizz([data_name])

if __name__ == "__main__":
    app.run(main)

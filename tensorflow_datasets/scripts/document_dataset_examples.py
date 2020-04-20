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
"""Script to update datasets catlog documents.

Args: data_name: name of the dataset whose document to be updated with example figures.

To run:
```
python -m tensorflow_datasets.scripts.document_dataset_examples

```
"""

import os
from absl import app
from absl import flags

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts import document_datasets
from tensorflow_datasets.scripts.generate_visualization import generate_vizz

FLAGS = flags.FLAGS
flags.DEFINE_string('tfds_dir', tfds.core.utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

# Datasets you want to test the script on.
DATASET_TO_TESTS = ['cats_vs_dogs', 'mnist', 'groove', 'emnist', 'imagewang', 'flic']

def doc_examples(data_name, path):
    """Write dataset documents with figures."""
    builder = tfds.builder(data_name)
    with open(os.path.join(path, f'{builder.name}.md'), "w") as file:
        doc_builder = document_datasets.document_single_builder(builder)
        file.write(doc_builder)

def dataset_configs_list():
    """Returns list of datasets with configs."""
    data_name_configs = []
    for data_name in DATASET_TO_TESTS:
        builder = tfds.builder(data_name)
        if builder.BUILDER_CONFIGS:
            for config in builder.BUILDER_CONFIGS:
                data_name_configs.append(os.path.join(builder.name, config.name))
        else:
            data_name_configs.append(builder.name)
    return data_name_configs

def main(_):
    """Main script."""
    doc_dir = os.path.join("..", "docs", "catalog")
    doc_full_path = os.path.join(FLAGS.tfds_dir, doc_dir)
    data_name_configs = dataset_configs_list()
    # Generate examples/figures for datasets.
    for data_name_config in data_name_configs:
        generate_vizz(data_name_config)
    # Document datasets with generated figures.
    for data_name in DATASET_TO_TESTS:
        doc_examples(data_name, doc_full_path)

if __name__ == "__main__":
    app.run(main)

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
r"""Generate doc for datasets.

Instructions:

```
python tensorflow_datasets/scripts/freeze_dataset_version.py
```


"""

import os

from absl import app
from absl import flags

import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.document_datasets import document_single_builder


FLAGS = flags.FLAGS

flags.DEFINE_string('tfds_dir', tfds.core.utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')

DATASET_TO_TESTS = ['scientific_papers', 'waymo_open_dataset']

def main(_):
  catalog_dir = tfds.core.get_tfds_path('../docs/catalog/')

  for ds_name in DATASET_TO_TESTS:
    builder = tfds.builder(ds_name)
    doc_builder = document_single_builder(builder)
    dataset_doc_path = os.path.join(catalog_dir, ds_name + ".md")
    with tf.io.gfile.GFile(dataset_doc_path, 'w') as f:
      f.write(doc_builder)

if __name__ == '__main__':
  app.run(main)

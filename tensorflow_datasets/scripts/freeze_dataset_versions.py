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
r"""Update list of all available datasets.

Instructions:

```
python tensorflow_datasets/scripts/freeze_dataset_version.py
```
"""

import os
import json

from absl import app

import tensorflow.compat.v2 as tf
gfile = tf.io.gfile
del tf

import tensorflow_datasets as tfds\

_STABLE_VERSIONS_FILEPATH = os.path.join(tfds.core.utils.tfds_dir(), 
    "../docs/stable_versions.txt")

def main(_):
  registered_names = tfds.core.registered.list_full_names()
  with gfile.GFile(_STABLE_VERSIONS_FILEPATH, "w") as file:
    json.dump(registered_names, file)

if __name__ == '__main__':
  app.run(main)

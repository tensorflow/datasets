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

r"""Dump the list of all registered datasets/config/version in a `.txt` file.

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

FLAGS = flags.FLAGS

flags.DEFINE_string('tfds_dir', tfds.core.utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')


def main(_):
  version_path = os.path.join(FLAGS.tfds_dir, 'stable_versions.txt')
  registered_names = tfds.core.registered.list_full_names()
  with tf.io.gfile.GFile(version_path, 'w') as f:
    f.write('\n'.join(registered_names))
  print(f'{len(registered_names)} datasets versions written.')


if __name__ == '__main__':
  app.run(main)

# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

r"""Script to call download_and_prepare on DatasetBuilder.

This is just a standalone script to generate a specific dataset. This can be
used if you don't want to separate download/generation of dataset from acual
usage.

By default, the dataset is generated in the default location
(~/tensorflow_datasets), which the same as when calling `tfds.load()`.
You can overwrite the dataset location with `--data_dir` and the cache location
with `--cache_dir`.

Instructions:
```
python -m tensorflow_datasets.scripts.download_and_prepare \
  --dataset_name=cifar10
```


"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pdb

import tensorflow as tf
import tensorflow_datasets as tfds
import termcolor

flags = tf.flags
FLAGS = flags.FLAGS

DEFAULT_DATA_DIR = os.path.expanduser(os.path.join("~", "tensorflow_datasets"))

flags.DEFINE_string("dataset_name", None, "Registered name of DatasetBuilder")
flags.DEFINE_string("data_dir", DEFAULT_DATA_DIR, "Were to place the data.")
flags.DEFINE_string("download_dir", None, "Where to place downloads.")
flags.DEFINE_string("extract_dir", None, "Where to extract files.")
flags.DEFINE_string(
    "manual_dir", None,
    "Directory where dataset have manually been downloaded / extracted.")
flags.DEFINE_boolean("debug", False,
                     "If True, will drop into debugger after generation")
flags.DEFINE_boolean("compute_stats", True,
                     "If True, will compute stats after generation")


def main(_):
  builder = tfds.builder(FLAGS.dataset_name, data_dir=FLAGS.data_dir)
  builder.download_and_prepare(download_dir=FLAGS.download_dir,
                               extract_dir=FLAGS.extract_dir,
                               manual_dir=FLAGS.manual_dir,
                               compute_stats=FLAGS.compute_stats)
  termcolor.cprint(str(builder.info.as_proto), attrs=["bold"])

  if FLAGS.debug:
    dataset = builder.as_dataset(split=tfds.Split.TRAIN)
    iterator = tf.contrib.eager.Iterator(dataset)
    pdb.set_trace()
    del iterator
    return


if __name__ == "__main__":
  flags.mark_flags_as_required(["dataset_name"])
  tf.enable_eager_execution()
  tf.app.run()

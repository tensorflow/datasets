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

Standalone script to generate specific dataset(s). This can be
used if you want to separate download/generation of dataset from acual usage.

By default, the dataset is generated in the default location
(~/tensorflow_datasets), which the same as when calling `tfds.load()`.

Instructions:
```
python -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=cifar10
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
BUILDERS = ",".join(tfds.list_builders())


DEFAULT_DATA_DIR = os.path.expanduser(os.path.join("~", "tensorflow_datasets"))

flags.DEFINE_string("datasets", BUILDERS,
                    "Comma separated list of datasets to build, defaults to all"
                    "registered builders.")
flags.DEFINE_string("exclude_datasets", "",
                    "Comma separated list of datasets to exclude,"
                    "(no download, no prepare).")

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



def download_and_prepare(builder, dataset_name, config_name):
  """Generate data for a given dataset."""
  print("download_and_prepare for dataset %s config %s ..." % (dataset_name,
                                                               config_name))
  # TODO(b/116270825): Add flag to force extraction / preparation.
  mode = tfds.download.GenerateMode.REUSE_DATASET_IF_EXISTS
  config = tfds.download.DownloadConfig(
      extract_dir=FLAGS.extract_dir,
      manual_dir=FLAGS.manual_dir,
      compute_stats=FLAGS.compute_stats,
      download_mode=mode)

  builder.download_and_prepare(
      download_dir=FLAGS.download_dir,
      download_config=config)
  termcolor.cprint(str(builder.info.as_proto), attrs=["bold"])

  if FLAGS.debug:
    dataset = builder.as_dataset(split=tfds.Split.TRAIN)
    iterator = tf.contrib.eager.Iterator(dataset)
    item = next(iterator)
    print("'item' is a single record. Use print(next(iterator)) to see more.")
    pdb.set_trace()
    del iterator, item



def main(_):
  datasets_to_build = (
      set(FLAGS.datasets.split(",")) -
      set(FLAGS.exclude_datasets.split(",")))
  tf.logging.info("Running download_and_prepare for datasets:\n%s",
                  "\n".join(datasets_to_build))
  builders = {
      name: tfds.builder(name, data_dir=FLAGS.data_dir)
      for name in datasets_to_build
  }

  for name, builder in builders.items():
    if builder.BUILDER_CONFIGS and "/" not in name:
      # If builder has multiple configs, and no particular config was
      # requested, then compute all.
      for config in builder.BUILDER_CONFIGS:
        builder_for_config = tfds.builder(
            builder.name, data_dir=FLAGS.data_dir, config=config)
        download_and_prepare(builder_for_config, builder.name, config.name)
    else:
      # If there is a slash in the name, then user requested a specific
      # dataset configuration.
      download_and_prepare(builder, builder.name,
                           name.split("/", 1)[1] if "/" in name else "")


if __name__ == "__main__":
  tf.enable_eager_execution()
  tf.app.run()

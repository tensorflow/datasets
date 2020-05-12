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
r"""Script to call download_and_prepare on DatasetBuilder.

Standalone script to generate specific dataset(s). This can be
used if you want to separate download/generation of dataset from actual usage.

By default, the dataset is generated in the default location
(~/tensorflow_datasets), which the same as when calling `tfds.load()`.

Instructions:

```
python -m tensorflow_datasets.scripts.download_and_prepare \
  --datasets=cifar10
```

If you have your dataset defined outside of `tensorflow_datasets`, use
`--module_import="path.to.my.dataset_module"` to have your Python module
containing your `DatasetBuilder` definition imported.


"""

import importlib
import os
import pdb
import time

from absl import app
from absl import flags
from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
import termcolor


FLAGS = flags.FLAGS

DEFAULT_DATA_DIR = os.path.expanduser(os.path.join("~", "tensorflow_datasets"))

flags.DEFINE_string("datasets", "",
                    "Comma separated list of datasets to build, defaults to all"
                    "registered builders.")
flags.DEFINE_string("exclude_datasets", "",
                    "Comma separated list of datasets to exclude,"
                    "(no download, no prepare).")
flags.DEFINE_multi_string(
    "module_import", None,
    "Modules to import. Use this when your DatasetBuilder is defined outside "
    "of tensorflow_datasets so that it is registered. Multiple imports can "
    "be passed by calling the flag multiple times, or using coma separated "
    "values.")
flags.DEFINE_integer(
    "builder_config_id", None,
    "If given 1 dataset with BUILDER_CONFIGS, id of config to build.")
flags.DEFINE_boolean(
    "experimental_latest_version", False,
    "Set to true to builder the latest version available, even if not default.")

flags.DEFINE_string("data_dir", DEFAULT_DATA_DIR, "Where to place the data.")
flags.DEFINE_string("download_dir", None, "Where to place downloads.")
flags.DEFINE_string("extract_dir", None, "Where to extract files.")
flags.DEFINE_string(
    "manual_dir", None,
    "Directory where dataset have manually been downloaded / extracted.")
flags.DEFINE_string("checksums_dir", None,
                    "For external datasets, specify the location of the "
                    "dataset checksums.")

flags.DEFINE_boolean(
    "add_name_to_manual_dir", False, "If true, append the dataset name to the "
    "`manual_dir`")

default_compute_stats = tfds.download.ComputeStatsMode.AUTO
flags.DEFINE_enum(
    "compute_stats",
    default_compute_stats.value,
    [e.value for e in tfds.download.ComputeStatsMode],
    "Whether to compute or not the dynamic statistics.")
flags.DEFINE_integer(
    "max_examples_per_split", None,
    "optional max number of examples to write into each split (for testing).")

# Beam flags
flags.DEFINE_list(
    "beam_pipeline_options", [],
    "A (comma-separated) list of flags to pass to `PipelineOptions` when "
    "preparing with Apache Beam. Example: "
    "`--beam_pipeline_options=job_name=my-job,project=my-project`")


# Development flags
flags.DEFINE_boolean("register_checksums", False,
                     "If True, store size and checksum of downloaded files.")
flags.DEFINE_boolean(
    "force_checksums_validation",
    False, "If True, raise an error if the checksums are not found.")

# Debug flags
flags.DEFINE_boolean("debug", False,
                     "If True, will drop into debugger after data generation")
flags.DEFINE_boolean("debug_start", False,
                     "If True, will drop into debugger on startup")
flags.DEFINE_boolean("sleep_start", False,
                     "If True, will sleep on startup; useful for ssh")
flags.DEFINE_boolean("disable_tqdm", False, "If True, disable tqdm.")


def download_config():
  return tfds.download.DownloadConfig(
      extract_dir=FLAGS.extract_dir,
      manual_dir=FLAGS.manual_dir,
      compute_stats=FLAGS.compute_stats,
      # TODO(b/116270825): Add flag to force extraction / preparation.
      download_mode=tfds.download.GenerateMode.REUSE_DATASET_IF_EXISTS,
      max_examples_per_split=FLAGS.max_examples_per_split,
      register_checksums=FLAGS.register_checksums,
      force_checksums_validation=FLAGS.force_checksums_validation,
  )


def download_and_prepare(builder):
  """Generate data for a given dataset."""
  logging.info("download_and_prepare for dataset %s...", builder.info.full_name)

  dl_config = download_config()

  if isinstance(builder, tfds.core.BeamBasedBuilder):
    beam = tfds.core.lazy_imports.apache_beam
    # TODO(b/129149715): Restore compute stats. Currently skipped because not
    # beam supported.
    dl_config.compute_stats = tfds.download.ComputeStatsMode.SKIP
    dl_config.beam_options = beam.options.pipeline_options.PipelineOptions(
        flags=["--%s" % opt for opt in FLAGS.beam_pipeline_options])

  if FLAGS.add_name_to_manual_dir:
    dl_config.manual_dir = os.path.join(dl_config.manual_dir, builder.name)

  builder.download_and_prepare(
      download_dir=FLAGS.download_dir,
      download_config=dl_config,
  )
  termcolor.cprint(str(builder.info.as_proto), attrs=["bold"])

  if FLAGS.debug:
    dataset = builder.as_dataset(split=tfds.Split.TRAIN)
    pdb.set_trace()
    del dataset


def import_modules(modules):
  for module in modules:
    for m in module.split(","):  # Allow to pass imports as coma separated vals.
      importlib.import_module(m)


def main(_):
  if FLAGS.module_import:
    import_modules(FLAGS.module_import)

  if FLAGS.debug_start:
    pdb.set_trace()
  if FLAGS.sleep_start:
    time.sleep(60*60*3)

  if FLAGS.disable_tqdm:
    logging.info("Disabling tqdm.")
    tfds.disable_progress_bar()

  if FLAGS.checksums_dir:
    tfds.download.add_checksums_dir(FLAGS.checksums_dir)

  datasets_to_build = set(FLAGS.datasets and FLAGS.datasets.split(",")
                          or tfds.list_builders())
  datasets_to_build -= set(FLAGS.exclude_datasets.split(","))

  # Only pass the version kwargs when required. Otherwise, `version=None`
  # overwrite the version parsed from the name.
  # `tfds.builder('my_dataset:1.2.0', version=None)`
  if FLAGS.experimental_latest_version:
    version_kwarg = {"version": "experimental_latest"}
  else:
    version_kwarg = {}

  logging.info("Running download_and_prepare for dataset(s):\n%s",
               "\n".join(datasets_to_build))
  builders = {
      name: tfds.builder(name, data_dir=FLAGS.data_dir, **version_kwarg)
      for name in datasets_to_build
  }

  if FLAGS.builder_config_id is not None:
    # Requesting a single config of a single dataset
    if len(builders) > 1:
      raise ValueError(
          "--builder_config_id can only be used when building a single dataset")
    builder = builders[list(builders.keys())[0]]
    if not builder.BUILDER_CONFIGS:
      raise ValueError(
          "--builder_config_id can only be used with datasets with configs")
    config = builder.BUILDER_CONFIGS[FLAGS.builder_config_id]
    logging.info("Running download_and_prepare for config: %s", config.name)
    builder_for_config = tfds.builder(
        builder.name, data_dir=FLAGS.data_dir, config=config, **version_kwarg)
    download_and_prepare(builder_for_config)
  else:
    for name, builder in builders.items():
      if builder.BUILDER_CONFIGS and "/" not in name:
        # If builder has multiple configs, and no particular config was
        # requested, then compute all.
        for config in builder.BUILDER_CONFIGS:
          builder_for_config = tfds.builder(
              builder.name,
              data_dir=FLAGS.data_dir,
              config=config,
              **version_kwarg)
          download_and_prepare(builder_for_config)
      else:
        # If there is a slash in the name, then user requested a specific
        # dataset configuration.
        download_and_prepare(builder)


if __name__ == "__main__":
  tf.enable_v2_behavior()
  app.run(main)

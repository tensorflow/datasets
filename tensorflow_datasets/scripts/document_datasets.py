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
"""Script to document datasets.

To test:
python -m tensorflow_datasets.scripts.document_datasets

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
from concurrent import futures
import os

from absl import app
import mako.lookup
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils import py_utils

WORKER_COUNT_DATASETS = 200
WORKER_COUNT_CONFIGS = 50

BASE_URL = "https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets"

# WmtTranslate: The raw wmt can only be instantiated with the config kwargs
# TODO(tfds): Document image_label_folder datasets in a separate section
BUILDER_BLACKLIST = ["wmt_translate"]


@py_utils.memoize()
def get_mako_template(tmpl_name):
  """Returns mako.lookup.Template object to use to render documentation.

  Args:
    tmpl_name: string, name of template to load.

  Returns:
    mako 'Template' instance that can be rendered.
  """
  tmpl_path = py_utils.get_tfds_path("scripts/templates/%s.mako.md" % tmpl_name)
  with tf.io.gfile.GFile(tmpl_path, "r") as tmpl_f:
    tmpl_content = tmpl_f.read()
  return mako.lookup.Template(tmpl_content, default_filters=["str", "trim"])


def cls_url(module_file):
  if module_file.endswith("pyc"):
    module_file = module_file[:-1]
  path = os.path.relpath(module_file, py_utils.tfds_dir())
  return os.path.join(BASE_URL, path)


def document_single_builder(builder):
  """Doc string for a single builder, with or without configs."""
  print("Document builder %s..." % builder.name)
  get_config_builder = lambda config: tfds.builder(builder.name, config=config)
  config_builders = []
  if builder.builder_configs:
    with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_CONFIGS) as tpool:
      config_builders = list(
          tpool.map(get_config_builder, builder.BUILDER_CONFIGS))
  tmpl = get_mako_template("dataset")
  out_str = tmpl.render_unicode(
      builder=builder,
      config_builders=config_builders,
  ).strip()
  schema_org_tmpl = get_mako_template("schema_org")
  schema_org_out_str = schema_org_tmpl.render_unicode(
      builder=builder,
      config_builders=config_builders,
  ).strip()
  out_str = schema_org_out_str + "\n" + out_str
  return out_str


def make_module_to_builder_dict(datasets=None):
  """Get all builders organized by module in nested dicts."""
  # pylint: disable=g-long-lambda
  # dict to hold tfds->image->mnist->[builders]
  module_to_builder = collections.defaultdict(
      lambda: collections.defaultdict(
          lambda: collections.defaultdict(list)))
  # pylint: enable=g-long-lambda

  if not datasets:
    datasets = [
        name for name in tfds.list_builders() if name not in BUILDER_BLACKLIST
    ]
  print("Creating the vanilla builders for %s datasets..." % len(datasets))
  with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_DATASETS) as tpool:
    builders = tpool.map(tfds.builder, datasets)
  print("Vanilla builders built, constructing module_to_builder dict...")

  for builder in builders:
    module_name = builder.__class__.__module__
    modules = module_name.split(".")
    if "testing" in modules:
      continue

    current_mod_ctr = module_to_builder
    for mod in modules:
      current_mod_ctr = current_mod_ctr[mod]
    current_mod_ctr.append(builder)

  module_to_builder = module_to_builder["tensorflow_datasets"]
  return module_to_builder


def dataset_docs_str(datasets=None):
  """Create dataset documentation string for given datasets.

  Args:
    datasets: list of datasets for which to create documentation.
              If None, then all available datasets will be used.

  Returns:
    - overview document
    - a dictionary of sections. Each dataset in a section is represented by a
    tuple (dataset_name, is_manual_dataset, string describing the datasets
    (in the MarkDown format))
  """

  print("Retrieving the list of builders...")
  module_to_builder = make_module_to_builder_dict(datasets)
  sections = sorted(list(module_to_builder.keys()))
  section_docs = collections.defaultdict(list)

  for section in sections:
    builders = tf.nest.flatten(module_to_builder[section])
    builders = sorted(builders, key=lambda b: b.name)
    unused_ = get_mako_template("dataset")  # To warm cache.
    with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_DATASETS) as tpool:
      builder_docs = tpool.map(document_single_builder, builders)
    builder_docs = [(builder.name, builder.MANUAL_DOWNLOAD_INSTRUCTIONS,
                     builder_doc)
                    for (builder, builder_doc) in zip(builders, builder_docs)]
    section_docs[section] = builder_docs
  tmpl = get_mako_template("catalog_overview")
  catalog_overview = tmpl.render_unicode().lstrip()
  return [catalog_overview, section_docs]


def main(_):
  print(dataset_docs_str())


if __name__ == "__main__":
  app.run(main)

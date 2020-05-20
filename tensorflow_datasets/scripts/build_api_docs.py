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
"""generates api_docs for tensorflow_datasets."""
import os

from absl import app
from absl import flags

import tensorflow_datasets as tfds
from tensorflow_datasets import testing

from tensorflow_docs.api_generator import generate_lib
import yaml

FLAGS = flags.FLAGS

flags.DEFINE_string("output_dir", "/tmp/datasets_api",
                    "Where to output the docs")
flags.DEFINE_string(
    "code_url_prefix",
    "https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/",
    "The url prefix for links to code.")

flags.DEFINE_bool("search_hints", True,
                  "Include metadata search hints in the generated files")

flags.DEFINE_string("site_path", "datasets/api_docs/python",
                    "Path prefix in the _toc.yaml")

MOVES = [("tfds/features/text.md", "tfds/features/text_lib.md")]


def execute(output_dir, code_url_prefix, search_hints, site_path):
  """Builds API docs for tensorflow_datasets."""
  # Internally, tfds.testing defaults to None. Fill it in here so that we get
  # documentation.
  tfds.testing = testing
  doc_generator = generate_lib.DocGenerator(
      root_title="TensorFlow Datasets",
      py_modules=[("tfds", tfds)],
      base_dir=os.path.dirname(tfds.__file__),
      search_hints=search_hints,
      code_url_prefix=code_url_prefix,
      site_path=site_path)

  doc_generator.build(output_dir)

  new_redirects = []
  for before, after in MOVES:
    old_path = os.path.join(output_dir, before)
    new_path = os.path.join(output_dir, after)
    os.rename(old_path, new_path)

    new_redirects.append({
        "from":
            os.path.join("/datasets/api_docs/python/",
                         os.path.splitext(before)[0]),
        "to":
            os.path.join("/datasets/api_docs/python/",
                         os.path.splitext(after)[0])
    })

  redirect_path = os.path.join(output_dir, "_redirects.yaml")
  with open(redirect_path) as f:
    redirect_content = yaml.load(f)
  redirect_content["redirects"].extend(new_redirects)
  with open(redirect_path, "w") as f:
    yaml.dump(redirect_content, f, default_flow_style=False)


def main(unused_argv):
  execute(FLAGS.output_dir, FLAGS.code_url_prefix, FLAGS.search_hints,
          FLAGS.site_path)


if __name__ == "__main__":
  app.run(main)

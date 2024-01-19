# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""generates api_docs for tensorflow_datasets."""
import os

from absl import app
from absl import flags
from absl import logging

import tensorflow_datasets as tfds
# Testing is lazily imported, so we first force its import.
from tensorflow_datasets.testing import *  # pylint: disable=wildcard-import
from tensorflow_docs.api_generator import generate_lib

from tensorflow.tools.docs import doc_controls  # pylint: disable=g-direct-tensorflow-import

# Force the definition of all documentation decorators declared in
# third_party/py/tensorflow_datasets/core/utils/docs.py to TensorFlow decorators
try:
  tfds.core.utils.docs.deprecated = doc_controls.set_deprecated
  tfds.core.utils.docs.doc_private = doc_controls.doc_private
  tfds.core.utils.docs.do_not_doc = doc_controls.do_not_generate_docs
  # Same as `do_not_doc`, but also applied to children
  tfds.core.utils.docs.do_not_doc_inheritable = (
      doc_controls.do_not_doc_inheritable
  )
  # Document the parent, but not the children
  tfds.core.utils.docs.do_not_doc_in_subclasses = (
      doc_controls.do_not_doc_in_subclasses
  )
except AttributeError:
  logging.info("Could not set TensorFlow documentation decorators.")

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "output_dir", "/tmp/datasets_api", "Where to output the docs"
)
flags.DEFINE_string(
    "code_url_prefix",
    "https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/",
    "The url prefix for links to code.",
)

flags.DEFINE_bool(
    "search_hints", True, "Include metadata search hints in the generated files"
)

flags.DEFINE_string(
    "site_path", "datasets/api_docs/python", "Path prefix in the _toc.yaml"
)


def execute(output_dir, code_url_prefix, search_hints, site_path):
  """Builds API docs for tensorflow_datasets."""
  doc_generator = generate_lib.DocGenerator(
      root_title="TensorFlow Datasets",
      py_modules=[("tfds", tfds)],
      base_dir=os.path.dirname(tfds.__file__),
      search_hints=search_hints,
      code_url_prefix=code_url_prefix,
      site_path=site_path,
  )

  doc_generator.build(output_dir)


def main(unused_argv):
  execute(
      FLAGS.output_dir,
      FLAGS.code_url_prefix,
      FLAGS.search_hints,
      FLAGS.site_path,
  )


if __name__ == "__main__":
  app.run(main)

# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

# pylint: disable=line-too-long
"""Script to document datasets.

python -m tensorflow_datasets.scripts.create_new_dataset --name dataset_name --type dataset_type

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils


_LICENCE = """\
# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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
""" + "\n"

_FUTURE_IMPORTS = """\
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function\n
"""

_DATASET_DEFAULT_IMPORTS = """\
import tensorflow_datasets as tfds\n
"""

_DATASET_TEST_DEFAULTS_IMPORTS = """
\"""Tests for {dataset_name} dataset.\"""

from tensorflow_datasets import testing
from tensorflow_datasets.{dataset_type} import {dataset_name}\n
"""

_CITATION = """\
# {TODO}
_CITATION = \"""
\"""\n
"""

_DESCRIPTION = """\
# {TODO}
_DESCRIPTION = \"""
\"""\n
"""

_DATASET_DEFAULTS = """\
class {dataset_name}(tfds.core.GeneratorBasedBuilder):
  \"""{TODO}Short description of my dataset.\"""

  # {TODO} Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self): 
  # {TODO} Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        # This is the features your dataset like images, labels ...
        features=tfds.features.FeaturesDict(),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        urls=[],
        citation=_CITATION,
    )
    pass
  {dataset_extra}
  def _split_generators(self, dl_manager):
    # {TODO} Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    pass

  def _generate_examples(self):
    # {TODO} Yields examples from the dataset
    pass\n
"""

_DATASET_EXTRA = """\
  # {TODO}
  def _vocab_text_gen(self, archive):
    pass \n
"""

_DATASET_TEST_DEFAULTS = """\
class {dataset_name_capital}(testing.DatasetBuilderTestCase):
  # {TODO}
  DATASET_CLASS = {dataset_name}.{dataset_name_capital}
""" + 5 * '\n' + """
if __name__ == "__main__":
  testing.test_main()\n
"""

_CHECKSUM_FILE = """\
# {TODO} Add a checksums for file. (url, size, checksum)
"""

_TFDS_DIR = py_utils.tfds_dir()

# pylint: disable=missing-docstring
def get_args():
  types = ['image', 'video', 'audio', 'text', 'structured', 'translate']
  parser = argparse.ArgumentParser(description="Generate-Dataset")

  parser.add_argument("-n", "--name", dest="dataset_name",
                      help="Dataset Name", required=True)
  parser.add_argument("-t", "--type", dest="dataset_type",
                      help="Dataset Type (audio, image, text"
                           ", video, structured, translate)", required=True)
  args = parser.parse_args()

  if args.dataset_type not in types:
    raise NameError('This type not found. Our types: ' +
                    (', '.join(str(x) for x in types)) + '.')
  return args

# pylint: disable=missing-docstring
def create_dataset_file(file_path, dataset_name, dataset_type):
  if dataset_type in ['image', 'video']:
    context = (_LICENCE + _FUTURE_IMPORTS + _DATASET_DEFAULT_IMPORTS + _CITATION + _DESCRIPTION +
               _DATASET_DEFAULTS).format(dataset_name=dataset_name.capitalize(),
                                         TODO="TODO({})".format(dataset_name),
                                         dataset_extra='')
  elif dataset_type in ['audio', 'text', 'structured', 'translate']:
    context = (_LICENCE + _FUTURE_IMPORTS + _DATASET_DEFAULT_IMPORTS + _CITATION + _DESCRIPTION +
               _DATASET_DEFAULTS).format(dataset_name=dataset_name.capitalize(),
                                         TODO="TODO({})".format(dataset_name),
                                         dataset_extra=_DATASET_EXTRA)
  else:
    raise NameError('Dataset type not valid!')

  with tf.io.gfile.GFile(file_path + '.py', "w") as f:
    f.write(context)


def add_the_init(dataset_name, dataset_type):
  init_file = os.path.join(_TFDS_DIR, dataset_type, "__init__.py")
  context = "from tensorflow_datasets." + dataset_type + '.' + dataset_name + " import " + \
            dataset_name.capitalize() + " # {} Place in the right place by letter order\n" \
              .format("TODO({})".format(dataset_name))
  with tf.io.gfile.GFile(init_file, "a") as f:
    f.write(context)


def create_dataset_test_file(test_path, dataset_name, dataset_type):
  context = (_LICENCE + _FUTURE_IMPORTS + _DATASET_TEST_DEFAULTS_IMPORTS +
             _DATASET_TEST_DEFAULTS).format(TODO="TODO({})".format(dataset_name),
                                            dataset_name=dataset_name,
                                            dataset_type=dataset_type,
                                            dataset_name_capital=dataset_name.capitalize())
  with tf.io.gfile.GFile(test_path + '_test.py', "w") as f:
    f.write(context)


def create_fake_examples_dir(dirname):
  try:
    tf.gfile.MkDir(dirname)
  except tf.errors.OpError:
    raise NameError('Dataset name not valid! Please check fake examples.')


def create_checksum_file(checksum_dir, dataset_name):
  with tf.io.gfile.GFile(checksum_dir + '.txt', "w") as f:
    f.write(_CHECKSUM_FILE.format(TODO="TODO({})".format(dataset_name)))


def main():
  args = get_args()
  dataset_name = args.dataset_name
  dataset_type = args.dataset_type
  dataset_file_path = os.path.join(_TFDS_DIR, dataset_type, dataset_name)
  fake_examples_dir = os.path.join(_TFDS_DIR, "testing", "test_data", "fake_examples", dataset_name)
  checksum_dir = os.path.join(_TFDS_DIR, 'url_checksums', dataset_name)

  create_dataset_file(dataset_file_path, dataset_name, dataset_type)
  add_the_init(dataset_name, dataset_type)
  create_dataset_test_file(dataset_file_path, dataset_name, dataset_type)
  create_fake_examples_dir(fake_examples_dir)
  create_checksum_file(checksum_dir, dataset_name)

  print('You can start with searching TODO({}).\n'
        'Please check this '
        '`https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md`'
        'for details.'.format(dataset_name))


if __name__ == '__main__':
  main()
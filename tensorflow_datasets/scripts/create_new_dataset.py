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

r"""Generate the minimal source code for a new dataset.

python -m tensorflow_datasets.scripts.create_new_dataset \
  --dataset dataset_name \
  --type dataset_type

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import app
from absl import flags

from tensorflow.io import gfile
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import py_utils

FLAGS = flags.FLAGS

_DATASET_TYPE = ['image', 'video', 'audio', 'text', 'structured', 'translate']

flags.DEFINE_string('tfds_dir', None, 'Root directory of tfds (auto-computed)')
flags.DEFINE_string('dataset', None, 'Dataset name')
flags.DEFINE_enum('type', None, _DATASET_TYPE, 'Dataset type')


_HEADER = """\
\"""{TODO}: Add a description here.\"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

"""

_DATASET_DEFAULT_IMPORTS = """\
import tensorflow_datasets as tfds\n
"""

_DATASET_TEST_DEFAULTS_IMPORTS = """\
from tensorflow_datasets import testing
from tensorflow_datasets.{dataset_type} import {dataset_name}

"""

_CITATION = """\
# {TODO}: BibTeX citation
_CITATION = \"""
\"""\n
"""

_DESCRIPTION = """\
# {TODO}:
_DESCRIPTION = \"""
\"""\n
"""

_DATASET_DEFAULTS = """\

class {dataset_cls}(tfds.core.GeneratorBasedBuilder):
  \"""{TODO}: Short description of my dataset.\"""

  # {TODO}: Set up version.
  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    # {TODO}: Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({{
            # These are the features of your dataset like images, labels ...
        }}),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=(),
        # Homepage of the dataset for documentation
        urls=[],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    \"""Returns SplitGenerators.\"""
    # {TODO}: Downloads the data and defines the splits
    # dl_manager is a tfds.download.DownloadManager that can be used to
    # download and extract URLs
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # {TODO}: Tune the number of shards such that each shard
            # is < 4 GB.
            num_shards=10,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={{}},
        ),
    ]

  def _generate_examples(self):
    \"""Yields examples.\"""
    # {TODO}: Yields examples from the dataset
    yield {{}}\n
"""

_DATASET_TEST_DEFAULTS = """\

class {dataset_cls}Test(testing.DatasetBuilderTestCase):
  # {TODO}:
  DATASET_CLASS = {dataset_name}.{dataset_cls}
  SPLITS = {{
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }}

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({{'some_key': 'http://a.org/out.txt', ...}})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {{'some_key': 'output_file1.txt', ...}}


if __name__ == "__main__":
  testing.test_main()

"""

_CHECKSUM_FILE = """\
# {TODO}: If your dataset downloads files, then the checksums will be
# automatically added here when running the download_and_prepare script
# with --register_checksums.
"""


def create_dataset_file(root_dir, data):
  """Create a new dataset from a template."""
  file_path = os.path.join(root_dir, '{dataset_type}', '{dataset_name}.py')
  context = (
      _HEADER + _DATASET_DEFAULT_IMPORTS + _CITATION
      + _DESCRIPTION + _DATASET_DEFAULTS
  )

  with gfile.GFile(file_path.format(**data), 'w') as f:
    f.write(context.format(**data))


def add_the_init(root_dir, data):
  """Append the new dataset file to the __init__.py."""
  init_file = os.path.join(root_dir, '{dataset_type}', '__init__.py')
  context = (
      'from tensorflow_datasets.{dataset_type}.{dataset_name} import '
      '{dataset_cls}  # {TODO} Sort alphabetically\n'
  )
  with gfile.GFile(init_file.format(**data), 'a') as f:
    f.write(context.format(**data))


def create_dataset_test_file(root_dir, data):
  """Create the test file associated with the dataset."""
  file_path = os.path.join(root_dir, '{dataset_type}', '{dataset_name}_test.py')
  context = (
      _HEADER + _DATASET_TEST_DEFAULTS_IMPORTS +
      _DATASET_TEST_DEFAULTS)

  with gfile.GFile(file_path.format(**data), 'w') as f:
    f.write(context.format(**data))


def create_fake_data(root_dir, data):
  fake_examples_dir = os.path.join(
      root_dir, 'testing', 'test_data', 'fake_examples', '{dataset_name}')
  fake_examples_dir = fake_examples_dir.format(**data)
  gfile.makedirs(fake_examples_dir)

  fake_path = os.path.join(
      fake_examples_dir, 'TODO-add_fake_data_in_this_directory.txt')
  with gfile.GFile(fake_path, 'w') as f:
    f.write('{TODO}: Add fake data in this directory'.format(**data))


def create_checksum_file(root_dir, data):
  checksum_path = os.path.join(root_dir, 'url_checksums', '{dataset_name}.txt')
  with gfile.GFile(checksum_path.format(**data), 'w') as f:
    f.write(_CHECKSUM_FILE.format(**data))


def main(_):
  dataset_name = FLAGS.dataset
  dataset_type = FLAGS.type
  root_dir = FLAGS.tfds_dir
  if not root_dir:
    root_dir = py_utils.tfds_dir()

  data = dict(
      dataset_name=dataset_name,
      dataset_type=dataset_type,
      dataset_cls=naming.snake_to_camelcase(dataset_name),
      TODO='TODO({})'.format(dataset_name),
  )

  create_dataset_file(root_dir, data)
  add_the_init(root_dir, data)
  create_dataset_test_file(root_dir, data)
  create_fake_data(root_dir, data)
  create_checksum_file(root_dir, data)

  print(
      'Dataset generated in {}\n'
      'You can start with searching TODO({}).\n'
      'Please check this '
      '`https://github.com/tensorflow/datasets/blob/master/docs/add_dataset.md`'
      'for details.'.format(root_dir, dataset_name)
  )


if __name__ == '__main__':
  app.run(main)

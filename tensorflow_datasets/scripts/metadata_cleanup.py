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
r"""Removes metadatas which are not present in the registered versions of TFDS.

Instructions:

```
python tensorflow_datasets/scripts/metadata_cleanup.py
```


"""

import os
from typing import List

from absl import app
from absl import flags

import tensorflow as tf

import tensorflow_datasets as tfds

FLAGS = flags.FLAGS

flags.DEFINE_boolean('dry_run', True, 'Dry run')
flags.DEFINE_string('tfds_dir', tfds.core.utils.tfds_dir(),
                    'Path to tensorflow_datasets directory')


def _extract_metadata_versions(metadata_dir: str) -> List[str]:
  """Get all metadata direcotry versions paths.

  It only extract the paths like 'dataset_name/version'
  or 'dataset_name/config/versions' in metadata dir.

  Args:
    metadata_dir: Path to metadat directory (testing/metadata).

  Returns:
    Existing metadata full names.
  """
  existing_names = []
  for root, _, _ in tf.io.gfile.walk(metadata_dir):
    full_name = root[len(metadata_dir) + 1:]
    if tfds.core.registered.is_full_name(full_name):
      existing_names.append(full_name)
  return existing_names


def _delete_metadata_dirs(metadata_dir: str) -> None:
  """Removes metadatas which are not present in the registered versions of TFDS.

  Args:
    metadata_dir: Path to metadata directory (testing/metadata).
  """
  registered_names = set(tfds.core.registered.list_full_names())
  existing_names = set(_extract_metadata_versions(metadata_dir))
  for extra_full_name in sorted(existing_names - registered_names):
    path_to_delete = os.path.join(metadata_dir, extra_full_name)
    print(f'Delete: {path_to_delete}')
    if FLAGS.dry_run:
      continue
    tf.io.gfile.rmtree(path_to_delete)


def main(_):
  """Main script."""
  # Delete metadata versions not present in register version.
  metadata_dir = os.path.join(FLAGS.tfds_dir, 'testing', 'metadata')
  _delete_metadata_dirs(metadata_dir)


if __name__ == '__main__':
  app.run(main)

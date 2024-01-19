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

r"""Beam pipeline which computes the number of examples in a given data dir.

Compute the split info (num shards, num examples,...) metadata required
by `tfds.core.DatasetInfo`. See documentation and usage at:
https://www.tensorflow.org/datasets/external_tfrecord

"""

import argparse
from typing import List

from absl import app
from absl.flags import argparse_flags
import tensorflow_datasets as tfds
from tensorflow_datasets.core import naming
from tensorflow_datasets.scripts.utils import flag_utils


# Open source pytests globally import all files, so create duplicate FLAGS
# error when using absl.flags. So we use argparse instead.
def _parse_flags(argv: List[str]) -> argparse.Namespace:
  """Parses command line flags."""
  argv = flag_utils.normalize_flags(argv)  # See b/174043007 for context.

  parser = argparse_flags.ArgumentParser(
      description='Tensorflow Datasets CLI tool',
  )
  parser.add_argument(
      '--data_dir',
      type=tfds.core.Path,
      help='Path to the dataset files.',
  )
  parser.add_argument(
      '--out_dir',
      type=tfds.core.Path,
      help='Computed metadata will be written here.',
  )
  parser.add_argument(
      '--filename_template',
      type=str,
      help='Filename template that describes the file names in the data dir.',
  )
  parser.add_argument(
      '--filetype',
      type=str,
      help='The file type of the data, e.g. `tfrecord` or `array_record`.',
  )
  parser.add_argument(
      '--dataset_name',
      type=str,
      help='The name of the dataset.',
  )
  return parser.parse_args(argv[1:])


def main(args: argparse.Namespace) -> None:

  if args.filename_template or args.filetype:
    filename_template = naming.ShardedFileTemplate(
        data_dir=args.data_dir,
        filetype_suffix=args.filetype or None,
        dataset_name=args.dataset_name or None,
        template=args.filename_template or None,
    )
  else:
    filename_template = None

  tfds.folder_dataset.compute_split_info_from_directory(
      data_dir=args.data_dir,
      out_dir=args.out_dir,
      filename_template=filename_template,
  )


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)

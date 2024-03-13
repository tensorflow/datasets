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

r"""Convert a prepared dataset to another file format.

For example, you have a dataset in tfrecord format, but want to convert it to
ArrayRecord.

Instructions:

```
python tensorflow_datasets/scripts/convert_format.py \
  --dataset_dir=/data/my_dataset/config/1.2.3 \
  --out_file_format=array_record \
  --out_dir=/data/array_record/my_dataset/config/1.2.3
```

If the dataset is big, you may want to use Beam to convert it. You can do that
by adding `--use_beam`.

"""

from absl import app
from absl import flags
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.scripts.cli import convert_format_utils


_ROOT_DATA_DIR = flags.DEFINE_string(
    'root_data_dir',
    required=False,
    help=(
        'Root data dir that contains all datasets. All datasets and all their'
        ' configs and versions that are in this folder will be converted.'
    ),
    default=None,
)
_DATASET_DIR = flags.DEFINE_string(
    'dataset_dir',
    required=False,
    help=(
        'Path where the dataset to be converted is located. Converts all'
        ' configs and versions in this folder.'
    ),
    default=None,
)
_DATASET_VERSION_DIR = flags.DEFINE_string(
    'dataset_version_dir',
    required=False,
    help=(
        'Path where the dataset to be converted is located. Should include'
        ' config and version.'
    ),
    default=None,
)

_OUT_FILE_FORMAT = flags.DEFINE_enum_class(
    'out_file_format',
    enum_class=file_adapters.FileFormat,
    required=True,
    help='File format to convert the dataset to.',
    default=None,
)

_OUT_DIR = flags.DEFINE_string(
    'out_dir',
    required=True,
    help=(
        'Path where the converted dataset will be stored. Should include the'
        ' config and version, e.g. `/data/dataset_name/config/1.2.3`.'
    ),
    default=None,
)

_USE_BEAM = flags.DEFINE_bool(
    'use_beam',
    default=False,
    help='Whether to use beam to convert the dataset.',
)

_OVERWRITE = flags.DEFINE_bool(
    'overwrite',
    default=False,
    help='Whether to overwrite the output folder.',
)


def main(_):
  convert_format_utils.convert_dataset(
      root_data_dir=_ROOT_DATA_DIR.value,
      dataset_dir=_DATASET_DIR.value,
      dataset_version_dir=_DATASET_VERSION_DIR.value,
      out_file_format=_OUT_FILE_FORMAT.value,
      out_dir=_OUT_DIR.value,
      use_beam=_USE_BEAM.value,
      overwrite=_OVERWRITE.value,
  )


if __name__ == '__main__':
  app.run(main)

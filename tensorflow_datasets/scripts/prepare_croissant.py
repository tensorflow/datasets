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

r"""Prepare a Croissant dataset.

Instructions:

```
python tensorflow_datasets/scripts/prepare_croissant.py \
  --jsonld=/tmp/croissant.json \
  --record_sets=record1 --record_sets=record2
  --file_format=array_record
  --out_dir=/tmp/foo
  --mapping='{"document.csv": "~/Downloads/document.csv"}"'
```
"""

from absl import app
from absl import flags
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.scripts.cli import croissant


_JSONLD = flags.DEFINE_string(
    name='jsonld', default=None, help='Path to the JSONLD file.', required=True
)
_OUT_FILE_FORMAT = flags.DEFINE_enum_class(
    name='out_file_format',
    default=None,
    enum_class=file_adapters.FileFormat,
    help='File format to convert the dataset to.',
    required=True,
)
_RECORD_SETS = flags.DEFINE_multi_string(
    name='record_sets',
    default=[],
    help=(
        'The names of the record sets to generate. Each record set will'
        ' correspond to a separate config. If not specified, it will use all'
        ' the record sets.'
    ),
)
_OUT_DIR = flags.DEFINE_string(
    name='out_dir',
    default=None,
    help='Path where the converted dataset will be stored.',
    required=True,
)
_MAPPING = flags.DEFINE_string(
    name='mapping',
    default=None,
    help=(
        'Mapping filename->filepath as a Python dict[str, str] to handle'
        ' manual downloads. If `document.csv` is the FileObject and you'
        ' downloaded it to `~/Downloads/document.csv`, you can'
        ' specify`--mapping=\'{"document.csv": "~/Downloads/document.csv"}\''
    ),
)


def main(_):
  croissant.prepare_croissant_builder(
      jsonld=_JSONLD.value,
      record_sets=_RECORD_SETS.value,
      out_file_format=_OUT_FILE_FORMAT.value,
      out_dir=_OUT_DIR.value,
      mapping=_MAPPING.value,
  )


if __name__ == '__main__':
  app.run(main)

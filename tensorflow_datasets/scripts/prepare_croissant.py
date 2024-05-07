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

Example usage:
```
python tensorflow_datasets/scripts/prepare_croissant.py \
  --jsonld=/tmp/croissant.json \
  --data_dir=/tmp/foo \
  --file_format=array_record \
  --record_sets=record1,record2 \
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
_DATA_DIR = flags.DEFINE_string(
    name='data_dir',
    default=None,
    help='Path where the converted dataset will be stored.',
    required=True,
)
_FILE_FORMAT = flags.DEFINE_enum_class(
    name='file_format',
    default=file_adapters.FileFormat.ARRAY_RECORD,
    enum_class=file_adapters.FileFormat,
    help='File format to convert the dataset to.',
)
_RECORD_SETS = flags.DEFINE_list(
    name='record_sets',
    default=[],
    help=(
        'The names of the record sets to generate. Each record set will'
        ' correspond to a separate config. If not specified, it will use all'
        ' the record sets.'
    ),
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
_DOWNLOAD_DIR = flags.DEFINE_string(
    name='download_dir',
    default=None,
    help='Where to place downloads. Default to `<data_dir>/downloads/`.',
)
_PUBLISH_DIR = flags.DEFINE_string(
    name='publish_dir',
    default=None,
    help=(
        'Where to optionally publish the dataset after it has been generated '
        'successfully. Should be the root data dir under which datasets are '
        'stored. If unspecified, dataset will not be published.'
    ),
)
_SKIP_IF_PUBLISHED = flags.DEFINE_bool(
    name='skip_if_published',
    default=False,
    help=(
        'If the dataset with the same version and config is already published, '
        'then it will not be regenerated.'
    ),
)
_OVERWRITE = flags.DEFINE_bool(
    name='overwrite',
    default=False,
    help='Delete pre-existing dataset if it exists.',
)


def main(_):
  croissant.prepare_croissant_builder(
      jsonld=_JSONLD.value,
      data_dir=_DATA_DIR.value,
      file_format=_FILE_FORMAT.value.value,
      record_sets=_RECORD_SETS.value,
      mapping=_MAPPING.value,
      download_dir=_DOWNLOAD_DIR.value,
      publish_dir=_PUBLISH_DIR.value,
      skip_if_published=_SKIP_IF_PUBLISHED.value,
      overwrite=_OVERWRITE.value,
  )


if __name__ == '__main__':
  app.run(main)

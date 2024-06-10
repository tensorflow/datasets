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
from etils import eapp
from tensorflow_datasets.scripts.cli import croissant


parse_flags = eapp.make_flags_parser(croissant.CmdArgs)


if __name__ == '__main__':
  app.run(croissant.prepare_croissant_builder, flags_parser=parse_flags)

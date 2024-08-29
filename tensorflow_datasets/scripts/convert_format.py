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
from etils import eapp
from tensorflow_datasets.scripts.cli import convert_format as convert_format_cli
from tensorflow_datasets.scripts.cli import convert_format_utils


def main(args: convert_format_cli.CmdArgs):

  convert_format_utils.convert_dataset(
      out_dir=args.out_dir,
      out_file_format=args.out_file_format,
      root_data_dir=args.root_data_dir,
      dataset_dir=args.dataset_dir,
      dataset_version_dir=args.dataset_version_dir,
      overwrite=args.overwrite,
      use_beam=args.use_beam,
      num_workers=args.num_workers,
  )


if __name__ == '__main__':
  app.run(main, flags_parser=eapp.make_flags_parser(convert_format_cli.CmdArgs))

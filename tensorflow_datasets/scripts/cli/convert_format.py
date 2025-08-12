# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

r"""`tfds convert_format` command.

Example usage:
```
tfds convert_format \
  --dataset_version_dir=/data/dataset/config/1.2.3 \
  --out_file_format=array_record \
  --out_dir=/data_array_record/dataset/config/1.2.3 \
  --use_beam=True
```
"""

import dataclasses

from etils import epath
import simple_parsing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.scripts.cli import cli_utils
from tensorflow_datasets.scripts.cli import convert_format_utils


@dataclasses.dataclass(frozen=True, kw_only=True)
class Args(cli_utils.Args):
  """Converts a dataset from one file format to another format.

  Attributes:
    root_data_dir: Root data dir that contains all datasets. All datasets and
      all their configs and versions that are in this folder will be converted.
    dataset_dir: Path where the dataset to be converted is located. Converts all
      configs and versions in this folder.
    dataset_version_dir: Path where the dataset to be converted is located.
      Should include config and version. Can also be a comma-separated list of
      paths. If multiple paths are specified, `--out_dir` should not be
      specified, since each dataset will be converted in the same directory as
      the input dataset.
    out_file_format: File format to convert the dataset to.
    out_dir: Path where the converted dataset will be stored. Datasets will be
      stored with the same folder structure as the input folder. If `None`, the
      converted shards will be stored in the same folder as the input datasets.
    overwrite: Whether to overwrite the output directory if it already exists.
    use_beam: Use beam to convert the dataset.
    num_workers: Number of workers to use when not using Beam. If `--use_beam`
      is set, this flag is ignored. If `--num_workers=1`, the conversion will be
      done sequentially.
    only_log_errors: If set, errors during the conversion will be logged as
      errors and will not crash the conversion. If you are converting a large
      number of datasets, you might want to set this flag to true.
  """

  root_data_dir: epath.Path | None = None
  dataset_dir: epath.Path | None = None
  dataset_version_dir: list[epath.Path] = simple_parsing.field(
      default_factory=list,
      type=lambda dataset_version_dirs_str: [
          epath.Path(path) for path in dataset_version_dirs_str.split(',')
      ],
      nargs='?',
  )
  out_file_format: str = simple_parsing.choice(
      *(file_format.value for file_format in file_adapters.FileFormat),
  )
  out_dir: epath.Path | None = None
  overwrite: bool = False
  use_beam: bool = False
  num_workers: int = 8
  only_log_errors: bool = False

  def execute(self) -> None:
    """Converts a dataset from one file format to another."""
    convert_format_utils.convert_dataset(
        out_dir=self.out_dir,
        out_file_format=self.out_file_format,
        dataset_dir=self.dataset_dir,
        root_data_dir=self.root_data_dir,
        dataset_version_dir=self.dataset_version_dir,
        overwrite=self.overwrite,
        use_beam=self.use_beam,
        num_workers=self.num_workers,
        fail_on_error=not self.only_log_errors,
    )

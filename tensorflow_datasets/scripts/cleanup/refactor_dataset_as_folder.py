# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

r"""A refactoring script to refactor the dataset files into a single folder.

```
my_dataset/
    dummy_data/
    __init__.py
    my_dataset.py
    my_dataset_test.py
    make_dummy_data.py
    checksums.tsv
```

Instructions:

```
python3 -m tensorflow_datasets.scripts.cleanup.refactor_dataset_as_folder
```

"""

import dataclasses
import shutil
from typing import Type

from absl import app
from absl import flags
import tensorflow_datasets as tfds

flags.DEFINE_string('datasets', None, 'Datasets to convert')

FLAGS = flags.FLAGS

TFDS_PATH = tfds.core.utils.tfds_write_path()


@dataclasses.dataclass(frozen=True)
class BuilderCodeInfo:
  """Wrapper around `DatasetBuilder` code metadata.

  Attributes:
    file: Path to dataset file (e.g. `.../image/mnist.py`)
    dir: Path to dataset directory (e.g. `.../image/`)
    dst: New dataset directory `.../image/mnist/`
    name: Dataset name, snake_case (`my_dataset`)
    cls_name: Dataset name, CamelCase (`MyDataset`)
    type: Dataset type (e.g. `image`, `text`, `object_detection`)
  """

  file: tfds.core.Path
  dir: tfds.core.Path
  dst: tfds.core.Path
  name: str
  cls_name: str
  type: str

  @classmethod
  def from_builder_cls(
      cls, builder_cls: Type[tfds.core.DatasetBuilder]
  ) -> 'BuilderCodeInfo':
    path = tfds.core.utils.to_write_path(builder_cls.code_path)
    return cls(
        file=path,
        dir=path.parent,
        dst=path.parent / builder_cls.name,
        name=builder_cls.name,
        cls_name=builder_cls.__name__,
        type=path.parent.name,
    )


# Util functions


def _rename_dir(
    src: tfds.core.Path,
    dst: tfds.core.Path,
) -> None:
  """Equivalent of `src.rename(dst)`."""
  # src.rename(dst) creates `Invalid cross-device link` on some remote file
  # systems, so uses manual operation instead.
  # Note, this is not atomic.
  shutil.copytree(src, dst)
  shutil.rmtree(src)


# Rename functions


def _add_init_file(code_info: BuilderCodeInfo) -> None:
  """Creates the `my_dataset/__init__.py` file."""
  init_path = code_info.dst / '__init__.py'
  init_path.write_text('\n')


def _mv_fake_data_dir(code_info: BuilderCodeInfo) -> None:
  """Move the fake data directory."""
  src_fake_dir_path = (
      TFDS_PATH / 'testing/test_data/fake_examples' / code_info.name
  )
  dst_fake_dir_path = code_info.dst / 'dummy_data'
  _rename_dir(src_fake_dir_path, dst_fake_dir_path)


def _mv_code(code_info: BuilderCodeInfo) -> None:
  """Move the `my_dataset.py` file."""
  code_info.file.rename(code_info.dst / f'{code_info.name}.py')


def _mv_code_test(code_info: BuilderCodeInfo) -> None:
  """Move the `my_dataset_test.py` file."""
  # Try to infer the test filename.
  test_file = code_info.dir / f'{code_info.file.stem}_test.py'
  assert test_file.exists(), f'{test_file} not found.'
  test_file.rename(code_info.dst / f'{code_info.name}_test.py')


def _mv_checksums(code_info: BuilderCodeInfo) -> None:
  """Move the `checksums.tsv` file."""
  src_checksums_path = TFDS_PATH / 'url_checksums' / f'{code_info.name}.txt'
  # Not all datasets have checksums (e.g. manual datasets)
  if src_checksums_path.exists():
    src_checksums_path.rename(code_info.dst / 'checksums.tsv')


def _mv_create_fake_data(code_info: BuilderCodeInfo) -> None:
  """Move the `fake_data` generation script file."""
  create_fake_data_file = (
      TFDS_PATH / 'testing/fake_data_generation' / f'{code_info.name}.py'
  )
  if create_fake_data_file.exists():
    create_fake_data_file.rename(code_info.dst / 'make_dummy_data.py')


# Main functions


def refactor_dataset(ds_name: str) -> None:
  """Refactor a single dataset."""
  code_info = BuilderCodeInfo.from_builder_cls(tfds.builder_cls(ds_name))

  print(f'Refactoring {code_info.name} in {code_info.dst}')

  # Eventually cleanup previous refactoring.
  if code_info.dst.exists():
    print(f'Cleanup existing {code_info.dst}')
    shutil.rmtree(code_info.dst)
  code_info.dst.mkdir()

  # Copy all files and folders
  _add_init_file(code_info)
  _mv_code(code_info)
  _mv_code_test(code_info)
  _mv_checksums(code_info)
  _mv_fake_data_dir(code_info)
  _mv_create_fake_data(code_info)

  # TODO(tfds):
  # * Add BUILD files
  # * Update `<type>/__init__.py` import (including builder config class)
  # * Support util scripts
  # * How to support shared data (e.g. imagenet labels shared between classes ?)


def refactor_datasets() -> None:
  """Refactoring all dataset into one folder."""
  for ds_name in FLAGS.datasets.split(',') or tfds.list_builders(
      with_community_datasets=False
  ):
    refactor_dataset(ds_name)


def main(_):
  refactor_datasets()


if __name__ == '__main__':
  app.run(main)

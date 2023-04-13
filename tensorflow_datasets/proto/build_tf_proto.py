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

"""Re-compiles tf.train.Example and tf.train.Feature protos from the source.

Disclaimer: we copy tf.train.Example and tf.train.Feature from TensorFlow.

We did this in order not to import all the TensorFlow library when we only need
these two protos.

Execute this script with a local version of Python (e.g., using `pyenv`):

```
python tensorflow_datasets/proto/build_tf_proto.py
```
"""

import enum
import os
import re
import subprocess

from absl import app
from etils import epath
import requests

PATH_TO_TFDS = epath.Path(__file__).parent.parent
PATH_TO_PROTO = PATH_TO_TFDS / 'proto'


class TFProto(enum.Enum):
  EXAMPLE = 'example'
  FEATURE = 'feature'


def get_tf_proto_content_from_github(tf_proto: TFProto) -> bytes:
  """Downloads the proto from Github and formats it."""
  url = f'https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/core/example/{tf_proto.value}.proto'
  request = requests.get(url)
  content = request.content
  content = clean_import_in_proto(
      content,
      b'import "tensorflow/core/example/feature.proto";',
      b'import "tensorflow_datasets/proto/tf_feature.proto";',
  )
  content = clean_package(content)
  content = remove_comments(content)
  content = add_header(content, url)
  return content


def get_tfds_proto_path(tf_proto: TFProto) -> epath.Path:
  return PATH_TO_PROTO / f'tf_{tf_proto.value}.proto'


def add_header(file_content: bytes, url: str) -> bytes:
  file_content_with_header = b'// DO NOT EDIT\n'
  file_content_with_header += b'// This file was copied from\n'
  file_content_with_header += b'// ' + url.encode() + b'\n\n'
  file_content_with_header += b'// Use according to the original license.\n\n'
  file_content_with_header += file_content
  return file_content_with_header


def clean_import_in_proto(
    file_content: bytes, before: bytes, after: bytes
) -> bytes:
  return file_content.replace(before, after)


def clean_package(file_content: bytes) -> bytes:
  """Declares a new package in order to avoid protobuf typing conflicts."""
  return file_content.replace(
      b'package tensorflow;',
      b'package tensorflow_copy;',
  )


def remove_comments(file_content: bytes) -> bytes:
  file_content = re.sub(rb'^\s*\/\/.*\n', b'', file_content, flags=re.MULTILINE)
  file_content = re.sub(rb'\s*\/\/.*\n', b'\n', file_content)
  return file_content


def change_imports_in_py(
    file_content: bytes, name_before: str, name_after: str
) -> bytes:
  name_before_without_suffix = os.path.splitext(name_before)[0]
  name_after_without_suffix = os.path.splitext(name_after)[0]
  return file_content.replace(
      f'import {name_before_without_suffix} as'.encode(),
      f'import {name_after_without_suffix} as'.encode(),
  )


def skip_pylint(file_content: bytes) -> bytes:
  file_content_without_pylint = b'# pylint: skip-file\n\n'
  file_content_without_pylint += file_content
  return file_content_without_pylint


def main(_) -> None:
  names_before = []
  names_after = []
  for proto_name in [TFProto.FEATURE, TFProto.EXAMPLE]:
    tf_proto_content = get_tf_proto_content_from_github(proto_name)
    tfds_proto_path = get_tfds_proto_path(proto_name)
    tfds_proto_path.write_bytes(tf_proto_content)

    # Launch protoc
    subprocess.run(
        [
            'protoc',
            os.fspath(tfds_proto_path),
            f'--proto_path={PATH_TO_TFDS.parent}',
            f'--python_out={PATH_TO_TFDS.parent}',
        ],
        check=True,
    )
    name_before = PATH_TO_PROTO / f'tf_{proto_name.value}_pb2.py'
    name_after = PATH_TO_PROTO / f'tf_{proto_name.value}_generated_pb2.py'
    names_before.append(name_before)
    names_after.append(name_after)

  # Rename tf_*_pb2.py -> tf_*_generated_pb2.py
  for name_before, name_after in zip(names_before, names_after):
    subprocess.run(
        ['mv', os.fspath(name_before), os.fspath(name_after)],
        check=True,
    )
    target_py_content = name_after.read_bytes()
    target_py_content = skip_pylint(target_py_content)
    for other_name_before, other_name_after in zip(names_before, names_after):
      target_py_content = change_imports_in_py(
          target_py_content, other_name_before.name, other_name_after.name
      )
    name_after.write_bytes(target_py_content)


if __name__ == '__main__':
  app.run(main)

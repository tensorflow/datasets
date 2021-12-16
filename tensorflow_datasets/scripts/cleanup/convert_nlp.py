# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Add HuggingFace Datasets.

Script to convert code for dataset in HuggingFace to tensorflow datasets

To convert a dataset from huggingface, first clone the git repo of
huggingface to local device.

To clone, copy and execute the following command in terminal

git clone https://github.com/huggingface/nlp.git

This will create a copy of the repo in local device. All datasets in
huggingface nlp will be copied.

"""

import argparse
import pathlib
import re

from absl import app
from absl.flags import argparse_flags
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.scripts.cli import new

TO_CONVERT = [
    # (pattern, replacement)
    # Order is important here for some replacements
    (r"from\s__future__\simport\sabsolute_import.*", r""),
    (r"from\s__future__\simport\sdivision.*", r""),
    (r"from\s__future__\simport\sprint_function.*", r""),
    (r"import\slogging", r"from absl import logging\n"),
    (r"import\snlp",
     r"import tensorflow as tf\nimport tensorflow_datasets.public_api as tfds\n"
    ),
    (r"with\sopen", r"with tf.io.gfile.GFile"),
    (r"encoding=\"utf-8\"", r"'r'"),
    (r"return\snlp\.DatasetInfo\(",
     r"    return tfds.core.DatasetInfo(\n        builder=self,\n"),
    (r"nlp\.ClassLabel", r"tfds.features.ClassLabel"),
    (r"nlp\.Value\(\"string\"\)", r"tfds.features.Text()"),
    (r"nlp\.Value\(\"([\w\d]+)\"\)", r"tf.\1"),
    (r"nlp\.features", "tfds.features"),
    (r"features\s*=\s*nlp\.Features\(",
     r"features=tfds.features.FeaturesDict("),
    (r"dict\(", r"tfds.features.FeaturesDict("),
    (r"nlp.SplitGenerator", r"tfds.core.SplitGenerator"),
    (r"self\.config\.data_dir", r"dl_manager.manual_dir"),
    (r"self\.config", r"self.builder_config"),
    (r"nlp\.Split", r"tfds.Split"),
    (r"nlp", r"tfds.core"),
]


def _parse_flags(_) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog="convert_dataset",
      description="Tool to add hugging face datasets",
  )
  parser.add_argument(
      "--nlp_path", type=pathlib.Path, help="Path of the nlp directory")
  parser.add_argument(
      "--dataset_name",
      type=str,
      help="Name of dataset to be converted. Ex. esnli",
  )
  parser.add_argument(
      "--dataset_type",
      type=str,
      help="Type of dataset. Ex. text, question_answering",
  )
  return parser.parse_args()


def main(args: argparse.Namespace):

  create_dataset_files(
      nlp_path=args.nlp_path,
      dataset_name=args.dataset_name,
      dataset_type=args.dataset_type,
  )


def create_dataset_files(
    nlp_path: pathlib.Path,
    dataset_name: str,
    dataset_type: str,
) -> None:
  """Create template files."""
  #  Path of the converted dataset directory
  tfds_root_path = tfds.core.utils.tfds_write_path()
  dataset_dir = tfds_root_path / dataset_type
  if not dataset_dir.is_dir():
    raise ValueError(f"Invalid Dataset Type {dataset_type}")

  #  Create dataset timeplate files from new.py
  new.create_dataset_files(dataset_name=dataset_name, dataset_dir=dataset_dir)  # pytype: disable=wrong-arg-types  # gen-stub-imports

  #  Path of the dataset file
  nlp_datasets_path = nlp_path.expanduser() / "datasets"
  nlp_file_path = nlp_datasets_path / dataset_name / f"{dataset_name}.py"

  #  Path of converted dataset file
  converted_file_path = dataset_dir / dataset_name / f"{dataset_name}.py"

  #  Convert nlp dataset --> tfds
  convert_dataset_file(nlp_file_path, converted_file_path)


def convert_dataset_file(nlp_file_path, converted_file_path):
  """Convert nlp dataset."""
  print("Starting conversion of nlp file")
  compiled_patterns = [
      (re.compile(pattern), replacement) for pattern, replacement in TO_CONVERT
  ]

  nlp_file_contents = nlp_file_path.read_text()
  for pattern, replacement in compiled_patterns:
    nlp_file_contents = pattern.sub(replacement, nlp_file_contents)

  converted_file_path.write_text(nlp_file_contents)
  print("File successfully converted")
  print(nlp_file_contents)


if __name__ == "__main__":
  app.run(main, flags_parser=_parse_flags)

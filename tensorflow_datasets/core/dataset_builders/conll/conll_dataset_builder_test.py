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

import textwrap

from etils import epath
import pytest
from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder
from tensorflow_datasets.core.dataset_builders.conll import conll_dataset_builder_utils as conll_lib
import tensorflow_datasets.public_api as tfds

_FOLDER_PATH = "mock/path"

_VALID_INPUT = textwrap.dedent("""
-DOCSTART- -X- -X- O
Winter NN B-NP O
is VBZ B-VP O

Air NN I-NP O
. . O O
""")

_INVALID_INPUT = textwrap.dedent("""
Winter NN B-NP
is VBZ B-VP O

Air NN I-NP O
. . O O
""")


class DummyConllDataset(conll_dataset_builder.ConllDatasetBuilder):
  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {"1.0.0": "Dummy notes."}
  BUILDER_CONFIGS = [conll_lib.CONLL_2003_CONFIG]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(
        description="Dummy CoNLL dataset.",
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    del dl_manager
    return {"train": self._generate_examples("/tmp/input.txt")}


def test_generate_example(tmpdir):
  tmpdir = epath.Path(tmpdir)
  input_path = tmpdir / "input_path.txt"
  input_path.write_text(_VALID_INPUT)

  dataset = DummyConllDataset(data_dir=tmpdir)
  examples = list(dataset._generate_examples(input_path))

  expected_examples = [
      (
          0,
          {
              "tokens": ["Winter", "is"],
              "pos": ["NN", "VBZ"],
              "chunks": ["B-NP", "B-VP"],
              "ner": ["O", "O"],
          },
      ),
      (
          1,
          {
              "tokens": ["Air", "."],
              "pos": ["NN", "."],
              "chunks": ["I-NP", "O"],
              "ner": ["O", "O"],
          },
      ),
  ]

  assert examples == expected_examples

  for _, example in examples:
    assert len(example) == len(conll_lib.CONLL_2003_ORDERED_FEATURES)

  assert len(examples) == 2


def test_generate_corrupted_example(tmpdir):
  tmpdir = epath.Path(tmpdir)
  input_path = tmpdir / "input_path.txt"
  input_path.write_text(_INVALID_INPUT)
  dataset = DummyConllDataset(data_dir=tmpdir)

  error_line = "Winter NN B-NP"
  error_msg = (
      f"Mismatch in the number of features found in line: {error_line}\n\n"
      "Should be 4, but found 3"
  )
  with pytest.raises(ValueError, match=error_msg):
    list(dataset._generate_examples(input_path))

# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for conllu_dataset_builder."""
import textwrap
from unittest import mock

from etils import epath
import pytest
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder
from tensorflow_datasets.core.dataset_builders.conll import conllu_dataset_builder_utils as conllu_lib
import tensorflow_datasets.public_api as tfds

_FOLDER_PATH = "mock/path"

_VALID_INPUT = textwrap.dedent("""
# sent_id = VIT-9558
# text = Il futuro.
1	Il	il	DET	RD	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	_
2	futuro	futuro	NOUN	S	Gender=Masc|Number=Sing	0	root	_	SpaceAfter=No
3	.	.	PUNCT	FS	_	2	punct	_	_

# sent_id = VIT-9478
# text = il responsabile dell'ambiente
1	il	il	DET	RD	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
2	responsabile	responsabile	NOUN	S	Number=Sing	1	nsubj	_	_
3-4	dell'	_	_	_	_	_	_	_	SpaceAfter=No
3	di	di	ADP	E	_	6	case	_	_
4	l'	il	DET	RD	Definite=Def|Number=Sing|PronType=Art	6	det	_	_
5	ambiente	ambiente	NOUN	S	Gender=Masc|Number=Sing	3	nmod	_	_
""")

# The error making this invalid is the missing lemma field in line 1.
_INVALID_INPUT = textwrap.dedent("""
# sent_id = VIT-9558
# text = Il futuro.
1	Il	DET	RD	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	_
2	futuro	futuro	NOUN	S	Gender=Masc|Number=Sing	0	root	_	SpaceAfter=No
3	.	.	PUNCT	FS	_	2	punct	_	_
""")

_INPUT_PATH = epath.Path(_FOLDER_PATH, "input_path.txt")


class DummyConllUDataset(conllu_dataset_builder.ConllUDatasetBuilder):
  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {"1.0.0": "Dummy notes."}
  BUILDER_CONFIGS = [
      conllu_lib.get_universal_morphology_config(
          language="italian",
          features=conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES)
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(description="Dummy CoNLL dataset.",)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    del dl_manager
    return {"train": self._generate_examples(_INPUT_PATH)}


def test_generate_example():
  tf_mock = mock.Mock()
  tf_mock.gfile.GFile.return_value = _VALID_INPUT
  expected_examples = []

  dataset = DummyConllUDataset()

  with tfds.testing.MockFs() as fs:
    fs.add_file(path=_INPUT_PATH, content=_VALID_INPUT)
    examples = list(dataset._generate_examples(_INPUT_PATH))
    expected_examples = [
        (
            0,
            {
                "idx": "VIT-9558",
                "text": "Il futuro.",
                "tokens": ["Il", "futuro", "."],
                "lemmas": ["il", "futuro", "."],
                "upos": ["DET", "NOUN", "PUNCT"],
                "xpos": ["RD", "S", "FS"],
                "feats": [
                    "{'Definite': 'Def', 'Gender': 'Masc', 'Number': 'Sing', "  # pylint:disable=implicit-str-concat
                    "'PronType': 'Art'}",
                    "{'Gender': 'Masc', 'Number': 'Sing'}",
                    "None"
                ],
                "head": ["2", "0", "2"],
                "deprel": ["det", "root", "punct"],
                "deps": ["None", "None", "None"],
                "misc": ["None", "{'SpaceAfter': 'No'}", "None"],
            }),
        (
            1,
            {
                "idx":
                    "VIT-9478",
                "text":
                    "il responsabile dell'ambiente",
                "tokens": [
                    "il", "responsabile", "dell'", "di", "l'", "ambiente"
                ],
                "lemmas": ["il", "responsabile", "_", "di", "il", "ambiente"],
                "upos": ["DET", "NOUN", "_", "ADP", "DET", "NOUN"],
                "xpos": ["RD", "S", "None", "E", "RD", "S"],
                "feats": [
                    "{'Definite': 'Def', 'Gender': 'Masc', 'Number': 'Sing', "  # pylint:disable=implicit-str-concat
                    "'PronType': 'Art'}",
                    "{'Number': 'Sing'}",
                    "None",
                    "None",
                    "{'Definite': 'Def', 'Number': 'Sing', 'PronType': 'Art'}",
                    "{'Gender': 'Masc', 'Number': 'Sing'}"
                ],
                "head": ["3", "1", "None", "6", "6", "3"],
                "deprel": ["det", "nsubj", "_", "case", "det", "nmod"],
                "deps": ["None", "None", "None", "None", "None", "None"],
                "misc": [
                    "None", "None", "{'SpaceAfter': 'No'}", "None", "None",
                    "None"
                ],
            }),
    ]

    assert examples == expected_examples

    for _, example in examples:
      assert len(example) == len(conllu_lib.UNIVERSAL_DEPENDENCIES_FEATURES)

  assert len(examples) == 2


def test_generate_corrupted_example():
  conllu = lazy_imports_lib.lazy_imports.conllu

  tf_mock = mock.Mock()
  tf_mock.gfile.GFile.return_value = _VALID_INPUT
  dataset = DummyConllUDataset()

  with pytest.raises(conllu.exceptions.ParseException):
    with tfds.testing.MockFs() as fs:
      fs.add_file(path=_INPUT_PATH, content=_INVALID_INPUT)
      list(dataset._generate_examples(_INPUT_PATH))


class DummyXtremePosConllUDataset(conllu_dataset_builder.ConllUDatasetBuilder):
  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {"1.0.0": "Dummy notes."}
  BUILDER_CONFIGS = [
      conllu_lib.get_universal_morphology_config(
          language="italian", features=conllu_lib.XTREME_POS_FEATURES)
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.create_dataset_info(description="Dummy CoNLL dataset.",)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    del dl_manager
    return {
        "train":
            self._generate_examples(
                filepaths=_INPUT_PATH,
                process_example_fn=conllu_dataset_builder.get_xtreme_pos_example
            )
    }


def test_generate_xtreme_pos_example():
  tf_mock = mock.Mock()
  tf_mock.gfile.GFile.return_value = _VALID_INPUT
  expected_examples = []

  dataset = DummyXtremePosConllUDataset()

  with tfds.testing.MockFs() as fs:
    fs.add_file(path=_INPUT_PATH, content=_VALID_INPUT)
    examples = list(dataset._generate_examples(_INPUT_PATH))
    expected_examples = [
        (0, {
            "tokens": ["Il", "futuro", "."],
            "upos": ["DET", "NOUN", "PUNCT"],
        }),
        (1, {
            "tokens": ["il", "responsabile", "dell'", "di", "l'", "ambiente"],
            "upos": ["DET", "NOUN", "_", "ADP", "DET", "NOUN"],
        }),
    ]

    assert examples == expected_examples

    for _, example in examples:
      assert len(example) == len(conllu_lib.XTREME_POS_FEATURES)

  assert len(examples) == 2


def test_generate_corrupted_xtreme_pos_example():
  conllu = lazy_imports_lib.lazy_imports.conllu

  tf_mock = mock.Mock()
  tf_mock.gfile.GFile.return_value = _VALID_INPUT
  dataset = DummyXtremePosConllUDataset()

  with pytest.raises(conllu.exceptions.ParseException):
    with tfds.testing.MockFs() as fs:
      fs.add_file(path=_INPUT_PATH, content=_INVALID_INPUT)
      list(dataset._generate_examples(_INPUT_PATH))

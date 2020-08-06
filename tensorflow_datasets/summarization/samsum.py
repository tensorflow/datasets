# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""SAMSum dataset."""

import json
import os
from typing import Dict, Iterator, List, Text, Tuple

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{gliwa2019samsum,
  title={SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization},
  author={Gliwa, Bogdan and Mochol, Iwona and Biesek, Maciej and Wawer, Aleksander},
  journal={arXiv preprint arXiv:1911.12237},
  year={2019}
}
"""

_DESCRIPTION = """
SAMSum Corpus contains over 16k chat dialogues with manually annotated
summaries.

There are two features:

  - dialogue: text of dialogue.
  - summary: human written summary of the dialogue.
  - id: id of a example.

"""

_DOCUMENT = "dialogue"
_SUMMARY = "summary"
_ID = "id"


class Samsum(tfds.core.GeneratorBasedBuilder):
  """SAMSum dataset builder."""

  VERSION = tfds.core.Version("1.0.0")
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Download https://arxiv.org/src/1911.12237v2/anc/corpus.7z, decompress and
  place train.json, val.json and test.json in the manual follder.
  """

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text(),
            _ID: tfds.features.Text(),
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://arxiv.org/src/1911.12237v2/anc",
        citation=_CITATION,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": os.path.join(dl_manager.manual_dir, "train.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "path": os.path.join(dl_manager.manual_dir, "val.json")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": os.path.join(dl_manager.manual_dir, "test.json")
            },
        ),
    ]

  def _generate_examples(self,
                         path: Text = None
                        ) -> Iterator[Tuple[Text, Dict[Text, Text]]]:
    """Yields examples."""
    with tf.io.gfile.GFile(path, "rb") as f:
      for example in json.load(f):
        yield example[_ID], example

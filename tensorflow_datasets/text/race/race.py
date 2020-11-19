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

"""race dataset."""

import json
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Race is a large-scale reading comprehension dataset with more than 28,000
passages and nearly 100,000 questions. The dataset is collected from English
examinations in China, which are designed for middle school and high school
students. The dataset can be served as the training and test sets for machine
comprehension.
"""

_CITATION = """
@article{lai2017large,
    title={RACE: Large-scale ReAding Comprehension Dataset From Examinations},
    author={Lai, Guokun and Xie, Qizhe and Liu, Hanxiao and Yang, Yiming and Hovy, Eduard},
    journal={arXiv preprint arXiv:1704.04683},
    year={2017}
}
"""

_MODULES = [
    "high",
    "middle",
]


def _make_builder_config(module):
  return tfds.core.BuilderConfig(
      name=module,
      description="Builder config for RACE dataset.",
  )


def _get_option_index(answer):
  return ord(answer) - ord("A")


class Race(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for race dataset."""

  VERSION = tfds.core.Version("1.0.0")
  BUILDER_CONFIGS = [_make_builder_config(module) for module in _MODULES]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "article": tfds.features.Text(),
            "question": tfds.features.Text(),
            "answer": tfds.features.Text()
        }),
        supervised_keys=None,  # Set to `None` to disable
        homepage="https://www.cs.cmu.edu/~glai1/data/race/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        "http://www.cs.cmu.edu/~glai1/data/race/RACE.tar.gz")

    path = path / "RACE"
    task = self.builder_config.name

    return {
        "train":
            self._generate_examples(
                path / "train" / task),
        "dev":
            self._generate_examples(
                path / "dev" / task),
        "test":
            self._generate_examples(
                path / "test" / task),
    }

  def _generate_examples(self, path):
    """Yields examples."""

    for file in path.iterdir():
      # Each file is one example and only has one line of the content.
      row = json.loads(file.read_text())
      article = row["article"]
      ex_id = row["id"]
      question_length = len(row["questions"])
      for idx in range(question_length):
        question = row["questions"][idx]
        option = row["options"][idx][_get_option_index(row["answers"][idx])]
        yield ex_id + "_" + str(idx), {
            "article": article,
            "question": question,
            "answer": option
        }

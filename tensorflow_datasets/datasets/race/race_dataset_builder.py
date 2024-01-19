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

"""race dataset."""

import json
import tensorflow_datasets.public_api as tfds

_MODULES = [
    "high",
    "middle",
]


def _make_builder_config(module):
  return tfds.core.BuilderConfig(
      name=module,
      description="Builder config for RACE dataset.",
  )


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for race dataset."""

  VERSION = tfds.core.Version("2.0.0")
  RELEASE_NOTES = {
      "2.0.0": "Add the example id.",
      "1.0.0": "Initial release.",
  }
  BUILDER_CONFIGS = [_make_builder_config(module) for module in _MODULES]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "article": tfds.features.Text(),
            "questions": tfds.features.Sequence(tfds.features.Text()),
            "answers": tfds.features.Sequence(tfds.features.Text()),
            "options": tfds.features.Sequence(
                tfds.features.Sequence(tfds.features.Text())
            ),
            "example_id": tfds.features.Text(),
        }),
        supervised_keys=None,  # Set to `None` to disable
        homepage="https://www.cs.cmu.edu/~glai1/data/race/",
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(
        "http://www.cs.cmu.edu/~glai1/data/race/RACE.tar.gz"
    )

    path = path / "RACE"
    task = self.builder_config.name

    return {
        "train": self._generate_examples(path / "train" / task),
        "dev": self._generate_examples(path / "dev" / task),
        "test": self._generate_examples(path / "test" / task),
    }

  def _generate_examples(self, path):
    """Yields examples."""

    for file in path.iterdir():
      # Each file is one example and only has one line of the content.
      row = json.loads(file.read_text())
      yield row["id"], {
          "article": row["article"],
          "questions": row["questions"],
          "answers": row["answers"],
          "options": row["options"],
          "example_id": row["id"],
      }

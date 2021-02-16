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

"""Dummy HG dataset."""

from pathlib import Path  # < Direct import of path should be patched  # pylint: disable=g-importing-member

import datasets  # pytype: disable=import-error
import tensorflow_datasets.public_api as tfds


class HFDataset(datasets.GeneratorBasedBuilder):
  """AdversarialQA. Version 1.0.0."""

  VERSION = datasets.Version("1.0.0")
  BUILDER_CONFIGS = [
      datasets.BuilderConfig(
          name="config1",
          description="Description.",
      ),
      datasets.BuilderConfig(
          name="config2",
          description="Description 2. ",
      ),
  ]
  DEFAULT_CONFIG_NAME = "config2"  # Config name can be in another position.

  def _info(self):
    assert isinstance(self, tfds.core.DatasetBuilder)
    return datasets.DatasetInfo(
        description="""Some description.""",
        features=datasets.Features({
            "id": datasets.Value("string"),
            "vals": [datasets.Value("int32")],  # list is alias for Sequence.
            "answers": datasets.features.Sequence({
                "text": datasets.Value("string"),
            }),
        }),
        homepage="http://some-webpage.org",
        citation="""@article{Some citation}""",
    )

  def _split_generators(self, dl_manager):
    assert isinstance(dl_manager, tfds.download.DownloadManager)

    return [
        datasets.SplitGenerator(
            name=datasets.Split.TRAIN,
            gen_kwargs={
                "num_vals": 10,
            },
        ),
        datasets.SplitGenerator(
            name=datasets.Split.VALIDATION,
            gen_kwargs={
                "num_vals": 5,
            },
        ),
    ]

  def _generate_examples(self, num_vals):
    """This function returns the examples in the raw (text) form."""
    # Path is mocked
    assert isinstance(Path("some_path/"), tfds.core.utils.gpath._GPath)  # pylint: disable=protected-access
    for i in range(num_vals):
      yield i, {
          "id": str(i),
          "vals": [i, i],
          "answers": {
              "text": ["some text", "some text2"],
          },
      }

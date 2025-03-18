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

"""The ag_news_subset dataset."""

import csv
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_HOMEPAGE_URL = "https://arxiv.org/abs/1509.01626"
_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=0Bz8a_Dbh9QhbUDNpeUdjb0wxRms"

_LABEL_NAMES = ["World", "Sports", "Business", "Sci/Tech"]


class Builder(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for classifying news articles into 4 classes."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "label": tfds.features.ClassLabel(names=_LABEL_NAMES),
            "title": tfds.features.Text(),
            "description": tfds.features.Text(),
        }),
        supervised_keys=("description", "label"),
        homepage=_HOMEPAGE_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({"ag_news_csv": _DOWNLOAD_URL})
    # Name of the extracted folder is 'ag_news_csv'
    base_path = os.path.join(dl_paths["ag_news_csv"], "ag_news_csv")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(base_path, "train.csv")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(base_path, "test.csv")},
        ),
    ]

  def _generate_examples(self, path):
    """Yeilds Examples.

    Args:
      path: The path of the file to be read for this split

    Yields:
      Generator yielding the next examples
    """
    with epath.Path(path).open() as f:
      reader = csv.reader(f)
      # CSV files : class label (as number), title, description
      for index, row in enumerate(reader):
        key = index
        # The values in the csv file do not have quotes
        example = {
            # The class labels start from 1 in this dataset
            "label": int(row[0]) - 1,
            "title": row[1],
            "description": row[2],
        }
        yield key, example

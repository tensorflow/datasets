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

"""reddit_disentanglement dataset."""

import collections
import csv
import itertools
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{zhu2019did,
  title={Who did They Respond to? Conversation Structure Modeling using Masked Hierarchical Transformer},
  author={Zhu, Henghui and Nan, Feng and Wang, Zhiguo and Nallapati, Ramesh and Xiang, Bing},
  journal={arXiv preprint arXiv:1911.10666},
  year={2019}
}
"""

_DESCRIPTION = """
This dataset contains ~3M messages from reddit.
Every message is labeled with metadata. The task is to predict the id of its
parent message in the corresponding thread.
Each record contains a list of messages from one thread.
Duplicated and broken records are removed from the dataset.


Features are:
  - id - message id
  - text - message text
  - author - message author
  - created_utc - message UTC timestamp
  - link_id - id of the post that the comment relates to
Target:
  - parent_id - id of the parent message in the current thread
"""

_THREAD_KEY = "thread"
_MESSAGE_ID = "id"
_MESSAGE_TEXT = "text"
_MESSAGE_TIMESTAMP = "created_utc"
_MESSAGE_AUTHOR = "author"
_MESSAGE_LINK_ID = "link_id"
_MESSAGE_PARENT_ID = "parent_id"


def _read_csv(path):
  with tf.io.gfile.GFile(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row["id"]:  # Filter out broken lines in the original dataset
        yield row


def _deduplicate(data):
  """Remove duplicated records."""
  cnt = collections.Counter(row["id"] for row in data)
  nonuniq_ids = set(id for id, count in cnt.items() if count > 1)
  nonuniq_data = [row for row in data if row["id"] in nonuniq_ids]

  unique_data = [row for row in data if row["id"] not in nonuniq_ids]
  # Make sure same id records are next to each other for itertools.groupby
  nonuniq_data = sorted(nonuniq_data, key=lambda row: row["id"])
  for _, same_id_data in itertools.groupby(nonuniq_data, lambda row: row["id"]):
    same_id_data = list(same_id_data)
    if all(same_id_data[0] == x for x in same_id_data):
      unique_data.append(same_id_data[0])
    else:
      non_deleted_same_id_data = [
          row for row in same_id_data if row["author"] != "[deleted]"
      ]
      if len(non_deleted_same_id_data) != 1:
        raise ValueError("Found several message with id {} in the original"
                         " data".format(non_deleted_same_id_data[0]["id"]))
      unique_data.append(non_deleted_same_id_data[0])

  return sorted(
      unique_data, key=lambda row: (row["link_id"], row["created_utc"]))


class RedditDisentanglement(tfds.core.GeneratorBasedBuilder):
  """Reddit Disentanglement dataset."""

  VERSION = tfds.core.Version("2.0.0")
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  Download https://github.com/henghuiz/MaskedHierarchicalTransformer, decompress
  raw_data.zip and run generate_dataset.py with your reddit api credentials.
  Then put train.csv, val.csv and test.csv from the output directory into the
  manual folder.
  """

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _THREAD_KEY:
                tfds.features.Sequence(
                    tfds.features.FeaturesDict({
                        _MESSAGE_ID: tfds.features.Text(),
                        _MESSAGE_TEXT: tfds.features.Text(),
                        _MESSAGE_TIMESTAMP: tfds.features.Text(),
                        _MESSAGE_AUTHOR: tfds.features.Text(),
                        _MESSAGE_LINK_ID: tfds.features.Text(),
                        _MESSAGE_PARENT_ID: tfds.features.Text()
                    }))
        }),
        homepage="https://github.com/henghuiz/MaskedHierarchicalTransformer",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "path": os.path.join(dl_manager.manual_dir, "train.csv")
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={"path": os.path.join(dl_manager.manual_dir, "val.csv")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path": os.path.join(dl_manager.manual_dir, "test.csv")
            },
        ),
    ]

  def _generate_examples(self, path):
    """Yields examples."""
    data = list(_read_csv(path))
    data = _deduplicate(data)
    for link_id, one_topic_data in itertools.groupby(
        data, lambda row: row["link_id"]):
      one_topic_data = list(one_topic_data)
      for row in one_topic_data:
        row["text"] = row.pop("body")
      yield link_id, {_THREAD_KEY: one_topic_data}

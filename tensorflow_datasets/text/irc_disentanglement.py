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

"""irc_disentanglement dataset."""

import collections
import os
from typing import List

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@InProceedings{acl19disentangle,
  author    = {Jonathan K. Kummerfeld and Sai R. Gouravajhala and Joseph Peper and Vignesh Athreya and Chulaka Gunasekara and Jatin Ganhotra and Siva Sankalp Patel and Lazaros Polymenakos and Walter S. Lasecki},
  title     = {A Large-Scale Corpus for Conversation Disentanglement},
  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
  location  = {Florence, Italy},
  month     = {July},
  year      = {2019},
  doi       = {10.18653/v1/P19-1374},
  pages     = {3846--3856},
  url       = {https://aclweb.org/anthology/papers/P/P19/P19-1374/},
  arxiv     = {https://arxiv.org/abs/1810.11118},
  software  = {https://jkk.name/irc-disentanglement},
  data      = {https://jkk.name/irc-disentanglement},
}
"""
_DESCRIPTION = """
IRC Disentanglement dataset contains over 77,563 messages from Ubuntu IRC
channel.

Features include message id, message text and timestamp.
Target is list of messages that current message replies to.
Each record contains a list of messages from one day of IRC chat.
"""
_DOWNLOAD_URL = "https://github.com/jkkummerfeld/irc-disentanglement/zipball/fd379e9"
_DOWNLOAD_ARCHIVE_SUBDIR = os.path.join(
    "jkkummerfeld-irc-disentanglement-fd379e9", "data")

_IRC_DAY_KEY = "day"
_MESSAGE_ID = "id"
_MESSAGE_TEXT = "text"
_MESSAGE_TIMESTAMP = "timestamp"
_MESSAGE_PARENTS_IDS = "parents"


def _get_day_to_paths(data_dir):
  """Prepares paths to files with raw chat messages and replies annotations.

  Args:
    data_dir: directory containing files with data. directory can be

  Returns:
    day_to_paths: dict formatted date -> dict with paths
      day_to_paths[day_str]["text"] - path to file with raw chat messages
      day_to_paths[day_str]["annot"] - path to file with replies annotations.
  """
  day_to_paths = collections.defaultdict(dict)
  for filename in tf.io.gfile.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)
    day_str = filename[:len("YYYY-MM-DD")]  # e.g. 2004-12-25.train-c.raw.txt

    if "raw" in filename:
      day_to_paths[day_str]["text"] = filepath
    if "annotation" in filename:
      day_to_paths[day_str]["annot"] = filepath

  return day_to_paths


def _read_texts_file(path):
  with tf.io.gfile.GFile(path, "r") as f:
    return [line.strip() for line in f]


def _read_annot_file(path):
  """Reads file with replies annotation."""
  with tf.io.gfile.GFile(path, "r") as f:
    return [(int(first), int(second)) for first, second, _ in map(str.split, f)]


def _parse_out_timestamps(raw_texts, day_str):
  """Parsing timestamps from IRC chat messages.

  Similar logic is implemented here.
  https://github.com/jkkummerfeld/irc-disentanglement/blob/master/src/disentangle.py#L174

  Args:
    raw_texts: list of raw chat messages.
    day_str: formatted date string.

  Returns:
    texts: list of texts without timestamps.
    timestamps: list of formatted timestamps
  """
  prev_hours = 0
  timestamps, texts = [], []
  for raw_text in raw_texts:
    if raw_text.startswith("["):  # Regular messsages e.g. "[04:13]<xxx>: Hi!"
      hours = int(raw_text[1:3])
      mins = int(raw_text[4:6])

      # 12h format -> 24h format
      if hours < prev_hours:  # All messages belong to the same day and are
        hours += 12  # chronologically ordered, but AM/PM info is absent
      prev_hours = hours

      timestamps.append("{}_{:02}_{:02}".format(day_str, hours, mins))
      raw_text = raw_text[7:]
    else:  # System messages e.g. "=== xxx has joned #ubuntu"
      timestamps.append("")

    texts.append(raw_text)

  return texts, timestamps


def _get_msg_id(day, line_num):
  return "{}_{:05}".format(day, line_num)


def _prepare_examples(texts_file_path, annot_file_path, day_str):
  """Prepares examples for 1 day."""
  # Read raw data
  raw_texts = _read_texts_file(texts_file_path)
  annotations = _read_annot_file(annot_file_path)

  # Construct replies graph
  idx_to_parents = {idx: [] for idx in range(len(raw_texts))}
  for parent_msg_idx, msg_idx in annotations:
    idx_to_parents[msg_idx].append(parent_msg_idx)

  texts, timestamps = _parse_out_timestamps(raw_texts, day_str)

  for line_idx, parents in idx_to_parents.items():
    parents_ids = [_get_msg_id(day_str, parent) for parent in parents]
    yield {
        _MESSAGE_ID: _get_msg_id(day_str, line_idx),
        _MESSAGE_TEXT: texts[line_idx],
        _MESSAGE_TIMESTAMP: timestamps[line_idx],
        _MESSAGE_PARENTS_IDS: parents_ids
    }


class IrcDisentanglement(tfds.core.GeneratorBasedBuilder):
  """IRC Disentanglement dataset."""

  VERSION = tfds.core.Version("2.0.0")

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _IRC_DAY_KEY:
                tfds.features.Sequence(
                    tfds.features.FeaturesDict({
                        _MESSAGE_ID:
                            tfds.features.Text(),
                        _MESSAGE_TEXT:
                            tfds.features.Text(),
                        _MESSAGE_TIMESTAMP:
                            tfds.features.Text(),
                        _MESSAGE_PARENTS_IDS:
                            tfds.features.Sequence(tfds.features.Text()),
                    }))
        }),
        homepage="https://jkk.name/irc-disentanglement",
        citation=_CITATION,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    base_dir = dl_manager.download_and_extract(_DOWNLOAD_URL)
    data_dir = os.path.join(base_dir, _DOWNLOAD_ARCHIVE_SUBDIR)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "day_to_paths":
                    _get_day_to_paths(os.path.join(data_dir, "train"))
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "day_to_paths": _get_day_to_paths(
                    os.path.join(data_dir, "dev"))
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "day_to_paths":
                    _get_day_to_paths(os.path.join(data_dir, "test"))
            },
        ),
    ]

  def _generate_examples(self, day_to_paths):
    """Yields examples."""
    for day, paths in day_to_paths.items():
      yield day, {
          _IRC_DAY_KEY:
              list(_prepare_examples(paths["text"], paths["annot"], day))
      }

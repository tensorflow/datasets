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

"""BookSum summarization dataset."""

import json
import logging
import os
from typing import Dict, Iterator, Text, Tuple

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
BookSum: A Collection of Datasets for Long-form Narrative Summarization

This implementation currently only supports book and chapter summaries.

GitHub: https://github.com/salesforce/booksum
"""

_CITATION = """\
@article{kryscinski2021booksum,
      title={BookSum: A Collection of Datasets for Long-form Narrative Summarization},
      author={Wojciech Kry{\'s}ci{\'n}ski and Nazneen Rajani and Divyansh Agarwal and Caiming Xiong and Dragomir Radev},
      year={2021},
      eprint={2105.08209},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
"""

_DOCUMENT = "document"
_SUMMARY = "summary"
_SPLIT_FILENAMES = {
    "book": {
        "train": "book_summaries_aligned_train.jsonl",
        "validation": "book_summaries_aligned_val.jsonl",
        "test": "book_summaries_aligned_test.jsonl",
    },
    "chapter": {
        "train": "chapter_summary_aligned_train_split.jsonl",
        "validation": "chapter_summary_aligned_val_split.jsonl",
        "test": "chapter_summary_aligned_test_split.jsonl",
    },
}


class BooksumConfig(tfds.core.BuilderConfig):
  """BuilderConfig for BooksumConfig."""

  def __init__(self, *, granularity=None, **kwargs):
    """BuilderConfig for BooksumConfig.

    Args:
      granularity: str ("book", "chapter")
      **kwargs: keyword arguments forwarded to super.
    """
    super(BooksumConfig, self).__init__(**kwargs)
    self.granularity = granularity


class Booksum(tfds.core.GeneratorBasedBuilder):
  """Booksum dataset builder."""

  VERSION = tfds.core.Version("1.0.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release.",
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = """\
  1) Go to https://github.com/salesforce/booksum, and run steps 1-3. Place the
     whole `booksum` git project in the manual folder.
  2) Download the chapterized books from https://storage.cloud.google.com/sfr-books-dataset-chapters-research/all_chapterized_books.zip
     and unzip to the manual folder.

  The manual folder should contain the following directories:

      - `booksum/`
      - `all_chapterized_books/`

  Note: Because the BookSum dataset is based on the availability of web-scraped
  data and may be incomplete, the `_generate_examples` method will automatically
  skip missing entries.
  """
  BUILDER_CONFIGS = [
      BooksumConfig(
          name="book",
          description="Book-level summarization",
          granularity="book",
      ),
      BooksumConfig(
          name="chapter",
          description="chapter-level summarization",
          granularity="chapter",
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _DOCUMENT: tfds.features.Text(),
            _SUMMARY: tfds.features.Text(),
        }),
        supervised_keys=(_DOCUMENT, _SUMMARY),
        homepage="https://github.com/salesforce/booksum",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    granularity = self._builder_config.granularity
    alignments_base_path = os.path.join(
        dl_manager.manual_dir, "booksum", "alignments",
        f"{granularity}-level-summary-alignments")
    return {
        "train":
            self._generate_examples(
                alignments_path=os.path.join(
                    alignments_base_path,
                    _SPLIT_FILENAMES[granularity]["train"]),
                base_path=dl_manager.manual_dir,
                granularity=granularity),
        "validation":
            self._generate_examples(
                alignments_path=os.path.join(
                    alignments_base_path,
                    _SPLIT_FILENAMES[granularity]["validation"]),
                base_path=dl_manager.manual_dir,
                granularity=granularity),
        "test":
            self._generate_examples(
                alignments_path=os.path.join(
                    alignments_base_path,
                    _SPLIT_FILENAMES[granularity]["test"]),
                base_path=dl_manager.manual_dir,
                granularity=granularity),
    }

  def _generate_examples(
      self,
      alignments_path: tfds.typing.PathLike,
      base_path: tfds.typing.PathLike,
      granularity: Text,
  ) -> Iterator[Tuple[Text, Dict[Text, Text]]]:
    """Yields examples."""
    with tf.io.gfile.GFile(alignments_path, "r") as f:
      for i, line in enumerate(f.read().strip().splitlines()):
        example_data = json.loads(line)
        input_path = os.path.join(base_path,
                                  example_data[f"{granularity}_path"])
        summary_path = os.path.join(base_path, "booksum", "scripts",
                                    example_data["summary_path"])
        if not tf.io.gfile.exists(input_path):
          logging.info("Skipping missing input: %s", input_path)
          continue
        if not tf.io.gfile.exists(summary_path):
          logging.info("Skipping missing summary: %s", summary_path)
          continue
        with tf.io.gfile.GFile(input_path, "r") as f:
          input_text = f.read().strip()
        with tf.io.gfile.GFile(summary_path, "r") as f:
          summary_text = " ".join(json.loads(f.read())["summary"]).strip()
        yield str(i), {
            _DOCUMENT: input_text,
            _SUMMARY: summary_text,
        }

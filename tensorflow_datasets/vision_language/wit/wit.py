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

"""Wikipedia-based Image Text (WIT) Dataset."""

from __future__ import annotations

import csv
import os
import sys

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Wikipedia-based Image Text (WIT) Dataset is a large multimodal multilingual
dataset. WIT is composed of a curated set of 37.6 million entity rich image-text
examples with 11.5 million unique images across 108 Wikipedia languages. Its
size enables WIT to be used as a pretraining dataset for multimodal machine
learning models.
"""

_CITATION = """
@article{srinivasan2021wit,
  title={WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning},
  author={Srinivasan, Krishna and Raman, Karthik and Chen, Jiecao and Bendersky, Michael and Najork, Marc},
  journal={arXiv preprint arXiv:2103.01913},
  year={2021}
}
"""


class Wit(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wit dataset."""

  VERSION = tfds.core.Version("1.1.0")
  RELEASE_NOTES = {
      "1.0.0": "Initial release. It loads the WIT dataset from "
               "https://storage.googleapis.com/gresearch/wit/",
      "1.1.0": "Added `val` and `test` splits."
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "language": tfds.features.Text(),
            "page_url": tfds.features.Text(),
            "image_url": tfds.features.Text(),
            "page_title": tfds.features.Text(),
            "section_title": tfds.features.Text(),
            "hierarchical_section_title": tfds.features.Text(),
            "caption_reference_description": tfds.features.Text(),
            "caption_attribution_description": tfds.features.Text(),
            "caption_alt_text_description": tfds.features.Text(),
            "mime_type": tfds.features.Text(),
            "original_height": tf.int32,
            "original_width": tf.int32,
            "is_main_image": tf.bool,
            "attribution_passes_lang_id": tf.bool,
            "page_changed_recently": tf.bool,
            "context_page_description": tfds.features.Text(),
            "context_section_description": tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage="https://github.com/google-research-datasets/wit/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    wit_homepage = "https://storage.googleapis.com/gresearch/wit/"
    wit_train_urls_to_download = [
        os.path.join(wit_homepage, f"wit_v1.train.all-0000{i}-of-00010.tsv.gz")
        for i in range(10)
    ]
    wit_val_urls_to_download = [
        os.path.join(wit_homepage, f"wit_v1.val.all-0000{i}-of-00005.tsv.gz")
        for i in range(5)
    ]
    wit_test_urls_to_download = [
        os.path.join(wit_homepage, f"wit_v1.test.all-0000{i}-of-00005.tsv.gz")
        for i in range(5)
    ]

    paths_per_split = dl_manager.download_and_extract({
        "train": wit_train_urls_to_download,
        "val": wit_val_urls_to_download,
        "test": wit_test_urls_to_download
    })

    return {
        "train": self._generate_examples(paths_per_split["train"]),
        "val": self._generate_examples(paths_per_split["val"]),
        "test": self._generate_examples(paths_per_split["test"]),
    }

  def _generate_examples(self, filepaths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam

    def _process_example(elements):
      # Create a unique key for each example.
      filename, row_number, row = elements
      image_url = row["image_url"]
      example_key = f"{filename}_{row_number}_{image_url}"
      return example_key, {
          "language":
              row["language"],
          "page_url":
              row["page_url"],
          "image_url":
              row["image_url"],
          "page_title":
              row["page_title"],
          "section_title":
              row["section_title"],
          "hierarchical_section_title":
              row["hierarchical_section_title"],
          "caption_reference_description":
              row["caption_reference_description"],
          "caption_attribution_description":
              row["caption_attribution_description"],
          "caption_alt_text_description":
              row["caption_alt_text_description"],
          "mime_type":
              row["mime_type"],
          "original_height":
              int(row["original_height"]),
          "original_width":
              int(row["original_width"]),
          "is_main_image":
              bool(row["is_main_image"]),
          "attribution_passes_lang_id":
              bool(row["attribution_passes_lang_id"]),
          "page_changed_recently":
              bool(row["page_changed_recently"]),
          "context_page_description":
              row["context_page_description"],
          "context_section_description":
              row["context_section_description"] or "",
      }

    def _read_rows(filename):
      # Limit to 100 MB. Value must be smaller than the C long maximum value.
      csv.field_size_limit(sys.maxsize)
      with epath.Path(filename).open() as f:
        csv_reader = csv.DictReader(
            f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        for i, row in enumerate(csv_reader):
          yield filename, i, row

    return (beam.Create(filepaths)
            | beam.FlatMap(_read_rows)
            | beam.Map(_process_example))

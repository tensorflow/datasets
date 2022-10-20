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

"""Librispeech language modeling dataset."""

import csv
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# TODO(b/228460133): Update with pages and doi when available.
_CITATION = """\
@inproceedings{breiner2022userlibri,
  title={UserLibri: A Dataset for ASR Personalization Using Only Text},
  author={Breiner, Theresa and Ramaswamy, Swaroop and Variani, Ehsan and Garg, Shefali and Mathews, Rajiv and Sim, Khe Chai and Gupta, Kilol and Chen, Mingqing and McConnaughey, Lara},
  booktitle={Proc. Interspeech 2022},
  year={2022}
}
"""

_DESCRIPTION = """\
UserLibri is a dataset containing paired audio-transcripts and additional text
only data for each of 107 users. It is a reformatting of the LibriSpeech dataset
found at http://www.openslr.org/12, reorganizing the data into users with an
average of 52 LibriSpeech utterances and about 6,700 text example sentences per
user. The UserLibriAudio class provides access to the audio-transcript pairs.
See UserLibriText for the additional text data.
"""

_URL = "https://www.kaggle.com/datasets/google/userlibri"
_DL_URL = tfds.download.Resource(
    url="https://www.kaggle.com/datasets/google/userlibri/download",
    extract_method=tfds.download.ExtractMethod.ZIP)

_KAGGLE_DATASET_ID = "google/userlibri"


def read_metadata_file(path):
  """Reads the tab-separated metadata from the path."""
  metadata = {}
  with epath.Path(path).open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
      # Collect metadata for each book ID.
      metadata[row["Book ID"]] = {
          "Num Text Examples": row["Num Text Examples"],
          "Average Words Per Example": row["Average Words Per Example"]
      }
  return metadata


class UserLibriText(tfds.core.BeamBasedBuilder):
  """UserLibri dataset of additional text-only data for each user."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "text":
                tfds.features.Text(
                    doc="A sentence of text extracted from a book"),
            "book_id":
                tfds.features.Text(doc="The book that this text was pulled from"
                                  ),
        }),
        supervised_keys=("text", "text"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict())

  def _split_generators(self, dl_manager):
    """Generates splits based on book_id, like '1234'."""
    extracted_dir = dl_manager.download_kaggle_data(
        competition_or_dataset=_KAGGLE_DATASET_ID)
    lm_dir = extracted_dir / "UserLibri/lm_data"
    # Load metadata file which is the same for both test-clean and test-other.
    metadata_file = lm_dir / "metadata.tsv"
    self.info.metadata["books"] = read_metadata_file(metadata_file)
    splits = []
    for book_txt in tf.io.gfile.listdir(lm_dir):
      if "metadata" in book_txt:
        continue
      book_id = book_txt.split("_")[0]
      splits.append(
          tfds.core.SplitGenerator(
              name=book_id,
              gen_kwargs={"book_train_file": os.path.join(lm_dir, book_txt)}))
    return splits

  def _build_pcollection(self, pipeline, book_train_file):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    return (pipeline
            | beam.Create([book_train_file])
            | beam.FlatMap(_generate_examples)
            | beam.Reshuffle())


def _generate_examples(book_train_file):
  """Yields text examples from the given book_train_file."""
  book_id = book_train_file.split("/")[-1].split("_")[0]
  with epath.Path(book_train_file).open() as f:
    for ind, line in enumerate(f):
      text = line.strip()
      if text:  # Skip empty lines.
        key = f"book_{book_id}_ex_{ind}"
        yield key, {"text": text, "book_id": book_id}

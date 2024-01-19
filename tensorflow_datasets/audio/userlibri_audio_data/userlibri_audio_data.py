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

"""Librispeech dataset."""

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
    extract_method=tfds.download.ExtractMethod.ZIP,
)

_KAGGLE_DATASET_ID = "google/userlibri"


def read_metadata_file(path):
  """Reads the tab-separated metadata from the path."""
  metadata = {}
  with epath.Path(path).open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
      # Collect metadata for each split_userID, for example
      # test-other_speaker-12-book-34.
      metadata[f'{row["Split"]}_{row["User ID"]}'] = {
          "Num Audio Examples": row["Num Audio Examples"],
          "Average Words Per Example": row["Average Words Per Example"],
      }
  return metadata


class UserLibriAudio(tfds.core.BeamBasedBuilder):
  """UserLibri dataset of paired audio transcripts."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id": tfds.features.Text(doc="The id of this unique utterance"),
            "user_id": tfds.features.Text(
                doc=(
                    "The user that this utterance belongs to (unique speaker"
                    " and book)"
                )
            ),
            "speaker_id": tfds.features.Text(
                doc="The speaker who read this utterance"
            ),
            "book_id": tfds.features.Text(
                doc="The book that this utterance is read from"
            ),
            "audio": tfds.features.Audio(
                sample_rate=16000,
                doc=(
                    "The audio clip containing a snippet from a book read aloud"
                ),
            ),
            "transcript": tfds.features.Text(
                doc="The text that the speaker read to produce the audio"
            ),
        }),
        supervised_keys=("audio", "transcript"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(
            sample_rate=16000,
        ),
    )

  def _split_generators(self, dl_manager):
    """Generates user splits like 'test-other_speaker-1234-book-5678'."""
    extracted_dir = dl_manager.download_kaggle_data(
        competition_or_dataset=_KAGGLE_DATASET_ID
    )
    audio_dir = extracted_dir / "UserLibri/audio_data"
    # Load metadata file which is the same for both test-clean and test-other.
    metadata_file = audio_dir / "metadata.tsv"
    self.info.metadata["users"] = read_metadata_file(metadata_file)
    splits = []
    for split in ["test-clean", "test-other"]:
      split_path = audio_dir / split
      for user_id in tf.io.gfile.listdir(split_path):
        split_and_user = f"{split}_{user_id}"
        splits.append(
            tfds.core.SplitGenerator(
                name=split_and_user,
                gen_kwargs={
                    "directory": os.path.join(audio_dir, split, user_id)
                },
            )
        )
    return splits

  def _build_pcollection(self, pipeline, directory):
    """Generates examples as dicts."""
    beam = tfds.core.lazy_imports.apache_beam
    return (
        pipeline
        | beam.Create([directory])
        | beam.FlatMap(_generate_userlibri_audio_examples)
        | beam.Reshuffle()
    )


def _generate_userlibri_audio_examples(user_directory):
  """Generate audio examples from a UserLibri directory."""
  transcripts_glob = os.path.join(user_directory, "*.txt")
  for transcript_file in tf.io.gfile.glob(transcripts_glob):
    with tf.io.gfile.GFile(os.path.join(user_directory, transcript_file)) as f:
      for line in f:
        line = line.strip()
        key, transcript = line.split(" ", 1)
        audio_file = f"{key}.flac"
        user_id = user_directory.split("/")[-1]
        _, speaker_id, _, book_id = user_id.split("-")
        example = {
            "id": key,
            "user_id": user_id,
            "speaker_id": speaker_id,
            "book_id": book_id,
            "audio": os.path.join(user_directory, audio_file),
            "transcript": transcript,
        }
        yield key, example

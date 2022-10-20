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

"""Mozilla Common Voice Dataset."""

import csv
import dataclasses
import functools
import io
import re
from typing import Any, Mapping, Sequence

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DEMOGRAPHICS_URL = "https://github.com/common-voice/common-voice/blob/main/web/src/stores/demographics.ts"
_SPLITS = {
    tfds.Split.TRAIN: "train",
    tfds.Split.TEST: "test",
    tfds.Split.VALIDATION: "validated",
    tfds.Split("dev"): "dev",
}
_GENDER_CLASSES = ("male", "female", "other")

_DATA_FOLDER_IN_ARCHIVE = epath.Path("cv-corpus-6.1-2020-12-11")
_AUDIO_FILE_REGEX = re.compile(r"^.+/([^/]+\.mp3)$")

_LANGUAGES = (
    "en",  # Keep English as first to have it as the default config.
    "ab",
    "ar",
    "as",
    "br",
    "ca",
    "cnh",
    "cs",
    "cv",
    "cy",
    "de",
    "dv",
    "el",
    "eo",
    "es",
    "et",
    "eu",
    "fa",
    "fi",
    "fr",
    "fy-NL",
    "ga-IE",
    "hi",
    "hsb",
    "hu",
    "ia",
    "id",
    "it",
    "ja",
    "ka",
    "kab",
    "ky",
    "lg",
    "lt",
    "lv",
    "mn",
    "mt",
    "nl",
    "or",
    "pa-IN",
    "pl",
    "pt",
    "rm-sursilv",
    "rm-vallader",
    "ro",
    "ru",
    "rw",
    "sah",
    "sl",
    "sv-SE",
    "ta",
    "th",
    "tr",
    "tt",
    "uk",
    "vi",
    "vot",
    "zh-CN",
    "zh-HK",
    "zh-TW",
)

_BEAM_NAMESPACE = "TFDS_COMMON_VOICE"


def _download_url(language: str) -> str:
  return ("https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4."
          f"s3.amazonaws.com/cv-corpus-6.1-2020-12-11/{language}.tar.gz")


class CommonVoiceConfig(tfds.core.BuilderConfig):
  """Configuration Class for Mozilla CommonVoice Dataset."""

  def __init__(self, *, language: str, **kwargs):
    """Constructs CommonVoiceConfig.

    Args:
     language: language Code of the Dataset to be used.
     **kwargs: keywords arguments forwarded to super
    """
    if language not in _LANGUAGES:
      raise ValueError((f"language {language} must be one of "
                        f"{', '.join(_LANGUAGES)}"))
    self.language = language

    super().__init__(
        name=language,
        description=f"Language Code: {language}",
        version=tfds.core.Version("2.0.0"),
        release_notes={
            "1.0.0": "Initial release.",
            "2.0.0": "Updated to corpus 6.1 from 2020-12-11.",
        },
        **kwargs,
    )


@dataclasses.dataclass()
class _IndexedExample:
  index: int
  clip_filename: str
  example: Mapping[str, Any]


def _parse_examples(examples_file_content: str) -> Sequence[_IndexedExample]:
  """Returns the examples in the given examples file content."""
  dataset = csv.DictReader(examples_file_content.splitlines(), delimiter="\t")
  examples = []
  for i, row in enumerate(dataset):
    path = row.get("path", None)
    if not path:
      continue
    try:
      example = {
          "client_id": row["client_id"],
          "sentence": row["sentence"],
          "upvotes": int(row["up_votes"]) if row["up_votes"] else 0,
          "downvotes": int(row["down_votes"]) if row["down_votes"] else 0,
          "age": row["age"],
          "gender": row["gender"] if row["gender"] else -1,
          "accent": row["accent"],
          "segment": row["segment"],
      }
      examples.append(
          _IndexedExample(index=i, example=example, clip_filename=path))
    except KeyError as e:
      raise ValueError(f"Could not parse row: {row}") from e
  return examples


class CommonVoice(tfds.core.GeneratorBasedBuilder):
  """Mozilla Common Voice Dataset."""
  BUILDER_CONFIGS = tuple(CommonVoiceConfig(language=l) for l in _LANGUAGES)

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=("Mozilla Common Voice Dataset"),
        features=tfds.features.FeaturesDict({
            "client_id":
                tfds.features.Text(doc="Hashed UUID of a given user"),
            "upvotes":
                tfds.features.Scalar(
                    tf.int32,
                    doc="Number of people who said audio matches the text"),
            "downvotes":
                tfds.features.Scalar(
                    tf.int32,
                    doc="Number of people who said audio does not match text"),
            "age":
                tfds.features.Text(
                    doc=("Age bucket of the speaker (e.g. teens, or fourties), "
                         f"see {_DEMOGRAPHICS_URL}")),
            "gender":
                tfds.features.ClassLabel(
                    names=_GENDER_CLASSES, doc="Gender of the speaker"),
            "accent":
                tfds.features.Text(
                    doc=f"Accent of the speaker, see {_DEMOGRAPHICS_URL}"),
            "segment":
                tfds.features.Text(
                    doc=("If sentence belongs to a custom dataset segment, "
                         "it will be listed here")),
            "sentence":
                tfds.features.Text(doc="Supposed transcription of the audio"),
            "voice":
                tfds.features.Audio(),
        }),
        homepage="https://voice.mozilla.org/en/datasets",
        license="https://github.com/common-voice/common-voice/blob/main/LICENSE",
    )

  def _split_generators(self, dl_manager, pipeline):
    """Returns generators for each split in the dataset."""
    beam = tfds.core.lazy_imports.apache_beam

    language = self.builder_config.language
    dl_path = dl_manager.download(_download_url(language))

    examples_per_file = {}
    for path_within_archive, file_obj in dl_manager.iter_archive(dl_path):
      if not path_within_archive.endswith(".tsv"):
        continue
      examples_per_file[path_within_archive] = _parse_examples(
          file_obj.read().decode("utf-8"))

    clips_pipeline = self._clips_pipeline(
        pipeline=pipeline, name="clips", dl_manager=dl_manager, dl_path=dl_path)

    generators = {}
    generate_examples = beam.ptransform_fn(self._generate_examples)
    for split, split_filename in _SPLITS.items():
      filename = _DATA_FOLDER_IN_ARCHIVE / language / f"{split_filename}.tsv"
      examples = examples_per_file.get(str(filename), None)
      if not examples:
        continue
      generators[split] = pipeline | f"{split}-{language}" >> generate_examples(
          clips_pipeline=clips_pipeline, examples=examples)
    return generators

  def _clips_pipeline(self, pipeline, name, dl_manager, dl_path):
    beam = tfds.core.lazy_imports.apache_beam
    counter = functools.partial(beam.metrics.Metrics.counter, _BEAM_NAMESPACE)

    def _read_clips(dl_path):
      for filename, fobj in dl_manager.iter_archive(dl_path):
        if not filename.endswith(".mp3"):
          counter("clips_pipeline_non_mp3").inc()
          continue
        match = _AUDIO_FILE_REGEX.match(filename)
        if not match:
          counter("clips_pipeline_no_regex_match").inc()
          continue
        clip_filename = match.group(1)
        if not clip_filename:
          counter("clips_pipeline_empty_filename").inc()
          continue
        counter("clips_pipeline_clips").inc()
        yield clip_filename, io.BytesIO(fobj.read())

    return (pipeline
            | f"{name} - Collection of clips" >> beam.Create([dl_path])
            | f"{name} - Read clips" >> beam.FlatMap(_read_clips))

  def _generate_examples(
      self,
      pipeline,
      clips_pipeline,
      examples: Sequence[_IndexedExample],
  ):
    """Generate Voice samples and statements given the data paths.

    Args:
      pipeline: Beam pipeline
      clips_pipeline: Beam pipeline with a stage that outputs a all audio clips
        keyed by the clip filename.
      examples: the examples in the split for which we need to generate
        examples.

    Returns:
      pipeline that produces dataset.
    """
    beam = tfds.core.lazy_imports.apache_beam
    counter = functools.partial(beam.metrics.Metrics.counter, _BEAM_NAMESPACE)

    def _process_join(el):
      try:
        (_, values) = el
        examples = values["examples"]
        if len(examples) != 1:
          counter(f"{len(examples)}_examples").inc()
          return
        indexed_example = examples[0]

        clips = values["clips"]
        if len(clips) != 1:
          counter("{len(clips)}_clips").inc()
          return
        clip = clips[0]

      except ValueError as e:
        raise ValueError(f"Unpacking element {el} failed") from e
      example = indexed_example.example.copy()
      example["voice"] = clip
      yield indexed_example.index, example

    examples_pipeline = (
        pipeline
        | "Collection of examples" >> beam.Create([[ex.clip_filename, ex]
                                                   for ex in examples]))

    return ({
        "examples": examples_pipeline,
        "clips": clips_pipeline
    }
            | "Group by clip path" >> beam.CoGroupByKey()
            | "Reshuffle" >> beam.Reshuffle()
            | "Process and yield examples" >> beam.FlatMap(_process_join))

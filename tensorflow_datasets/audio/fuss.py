# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""FUSS dataset."""

import os
from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = r"""\
@inproceedings{wisdom2020fuss,
  title = {What's All the {FUSS} About Free Universal Sound Separation Data?},
  author = {Scott Wisdom and Hakan Erdogan and Daniel P. W. Ellis and Romain Serizel and Nicolas Turpault and Eduardo Fonseca and Justin Salamon and Prem Seetharaman and John R. Hershey},
  year = {2020},
  url = {https://arxiv.org/abs/2011.00803},
}

@inproceedings{fonseca2020fsd50k,
  author = {Eduardo Fonseca and Xavier Favory and Jordi Pons and Frederic Font Corbera and Xavier Serra},
  title = {{FSD}50k: an open dataset of human-labeled sound events},
  year = {2020},
  url = {https://arxiv.org/abs/2010.00475},
}
"""

_DESCRIPTION = """\
The Free Universal Sound Separation (FUSS) Dataset is a database of arbitrary
sound mixtures and source-level references, for use in experiments on arbitrary
sound separation.

This is the official sound separation data for the DCASE2020 Challenge Task 4:
Sound Event Detection and Separation in Domestic Environments.

Overview: FUSS audio data is sourced from a pre-release of Freesound dataset
known as (FSD50k), a sound event dataset composed of Freesound content annotated
with labels from the AudioSet Ontology. Using the FSD50K labels, these source
files have been screened such that they likely only contain a single type of
sound. Labels are not provided for these source files, and are not considered
part of the challenge. For the purpose of the DCASE Task4 Sound Separation and
Event Detection challenge,  systems should not use FSD50K labels, even though
they may become available upon FSD50K release.

To create mixtures, 10 second clips of sources are convolved with simulated room
impulse responses and added together. Each 10 second mixture contains between
1 and 4 sources. Source files longer than 10 seconds are considered "background"
sources. Every mixture contains one background source, which is active for the
entire duration. We provide: a software recipe to create the dataset, the room
impulse responses, and the original source audio.
"""

_URL = "https://github.com/google-research/sound-separation/blob/master/datasets/fuss/FUSS_license_doc/README.md"
_DL_METADATA = {
    "reverberant":
        ("https://zenodo.org/record/3743844/files/FUSS_ssdata_reverb.tar.gz",
         "ssdata_reverb"),
    "unprocessed":
        ("https://zenodo.org/record/3743844/files/FUSS_ssdata.tar.gz", "ssdata"
        ),
}


class Fuss(tfds.core.GeneratorBasedBuilder):
  """FUSS: Free Universal Sound Separation dataset."""

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name="reverberant",
          description="Default reverberated audio.",
          version=tfds.core.Version("1.2.0")),
      tfds.core.BuilderConfig(
          name="unprocessed",
          description="Unprocessed audio without additional reverberation.",
          version=tfds.core.Version("1.2.0")),
  ]

  def _info(self):
    source_labels = ["background0", "foreground0", "foreground1", "foreground2"]
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "mixture_audio":
                tfds.features.Audio(
                    file_format="wav",
                    shape=(160000,),
                    sample_rate=16000,
                    dtype=tf.int16),
            "sources":
                tfds.features.Sequence({
                    "audio":
                        tfds.features.Audio(
                            file_format="wav",
                            shape=(160000,),
                            sample_rate=16000,
                            dtype=tf.int16),
                    "label":
                        tfds.features.ClassLabel(names=source_labels),
                }),
            "segments":
                tfds.features.Sequence({
                    "start_time_seconds": tf.float32,
                    "end_time_seconds": tf.float32,
                    "label": tf.string
                }),
            "jams":
                tf.string,
            "id":
                tf.string,
        }),
        supervised_keys=("mixture_audio", "sources"),
        homepage=_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    url, extracted_dirname = _DL_METADATA[self.builder_config.name]
    base_dir = dl_manager.download_and_extract(url)
    splits = []
    for split_name, split_dir in [(tfds.Split.TRAIN, "train"),
                                  (tfds.Split.VALIDATION, "validation"),
                                  (tfds.Split.TEST, "eval")]:
      splits.append(
          tfds.core.SplitGenerator(
              name=split_name,
              gen_kwargs={
                  "base_dir": os.path.join(base_dir, extracted_dirname),
                  "split": split_dir,
              }))
    return splits

  def _parse_segments(self, path):
    segments = []
    if not tf.io.gfile.exists(path):
      # Some segments files are missing in the "unprocessed" set.
      logging.info("Missing segments file: %s", path)
      return segments
    with tf.io.gfile.GFile(path) as f:
      for l in f:
        try:
          start, end, label = l.split()
        except ValueError:
          continue
        segments.append({
            "start_time_seconds": float(start),
            "end_time_seconds": float(end),
            "label": label
        })
    return segments

  def _generate_examples(self, base_dir, split):
    """Generates examples for the given split."""
    path = os.path.join(base_dir, "%s_example_list.txt" % split)
    split_dir = os.path.join(base_dir, split)
    with tf.io.gfile.GFile(path) as example_list:
      for line in example_list:
        paths = line.split()
        key = _basename_without_ext(paths[0])
        sources = []
        for p in paths[1:]:
          sources.append({
              "audio": os.path.join(base_dir, p),
              "label": _basename_without_ext(p).split("_")[0],
          })
        segments = self._parse_segments(os.path.join(split_dir, "%s.txt" % key))
        jams = tf.io.gfile.GFile(os.path.join(split_dir,
                                              "%s.jams" % key)).read()
        example = {
            "mixture_audio": os.path.join(base_dir, paths[0]),
            "sources": sources,
            "segments": segments,
            "jams": jams,
            "id": key,
        }
        yield key, example


def _basename_without_ext(p):
  basename, _ = os.path.splitext(os.path.basename(p))
  return basename

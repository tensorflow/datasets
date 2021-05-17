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

"""YesNo dataset."""

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@ONLINE {YesNo,
    author = "Created for the Kaldi Project",
    title  = "YesNo",
    url    = "http://www.openslr.org/1/"
}
"""

_DESCRIPTION = """\
Sixty recordings of one individual saying yes or no in Hebrew; each recording is eight words long.

The main point of the dataset is to provide an easy and fast way to test out the Kaldi scripts for free.

The archive "waves_yesno.tar.gz" contains 60 .wav files, sampled at 8 kHz.
All were recorded by the same male speaker, in Hebrew.
In each file, the individual says 8 words; each word is either the Hebrew for "yes" or "no",
so each file is a random sequence of 8 yes-es or noes.
There is no separate transcription provided; the sequence is encoded in the filename, with 1 for yes and 0 for no.
"""

_HOMEPAGE_URL = "https://www.openslr.org/1/"
_DOWNLOAD_URL = "http://www.openslr.org/resources/1/waves_yesno.tar.gz"


class YesNo(tfds.core.GeneratorBasedBuilder):
  """YesNo Dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "audio":
                tfds.features.Audio(file_format="wav", sample_rate=8000),
            "label":
                tfds.features.Sequence(
                    tfds.features.ClassLabel(names=["no", "yes"])),
            "audio/filename":
                tfds.features.Text()
        }),
        supervised_keys=("audio", "label"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({"waves_yesno": _DOWNLOAD_URL})
    path = os.path.join(dl_paths["waves_yesno"], "waves_yesno")
    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"path": path}),
    ]

  def _generate_examples(self, path):
    """Yields examples.

    Args:
       path: Path of the downloaded and extracted directory

    Yields:
       Next examples
    """
    for root, _, file_name in tf.io.gfile.walk(path):
      for fname in file_name:
        if fname.endswith(".wav"):  # select only .wav files
          # Example of audio file name: 0_0_1_1_0_1_0_0.wav
          labels = fname.split(".")[0].split("_")
          labels = list(map(int, labels))
          key = fname
          example = {
              "audio": os.path.join(root, fname),
              "label": labels,
              "audio/filename": fname,
          }
          yield key, example

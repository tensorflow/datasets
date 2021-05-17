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

"""VCTK speech synthesis dataset."""

import os
from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{yamagishi2019vctk,
  author={Yamagishi, Junichi and Veaux, Christophe and MacDonald, Kirsten},
  title={{CSTR VCTK Corpus}: English Multi-speaker Corpus for {CSTR} Voice Cloning Toolkit (version 0.92)},
  publisher={University of Edinburgh. The Centre for Speech Technology Research (CSTR)},
  year=2019,
  doi={10.7488/ds/2645},
}
"""

_DESCRIPTION = """\
This CSTR VCTK Corpus includes speech data uttered by 110 English speakers with
various accents. Each speaker reads out about 400 sentences, which were selected
from a newspaper, the rainbow passage and an elicitation paragraph used for the
speech accent archive.

Note that the 'p315' text was lost due to a hard disk error.
"""

_URL = "https://doi.org/10.7488/ds/2645"
_DL_URL = "https://datashare.is.ed.ac.uk/bitstream/handle/10283/3443/VCTK-Corpus-0.92.zip"


class Vctk(tfds.core.GeneratorBasedBuilder):
  """VCTK speech synthesis dataset.

  The dataset is broken into two separate configs, each containing audio
  recorded using different microphones.  They are split this way for consistency
  with previous releases which only included a single microphone.
  """

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name="mic1",
          description="""
              Audio recorded using an omni-directional microphone (DPA 4035).
              Contains very low frequency noises.

              This is the same audio released in previous versions of VCTK:
              https://doi.org/10.7488/ds/1994
          """,
          version=tfds.core.Version("1.0.0"),
          release_notes={"1.0.0": "VCTK release 0.92.0."},
      ),
      tfds.core.BuilderConfig(
          name="mic2",
          description="""
              Audio recorded using a small diaphragm condenser microphone with
              very wide bandwidth (Sennheiser MKH 800).

              Two speakers, p280 and p315 had technical issues of the audio
              recordings using MKH 800.
          """,
          version=tfds.core.Version("1.0.0"),
          release_notes={"1.0.0": "VCTK release 0.92.0."},
      ),
  ]

  def _info(self):
    speaker_list = [
        "p225", "p226", "p227", "p228", "p229", "p230", "p231", "p232", "p233",
        "p234", "p236", "p237", "p238", "p239", "p240", "p241", "p243", "p244",
        "p245", "p246", "p247", "p248", "p249", "p250", "p251", "p252", "p253",
        "p254", "p255", "p256", "p257", "p258", "p259", "p260", "p261", "p262",
        "p263", "p264", "p265", "p266", "p267", "p268", "p269", "p270", "p271",
        "p272", "p273", "p274", "p275", "p276", "p277", "p278", "p279", "p280",
        "p281", "p282", "p283", "p284", "p285", "p286", "p287", "p288", "p292",
        "p293", "p294", "p295", "p297", "p298", "p299", "p300", "p301", "p302",
        "p303", "p304", "p305", "p306", "p307", "p308", "p310", "p311", "p312",
        "p313", "p314", "p315", "p316", "p317", "p318", "p323", "p326", "p329",
        "p330", "p333", "p334", "p335", "p336", "p339", "p340", "p341", "p343",
        "p345", "p347", "p351", "p360", "p361", "p362", "p363", "p364", "p374",
        "p376", "s5"
    ]
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "id":
                tf.string,
            "text":
                tfds.features.Text(),
            "speech":
                tfds.features.Audio(sample_rate=48000),
            "speaker":
                tfds.features.ClassLabel(names=speaker_list),
            "gender":
                tfds.features.ClassLabel(names=["F", "M"]),
            "accent":
                tfds.features.ClassLabel(names=[
                    "American", "Australian", "British", "Canadian", "English",
                    "Indian", "Irish", "NewZealand", "NorthernIrish",
                    "Scottish", "SouthAfrican", "Unknown", "Welsh"
                ]),
        }),
        supervised_keys=("text", "speech"),
        homepage=_URL,
        citation=_CITATION,
        metadata=tfds.core.MetadataDict(),
    )

  def _split_generators(self, dl_manager):
    extracted_dir = dl_manager.download_and_extract(_DL_URL)
    self._populate_metadata(extracted_dir)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"extracted_dir": extracted_dir},
        ),
    ]

  def _populate_metadata(self, extracted_dir):
    path = os.path.join(extracted_dir, "speaker-info.txt")
    speaker_info = tf.io.gfile.GFile(path).read()
    speaker_to_gender = {}
    speaker_to_accent = {}
    for line in speaker_info.splitlines()[1:]:
      fields = line.split()
      speaker, gender, accent = fields[0], fields[2], fields[3]
      speaker_to_gender[speaker] = gender
      speaker_to_accent[speaker] = accent
    self.info.metadata["speaker_info"] = speaker_info
    self.info.metadata["speaker_to_gender"] = speaker_to_gender
    self.info.metadata["speaker_to_accent"] = speaker_to_accent

  def _generate_examples(self, extracted_dir):
    """Yields examples."""
    speech_dir = "wav48_silence_trimmed"
    mic = "_%s" % self.builder_config.name
    speech_glob = os.path.join(extracted_dir, speech_dir, "*", "*%s.flac" % mic)
    for speech_path in tf.io.gfile.glob(speech_glob):
      text_path = speech_path.replace(speech_dir, "txt").split(mic)[0] + ".txt"
      key, _ = os.path.splitext(os.path.basename(text_path))
      if tf.io.gfile.exists(text_path):
        text = tf.io.gfile.GFile(text_path).read().strip()
      else:
        logging.info("No transcript found for utterance %s", key)
        text = ""
      speaker = key.split("_")[0]
      example = {
          "id": key,
          "text": text,
          "speech": speech_path,
          "speaker": speaker,
          "gender": self.info.metadata["speaker_to_gender"][speaker],
          "accent": self.info.metadata["speaker_to_accent"][speaker],
      }
      yield key, example

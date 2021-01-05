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

"""AccentDB dataset."""

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@InProceedings{ahamad-anand-bhargava:2020:LREC,
  author    = {Ahamad, Afroz  and  Anand, Ankit  and  Bhargava, Pranesh},
  title     = {AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition},
  booktitle      = {Proceedings of The 12th Language Resources and Evaluation Conference},
  month          = {May},
  year           = {2020},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5353--5360},
  url       = {https://www.aclweb.org/anthology/2020.lrec-1.659}
}"""

_DESCRIPTION = """
AccentDB is a multi-pairwise parallel corpus of structured and labelled
accented speech. It contains speech samples from speakers of 4 non-native
accents of English (8 speakers, 4 Indian languages); and also has a compilation
of 4 native accents of English (4 countries, 13 speakers) and a metropolitan
Indian accent (2 speakers). The dataset available here corresponds to release
titled accentdb_extended on https://accentdb.github.io/#dataset.
"""

_LABELS = [
    'american', 'australian', 'bangla', 'british', 'indian', 'malayalam',
    'odiya', 'telugu', 'welsh'
]

_DOWNLOAD_URL = 'https://drive.google.com/uc?export=download&id=1NO1NKQSpyq3DMLEwiqA-BHIqXli8vtIL'


class Accentdb(tfds.core.GeneratorBasedBuilder):
  """AccentDB dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'audio': tfds.features.Audio(file_format='wav', sample_rate=44100),
            'label': tfds.features.ClassLabel(names=_LABELS),
            'speaker_id': tf.string
        }),
        supervised_keys=('audio', 'label'),
        homepage='https://accentdb.github.io/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    extract_path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'extract_path': extract_path},
        ),
    ]

  def _generate_examples(self, extract_path):
    """Yields examples."""
    data_path = os.path.join(extract_path, 'data')
    for accent in tf.io.gfile.listdir(data_path):
      accent_path = os.path.join(data_path, accent)
      for speaker in tf.io.gfile.listdir(accent_path):
        speaker_path = os.path.join(accent_path, speaker)
        speaker_id = f'{accent}_{speaker}'
        for file in tf.io.gfile.listdir(speaker_path):
          filepath = os.path.join(speaker_path, file)
          key = f'{accent}_{speaker}_{file}'
          yield key, {
              'audio': filepath,
              'label': accent,
              'speaker_id': speaker_id,
          }

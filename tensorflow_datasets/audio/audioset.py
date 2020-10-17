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

"""Google AudioSet Dataset"""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{45857,
title   = {Audio Set: An ontology and human-labeled dataset for audio events},
author  = {Jort F. Gemmeke and Daniel P. W. Ellis and Dylan Freedman and Aren Jansen and Wade Lawrence and R. Channing Moore and Manoj Plakal and Marvin Ritter},
year    = {2017},
booktitle  = {Proc. IEEE ICASSP 2017},
address = {New Orleans, LA}
}
"""

_DESCRIPTION = """
The AudioSet dataset is a large-scale collection of human-labeled 10-second sound clips drawn from YouTube videos. 
To collect all our data we worked with human annotators who verified the presence of sounds they heard within YouTube segments. 
To nominate segments for annotation, we relied on YouTube metadata and content-based search. Some audio examples from Audioset
were skipped during the raw data extraction due to some videos being removed by the uploader at the time.
"""

_DOWNLOAD_LINK = 'https://storage.googleapis.com/bme590/william/audioset.tar.gz'

class Audioset(tfds.core.GeneratorBasedBuilder):
  """This dataset takes in a manual directory of 10-second .mp3 files taken from
  Youtube. It yields Audio using pydub AudioSegment and corresponding labels
  according to the CLASS_LABELS_CSV provided by Audioset.
  """

  VERSION = tfds.core.Version('0.1.0')
  MANUAL_DOWNLOAD_INSTRUCTIONS = 'give bucket path gs://bme590/william/manual'
  def _info(self):
    return tfds.core.DatasetInfo(
      builder=self,
      description=_DESCRIPTION,
      features=tfds.features.FeaturesDict({
        'audio': tfds.features.Audio(file_format=None, sample_rate=48000),
        'label': tfds.features.Tensor(shape=(None,), dtype=tf.int32)
      }),
      supervised_keys=('audio','label'),
      homepage='https://research.google.com/audioset/index.html',
      citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(_DOWNLOAD_LINK)
    return [
      tfds.core.SplitGenerator(
        name=tfds.Split.TRAIN,
        gen_kwargs={
          'data_dir': data_dir
        },
      ),
    ]

  def _generate_examples(self, data_dir=None):
    """Yields examples."""
    json = tfds.core.lazy_imports.json
    pydub = tfds.core.lazy_imports.pydub
    os = tfds.core.lazy_imports.os
    np = tfds.core.lazy_imports.numpy

    trimmed_audio_path = os.path.join(data_dir, 'trimmed_audio')
    id2label_path = os.path.join(data_dir, 'id2label.json')
    #gets list of files in folder given
    my_files = tf.io.gfile.listdir(trimmed_audio_path)
    #uses json to match ids to labels
    with tf.io.gfile.GFile(id2label_path, 'r') as read_file:
      datas = json.load(read_file)
    for f in my_files:
      try:
        label_list = []
        filepath = os.path.join(trimmed_audio_path, f)
        with tf.io.gfile.GFile(filepath, 'rb') as read_file:
          #passes bad mp3 files
          errorcheck = pydub.AudioSegment.from_file(read_file)
        ids = f.replace('.mp3','')
        for x in datas[ids]:
          for y in x:
            #gets multiple labels index
            label_list.append(y)
          label_tensor = np.zeros(527, dtype=np.int32)
          for i in label_list:
            # creates a tensor of zeros with ones at indices
            label_tensor[i] = 1
          break
        yield f, {
          'audio': filepath,
          'label': label_tensor,
        }
      except:
        pass

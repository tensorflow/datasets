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
import tensorflow_io as tfio
import os
import json
import numpy as np
from pydub import AudioSegment

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
To nominate segments for annotation, we relied on YouTube metadata and content-based search.
"""

class Audioset(tfds.core.GeneratorBasedBuilder):
  """This dataset takes in a manual directory of 10-second .mp3 files taken from Youtube.
  It yields Audio using pydub AudioSegment and corresponding labels according to the CLASS_LABELS_CSV provided by Audioset.
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
    data_dir = dl_manager.manual_dir
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
    TRIMMED_AUDIO_PATH = os.path.join(data_dir, 'trimmed_audio')
    ID2LABEL_PATH = os.path.join(data_dir, 'id2label.json')
    
    my_files = tf.io.gfile.listdir(TRIMMED_AUDIO_PATH) #gets list of files in folder given
    with tf.io.gfile.GFile(ID2LABEL_PATH, "r") as read_file: #uses json to match ids to labels
      datas = json.load(read_file)    
    for f in my_files:
      try:
        label_list = []
        filepath = os.path.join(TRIMMED_AUDIO_PATH,f)
        with tf.io.gfile.GFile(filepath, "rb") as read_file:
          errorcheck = AudioSegment.from_file(read_file) #ignores bad mp3 files
        ids = f.replace(".mp3","")
        for x in datas[ids]:
          for y in x:
            label_list.append(y) #gets multiple labels index that apply to audio in a list in label_list
          label_tensor = np.zeros(527, dtype=np.int32)
          for i in label_list:
            label_tensor[i] = 1 # creates a tensor of zeros with ones at indices that indicate positive for a label
          break
        yield f, {
          'audio': filepath,
          'label': label_tensor,
        }
      except:
        pass
    


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

'''Wikipedia Dump Dataset'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{
  author = {Ortman, Mike},
  title = {wikipedia-dump},
  year = {2018},
  howpublished = {\\url{https://www.kaggle.com/mikeortman/wikipedia-sentences}}
}\
"""

_DESCRIPTION = '''\
Collection of 7.8 million sentences (one per line) from August 2018 English Wikipedia dump. 
'''

class WikipediaDump(tfds.core.GeneratorBasedBuilder):
  '''Wikipedia dump dataset builder'''

  VERSION = tfds.core.Version('2.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder = self,
        description = _DESCRIPTION,
        features = tfds.features.FeaturesDict({'text': tfds.features.Text()}),
        supervised_keys = None,
        homepage = 'https://www.kaggle.com/mikeortman/wikipedia-sentences',
        citation = _CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    '''RETURNS SplitGenerators'''
    dl_paths = dl.manager.download_kaggle_data('Wikipedia sentences')

    data_dir = dl_manager.download({
            'sentences_train': dl_paths['wikisent2.txt'],
    })

    txt_path = data_dir
    
    with tf.io.gfile.GFile(txt_path, 'r') as f:
      text = f.read()

    # Since there's no official split, putting everything under training split

    return [
            tfds.core.SplitGenerator(
                name = tfds.Split.TRAIN,
                gen_kwargs = {
                    'split_key' : 'train',
                    'split_text' : text,
                },
            ),
    ]

    def _generate_examples(self, split_key, split_text):
      each_sentence = iter(text)
      for index, text in enumerate(each_sentence):
        yield index, {"text": split_text}

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

import tensorflow_datasets.public_api as tfds
import tensorflow as tf
import os
import glob
import pandas as pd

_CITATION = """
@inproceedings{45857,
title	= {Audio Set: An ontology and human-labeled dataset for audio events},
author	= {Jort F. Gemmeke and Daniel P. W. Ellis and Dylan Freedman and Aren Jansen and Wade Lawrence and R. Channing Moore and Manoj Plakal and Marvin Ritter},
year	= {2017},
booktitle	= {Proc. IEEE ICASSP 2017},
address	= {New Orleans, LA}
}
"""

_DESCRIPTION = """
The AudioSet dataset is a large-scale collection of human-labeled 10-second sound clips drawn from YouTube videos.
To collect all our data we worked with human annotators who verified the presence of sounds they heard within
YouTube segments. To nominate segments for annotation, we relied on YouTube metadata and content-based search.
"""

DOWNLOAD_PATH = "http://storage.googleapis.com/us_audioset/youtube_corpus/v1/features/features.tar.gz"
CLASS_LABELS_CSV = "http://storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/class_labels_indices.csv"


class AudioSet(tfds.core.GeneratorBasedBuilder):
  """AudioSet: Human labeled 10-second sound clips from Youtube"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
          'yt_id': tf.string,
          'start_sec':tf.int64,
          'end_sec':tf.int64,
          'labels':tfds.features.Sequence(tf.string),
        }),
        supervised_keys=('id','labels'),
        # Homepage of the dataset for documentation
        homepage='https://research.google.com/audioset/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    labelFile = dl_manager.download(CLASS_LABELS_CSV)

    extracted_path = dl_manager.download_and_extract(DOWNLOAD_PATH)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
              'record_dir_path': os.path.join(extracted_path,"audioset_v1_embeddings/unbal_train"),
              'label_csv':labelFile
            },
        ),

        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
              'record_dir_path': os.path.join(extracted_path,"audioset_v1_embeddings/bal_train"),
              'label_csv':labelFile
            },
        ),

        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
              'record_dir_path': os.path.join(extracted_path,"audioset_v1_embeddings/eval"),
              'label_csv':labelFile
            },
        ),
    ]

  def _generate_examples(self,record_dir_path,label_csv):
    """Yields examples."""
    tfrecords = glob.glob("{}/*".format(record_dir_path))
    df = pd.read_csv(label_csv)
    index = -1
    for record in tfrecords:
      raw_dataset = tf.data.TFRecordDataset(record)

      for raw_record in raw_dataset.take(1000):
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())
        int_labels = example.features.feature['labels'].int64_list.value

        labels = []

        for lab in int_labels:
          for label in df[df['index']==lab]['display_name'].get(lab).split(','):
            labels.append(label.strip())

        yt_id = example.features.feature['video_id'].bytes_list.value[0].decode("utf-8")
        start_sec = example.features.feature['start_time_seconds'].float_list.value[0]
        end_sec = example.features.feature['end_time_seconds'].float_list.value[0]

        index+=1
        yield index,{
          'yt_id': yt_id,
          'start_sec': start_sec,
          'end_sec': end_sec,
          'labels': labels
        }

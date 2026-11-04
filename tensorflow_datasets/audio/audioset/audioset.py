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

"""audioset dataset."""

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
AudioSet consists of an expanding ontology of 632 audio event classes and a
collection of 2,084,320 human-labeled 10-second sound clips drawn from YouTube
videos. The ontology is specified as a hierarchical graph of event categories,
covering a wide range of human and animal sounds, musical instruments and
genres, and common everyday environmental sounds.

By releasing AudioSet, we hope to provide a common, realistic-scale evaluation
task for audio event detection, as well as a starting point for a comprehensive
vocabulary of sound events.
"""

_CITATION = """
@inproceedings{45857,
  title	= {Audio Set: An ontology and human-labeled dataset for audio events},
  author = {Jort F. Gemmeke and Daniel P. W. Ellis and Dylan Freedman and Aren Jansen and Wade Lawrence and R. Channing Moore and Manoj Plakal and Marvin Ritter},
  year = {2017},
  booktitle	= {Proc. IEEE ICASSP 2017},
  address	= {New Orleans, LA}
}
"""

_DOWNLOAD_URL = 'http://storage.googleapis.com/us_audioset/youtube_corpus/v1/features/features.tar.gz'


class Audioset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Audioset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'labels':
                tfds.features.Sequence(tf.int64),
            'video_id':
                tf.string,
            'start_time_seconds':
                tf.float32,
            'end_time_seconds':
                tf.float32,
            'audio_embedding':
                tfds.features.Sequence(tfds.features.Sequence(tf.uint8, 128)),
        }),
        supervised_keys=('audio_embedding', 'labels'),
        homepage='https://research.google.com/audioset/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    examples_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    evaluation = self._generate_examples(examples_path /
                                         'audioset_v1_embeddings/eval')
    bal_train = self._generate_examples(examples_path /
                                        'audioset_v1_embeddings/bal_train')
    unbal_train = self._generate_examples(examples_path /
                                          'audioset_v1_embeddings/unbal_train')
    return {
        'evaluation': evaluation,
        'balanced_train': bal_train,
        'unbalanced_train': unbal_train,
    }

  def _generate_examples(self, path):
    """Yields examples.

    Args:
       path: Path of the downloaded and extracted directory

    Yields:
       Next examples
    """
    # Specification of the context features in the sequence example
    context_feature_spec = {
        'labels': tf.io.VarLenFeature(tf.int64),
        'video_id': tf.io.FixedLenFeature([], tf.string),
        'start_time_seconds': tf.io.FixedLenFeature([], tf.float32),
        'end_time_seconds': tf.io.FixedLenFeature([], tf.float32),
    }
    # Specification of the features in the sequence example
    example_feature_spec = {
        'audio_embedding': tf.io.FixedLenSequenceFeature([], tf.string),
    }
    for f in path.glob('*.tfrecord'):
      tfrecord = tf.data.TFRecordDataset(f)
      for row in tfrecord.as_numpy_iterator():
        context, sequence, _ = tf.io.parse_sequence_example(
            row,
            context_features=context_feature_spec,
            sequence_features=example_feature_spec)
        video_id: str = tf.compat.as_str_any(context['video_id'])
        start_time_seconds = context['start_time_seconds'].numpy()
        end_time_seconds = context['end_time_seconds'].numpy()
        key: str = f'{video_id}_{start_time_seconds}_{end_time_seconds}'
        audio_embedding = tf.io.decode_raw(sequence['audio_embedding'],
                                           tf.uint8)
        yield key, {
            'labels': tf.sparse.to_dense(context['labels']).numpy(),
            'video_id': video_id,
            'start_time_seconds': start_time_seconds,
            'end_time_seconds': end_time_seconds,
            'audio_embedding': audio_embedding.numpy(),
        }

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

# Lint as: python3
"""TeachFX Voice Sample Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.core import lazy_imports_lib
import numpy as np
import collections
import logging
import csv

_CITATION = """\
TeachFX
"""

_DESCRIPTION = """\
TeachFX voice samples
"""

_URL = "private"
_DL_URL = "private"
_SPLIT_URL = os.path.join(
	'gs://teachfx-532-kubeflowpipelines-default',
	'tensorflow_datasets',
	'manual',
	'teachfx')

SPLITS_URLS = {
    "train": os.path.join(_SPLIT_URL, "voice_sample_train.csv"),
    "validation": os.path.join(_SPLIT_URL, "voice_sample_validation.csv"),
    "test": os.path.join(_SPLIT_URL, "voice_sample_test.csv")
}


class TFXVoice(tfds.core.BeamBasedBuilder):
	"""TeachFX Voice Samples dataset."""

	VERSION = tfds.core.Version("0.0.0")
	SUPPORTED_VERSIONS = [VERSION]
	MANUAL_DOWNLOAD_INSTRUCTIONS = "Please download this bad boy"

	def _info(self):
		return tfds.core.DatasetInfo(
			builder=self,
			description=_DESCRIPTION,
			features=tfds.features.FeaturesDict({
				"speech":
					tfds.features.Audio(sample_rate=16000),
				"speaker_id":
					tf.string,
				"duration":
					tf.int64,
			}),
			homepage=_URL,
			citation=_CITATION,
			metadata=tfds.core.MetadataDict(sample_rate=16000,),
		)

	def _calculate_splits(self):
		"""Read the train/dev/test splits from split.txt file."""
		data_splits = collections.defaultdict(set)
		BASEPATH = 'gs://teachfx-532.appspot.com'
		for SPLIT_NAME, SPLIT_URL in SPLITS_URLS.items():
			with tf.io.gfile.GFile(SPLIT_URL) as f:
				reader = csv.DictReader(f)
				split = list(
				    map(lambda e: (os.path.join(BASEPATH, e['path']), e['speaker_id']), reader))
			data_splits[SPLIT_NAME] = split
		return data_splits

	def _split_generators(self, dl_manager):
		"""Returns SplitGenerators."""
		splits = self._calculate_splits()

		return [
			tfds.core.SplitGenerator(
				name=tfds.Split.TRAIN,
				gen_kwargs={
					'examples': splits['train']
				},
			),
			tfds.core.SplitGenerator(
				name=tfds.Split.VALIDATION,
				gen_kwargs={
					'examples': splits['validation']
				},
			),
			tfds.core.SplitGenerator(
				name=tfds.Split.TEST,
				gen_kwargs={
					'examples': splits['test']
				},
			),
		]

	def _build_pcollection(self, pipeline, examples):
		"""Generates examples as dicts."""
		beam = tfds.core.lazy_imports.apache_beam
		too_short, long_enough = (pipeline
								  | beam.Create(examples)
								  | beam.FlatMapTuple(_generate_example)
								  | beam.FlatMapTuple(_encode_audio)
								  | beam.Partition(_separate_less_than_5_sec, 2)
								  )
		unique_key_joined_short = (too_short
						| beam.GroupByKey()
						| beam.FlatMap(_join_short_audio)
						)
		unique_key_long_enough = (long_enough
						| beam.FlatMapTuple(_use_unique_key)
						)

		return ((unique_key_joined_short, unique_key_long_enough)
				| beam.Flatten()
				| beam.Reshuffle()
				)


def _use_unique_key(_key, example):
	key = example.pop("key")
	yield key, example


def _join_short_audio(grouped_example):
	speaker, examples = grouped_example
	examples = list(examples)
	# logging.info(examples)
	duration = 0.0
	speech = np.array([])
	key = ""
	i = 0
	while i < len(examples):
		speech = np.concatenate((speech, examples[i]['speech']))
		duration += examples[i]['duration']
		key += examples[i]['key']
		if duration > 5:
			example = {"speaker_id": speaker,
					   "speech": speech,
					   "duration": duration,
					  }
			yield key, example
			duration = 0.0
			speech = np.array([])
			key = ""
		i += 1
		if duration > 5:
			example = {"speaker_id": speaker,
					   "speech": speech,
					   "duration": duration}
			yield key, example


def _generate_example(path_to_file, speaker_id):
	key = hash(path_to_file)
	example = {
		"speaker_id": speaker_id,
		"speech": path_to_file,
		"key": key
	}
	yield speaker_id, example


def _encode_audio(key, example):
	SAMPLE_RATE = 16000
	if 'audiowebm' in example['speech']:
		file_format = 'webm'
	else:
		file_format = example['speech'].split(".")[-1]
	with tf.io.gfile.GFile(example['speech'], 'rb') as fobj:
		audio_segment = lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
			fobj, format=file_format)
	np_dtype = np.dtype(tf.int64.as_numpy_dtype)

	speech = np.array(audio_segment.set_frame_rate(
	    SAMPLE_RATE).get_array_of_samples()).astype(np_dtype)

	duration = len(speech) / SAMPLE_RATE
	example['duration'] = duration
	example['speech'] = speech
	yield example['speaker_id'], example

def _separate_less_than_5_sec(element, num_partitions):
	key, example = element
	return 1 if example['duration'] >= 5 else 0


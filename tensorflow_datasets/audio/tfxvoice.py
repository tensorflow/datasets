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
    "train": os.path.join(_SPLIT_URL, "voice_sample_wav_train.csv"),
    "validation": os.path.join(_SPLIT_URL, "voice_sample_wav_validation.csv"),
    "test": os.path.join(_SPLIT_URL, "voice_sample_wav_test.csv")
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
				    map(lambda e: (e['wav_path'], e['speaker_id']), reader))
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
		return (pipeline
				| beam.Create(examples)
				| beam.FlatMapTuple(_generate_example)
				| beam.Reshuffle()
				)

def _generate_example(path_to_file, speaker_id):

	def frame_generator(frame_duration_ms, audio, sample_rate):
		"""Generates audio frames from PCM audio data.

		Takes the desired frame duration in milliseconds, the PCM data, and
		the sample rate.

		Yields Frames of the requested duration.
		"""
		n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
		offset = 0
		while offset + n < len(audio):
			yield audio[offset:offset + n]
			offset += n


	def vad_collector(sample_rate,
					vad,
					frames):
		"""Filters out non-voiced audio frames.
		"""
		voiced_frames = []
		for frame in frames:
			is_speech = vad.is_speech(frame, sample_rate)
			if is_speech:
				voiced_frames += [frame]
		return np.concatenate(voiced_frames)

	SAMPLE_RATE = 16000
	np_dtype = np.dtype(tf.int64.as_numpy_dtype)
	print(path_to_file, speaker_id)
	with tf.io.gfile.GFile(path_to_file, 'rb') as fobj:
		audio_segment = lazy_imports_lib.lazy_imports.pydub.AudioSegment.from_file(
			fobj, format='wav')

	speech = np.array(audio_segment.set_frame_rate(
	    SAMPLE_RATE).get_array_of_samples()).astype(np_dtype)
	vad = lazy_imports_lib.lazy_imports.webrtcvad.Vad(3) #aggressiveness = 3
	frames = list(frame_generator(30, speech, SAMPLE_RATE))
	voiced_audio = list(vad_collector(SAMPLE_RATE, vad, frames))
	print("len audio", len(voiced_audio))
	#split into 5-10 sec chunks
	indices = list(range(0, len(voiced_audio) + 1, 16000*5))
	print("indices", indices)
	indices[len(indices)-1] = len(voiced_audio)
	for p in range(len(indices)-1):
		i, j = indices[p], indices[p+1]
		speech = np.array(voiced_audio[i: j]).astype(np_dtype)
		duration = (j-i) / SAMPLE_RATE

		example = {
			'duration' : duration,
			'speech' : speech,
			'speaker_id' : speaker_id
		}

	yield path_to_file + '%i.%i'%(i, j) , example




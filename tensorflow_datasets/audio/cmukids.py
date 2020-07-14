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
"""CMU Kids dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
import numpy as np
import collections
import logging

_CITATION = """\
{
Item Name:	The CMU Kids Corpus
Author(s):	Maxine Eskenazi, Jack Mostow, David Graff
LDC Catalog No.:	LDC97S63
ISBN:	1-58563-120-5
ISLRN:	566-795-587-797-8
Member Year(s):	1997
DCMI Type(s):	Sound
Sample Type:	1-channel pcm
Sample Rate:	16000
Data Source(s):	microphone speech
Application(s):	speech recognition
Language(s):	English
Language ID(s):	eng
}
"""

_DESCRIPTION = """\
This database is comprised of sentences read aloud by
children.  It was originally designed in order to create a training
set of children's speech for the SPHINX II automatic speech recognizer
for its used by the LISTEN project at Carnegie Mellon University.
This project uses the recognizer to follow children reading text from
a screen in order to be able to intervene when they are stuck or make
an error.  In the past, the recognizer had been trained on samples of
female speech.

	The children range in age from 6 to 11 (see details below) and
were in first through third grades (the 11-year-old was in 6th grade)
at the time of recording.  There were 24 male and 52 female
speakers.  Although the girls outnumber the boys, we feel that the
small difference in vocal tract length between the two at this age
should make the effect of this imbalance negligible.  There are 5180
utterances in all.
"""

_URL = "https://catalog.ldc.upenn.edu/LDC97S63"
_DL_URL = "https://www.isip.piconepress.com/projects/speech/databases/kids_speech/"
SPLITS_URL = os.path.join(
	'gs://teachfx-532-kubeflowpipelines-default',
	'tensorflow_datasets',
	'manual',
	'extracted',
	'TGZ.LDC97S63-cmu-kids.tgz',
	'splits.txt')


class CMUKids(tfds.core.BeamBasedBuilder):
	"""CMU Kids dataset."""

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
		with tf.io.gfile.GFile(SPLITS_URL) as f:
			for line in f:
				group, path = line.strip().split()
				split_name = {1: 'train', 2: 'validation',
							  3: 'test'}[int(group)]
				data_splits[split_name].add(path.strip())
		return data_splits

	def _split_generators(self, dl_manager):
		"""Returns SplitGenerators."""
		extract_path = os.path.join(
			'gs://teachfx-532-kubeflowpipelines-default',
			'tensorflow_datasets',
			'manual',
			'extracted',
			'TGZ.LDC97S63-cmu-kids.tgz',
			'cmu_kids',
			'kids')

		splits = self._calculate_splits()

		return [
			tfds.core.SplitGenerator(
				name=tfds.Split.TRAIN,
				gen_kwargs={
					'extract_path': extract_path,
					'file_names': splits['train']
				},
			),
			tfds.core.SplitGenerator(
				name=tfds.Split.VALIDATION,
				gen_kwargs={
					'extract_path': extract_path,
					'file_names': splits['validation']
				},
			),
			tfds.core.SplitGenerator(
				name=tfds.Split.TEST,
				gen_kwargs={
					'extract_path': extract_path,
					'file_names': splits['test']
				},
			),
		]

	def _build_pcollection(self, pipeline, extract_path, file_names):
		"""Generates examples as dicts."""
		beam = tfds.core.lazy_imports.apache_beam
		logging.info("EXTRACT_PATH", extract_path)
		logging.info("FILE_NAMES", file_names)
		too_short, long_enough = (pipeline
								  | beam.Create([(extract_path, filename) for filename in file_names])
								  | beam.FlatMapTuple(_generate_example)
								  | beam.Partition(_separate_less_than_5_sec, 2)
								  )
		joined_short = (too_short
						| beam.GroupByKey()
						| beam.FlatMap(_join_short_audio)
						)
		return ((joined_short, long_enough)
				| beam.Flatten()
				| beam.Reshuffle()
				)


def _join_short_audio(grouped_example):
	key, examples = grouped_example
	examples = list(examples)
	# logging.info(examples)
	duration = 0.0
	speech = np.array([])
	i = 0
	while i < len(examples) :
		speech = np.concatenate((speech, examples[i]['speech']))
		duration += examples[i]['duration']
		if duration > 5:
			example = {"speaker_id": key,
					   "speech": speech, "duration": duration}
			yield key, example
			duration = 0.0
			speech = np.array([])
		i += 1
		if duration > 5:
			example = {"speaker_id": key,
					   "speech": speech, "duration": duration}
			yield key, example


def _generate_example(extract_path, file_name):
	path_to_file = os.path.join(extract_path, file_name)
	speaker_id = parse_speaker_id(file_name)
	with tf.io.gfile.GFile(path_to_file, 'rb') as f:
		header, content = get_header_content(f)
	example = {
		"speaker_id": speaker_id,
		"speech": content,
		"duration": len(content)/header['sample_rate']
	}
	yield speaker_id, example


def _separate_less_than_5_sec(element, num_partitions):
	key, example = element
	return 1 if example['duration'] >= 5 else 0


def parse_speaker_id(filename):
	"""
			speaker_id/signal/filename
	"""
	return filename.split("/")[0]


def parse_sph_header(fh):
	import re
	"""Read the file-format header for an sph file

	The SPH header-file is exactly 1024 bytes at the head of the file,
	there is a simple textual format which AFAIK is always ASCII, but
	we allow here for latin1 encoding.  The format has a type declaration
	for each field and we only pay attention to fields for which we
	have some understanding.

	returns dictionary describing the format
	"""
	file_format = {
		'sample_rate': 8000,
		'channel_count': 1,
		'sample_byte_format': '01',  # little-endian
		'sample_n_bytes': 2,
		'sample_sig_bits': 16,
		'sample_coding': 'pcm',
	}
	end = b'end_head'
	NAME_MATCH = re.compile(
		r'^[a-zA-Z][a-zA-Z0-9]*([_][a-zA-Z][a-zA-Z0-9]*)*$')
	for line in fh.read(1024).splitlines():
		if line.startswith(end):
			break
		line = line.decode('latin-1')
		try:
			key, format, value = line.split(None, 3)
		except (ValueError, KeyError, TypeError) as err:
			pass
		else:
			key, format, value = line.split(None, 3)
			if not NAME_MATCH.match(key):
				# we'll ignore invalid names for now...
				continue
			if format == '-i':
				value = int(value, 10)
			file_format[key] = value
	return file_format


def get_header_content(fh):
	header = parse_sph_header(fh)
	content = fh.read()
	if header['sample_n_bytes'] == 1:
		np_format = np.uint8
	elif header['sample_n_bytes'] == 2:
		np_format = np.int16
	elif header['sample_n_bytes'] == 4:
		np_format = np.int32
	else:
		raise RuntimeError(
			"Unrecognized byte count: %s", header['sample_n_bytes']
		)
	remainder = len(content) % header['sample_n_bytes']
	if remainder:
		content = content[:-remainder]
	content = np.frombuffer(content, dtype=np_format)
	if header['sample_byte_format'] == '10':
		# deal with big-endian data-files as wav is going to expect little-endian
		content = content.byteswap()
	return header, content

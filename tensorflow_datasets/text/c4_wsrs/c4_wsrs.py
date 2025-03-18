# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""C4-WSRS dataset."""

from __future__ import annotations
import collections
import csv
from typing import Mapping, Sequence
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.c4_wsrs import c4_wsrs_utils

WSRSFeatures = c4_wsrs_utils.WSRSFeatures

_ABBREV_EXPANSION_DICT_URI = 'gs://gresearch/deciphering_clinical_abbreviations/abbreviation_expansion_dictionary.csv'

_DESCRIPTION = """\
A medical abbreviation expansion dataset which applies web-scale reverse
substitution (wsrs) to the C4 dataset, which is a colossal, cleaned version of
Common Crawl's web crawl corpus.

The original source is the Common Crawl dataset: https://commoncrawl.org
"""


class C4WSRSConfig(tfds.core.BuilderConfig):
  """BuilderConfig for C4-WSRS dataset."""

  def __init__(
      self,
      name: str,
      max_sentences_per_snippet: int,
      max_snippet_char_len: int,
      alpha_keep_no_rs: float,
      alpha_keep_rs: float,
      subsitution_rate: float,
      min_snippet_token_len: int,
      num_snippets_per_substitution: int,
      **kwargs,
  ):
    """Initializes the BuilderConfig for C4-WSRS.

    Args:
      name: The name for the config.
      max_sentences_per_snippet: The maximum number of sentences that can be
        combined into a single snippet. The number of sentences combined into
        each snippet will be a randomly sampled integer from 1 to
        max_sentences_per_snippet.
      max_snippet_char_len: The maximum number of characters an original snippet
        can be composed of.
      alpha_keep_no_rs: Alpha value used to compute the probability of keeping a
        snippet containing no reverse substitutions. The complete formula is p =
        (n+1)**-alpha where n is the count of previously kept snippets from the
        same document.
      alpha_keep_rs: Alpha value used to compute the probability of keeping a
        snippet containing a particular abbreviation-expansion reverse
        substitution candidate. The complete formula is p = (n+1)**-alpha where
        n is the count of previously kept snippets from the same document
        containing the same reverse substitution candidate.
      subsitution_rate: The rate at which expansions should be substituted for
        abbreviations.
      min_snippet_token_len: The minimum number of tokens an abbreviated snippet
        can be composed of.
      num_snippets_per_substitution: The number of snippets to sample for each
        unique abbreviation-expansion substitution.
      **kwargs: keyword arguments forwarded to super.
    """
    super().__init__(name=name, **kwargs)
    self.max_sentences_per_snippet = max_sentences_per_snippet
    self.max_snippet_char_len = max_snippet_char_len
    self.alpha_keep_no_rs = alpha_keep_no_rs
    self.alpha_keep_rs = alpha_keep_rs
    self.subsitution_rate = subsitution_rate
    self.min_snippet_token_len = min_snippet_token_len
    self.num_snippets_per_substitution = num_snippets_per_substitution


class C4WSRS(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for C4-WSRS dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
      C4WSRSConfig(
          'default',
          max_sentences_per_snippet=3,
          max_snippet_char_len=1024,
          alpha_keep_no_rs=1.5,
          alpha_keep_rs=1.0,
          subsitution_rate=0.95,
          min_snippet_token_len=3,
          num_snippets_per_substitution=4000,
          description='Default C4-WSRS dataset.',
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features = {
        'original_snippet': tfds.features.Text(),
        'abbreviated_snippet': tfds.features.Text(),
    }
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        homepage='https://github.com/google-research/google-research/tree/master/deciphering_clinical_abbreviations',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    abbreviation_expansions_dict_file = dl_manager.download(
        _ABBREV_EXPANSION_DICT_URI
    )
    abbreviations_by_expansion = collections.defaultdict(list)
    with tf.io.gfile.GFile(abbreviation_expansions_dict_file) as f:
      reader = csv.reader(f)
      for row in reader:
        abbrev, exp = row
        abbreviations_by_expansion[exp].append(abbrev)
    return {
        'train': self._generate_examples('train', abbreviations_by_expansion),
        'validation': self._generate_examples(
            'validation', abbreviations_by_expansion
        ),
    }

  def _generate_examples(
      self, split: str, abbreviations_by_expansion: Mapping[str, Sequence[str]]
  ):
    """Yields examples."""

    def _process_example(element: tuple[str, WSRSFeatures]):
      key, features = element
      return key, {
          'original_snippet': features.original_snippet,
          'abbreviated_snippet': features.abbreviated_snippet,
      }

    expansion_re = c4_wsrs_utils.create_word_finder_regex(
        sorted(abbreviations_by_expansion.keys(), key=len, reverse=True)
    )

    beam = tfds.core.lazy_imports.apache_beam

    builder = tfds.builder('c4', config='en', version='3.1.0')
    return (
        tfds.beam.ReadFromTFDS(builder, split=split, workers_per_shard=10)
        | 'AsNumpy' >> beam.Map(tfds.as_numpy)
        | 'ExtractSnippets'
        >> beam.FlatMap(
            c4_wsrs_utils.extract_snippets,
            self.builder_config.max_sentences_per_snippet,
            abbreviations_by_expansion,
            expansion_re,
            self.builder_config.max_snippet_char_len,
            self.builder_config.alpha_keep_no_rs,
            self.builder_config.alpha_keep_rs,
        )
        | 'ReshuffleSnippets1' >> beam.Reshuffle()
        | 'ReverseSubstitution'
        >> beam.FlatMap(
            c4_wsrs_utils.reverse_substitution,
            self.builder_config.subsitution_rate,
            self.builder_config.min_snippet_token_len,
        )
        | 'GroupByRarestSubstitution' >> beam.GroupByKey()
        | 'SampleSnippetsByRarestSubstitution'
        >> beam.FlatMap(
            c4_wsrs_utils.sample_snippets_by_substitution,
            self.builder_config.num_snippets_per_substitution,
        )
        | 'ReshuffleSnippets2' >> beam.Reshuffle()
        | 'ProcessExamples' >> beam.Map(_process_example)
    )

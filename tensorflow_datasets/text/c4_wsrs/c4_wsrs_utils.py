# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Utils to process C4-WSRS."""

from __future__ import annotations
import collections
import dataclasses
import random
import re
from typing import Iterator, Mapping, Sequence, Tuple
import numpy as np

# Type annotations.
AbbrevExpansionPair = Tuple[str, str]


FREQUENT_EXPANSIONS = frozenset([
    'and',
    'by',
    'with',
    'home',
    'year',
    'years',
    'great',
    'two',
    'well',
    'work',
    'service',
    'company',
    'family',
    'quality',
    'day',
    'before',
    'every',
    'after',
    'small',
    'days',
    'old',
    'does',
    'please',
    'start',
    'center',
    'week',
    'high',
    'with a',
    'management',
    'food',
    'month',
    'north',
    'she',
    'black',
    'give',
    'county',
    'building',
    'right',
    'room',
    'four',
    'light',
    'call',
    'friday',
    'general',
    'companies',
    'times',
    'check',
    'west',
    'road',
    'report',
    'once',
    'heart',
    'five',
    'street',
    'point',
    'because',
    'size',
    'each',
    'east',
    'weeks',
    'united states',
    'type',
    'tuesday',
    'phone',
    'water',
    'december',
    'per',
    'second',
    'word',
    'established',
    'repair',
    'minutes',
    'regarding',
    'yesterday',
])


@dataclasses.dataclass
class WSRSFeatures:
  """Stores the original snippet and the snippet abbreviated by WSRS."""

  original_snippet: str = ''
  abbreviated_snippet: str = ''


def _get_backoff_prob(n: int, alpha: float) -> float:
  """Computes the back-off probability given current count and alpha value."""
  return (n + 1) ** -alpha


def create_word_finder_regex(words: Sequence[str]) -> re.Pattern[str]:
  """Creates regex pattern that matches any of the provided words.

  The regex pattern is comprised of 3 components: the prefix, the words, and the
  suffix. The words are a concatenation of all provided words separated by the
  OR operator. The prefix and suffix ensure that the matched word represents a
  distinct, delineated instance of that word.
    - prefix: A word must be preceded by any one of the following patterns:
      1. The string start
      2. Any character OTHER than alphanumeric or apostrophe
      3. An apostrophe preceded by a non-alphanumeric character (this
        ensures contractions and possessives do not lead to false positives)
    - suffix: A word must be followed by any one of the following patterns:
      1. The string end
      2. Any non-alphanumeric character
  Note: the order of the words matters, as the regex pattern will greedily
  match with the first word in the list. This has implications for instances
  in which a word is a distinguishable substring of another word.

  Args:
    words: A list of words that the pattern will find.

  Returns:
    A regex pattern that will match any instance of the provided words.
  """
  words_re = '|'.join([re.escape(word) for word in words])
  prefix_re = "^|[^\\w']|(?:^|\\W)'"
  suffix_re = '(?:$|\\W)'
  # We exclude the suffix from capture so that consecutive abbreviations
  # separated by spaces can be matched.
  re_string = f'(?:{prefix_re})({words_re})(?={suffix_re})'
  return re.compile(re_string)


def _get_abbreviation_expansion_pairs(
    snippet: str,
    abbreviations_by_expansion: Mapping[str, Sequence[str]],
    expansion_regex: re.Pattern[str],
) -> dict[int, AbbrevExpansionPair]:
  """Extracts possible abbreviation-expansion pairs from a snippet."""
  index_to_pair = {}
  for match in expansion_regex.finditer(snippet):
    match_start = match.span(1)[0]
    expansion = match.group(1)
    abbrev = random.choice(abbreviations_by_expansion[expansion])
    index_to_pair[match_start] = (abbrev, expansion)
  return index_to_pair


def extract_snippets(
    c4_doc: Mapping[str, bytes],
    max_sentences_per_snippet: int,
    abbreviations_by_expansion: Mapping[str, Sequence[str]],
    expansion_regex: re.Pattern[str],
    max_snippet_char_len: int,
    alpha_keep_no_rs: float,
    alpha_keep_rs: float,
) -> Iterator[
    tuple[
        str, tuple[str, AbbrevExpansionPair, Mapping[int, AbbrevExpansionPair]]
    ]
]:
  """Extracts variable-length multi-sentence snippets from C4 web text.

  Determines whether to keep or discard snippets based on the number of snippets
  previously kept which contain the same reverse substitution candidates (or
  lack thereof).

  Args:
    c4_doc: The C4 web crawl document.
    max_sentences_per_snippet: The maximum number of sentences that can be
      combined into a single snippet. The number of sentences combined into each
      snippet will be a randomly sampled integer from 1 to
      max_sentences_per_snippet.
    abbreviations_by_expansion: A mapping from expansion to all valid
      abbreviations for that expansion.
    expansion_regex: A regex pattern that will match any valid expansion.
    max_snippet_char_len: The maximum number of characters an original snippet
      can be composed of.
    alpha_keep_no_rs: Alpha value used to compute the probability of keeping a
      snippet containing no reverse substitutions. The complete formula is p =
      (n+1)**-alpha where n is the count of previously kept snippets from the
      same document.
    alpha_keep_rs: Alpha value used to compute the probability of keeping a
      snippet containing a particular abbreviation-expansion reverse
      substitution candidate. The complete formula is p = (n+1)**-alpha where n
      is the count of previously kept snippets from the same document containing
      the same reverse substitution candidate.

  Yields:
    A key-value tuple where the key is a string containing the document url and
    incremental snippet id, and the value is a 3-tuple containing the snippet,
    the rarest abbreviation-expansion substitution candidate in the snippet, and
    a mapping from snippet index to each substitution candidate.
  """
  count_by_pair = collections.Counter()
  text = c4_doc['text'].decode()
  text = text.replace('\n', ' ')
  sentences = text.split('. ')
  sentence_idx = 0
  snippet_id = 0
  while sentence_idx < len(sentences):
    num_sentences_sampled = np.random.randint(1, max_sentences_per_snippet + 1)
    snippet = '. '.join(
        sentences[sentence_idx : sentence_idx + num_sentences_sampled]
    )
    # Period added stochastically to make models robust to the absence of
    # ending punctuation.
    if not snippet.endswith('.') and np.random.uniform() < 0.5:
      snippet += '.'
    key = f'url={c4_doc["url"].decode()},snippet_id={snippet_id}'
    snippet_id += 1
    sentence_idx += num_sentences_sampled
    snippet = snippet.lower().strip()
    if len(snippet) > max_snippet_char_len:
      continue
    index_to_pair = _get_abbreviation_expansion_pairs(
        snippet, abbreviations_by_expansion, expansion_regex
    )
    if index_to_pair:
      smallest_count, rarest_pair = None, None
      for pair in index_to_pair.values():
        if pair[1] in FREQUENT_EXPANSIONS:
          continue
        count = count_by_pair[pair]
        if smallest_count is None or count < smallest_count:
          smallest_count = count
          rarest_pair = pair
      sample_prob = (
          _get_backoff_prob(smallest_count, alpha=alpha_keep_rs)
          if smallest_count is not None
          else 0.0
      )
      if np.random.uniform() >= sample_prob:
        continue
      # Count should only be increased if snippet is sampled.
      for pair in index_to_pair.values():
        count_by_pair[pair] += 1
    else:
      rarest_pair = ('', '')
      index_to_pair = {0: ('', '')}
      count = count_by_pair[('', '')]
      sample_prob = _get_backoff_prob(count + 100, alpha=alpha_keep_no_rs)
      if np.random.uniform() >= sample_prob:
        continue
      count_by_pair[('', '')] += 1

    yield key, (snippet, rarest_pair, index_to_pair)  # pytype: disable=bad-return-type  # container-simplification


def _reverse_substitute_snippet(
    snippet: str,
    index_to_pair: Mapping[int, AbbrevExpansionPair],
    substitution_rate: float,
) -> str:
  """Reverse substitutes a snippet, swapping expansions for abbreviations.

  For each candidate abbreviation, its abbreviation is sampled using the
  substitution_rate value.

  Args:
    snippet: The snippet to abbreviate.
    index_to_pair: A mapping from snippet index to reverse-substitution
      candidate for that index.
    substitution_rate: The rate at which expansions should be substituted for
      abbreviations.

  Returns:
    The abbreviated snippet.
  """
  abbreviated_snippet = ''
  for index, (abbrev, expansion) in sorted(index_to_pair.items(), reverse=True):
    if np.random.uniform() >= substitution_rate:
      continue
    abbreviated_snippet = (
        abbrev + snippet[index + len(expansion) :] + abbreviated_snippet
    )
    snippet = snippet[:index]
  abbreviated_snippet = snippet + abbreviated_snippet
  return abbreviated_snippet


def reverse_substitution(
    element: tuple[
        str, tuple[str, AbbrevExpansionPair, Mapping[int, AbbrevExpansionPair]]
    ],
    substitution_rate: float,
    min_snippet_token_len: int,
) -> Iterator[tuple[AbbrevExpansionPair, tuple[str, WSRSFeatures]]]:
  """Conducts reverse substitution.

  Yields one WSRSFeatures obj per unique replacement.

  Args:
    element: A key-value tuple containing the url as the key, and a 3-tuple as
      the value containing the snippet extracted from the c4 doc, the rarest
      abbreviation-expansion substitution candidate in the snippet, and a
      mapping from snippet index to each substitution candidate.
    substitution_rate: The rate at which expansions should be substituted for
      abbreviations.
    min_snippet_token_len: The minimum number of tokens an abbreviated snippet
      can be composed of.

  Yields:
    A key-value tuple in which the key is a tuple containing the rarest
    abbreviation-expansion pair replacement for that snippet, and the value is a
    tuple containing the original key and a WSRSFeatures object holding the
    extracted snippet and its abbreviated form.
  """
  key, (snippet, rarest_pair, index_to_pair) = element
  abbreviated_snippet = snippet
  if index_to_pair:
    abbreviated_snippet = _reverse_substitute_snippet(
        snippet, index_to_pair, substitution_rate
    )
  if len(abbreviated_snippet.split(' ')) < min_snippet_token_len:
    return
  features = WSRSFeatures()
  features.original_snippet = snippet
  features.abbreviated_snippet = abbreviated_snippet

  yield rarest_pair, (key, features)


def sample_snippets_by_substitution(
    snippets_by_substitution: tuple[
        AbbrevExpansionPair, Sequence[tuple[str, WSRSFeatures]]
    ],
    num_snippets_per_substitution: int,
) -> Iterator[tuple[str, WSRSFeatures]]:
  """Samples a fixed number of snippets for each substitution pair."""
  limit = num_snippets_per_substitution
  if limit == 0:
    return
  snippets = snippets_by_substitution[1]
  for key, features in snippets:
    yield key, features
    limit -= 1
    if limit <= 0:
      break

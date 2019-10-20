# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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
"""Utilities for generating the C4 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import gzip
import hashlib
import io
import re
import threading

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# WET file constants
_PAGE_DELIMITER = "WARC/1.0"
_URL_KEY = "WARC-Target-URI:"
_METADATA_PREFIXES = ("WARC", "CONTENT-", "Content-")

# Filters
_MIN_WORDS_PER_LINE = 5
_MIN_NUM_SENTENCES = 3
_END_MARKS = (".", "?", "!", "\"")
_ELLIPSIS = "..."
_POLICY_SUBSTRINGS = [
    "terms of use", "privacy policy", "cookie policy", "uses cookies",
    "use of cookies", "use cookies"]

# Memoized sentence tokenizer.
_SENTENCE_TOKENIZER = None


def get_counter_inc_fn(namespace):
  def counter_inc_fn(counter, amt=1):
    tfds.core.lazy_imports.apache_beam.metrics.Metrics.counter(
        namespace, counter).inc(amt)
  return counter_inc_fn


def _load_sentence_tokenizer():
  """Returns a sentence tokenization function."""
  nltk = tfds.core.lazy_imports.nltk
  # Lock to avoid a race-condition in the creation of the download directory.
  with threading.Lock():
    nltk.download("punkt")
    return nltk.data.load("nltk:tokenizers/punkt/english.pickle")




def _get_sentences(text):
  global _SENTENCE_TOKENIZER
  if not _SENTENCE_TOKENIZER:
    _SENTENCE_TOKENIZER = _load_sentence_tokenizer()
  return list(_SENTENCE_TOKENIZER.tokenize(tf.compat.as_text(text)))


def _get_sentences_by_line(text, lower=False):
  sentences = []
  for line in text.splitlines():
    sentences.append([
        s.lower() if lower else s for s in _get_sentences(line)
    ])
  return sentences


def is_language(page, language, min_probability=0.99):
  """Returns True iff text is in `language` with at least `min_probability`."""
  unused_url, text = page

  counter_inc_fn = get_counter_inc_fn("detected-lang")

  langdetect = tfds.core.lazy_imports.langdetect
  # Make langdetect predictions deterministic.
  langdetect.DetectorFactory.seed = 0
  try:
    predictions = langdetect.detect_langs(text)
  except langdetect.lang_detect_exception.LangDetectException:
    counter_inc_fn("langdetect-exception")
    return False
  if not predictions:
    counter_inc_fn("page-filtered-nolangpredictions")
    return False
  best_prediction = predictions[0]
  if best_prediction.prob < min_probability:
    counter_inc_fn("page-filtered-lowlangdetectconf")
    return False
  if best_prediction.lang != language:
    counter_inc_fn("page-filtered-ignoredlang")
    counter_inc_fn("page-filtered-ignoredlang-%s" % (best_prediction.lang))
    return False
  counter_inc_fn("page-emited-%s" % best_prediction.lang)
  return True


def get_clean_page_fn(badwords=None):
  """Returns `clean_page` with pre-compiled badword and citation regexes."""
  # Used to filter citation from Wikipedia pages (among others).
  citation_regex = re.compile(r"\[\d*\]|\[edit\]|\[citation needed\]")
  if badwords:
    badwords_regex = re.compile(
        "[^a-z]({})[^a-z]".format("|".join(badwords or [])))
  else:
    badwords_regex = None
  return functools.partial(
      clean_page, citation_regex=citation_regex, badwords_regex=badwords_regex)


def clean_page(url_and_text, citation_regex, badwords_regex=None,
               counter_inc_fn=None,
               min_words_per_line=_MIN_WORDS_PER_LINE,
               min_num_sentences=_MIN_NUM_SENTENCES):
  """Cleans a CommonCrawl page, yielding nothing if it should be skipped.

  Cleaning removes lines with no end marks or with too few words. After line
  filtering, pages are filtered out if they have too few sentences based on a
  simple count of end marks.

  Args:
    url_and_text: tuple(string, string), the url and raw text of the page.
    citation_regex: Regex to use for finding Wikipedia-like citations to filter.
    badwords_regex: Regex to use for finding badwords. Default None, which means
      don't apply badwords filtering.
    counter_inc_fn: function, a function taking the name of a counter to be
      incremented and the (optional) amount. Defaults to a beam Metric counter.
    min_words_per_line: int, the minimum number of words a line needs to not be
      removed.
    min_num_sentences: int, the minimum number of sentences a page needs to not
      be skipped.
  Yields:
    The url and cleaned text for the page.
  """
  url, text = url_and_text
  if not counter_inc_fn:
    counter_inc_fn = get_counter_inc_fn("clean-page")

  lines = text.splitlines()
  valid_lines = []
  num_sentences = 0

  for line in lines:
    line = line.strip()
    line = citation_regex.sub("", line)
    if not line.endswith(_END_MARKS) or line.endswith(_ELLIPSIS):
      counter_inc_fn("lines-no-endmark")
      continue
    if len(line.split()) < min_words_per_line:
      counter_inc_fn("lines-too-short")
      continue
    line_lower = line.lower()
    # Remove documents which contain lorem ipsum
    if "lorem ipsum" in line_lower:
      counter_inc_fn("filtered-url-loremipsum")
      return
    # Remove "javascript must be enabled" notices
    if "javascript" in line_lower:
      counter_inc_fn("lines-javascript")
      continue
    # Remove docs which probably contain javascript code
    if "{" in line:
      counter_inc_fn("filtered-url-squigglybracket")
      return
    # Remove policy lines
    if any(p in line_lower for p in _POLICY_SUBSTRINGS):
      counter_inc_fn("lines-policy")
      continue
    # If any badword appears on its own in the line, skip this doc
    if badwords_regex:
      badwords_found = badwords_regex.search(line_lower)
      if badwords_found is not None:
        counter_inc_fn("filtered-url-badword")
        return
    num_sentences += len(_get_sentences(line))
    valid_lines.append(line)
    counter_inc_fn("lines-valid")

  if num_sentences < min_num_sentences:
    counter_inc_fn("filtered-url-toofewsentences")
    return
  counter_inc_fn("emitted-clean-pages")
  yield url, "\n".join(valid_lines).strip()


def _emit_url_to_sentences(page, max_window_size):
  """Emits url to all (lower-cased) sentences grouped by sliding window."""
  url, text = page
  for sentences in _get_sentences_by_line(text, lower=True):
    # We don't want to emit windows where all "sentences" are just endmarks
    # (e.g., "! ! !").
    is_solo_endmark = [w in _END_MARKS for w in sentences]
    for i in range(len(sentences) - min(len(sentences), max_window_size) + 1):
      if not all(is_solo_endmark[i:i+max_window_size]):
        yield tuple(sentences[i:i+max_window_size]), url


def _emit_sentences_to_urls(el, counter_inc_fn, skip_n=1):
  """Emits sentences to all but `skip_n` urls."""
  sentences, urls = el
  # Hash urls and sort to have a consistent, but unbiased, selection when the
  # same urls exist for multiple sentences.
  sorted_urls = sorted(
      urls,
      key=lambda x: hashlib.md5(tf.compat.as_text(x).encode("utf-8")).
      hexdigest())
  del sorted_urls[:skip_n]
  if sorted_urls:
    counter_inc_fn("emitted-sentences-duplicate")
    logging.info(
        "Emitting sentences to %d documents: %s", len(sorted_urls), sentences)
    for url in sorted_urls:
      yield url, sentences


def _remove_sentences_from_text(
    el, counter_inc_fn, max_window_size,
    min_num_sentences=_MIN_NUM_SENTENCES):
  """Removes matching sentence windows from the page.

  Process the result of a join containing a single value for 'text' and zero or
  more values for 'sentences'. Each value in 'sentences' is a tuple containing
  a window of one or more sentences.

  If a line has fewer sentences than `max_window_size`, the full line is
  compared for a match.

  Args:
    el: `(string, {'text': [string], 'sentences': [tuple(string)]})`,
      element containing the result of a join on key with both the page text
      and lower-cased sentence windows to remove.
    counter_inc_fn: function, a function taking the name of a counter to be
      incremented and the (optional) amount.
    max_window_size: int, the maximum size of a sentence window to slide across
      lines.
    min_num_sentences: int, the minimum number of sentences a page needs to not
      be skipped.

  Yields:
    url: The URL of the page.
    text: The text of the page with sentences removed.
  """
  url, join_values = el
  text = join_values["text"]
  assert len(text) == 1, "Invalid page count (%d) for %s" % (len(text), url)
  text = text[0]
  sentences_to_remove = set(join_values["sentences"])
  sentences_by_line = _get_sentences_by_line(text, lower=False)
  new_sentences_by_line = []
  for line_sentences in sentences_by_line:
    indices_to_remove = set()
    for i in range(
        len(line_sentences) - min(len(line_sentences), max_window_size) + 1):
      sentence_window = tuple(
          s.lower() for s in line_sentences[i:i+max_window_size])
      if sentence_window in sentences_to_remove:
        indices_to_remove.update(range(i, i+len(sentence_window)))
    counter_inc_fn("filtered-sentence-duplicate", len(indices_to_remove))
    new_line_sentences = [
        s for i, s in enumerate(line_sentences) if i not in indices_to_remove]
    if new_line_sentences:
      new_sentences_by_line.append(new_line_sentences)
  if sum(len(sents) for sents in new_sentences_by_line) < min_num_sentences:
    counter_inc_fn("filtered-doc-toofewsentences")
    return
  yield (url, "\n".join(" ".join(sent) for sent in new_sentences_by_line))


def remove_duplicate_text(pages, sentence_window_size=3):
  """Utility to remove duplicate sentence windows across text documents."""
  # Output: url, sentence
  beam = tfds.core.lazy_imports.apache_beam
  counter_inc_fn = get_counter_inc_fn("dedupe-sentences")
  sentences_to_remove = (
      pages
      | beam.FlatMap(_emit_url_to_sentences,
                     max_window_size=sentence_window_size)
      | "group_sentences" >> beam.GroupByKey()
      | beam.FlatMap(_emit_sentences_to_urls, counter_inc_fn=counter_inc_fn))

  # Output: url, text
  final_docs = (
      {"text": pages, "sentences": sentences_to_remove}
      | "group_text_and_sentences_by_url" >> beam.CoGroupByKey()
      | beam.FlatMap(_remove_sentences_from_text,
                     max_window_size=sentence_window_size,
                     counter_inc_fn=counter_inc_fn))

  return final_docs


def split_wet_file(wet_file_path, counter_inc_fn=None):
  """Split a WET file into separate pages."""
  logging.info("Splitting file: %s", wet_file_path)
  if not counter_inc_fn:
    counter_inc_fn = get_counter_inc_fn("split-wet-file")
  counter_inc_fn("wet-file")

  with tf.io.gfile.GFile(wet_file_path, "rb") as f, gzip.GzipFile(
      fileobj=f) as g:
    url = None
    content = None

    def _maybe_get_page():
      if not url and url is not None:
        counter_inc_fn("page-filitered-nourl")
      if not content and content is not None:
        counter_inc_fn("page-filtered-nocontent")
      if content and url:
        counter_inc_fn("page-emitted")
        return (url, "\n".join(content))
      return None

    for line in io.TextIOWrapper(g, encoding="utf-8"):
      line = line.strip()
      if not line:
        continue
      if line == _PAGE_DELIMITER:
        page = _maybe_get_page()
        if page:
          yield page
        url = ""
        content = []

      if line.startswith(_URL_KEY):
        url = line[len(_URL_KEY):].strip()

      if line.startswith(_METADATA_PREFIXES):
        continue

      content.append(line)

    page = _maybe_get_page()
    if page:
      yield page


def dedupe_urls(el):
  """Returns the first value for a given URL."""
  counter_inc_fn = get_counter_inc_fn("dedupe-urls")
  url, vals = el
  cnt = 0
  v = None
  for v in vals:
    cnt += 1
  counter_inc_fn("filtered-url-duplicate", cnt - 1)
  counter_inc_fn("unique-url")
  return url, v


def is_valid_length(el, max_length=1.9e5):
  """Returns False iff page's content is too long."""
  counter_inc_fn = get_counter_inc_fn("is-valid-length")
  _, content = el
  if len(content) > max_length:
    counter_inc_fn("filtered-url-contenttoolong")
    return False
  counter_inc_fn("valid-length")
  return True


def is_realnews_domain(el, realnews_domains):
  """Returns False iff page's (sub)domain is not allowed."""
  counter_inc_fn = get_counter_inc_fn("is-realnews-domain")
  url, _ = el
  ext = tfds.core.lazy_imports.tldextract.extract(url)
  main_domain = ext.domain + "." + ext.suffix
  if main_domain not in realnews_domains:
    counter_inc_fn("filtered-url-invaliddomain")
    return False
  allowed_subdomains = realnews_domains[main_domain]
  if (isinstance(allowed_subdomains, list) and
      ext.subdomain not in allowed_subdomains):
    counter_inc_fn("filtered-url-invalidsubdomain")
    return False
  counter_inc_fn("realnews-domain")
  return True


def filter_by_webtextlike(el):
  """Yields only pages with a matching WebText-like URL."""
  counter_inc_fn = get_counter_inc_fn("filter-by-webtextlike")
  url, join_values = el
  text = join_values["text"]
  webtextlike = join_values["webtextlike_urls"]
  if not webtextlike:
    counter_inc_fn("filtered-url-notwebtextlike")
    return
  if not text:
    counter_inc_fn("missing-webtextlike")
    return
  assert len(text) == 1
  counter_inc_fn("found-webtextlike")
  yield url, text[0]


def normalize_url(el):
  url, val = el
  url = tf.compat.as_text(url)
  url = re.sub(r"https?:\/\/(www\.)?", "", url)
  url = re.sub(r"\?(utm_|ref|feed).*", "", url)
  url = url.rstrip("/")
  return url, val

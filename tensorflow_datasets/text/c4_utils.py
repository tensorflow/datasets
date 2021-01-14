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

"""Utilities for generating the C4 dataset."""

import functools
import gzip
import hashlib
import heapq
import io
import re
import threading

from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

# WET file constants
_PAGE_DELIMITER = "WARC/1.0"
_URL_KEY = "WARC-Target-URI:"
_URL_DATE = "WARC-Date:"
_CONTENT_TYPE = "Content-Type:"
_CONTENT_LEN = "Content-Length:"
_METADATA_PREFIXES = ("WARC", "CONTENT-", "Content-")

# Filters
_MIN_WORDS_PER_LINE = 5
_MIN_NUM_SENTENCES = 3
_MAX_WORD_LENGTH = 1000
_END_MARKS = (".", "?", "!", "\"")
_ELLIPSIS = "..."
_POLICY_SUBSTRINGS = [
    "terms of use", "privacy policy", "cookie policy", "uses cookies",
    "use of cookies", "use cookies"]

# Memoized sentence tokenizer.
_SENTENCE_TOKENIZER = None

UNKNOWN_LANGUAGE = "und"


def get_counter_inc_fn(namespace):
  def counter_inc_fn(counter, amt=1):
    tfds.core.lazy_imports.apache_beam.metrics.Metrics.counter(
        namespace, counter).inc(amt)
  return counter_inc_fn


def get_hashed_url_filter_fn(predicate_fn):
  def filter_fn(el):
    url, _ = el
    val = int(
        hashlib.md5(tf.compat.as_text(url).encode("utf-8")).hexdigest(), 16)
    return predicate_fn(val)
  return filter_fn


_nltk_lock = threading.Lock()


def _load_sentence_tokenizer():
  """Returns a sentence tokenization function."""
  nltk = tfds.core.lazy_imports.nltk
  # Lock to avoid a race-condition in the creation of the download directory.
  with _nltk_lock:
    nltk.download("punkt")
    return nltk.data.load("nltk:tokenizers/punkt/english.pickle")




def _get_sentences(text):
  global _SENTENCE_TOKENIZER
  if not _SENTENCE_TOKENIZER:
    _SENTENCE_TOKENIZER = _load_sentence_tokenizer()
  return list(_SENTENCE_TOKENIZER.tokenize(tf.compat.as_text(text)))

# Global lock used for language detection modules that aren't threadsafe.
langdetect_lock = threading.Lock()


def detect_english(page, min_probability=0.99):
  """Yields page iff text is 'en' with at least `min_probability`."""
  url, features = page
  text = features["text"]

  counter_inc_fn = get_counter_inc_fn("english-filter")

  langdetect = tfds.core.lazy_imports.langdetect
  # Make langdetect predictions deterministic.
  with langdetect_lock:
    langdetect.DetectorFactory.seed = 0
    try:
      predictions = langdetect.detect_langs(text)
    except langdetect.lang_detect_exception.LangDetectException:
      counter_inc_fn("filtered:langdetect_exception")
      return
  if not predictions:
    counter_inc_fn("filtered:no_predictions")
    return
  best_prediction = predictions[0]
  if best_prediction.prob < min_probability:
    counter_inc_fn("filtered:low_confidence")
    return
  if best_prediction.lang != "en":
    counter_inc_fn("filtered:ignored_language")
    counter_inc_fn("filtered:ignored_language-%s" % (best_prediction.lang,))
    return

  counter_inc_fn("passed")
  features = dict(features)
  features["language"] = "en"
  yield url, features


def detect_languages(pages, valid_languages):
  """Predicts page language using cld3 and adds to features."""

  beam = tfds.core.lazy_imports.apache_beam

  class _PredictLanguageFn(beam.DoFn):
    """Predicts page's language using cld3 and adds to features."""

    def __init__(self, valid_languages, min_probability=0.7):
      self._valid_languages = set(valid_languages)
      self._counter_inc_fn = get_counter_inc_fn("language-filter")
      self._min_probability = min_probability

    def start_bundle(self):

      with langdetect_lock:
        self._detector = tfds.core.lazy_imports.gcld3.NNetLanguageIdentifier(
            # CLD3 is not expected to work well on very short documents.
            min_num_bytes=100,
            max_num_bytes=10000)

    def process(self, page):
      url, features = page
      features = dict(features)
      with langdetect_lock:
        result = self._detector.FindLanguage(features["text"])
      if not result.is_reliable:
        self._counter_inc_fn("filtered:no_predictions")
        lang = UNKNOWN_LANGUAGE
      elif result.probability < self._min_probability:
        self._counter_inc_fn("filtered:low_confidence")
        lang = UNKNOWN_LANGUAGE
      else:
        lang = result.language
        if lang not in self._valid_languages:
          self._counter_inc_fn("filtered:ignored_language")
          return
      self._counter_inc_fn("passed")
      self._counter_inc_fn("passed:%s" % lang)
      features["language"] = lang
      yield url, features

  return pages | beam.ParDo(_PredictLanguageFn(valid_languages=valid_languages))


def get_clean_page_fn():
  """Returns `clean_page` with pre-compiled badword and citation regexes."""
  # Used to filter citation from Wikipedia pages (among others).
  citation_regex = re.compile(r"\[\d*\]|\[edit\]|\[citation needed\]")
  return functools.partial(clean_page, citation_regex=citation_regex)


def clean_page(url_and_features,
               citation_regex,
               counter_inc_fn=None,
               min_words_per_line=_MIN_WORDS_PER_LINE,
               min_num_sentences=_MIN_NUM_SENTENCES,
               max_word_length=_MAX_WORD_LENGTH):
  """Cleans a CommonCrawl page, yielding nothing if it should be skipped.

  Cleaning removes lines with no end marks or with too few words. After line
  filtering, pages are filtered out if they have too few sentences based on a
  simple count of end marks.

  Args:
    url_and_features: tuple(string, dict), the url and features of the page.
    citation_regex: Regex to use for finding Wikipedia-like citations to filter.
    counter_inc_fn: function, a function taking the name of a counter to be
      incremented and the (optional) amount. Defaults to a beam Metric counter.
    min_words_per_line: int, the minimum number of words a line needs to not be
      removed.
    min_num_sentences: int, the minimum number of sentences a page needs to not
      be skipped.
    max_word_length: int, the maximum number of characters allowed in a word.
      Lines containing a word with too many characters are removed.
  Yields:
    The url and cleaned text for the page.
  """
  url, features = url_and_features
  text = features["text"]

  if not counter_inc_fn:
    counter_inc_fn = get_counter_inc_fn("clean-page")

  lines = text.splitlines()
  valid_lines = []
  num_sentences = 0

  def line_has_too_long_word(line):
    for word in line.split():
      if len(word) > max_word_length:
        return True
    return False

  for line in lines:
    line = line.strip()
    if line_has_too_long_word(line):
      counter_inc_fn("line-filtered:too_long_word")
      continue
    line = citation_regex.sub("", line)
    if not line.endswith(_END_MARKS) or line.endswith(_ELLIPSIS):
      counter_inc_fn("line-filtered:no_endmark")
      continue
    if len(line.split()) < min_words_per_line:
      counter_inc_fn("line-filtered:too_short")
      continue
    line_lower = line.lower()
    # Remove documents which contain lorem ipsum
    if "lorem ipsum" in line_lower:
      counter_inc_fn("filtered:loremipsum")
      return
    # Remove "javascript must be enabled" notices
    if "javascript" in line_lower:
      counter_inc_fn("line-filtered:javascript")
      continue
    # Remove docs which probably contain javascript code
    if "{" in line:
      counter_inc_fn("filtered:squigglybracket")
      return
    # Remove policy lines
    if any(p in line_lower for p in _POLICY_SUBSTRINGS):
      counter_inc_fn("line-filtered:policy")
      continue
    num_sentences += len(_get_sentences(line))
    valid_lines.append(line)
    counter_inc_fn("line-passed")

  if num_sentences < min_num_sentences:
    counter_inc_fn("filtered:too_few_sentences")
    return
  counter_inc_fn("passed")
  features["text"] = "\n".join(valid_lines).strip()
  yield url, features


def _hash_text(text):
  return hashlib.md5(tf.compat.as_text(text).encode("utf-8")).hexdigest()


def _emit_url_to_lines(page):
  """Emits url to all (lower-cased, hashed) lines."""
  url, features = page
  text = features["text"]
  for line in text.split("\n"):
    yield _hash_text(line.strip().lower()), url


def _remove_lines_from_text(el, counter_inc_fn, min_num_sentences):
  """Removes all lines from the page that do not match the given set of hashes.

  Process the result of a join containing a single value for 'features' and zero
  or more values for 'lines'. Each value in 'lines' is a lower-cased, hashed
  line that has been selected to keep.

  Args:
    el: `(string, {'features': features_dict, 'lines': [string]})`,
      element containing the result of a join on key with both the page text
      and lower-cased, hashed lines to remove.
    counter_inc_fn: function, a function taking the name of a counter to be
      incremented and the (optional) amount.
    min_num_sentences: int, the minimum number of sentences a page needs to not
      be skipped.

  Yields:
    url: The URL of the page.
    features: The page features with lines removed from text.
  """
  url, join_values = el
  features = join_values["features"]

  assert len(features) == 1, "Invalid page count (%d) for %s" % (
      len(features), url)
  features = features[0]
  text = features["text"]
  lines_to_keep = set(join_values["lines"])
  new_lines = []
  hashed_lines = set()
  for line in text.split("\n"):
    hashed_line = _hash_text(line.strip().lower())
    if hashed_line not in lines_to_keep:
      counter_inc_fn("line-filtered:global_duplicate")
    elif hashed_line in hashed_lines:
      counter_inc_fn("line-filtered:local_duplicate")
    else:
      counter_inc_fn("line-passed")
      new_lines.append(line)
      hashed_lines.add(hashed_line)
  new_text = "\n".join(new_lines)
  if not new_text:
    counter_inc_fn("filtered:empty")
    return
  if min_num_sentences and len(_get_sentences(new_text)) < min_num_sentences:
    counter_inc_fn("filtered:too_few_sentences")
    return
  counter_inc_fn("passed")
  new_features = features.copy()
  new_features["text"] = new_text
  yield (url, new_features)


def remove_duplicate_text(pages, min_num_sentences=_MIN_NUM_SENTENCES):
  """Utility to remove duplicate lines across text documents."""
  # Output: url, lines
  beam = tfds.core.lazy_imports.apache_beam

  # Select a single URL for each line in the input pages.
  # Hash before comparison to avoid biasing by domain.
  # line, [url]
  line_to_selected_url = (
      pages
      | beam.FlatMap(_emit_url_to_lines)
      | beam.combiners.Top.PerKey(1, key=_hash_text, reverse=True))
  # url, line
  lines_to_keep = line_to_selected_url | beam.Map(lambda x: (x[1][0], x[0]))

  # Output: url, text
  final_docs = (
      {
          "features": pages,
          "lines": lines_to_keep
      }
      | "group_features_and_lines_by_url" >> beam.CoGroupByKey()
      | beam.FlatMap(
          _remove_lines_from_text,
          counter_inc_fn=get_counter_inc_fn("dedupe-lines"),
          min_num_sentences=min_num_sentences))

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
    content_len = None
    content_type = None
    timestamp = None

    def _maybe_get_page():
      """Generate a (url, {features}) page."""
      if not url and url is not None:
        counter_inc_fn("filtered:no_url")
      if not content and content is not None:
        counter_inc_fn("filtered:no_content")
      if not content_type and content_type is not None:
        counter_inc_fn("filtered:no_content_type")
      if not content_len and content_len is not None:
        counter_inc_fn("filtered:no_content_len")
      if not timestamp and timestamp is not None:
        counter_inc_fn("filtered:no_timestamp")
      if content and url:
        counter_inc_fn("passed")
        return (url, {
            "text": "\n".join(content),
            "content-type": content_type,
            "content-length": content_len,
            "timestamp": timestamp,
            "url": url
        })
      return None

    for line in io.TextIOWrapper(g, encoding="utf-8"):  # pytype: disable=wrong-arg-types
      line = line.strip()
      if not line:
        continue
      if line == _PAGE_DELIMITER:
        page = _maybe_get_page()
        if page:
          yield page
        url = ""
        content = []
        content_len = ""
        content_type = ""
        timestamp = ""

      if line.startswith(_URL_KEY):
        url = line[len(_URL_KEY):].strip()

      if line.startswith(_URL_DATE):
        timestamp = line[len(_URL_DATE):].strip()

      if line.startswith(_CONTENT_TYPE):
        content_type = line[len(_CONTENT_TYPE):].strip()

      if line.startswith(_CONTENT_LEN):
        content_len = line[len(_CONTENT_LEN):].strip()

      if line.startswith(_METADATA_PREFIXES):
        continue

      content.append(line)  # pytype: disable=attribute-error

    page = _maybe_get_page()
    if page:
      yield page


def dedupe_urls(el):
  """Deterministically return as random page for a given URL."""
  counter_inc_fn = get_counter_inc_fn("duplicate-url-filter")

  url, pages = el
  cnt = 0
  page, page_hash = None, None
  for p in pages:
    cnt += 1
    p_hash = _hash_text(p["text"])
    if not page_hash or p_hash > page_hash:
      page = p
      page_hash = p_hash
  counter_inc_fn("filtered", cnt - 1)
  counter_inc_fn("passed")
  return url, page


def is_valid_length(el, max_length=1.9e5):
  """Returns False iff page's text is too long."""
  counter_inc_fn = get_counter_inc_fn("too-long-filter")
  _, page = el
  if len(page["text"]) > max_length:
    counter_inc_fn("filtered")
    return False
  counter_inc_fn("passed")
  return True


def is_realnews_domain(el, realnews_domains):
  """Returns False iff page's (sub)domain is not allowed."""
  counter_inc_fn = get_counter_inc_fn("realnews-domain-filter")
  url, _ = el
  ext = tfds.core.lazy_imports.tldextract.extract(url)
  main_domain = ext.domain + "." + ext.suffix
  if main_domain not in realnews_domains:
    counter_inc_fn("filtered:bad_domain")
    return False
  allowed_subdomains = realnews_domains[main_domain]
  if (isinstance(allowed_subdomains, list) and
      ext.subdomain not in allowed_subdomains):
    counter_inc_fn("filtered:bad_subdomain")
    return False
  counter_inc_fn("passed")
  return True


def filter_by_webtextlike(el):
  """Yields only pages with a matching WebText-like URL."""
  counter_inc_fn = get_counter_inc_fn("webtextlike-filter")
  url, join_values = el
  text = join_values["text"]
  webtextlike = join_values["webtextlike_urls"]
  if not webtextlike:
    counter_inc_fn("filtered")
    return
  if not text:
    counter_inc_fn("missing-page")
    return
  assert len(text) == 1
  counter_inc_fn("passed")
  yield url, text[0]


def normalize_url(el):
  url, val = el
  url = tf.compat.as_text(url)
  url = re.sub(r"https?:\/\/(www\.)?", "", url)
  url = re.sub(r"\?(utm_|ref|feed).*", "", url)
  url = url.rstrip("/")
  return url, val


def get_badwords_filter_fn(badwords):
  """Filters pages that contain any language-specific bad words."""
  badwords_regex = {  # pylint:disable=g-complex-comprehension
      lang: (
          # For Chinese and Thai, match bad words regardless of context.
          re.compile("|".join(words)) if lang in ("th", "zh")
          # For other languages, match only when flanked by non-word chars.
          else re.compile(r"(?:\W|^)({})(?:\W|$)".format("|".join(words))))
      for lang, words in badwords.items()
  }

  def badwords_filter(page):
    _, features = page
    lang = features["language"].split("-")[0]  # remove suffix if present

    if lang in badwords_regex:
      text = features["text"]
      badwords_found = badwords_regex[lang].search(text.lower())
      if badwords_found is not None:
        get_counter_inc_fn("badwords-filter")("filtered")
        get_counter_inc_fn("badwords-filter-%s" % lang)("filtered")
        return False
      get_counter_inc_fn("badwords-filter-%s" % lang)("passed")

    get_counter_inc_fn("badwords-filter")("passed")
    return True

  return badwords_filter


def paragraph_filter(page, min_paragraphs=3, min_paragraph_len=200):
  """Returns False iff a page has too few or too short paragraphs."""

  _, features = page

  lines = features["text"].split("\n")
  # Filter out docs that don't have at least three "paragraphs"
  # (lines >= `min_paragraph_len` chars).
  if (len(lines) < min_paragraphs or
      min(heapq.nlargest(3, [len(l) for l in lines])) < min_paragraph_len):
    get_counter_inc_fn("paragraph-filter")("filtered")
    return False
  get_counter_inc_fn("paragraph-filter")("passed")
  return True


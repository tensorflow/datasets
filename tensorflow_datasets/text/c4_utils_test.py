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
"""Tests for c4_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os

import six
from tensorflow_datasets import testing
from tensorflow_datasets.text import c4_utils


EN_TEXT = """This line has enough words and ends in punctuation, Dr. Roberts!
Economic History | All Institutions | Open Access Articles | Digital Commons Network
\"Open Access. Powered by Scholars. Published by Universities.\"
Digital Commons Network™/ Social and Behavioral Sciences...
Too few words.
You need to enable javascript in your browser in order to see this page.
You have JavaScript disabled and that means you can't see this page.
Adam Roberts has a cookie policy: always eat them.
Colin has a privacy policy: don't share people's secrets.
You'd better follow our terms of use!
"""

EXPECTED_CLEAN_EN = """This line has enough words and ends in punctuation, Dr. Roberts!
\"Open Access. Powered by Scholars. Published by Universities.\""""


def _get_counters():
  counters = collections.defaultdict(int)
  def counter_inc_fn(c, amt=1):
    counters[c] += amt
  return counters, counter_inc_fn


class C4UtilsTest(testing.TestCase):

  def run_clean_page(self, text, badwords=None):
    counters, counter_inc_fn = _get_counters()
    results = list(
        c4_utils.get_clean_page_fn(badwords)(
            url_and_text=("url", text),
            counter_inc_fn=counter_inc_fn))
    self.assertLessEqual(len(results), 1)
    result = None if not results else results[0][1]
    return result, counters

  def test_clean_page(self):
    clean_en, counters = self.run_clean_page(EN_TEXT)
    self.assertEqual(EXPECTED_CLEAN_EN, clean_en)
    self.assertEqual(
        {"lines-valid": 2, "lines-too-short": 1, "lines-no-endmark": 2,
         "lines-javascript": 2, "lines-policy": 3, "emitted-clean-pages": 1},
        dict(counters))

  def test_clean_page_toofewsentences(self):
    text_with_toofewsentences = """This first line has one sentence.
This line looks like it has three sentences...but it's actually just 1."""
    clean_en, counters = self.run_clean_page(text_with_toofewsentences)
    self.assertEqual(None, clean_en)
    self.assertEqual(
        {"lines-valid": 2, "filtered-url-toofewsentences": 1},
        dict(counters))

  def test_clean_page_squigglybracket(self):
    text_that_is_actually_code = """This page starts out with some text.
Everything looks good at first, since these are sentences.
But then, all of a sudden, there's a bunch of code like the next block.
fn foo(a) { bar = a + 10; }."""
    clean_en, counters = self.run_clean_page(text_that_is_actually_code)
    self.assertEqual(None, clean_en)
    self.assertEqual(
        {"filtered-url-squigglybracket": 1, "lines-valid": 3}, dict(counters)
    )

  def test_clean_page_loremipsum(self):
    lorem_ipsum_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    clean_en, counters = self.run_clean_page(lorem_ipsum_text)
    self.assertEqual(None, clean_en)
    self.assertEqual({"filtered-url-loremipsum": 1}, dict(counters))

  def test_clean_page_badwords(self):
    padding_text = """This page starts out with some text.
Everything looks good at first, since these are sentences.
But then, all of a sudden, there's a badword... or not?
"""
    final_sentences = [
        # Make sure ass in a longer word doesn't cause false-positive
        "I asked my friend for assistance polishing my cutlass.",
        # Check that a standard appearance of a badword triggers
        "He took the saddle and put it on his ass in preparation for travel.",
        # Make sure lowercasing works
        "Ass is one of several species of small, horse-like animals."
        # Make sure it will still trigger when surrounded by punctuation.
        "Donkey is one synonym for the word \"ass\"."
    ]
    outputs_should_be_none = [False, True, True, True]
    expected_counters = [
        {"lines-valid": 4, "emitted-clean-pages": 1},
        {"lines-valid": 3, "filtered-url-badword": 1},
        {"lines-valid": 3, "filtered-url-badword": 1},
        {"lines-valid": 3, "filtered-url-badword": 1},
    ]
    for final_sentence, output_should_be_none, expected_counter in zip(
        final_sentences, outputs_should_be_none, expected_counters
    ):
      text = padding_text + final_sentence
      out, counters = self.run_clean_page(text, badwords=["ass"])
      self.assertEqual(None if output_should_be_none else text, out)
      self.assertEqual(expected_counter, dict(counters))

  def test_clean_page_citations(self):
    text = """This page has some text.
Some lines don't end with punctuation
And some of these lines end with citations.[3]
Or have requested citations[citation needed]. Or the option to edit.[edit]
"""
    expected_clean_text = """This page has some text.
And some of these lines end with citations.
Or have requested citations. Or the option to edit."""
    expected_counters = {
        "lines-valid": 3, "lines-no-endmark": 1, "emitted-clean-pages": 1}
    out, counters = self.run_clean_page(text)
    self.assertEqual(expected_clean_text, out)
    self.assertEqual(expected_counters, dict(counters))

  def test_clean_page_policy(self):
    text = """This page has with some text. So, that's good!
But at the end it has some polciy lines.
This line mentions the Terms of Use.
This line should be okay.
The privacy policy is mentioned in this line.
Let's talk about the Cookie Policy now.
"""
    expected_clean_text = """This page has with some text. So, that's good!
But at the end it has some polciy lines.
This line should be okay."""
    expected_counters = {
        "lines-valid": 3, "lines-policy": 3, "emitted-clean-pages": 1}
    out, counters = self.run_clean_page(text)
    self.assertEqual(expected_clean_text, out)
    self.assertEqual(expected_counters, dict(counters))

  def test_emit_url_to_sentences(self):
    # Try with punkt language (en).
    expected_sentences = (
        ("this line has enough words and ends in punctuation, dr. roberts!",),
        ("\"open access.", "powered by scholars.",
         "published by universities.\""),
        ("sentence 1.", "sentence 2.", "sentence 3."),
        ("sentence 2.", "sentence 3.", "sentence 4."),
        ("another sentence.", ".", "."),
    )
    results = c4_utils._emit_url_to_sentences(
        ("url",
         EXPECTED_CLEAN_EN +
         "\nSentence 1. Sentence 2. Sentence 3. Sentence 4."
         "\nAnother sentence. . . ? ? ! ! !"),
        max_window_size=3)
    ret_sentences, ret_urls = zip(*results)
    self.assertEqual(("url",) * len(expected_sentences), ret_urls)
    self.assertEqual(expected_sentences, ret_sentences)

  def test_emit_sentences_to_urls(self):
    counters, counter_inc_fn = _get_counters()
    urls = ["urlA", "urlB", "urlC", "urlD"]
    sentence = "test sentence."
    expected_urls = ("urlA", "urlD")
    results = c4_utils._emit_sentences_to_urls(
        (sentence, urls), counter_inc_fn, skip_n=2)
    ret_urls, ret_sentences = zip(*results)
    self.assertEqual(expected_urls, ret_urls)
    self.assertEqual((sentence,) * 2, ret_sentences)
    self.assertEqual({"emitted-sentences-duplicate": 1}, dict(counters))

  def test_remove_sentences_from_page(self):
    counters, counter_inc_fn = _get_counters()
    sentences_to_remove = [
        ("this line has enough words and ends in punctuation, dr. roberts!",),
        ("sentence 1.", "sentence 2.", "sentence 3."),
        ("sentence 3.", "sentence 4."),  # no match
        ("sentence 1.", "sentence 3.", "sentence 4."),  # no match
        ("sentence 3.", "sentence 4.", "sentence 5."),  # no match
    ]
    text = (
        EXPECTED_CLEAN_EN + "\nSentence 1. Sentence 2. Sentence 3. Sentence 4.")
    expected_text = ("\"Open Access. Powered by Scholars. "
                     "Published by Universities.\"\nSentence 4.")
    result = list(c4_utils._remove_sentences_from_text(
        ("url", {"text": [text], "sentences": sentences_to_remove}),
        max_window_size=3,
        counter_inc_fn=counter_inc_fn))
    self.assertEqual([("url", expected_text)], result)
    self.assertEqual({"filtered-sentence-duplicate": 4}, dict(counters))

    counters.clear()
    sentences_to_remove.append(("sentence 2.", "sentence 3.", "sentence 4."))
    expected_text = (
        "\"Open Access. Powered by Scholars. Published by Universities.\"")
    result = list(c4_utils._remove_sentences_from_text(
        ("url", {"text": [text], "sentences": sentences_to_remove}),
        counter_inc_fn=counter_inc_fn,
        max_window_size=3,
        min_num_sentences=3))
    self.assertEqual([("url", expected_text)], result)
    self.assertEqual({"filtered-sentence-duplicate": 5}, dict(counters))

    counters.clear()
    result = list(c4_utils._remove_sentences_from_text(
        ("url", {"text": [text], "sentences": sentences_to_remove}),
        counter_inc_fn=counter_inc_fn,
        max_window_size=3,
        min_num_sentences=4))
    self.assertEqual([], result)
    self.assertEqual(
        {"filtered-sentence-duplicate": 5, "filtered-doc-toofewsentences": 1},
        dict(counters))

  def test_split_wet_file(self):
    if six.PY2:
      # GzipFile + GFile and TextIOWrapper are broken for py2.
      return
    counters, counter_inc_fn = _get_counters()
    list(c4_utils.split_wet_file(
        os.path.join(testing.fake_examples_dir(), "c4", "cc_0.warc.wet.gz"),
        counter_inc_fn=counter_inc_fn))
    self.assertEqual(
        {"wet-file": 1, "page-emitted": 2, "page-filitered-nourl": 1},
        dict(counters))


if __name__ == "__main__":
  testing.test_main()

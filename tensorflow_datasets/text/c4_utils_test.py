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

"""Tests for c4_utils."""

import collections
import os

import six
from tensorflow_datasets import testing
from tensorflow_datasets.core.lazy_imports_lib import lazy_imports
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

FAKE_CONTENT_LENGTH = "5793"
FAKE_CONTENT_TYPE = "text/plain"
FAKE_TIMESTAMP = "2019-04-24T09:23:58Z"

PageFeatures = c4_utils.PageFeatures


def _get_counters():
  counters = collections.defaultdict(int)

  def counter_inc_fn(c, amt=1):
    counters[c] += amt

  return counters, counter_inc_fn


class C4UtilsTest(testing.TestCase):

  def run_clean_page(self, page):
    counters, counter_inc_fn = _get_counters()
    results = list(
        c4_utils.get_clean_page_fn()(page=page, counter_inc_fn=counter_inc_fn)
    )
    self.assertLessEqual(len(results), 1)
    result = None if not results else results[0]
    return result, counters

  def test_clean_page(self):
    clean_en, counters = self.run_clean_page(
        PageFeatures(
            text=EN_TEXT,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertEqual(EXPECTED_CLEAN_EN, clean_en.text)
    self.assertEqual(
        {
            "line-passed": 2,
            "line-filtered:too_short": 1,
            "line-filtered:no_endmark": 2,
            "line-filtered:javascript": 2,
            "line-filtered:policy": 3,
            "passed": 1,
        },
        dict(counters),
    )

  def test_clean_page_toofewsentences(self):
    text_with_toofewsentences = """This first line has one sentence.
This line looks like it has three sentences...but it's actually just 1."""
    clean_en, counters = self.run_clean_page(
        PageFeatures(
            text=text_with_toofewsentences,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertIsNone(clean_en)
    self.assertEqual(
        {"line-passed": 2, "filtered:too_few_sentences": 1}, dict(counters)
    )

  def test_clean_page_squigglybracket(self):
    text_that_is_actually_code = """This page starts out with some text.
Everything looks good at first, since these are sentences.
But then, all of a sudden, there's a bunch of code like the next block.
fn foo(a) { bar = a + 10; }."""
    clean_en, counters = self.run_clean_page(
        PageFeatures(
            text=text_that_is_actually_code,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertIsNone(clean_en)
    self.assertEqual(
        {"filtered:squigglybracket": 1, "line-passed": 3}, dict(counters)
    )

  def test_clean_page_loremipsum(self):
    lorem_ipsum_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    clean_en, counters = self.run_clean_page(
        PageFeatures(
            text=lorem_ipsum_text,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertIsNone(clean_en)
    self.assertEqual({"filtered:loremipsum": 1}, dict(counters))

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
        "line-passed": 3,
        "line-filtered:no_endmark": 1,
        "passed": 1,
    }
    out, counters = self.run_clean_page(
        PageFeatures(
            text=text,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertEqual(expected_clean_text, out.text)
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
        "line-passed": 3,
        "line-filtered:policy": 3,
        "passed": 1,
    }
    out, counters = self.run_clean_page(
        PageFeatures(
            text=text,
            content_type=FAKE_CONTENT_TYPE,
            content_length=FAKE_CONTENT_LENGTH,
            timestamp=FAKE_TIMESTAMP,
        )
    )
    self.assertEqual(expected_clean_text, out.text)
    self.assertEqual(expected_counters, dict(counters))

  def test_remove_duplicate_text(self):
    import apache_beam.testing.util as beam_testing_util  # pylint:disable=g-import-not-at-top

    beam = lazy_imports.apache_beam
    input_pages = [
        PageFeatures(
            url="url/1-0",
            text="This is a duplicated line.\nThis is a unique line.\n"
            + "This one comes first and so it stays.\n"
            + "This is duplicate within the page so the others are removed.\n"
            + "Here is a sentence between the duplicates.\n"
            + "This is duplicate within the page so the others are removed.\n"
            + "this is Duplicate WITHIN the page so the others are removed. ",
        ),
        PageFeatures(
            url="url/2-1",
            text="This is 2nd unique line.\nThis one comes second so it is "
            + "removed even though the capitalizaiton is different.\n"
            + "this is a Duplicated line. ",
        ),
        PageFeatures(
            url="url/3-4",
            text="This is a 3rd unique line.\nThis is a duplicated line.\n"
            + "This one comes third and so it is removed. But the page stays "
            + "because there are still 3 sentences remaining.",
        ),
        PageFeatures(
            url="url/4-4",
            text="This is a 4th unique line.\nThis is a duplicated line.\n"
            + "This one comes third and so it is removed, and the page is too "
            + "since there aren't enough sentences left.",
        ),
    ]
    expected_pages = [
        PageFeatures(
            url="url/1-0",
            text="This is a duplicated line.\nThis is a unique line.\n"
            + "This one comes first and so it stays.\n"
            + "This is duplicate within the page so the others are removed.\n"
            + "Here is a sentence between the duplicates.",
        ),
        PageFeatures(
            url="url/3-4",
            text="This is a 3rd unique line.\n"
            + "This one comes third and so it is removed. But the page stays "
            + "because there are still 3 sentences remaining.",
        ),
    ]
    with beam.Pipeline() as pipeline:
      pages = pipeline | beam.Create(input_pages)
      deduped_pages = c4_utils.remove_duplicate_text(pages)
      beam_testing_util.assert_that(
          deduped_pages, beam_testing_util.equal_to(expected_pages)
      )

  def test_split_wet_file(self):
    if six.PY2:
      # GzipFile + GFile and TextIOWrapper are broken for py2.
      return
    counters, counter_inc_fn = _get_counters()
    list(
        c4_utils.split_wet_file(
            os.path.join(
                testing.fake_examples_dir(), "c4/c4_wet_files/cc_0.warc.wet.gz"
            ),
            counter_inc_fn=counter_inc_fn,
        )
    )
    self.assertEqual(
        {
            "wet-file": 1,
            "passed": 6,
            "filtered:no_url": 1,
        },
        dict(counters),
    )

  def test_badwords_filter(self):
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
        "Ass is one of several species of small, horse-like animals.",
        # Make sure it will still trigger when surrounded by punctuation.
        'Donkey is one synonym for the word "ass".',
        # Make sure it correctly handles different languages.
        "Ass is not a badword in Spanish.",
        "Culo is though.",
        "Ass and culo aren't badwords in German.",
    ]
    languages = [
        "en",
        "en",
        "en-latin",
        "en",
        "es",
        "es",
        "de",  # doesn't have badwords listed
    ]
    expected_outputs = [True, False, False, False, True, False, True]
    badwords_filter_fn = c4_utils.get_badwords_filter_fn(
        badwords={"en": ["ass"], "es": ["culo"]}
    )

    outputs = [
        badwords_filter_fn(  # pylint:disable=g-complex-comprehension
            PageFeatures(text=padding_text + final_sentence, language=language)
        )
        for final_sentence, expected_output, language in zip(
            final_sentences, expected_outputs, languages
        )
    ]

    self.assertListEqual(expected_outputs, outputs)

  def test_soft_badwords_filter(self):
    badwords_filter_fn = c4_utils.get_badwords_filter_fn(
        badwords={"": ["bad"]}, filter_fraction=0.5
    )

    self.assertTrue(
        badwords_filter_fn(
            page=PageFeatures(
                text="good page", normalized_url="filtered.url.com", language=""
            )
        )
    )
    self.assertFalse(
        badwords_filter_fn(
            page=PageFeatures(
                text="bad page", normalized_url="filtered.url.com", language=""
            )
        )
    )
    self.assertTrue(
        badwords_filter_fn(
            page=PageFeatures(
                text="bad page",
                normalized_url="unfiltered.url.com",
                language="",
            )
        )
    )

  def test_paragraph_filter(self):
    text = """This line is long enough to be a paragraph.
This one is not.
This one is. I promise!
"""
    additional_paragraph = "If we add this paragraph, the page should pass."

    page = PageFeatures(text=text)
    self.assertFalse(
        c4_utils.paragraph_filter(page, min_paragraphs=2, min_paragraph_len=20)
    )
    self.assertFalse(
        c4_utils.paragraph_filter(page, min_paragraphs=3, min_paragraph_len=20)
    )
    page = PageFeatures(text=text + additional_paragraph)
    self.assertTrue(
        c4_utils.paragraph_filter(page, min_paragraphs=3, min_paragraph_len=20)
    )


if __name__ == "__main__":
  testing.test_main()

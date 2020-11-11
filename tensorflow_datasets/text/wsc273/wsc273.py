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

"""WSC273 Dataset."""

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{levesque2012winograd,
  title={The winograd schema challenge},
  author={Levesque, Hector and Davis, Ernest and Morgenstern, Leora},
  booktitle={Thirteenth International Conference on the Principles of Knowledge Representation and Reasoning},
  year={2012},
  organization={Citeseer}
}
"""

_DESCRIPTION = """
WSC273 is a common sense reasoning benchmark that requires the system to read a sentence with an ambiguous pronoun and select the referent of that pronoun from two choices.
It contains the first 273 examples from the Winograd Schema Challenge.
A Winograd schema is a pair of sentences that differ in only one or two words and that contain an ambiguity that is resolved in opposite ways in the two sentences and requires the use of world knowledge and reasoning for its resolution.
The schema takes its name from a well-known example by Terry Winograd: ``The city councilmen refused the demonstrators a permit because they [feared/advocated] violence.''
If the word is ``feared'', then ``they'' presumably refers to the city council; if it is ``advocated'' then ``they'' presumably refers to the demonstrators.
"""

_HOMEPAGE_URL = "https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WS.html"

_DOWNLOAD_URL = "https://cs.nyu.edu/faculty/davise/papers/WinogradSchemas/WSCollection.xml"


class Wsc273(tfds.core.GeneratorBasedBuilder):
  """The WSC273 dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "text": tfds.features.Text(),
            "option1": tfds.features.Text(),
            "option1_normalized": tfds.features.Text(),
            "option2": tfds.features.Text(),
            "option2_normalized": tfds.features.Text(),
            "pronoun_start": tf.int32,
            "pronoun_end": tf.int32,
            "pronoun_text": tfds.features.Text(),
            "label": tf.int32,
            "idx": tf.int32,
        }),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_path = dl_manager.download(_DOWNLOAD_URL)
    return {tfds.Split.TEST: self._generate_examples(file_path)}

  def _generate_examples(self, file_path):
    """Yields Examples.

    Args:
      file_path: Path of the test xml file.

    Yields:
      The next examples
    """
    examples = parse_wsc273_xml(file_path.read_text())
    for e in examples:
      yield e["idx"], e


def normalize_text(text):
  text = text.strip()
  # Correct a misspell.
  text = text.replace("recieved", "received")
  text = text.replace("\n", " ")
  text = text.replace("  ", " ")
  return text


def normalize_cap(option, pron):
  """Normalize the capitalization of the option according to the pronoun."""
  cap_tuples = [
      ("The", "the"), ("His", "his"), ("My", "my"),
      ("Her", "her"), ("Their", "their"), ("An", "an"), ("A", "a")]
  uncap_dict = dict(cap_tuples)
  cap_dict = dict([(t[1], t[0]) for t in cap_tuples])
  words = option.split(" ")
  first_word = words[0]
  if pron[0].islower():
    first_word = uncap_dict.get(first_word, first_word)
  else:
    first_word = cap_dict.get(first_word, first_word)
  words[0] = first_word
  option = " ".join(words)
  return option


def parse_wsc273_xml(xml_data):
  """Parse the XML file containing WSC273 examples."""
  soup = tfds.core.lazy_imports.bs4.BeautifulSoup(xml_data, "lxml")
  schemas = soup.find_all("schema")
  # Only the first 273 examples are included in WSC273.
  for i, schema in enumerate(schemas[:273]):
    txt1 = schema.find_all("txt1")[0].get_text()
    txt1 = normalize_text(txt1)
    txt2 = schema.find_all("txt2")[0].get_text()
    txt2 = normalize_text(txt2)
    pron = schema.find_all("pron")[0].get_text()
    pron = normalize_text(pron)
    answers = [ans.get_text().strip() for ans in schema.find_all("answer")]
    normalized_answers = [normalize_cap(ans, pron) for ans in answers]
    assert len(answers) == 2
    choice = schema.find_all("correctanswer")[0].get_text().strip()
    label = {"A": 0, "B": 1}[choice[0]]
    if len(txt2) == 1:
      # If there is only one punctuation left after the pronoun,
      # then no space should be inserted.
      text = f"{txt1} {pron}{txt2}"
    else:
      text = f"{txt1} {pron} {txt2}"
    pronoun_text = pron
    pronoun_start = len(txt1) + 1
    pronoun_end = len(txt1) + len(pron) + 1
    example = dict(
        text=text,
        pronoun_text=pronoun_text,
        pronoun_start=pronoun_start,
        pronoun_end=pronoun_end,
        option1=answers[0],
        option2=answers[1],
        option1_normalized=normalized_answers[0],
        option2_normalized=normalized_answers[1],
        label=label,
        idx=i)
    assert text[pronoun_start:pronoun_end] == pronoun_text
    yield example

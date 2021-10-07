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

"""Facebook Low Resource (FLoRes) machine translation benchmark dataset."""

import collections

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Evaluation datasets for low-resource machine translation: Nepali-English and Sinhala-English.
"""

_CITATION = """\
@misc{guzmn2019new,
    title={Two New Evaluation Datasets for Low-Resource Machine Translation: Nepali-English and Sinhala-English},
    author={Francisco Guzman and Peng-Jen Chen and Myle Ott and Juan Pino and Guillaume Lample and Philipp Koehn and Vishrav Chaudhary and Marc'Aurelio Ranzato},
    year={2019},
    eprint={1902.01382},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
"""

_DATA_URL = "https://github.com/facebookresearch/flores/raw/master/data/wikipedia_en_ne_si_test_sets.tgz"

# Tuple that describes a single pair of files with matching translations.
# language_to_file is the map from language (2 letter string: example 'en')
# to the file path in the extracted directory.
TranslateData = collections.namedtuple("TranslateData",
                                       ["url", "language_to_file"])


class FloresConfig(tfds.core.BuilderConfig):
  """BuilderConfig for FLoRes."""

  def __init__(self, *, language_pair=(None, None), **kwargs):
    """BuilderConfig for FLoRes.

    Args:
      language_pair: pair of languages that will be used for translation. Should
        contain 2-letter coded strings. First will be used at source and second
        as target in supervised mode. For example: ("se", "en").
      **kwargs: keyword arguments forwarded to super.
    """
    name = f"{language_pair[0]}{language_pair[1]}"

    description = (
        f"Translation dataset from {language_pair[0]} to {language_pair[1]}.")
    super(FloresConfig, self).__init__(
        name=name,
        description=description,
        version=tfds.core.Version("1.2.0"),
        **kwargs)

    # Validate language pair.
    assert "en" in language_pair, (
        "Config language pair must contain `en`, got: %s", language_pair)
    source, target = language_pair
    non_en = source if target == "en" else target
    assert non_en in ["ne",
                      "si"], ("Invalid non-en language in pair: %s", non_en)

    self.language_pair = language_pair


class Flores(tfds.core.GeneratorBasedBuilder):
  """FLoRes machine translation dataset."""

  BUILDER_CONFIGS = [
      FloresConfig(language_pair=("ne", "en"),),
      FloresConfig(language_pair=("si", "en"),),
  ]

  def _info(self):
    source, target = self.builder_config.language_pair
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(
            languages=self.builder_config.language_pair),
        supervised_keys=(source, target),
        homepage="https://github.com/facebookresearch/flores/",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_dir = dl_manager.download_and_extract(_DATA_URL)

    source, target = self.builder_config.language_pair
    non_en = source if target == "en" else target
    path_tmpl = (
        "{dl_dir}/wikipedia_en_ne_si_test_sets/wikipedia.{split}.{non_en}-en."
        "{lang}")

    files = {}
    for split in ("dev", "devtest"):
      files[split] = {
          "source_file":
              path_tmpl.format(
                  dl_dir=dl_dir, split=split, non_en=non_en, lang=source),
          "target_file":
              path_tmpl.format(
                  dl_dir=dl_dir, split=split, non_en=non_en, lang=target),
      }

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION, gen_kwargs=files["dev"]),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, gen_kwargs=files["devtest"]),
    ]

  def _generate_examples(self, source_file, target_file):
    """This function returns the examples in the raw (text) form."""
    with tf.io.gfile.GFile(source_file) as f:
      source_sentences = f.read().split("\n")
    with tf.io.gfile.GFile(target_file) as f:
      target_sentences = f.read().split("\n")

    assert len(target_sentences) == len(
        source_sentences), "Sizes do not match: %d vs %d for %s vs %s." % (len(
            source_sentences), len(target_sentences), source_file, target_file)

    source, target = self.builder_config.language_pair
    for idx, (l1, l2) in enumerate(zip(source_sentences, target_sentences)):
      result = {source: l1, target: l2}
      # Make sure that both translations are non-empty.
      if all(result.values()):
        yield idx, result

# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Google's Natural Questions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_BUCKET = "gs://natural_questions/v1.0/"

_CITATION = """\

"""

_DESCRIPTION = """\
The NQ corpus contains questions from real users, and it requires QA systems to
read and comprehend an entire Wikipedia article that may or may not contain the
answer to the question.

Note that we currently:
* Keep the document text as HTML
* Keep only the first short answer
* Drop the tokens fields (we use the built-in TextEncoders instead)
* Drop the long answer candidates
* Share the vocabulary amongst all text features

Please leave feedback in the [GitHub
issue](https://github.com/tensorflow/datasets/issues/33) about how this dataset
is configured and exposed.
"""

_URL = "https://ai.google.com/research/NaturalQuestions/dataset"


class NQConfig(tfds.core.BuilderConfig):
  """BuilderConfig for NaturalQuestions."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """BuilderConfig for NaturalQuestions.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the text features.
      **kwargs: keyword arguments forwarded to super.
    """
    super(NQConfig, self).__init__(**kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())


class NaturalQuestions(tfds.core.GeneratorBasedBuilder):
  """Natural Questions dataset."""

  BUILDER_CONFIGS = [
      NQConfig(
          name="plain_text",
          version="0.0.1",
          description="Plain text",
      ),
      NQConfig(
          name="bytes",
          version="0.0.1",
          description=("Uses byte-level text encoding with "
                       "`tfds.features.text.ByteTextEncoder`"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder=tfds.features.text.ByteTextEncoder()),
      ),
      NQConfig(
          name="subwords8k",
          version="0.0.1",
          description=("Uses `tfds.features.text.SubwordTextEncoder` with 8k "
                       "vocab size"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              vocab_size=2**13),
      ),
      NQConfig(
          name="subwords32k",
          version="0.0.1",
          description=("Uses `tfds.features.text.SubwordTextEncoder` with "
                       "32k vocab size"),
          text_encoder_config=tfds.features.text.TextEncoderConfig(
              encoder_cls=tfds.features.text.SubwordTextEncoder,
              vocab_size=2**15),
      ),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "example_id": tf.int64,
            "document_url": tfds.features.Text(),
            "document_title":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "question_text":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "document_html":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "long_answer":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "short_answer":
                tfds.features.Text(
                    encoder_config=self.builder_config.text_encoder_config),
            "yes_no_answer": tfds.features.ClassLabel(
                names=["NO", "YES", "NONE"]),
        }),
        supervised_keys=None,
        urls=[_URL],
        citation=_CITATION,
    )

  def _vocab_text_gen(self, filepath):
    for i, ex in self._generate_examples(filepath):
      # Use 10k examples for vocab generation
      if i >= 10000:
        break
      # long_answer and short_answer are in the document_html so no need to
      # include them here.
      vocab_fields = ["document_title", "question_text", "document_html"]
      yield " ".join([ex[name] for name in vocab_fields])

  def _split_generators(self, dl_manager):
    files = {
        split: tf.io.gfile.listdir(os.path.join(_BUCKET, split)) for split in
        ["train", "dev"]
    }
    downloads = dl_manager.download_and_extract(files)

    # Generate vocabulary
    # maybe_build_from_corpus uses SubwordTextEncoder if that's configured
    shared_vocab_features = ["document_title", "question_text", "document_html",
                             "short_answer", "long_answer"]
    text_feature = self.info.features[shared_vocab_features[0]]
    text_feature.maybe_build_from_corpus(
        self._vocab_text_gen(downloads["train"]))
    encoder = text_feature.encoder
    for feature in shared_vocab_features:
      self.info.features[feature].maybe_set_encoder(encoder)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=100,
            gen_kwargs={"files": downloads["train"]}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=10,
            gen_kwargs={"files": downloads["dev"]}),
    ]

  def _generate_examples(self, files):
    """This function returns the examples in the raw (text) form."""
    for filename in files:
      with tf.io.gfile.GFile(filename) as f:
        reader = tfds.core.lazy_imports.jsonlines.Reader(f)
        for record in reader:

          def _answer(annotation):
            start_byte = annotation["start_byte"]
            end_byte = annotation["end_byte"]
            return record["document_html"].encode(
                "utf-8")[start_byte:end_byte].decode("utf-8")

          annotation = record["annotations"][0]
          yield {
              "example_id": record["example_id"],
              "document_title": record["document_title"],
              "question_text": record["question_text"],
              "document_html": record["document_html"],
              "document_url": record["document_url"],
              "long_answer": _answer(annotation["long_answer"]),
              "short_answer": _answer(annotation["short_answer"]),
              "yes_no_answer": annotation["yes_no_answer"],
          }

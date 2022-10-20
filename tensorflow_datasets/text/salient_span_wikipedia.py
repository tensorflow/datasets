# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

r"""Wikipedia sentences with labeled salient spans."""
from __future__ import annotations

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_VERSION = tfds.core.utils.Version("1.0.0")
_DESCRIPTION = "Wikipedia sentences with labeled salient spans."
_CITATION = """
@article{guu2020realm,
    title={REALM: Retrieval-Augmented Language Model Pre-Training},
    author={Kelvin Guu and Kenton Lee and Zora Tung and Panupong Pasupat and Ming-Wei Chang},
    year={2020},
    journal = {arXiv e-prints},
    archivePrefix = {arXiv},
    eprint={2002.08909},
}
"""

_INPUT_FILE_PATTERN = "gs://realm-data/realm-data/pretrain_corpus/wikipedia_annotated_with_dates_public@5000.tfrecord.gz"


class SalientSpanWikipediaConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SalientSpanWikipedia dataset."""

  def __init__(self, *, split_sentences, **kwargs):
    """BuilderConfig for SalientSpanWikipedia.

    Args:
      split_sentences: bool, whether to split individual sentences into separate
        examples.
      **kwargs: keyword arguments forwarded to super.
    """
    self.split_sentences = split_sentences
    super(SalientSpanWikipediaConfig, self).__init__(version=_VERSION, **kwargs)


class SalientSpanWikipedia(tfds.core.BeamBasedBuilder):
  """Wikipedia articles with labeled salient spans."""

  BUILDER_CONFIGS = [
      SalientSpanWikipediaConfig(
          name="sentences",
          split_sentences=True,
          description="Examples are individual sentences containing entities."),
      SalientSpanWikipediaConfig(
          name="documents",
          split_sentences=False,
          description="Examples re full documents."),
  ]

  def _info(self):
    feature_dict = {
        "title":
            tfds.features.Text(),
        "text":
            tfds.features.Text(),
        "spans":
            tfds.features.Sequence({
                "start": tf.int32,
                "limit": tf.int32,
                "type": tf.string,
            }),
    }
    if not self.builder_config.split_sentences:
      feature_dict["sentences"] = tfds.features.Sequence({
          "start": tf.int32,
          "limit": tf.int32,
      })

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        citation=_CITATION,
        features=tfds.features.FeaturesDict(feature_dict),
    )

  def _split_generators(self, dl_manager):
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"split_sentences": self.builder_config.split_sentences
                       }),
    ]

  def _build_pcollection(self, pipeline, split_sentences):
    """Build Pcollection of examples in text form."""
    beam = tfds.core.lazy_imports.apache_beam

    def _inc_counter(name, amt=1):
      beam.metrics.Metrics.counter("salient_span_wikipedia", name).inc(amt)

    def _emit_example(ex):
      _inc_counter("input-examples")

      def int_feat(key):
        return np.array(ex.features.feature[key].int64_list.value, np.int32)

      def str_feat(key):
        return np.array(ex.features.feature[key].bytes_list.value)

      uid = str_feat("uid")
      title = str_feat("title")[0]
      text = str_feat("text")[0]
      span_start = int_feat("span_byte_start")
      span_limit = int_feat("span_byte_limit")
      span_type = str_feat("span_type")
      sent_start = int_feat("sentence_byte_start")
      sent_limit = int_feat("sentence_byte_limit")

      if not split_sentences:
        _inc_counter("output-examples")
        yield uid, {
            "title": title,
            "text": text,
            "spans": {
                "start": span_start,
                "limit": span_limit,
                "type": span_type,
            },
            "sentences": {
                "start": sent_start,
                "limit": sent_limit
            }
        }
      else:
        span_i = 0
        for sent_i, (sent_start,
                     sent_limit) in enumerate(zip(sent_start, sent_limit)):
          span_indices = []
          while (span_i < len(span_start) and span_start[span_i] < sent_limit):
            if span_limit[span_i] <= sent_limit:
              span_indices.append(span_i)
            else:
              _inc_counter("cross-sentence-spans")
            span_i += 1

          if not span_indices:
            _inc_counter("sentence-no-spans")
            continue
          _inc_counter("in-sentence-spans", len(span_indices))

          _inc_counter("output-examples")
          yield "%s:%d" % (uid, sent_i), {
              "title": title,
              "text": text[sent_start:sent_limit],
              "spans": {
                  "start": span_start[span_indices] - sent_start,
                  "limit": span_limit[span_indices] - sent_start,
                  "type": span_type[span_indices],
              }
          }

    return (pipeline
            | beam.io.ReadFromTFRecord(
                _INPUT_FILE_PATTERN,
                coder=beam.coders.ProtoCoder(tf.train.Example))
            | beam.FlatMap(_emit_example))

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

# Lint as: python2, python3
"""Opinion Abstracts Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
from typing import Any, Dict, Iterator, List, Text, Tuple

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{wang-ling-2016-neural,
    title = "Neural Network-Based Abstract Generation for Opinions and Arguments",
    author = "Wang, Lu  and
      Ling, Wang",
    booktitle = "Proceedings of the 2016 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2016",
    address = "San Diego, California",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N16-1007",
    doi = "10.18653/v1/N16-1007",
    pages = "47--57",
}
"""

_DESCRIPTION = """
There are two sub datasets:

(1) RottenTomatoes: The movie critics and consensus crawled from
http://rottentomatoes.com/. It has fields of "_movie_name", "_movie_id",
"_critics", and "_critic_consensus".

(2) IDebate: The arguments crawled from http://idebate.org/. It has fields of
"_debate_name", "_debate_id", "_claim", "_claim_id", "_argument_sentences".

"""

_URL = "http://www.ccs.neu.edu/home/luwang/datasets/opinion_abstracts.zip"


class OpinionAbstractsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for OpinionAbstracts."""

  @tfds.core.disallow_positional_args
  def __init__(self,
               filename: Text = None,
               name_key: Text = None,
               id_key: Text = None,
               opinions_key: Text = None,
               summary_key: Text = None,
               **kwargs):
    """BuilderConfig for OpinionAbstracts."""
    super(OpinionAbstractsConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs)
    self.filename = filename
    self.name_key = name_key
    self.id_key = id_key
    self.opinions_key = opinions_key
    self.summary_key = summary_key


class OpinionAbstracts(tfds.core.GeneratorBasedBuilder):
  """OpinionAbstracts Dataset Builder."""

  VERSION = tfds.core.Version("1.0.0")
  BUILDER_CONFIGS = [
      OpinionAbstractsConfig(
          name="rotten_tomatoes",
          filename="rottentomatoes.json",
          name_key="_movie_name",
          id_key="_movie_id",
          opinions_key="_critics",
          summary_key="_critic_consensus",
          description="Professional critics and consensus of 3,731 movies.",
      ),
      OpinionAbstractsConfig(
          name="idebate",
          filename="idebate.json",
          name_key="_debate_name",
          id_key="_claim_id",
          opinions_key="_argument_sentences",
          summary_key="_claim",
          description="2,259 claims for 676 debates.",
      )
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    config = self.builder_config
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            config.name_key:
                tf.string,
            config.id_key:
                tf.string,
            config.summary_key:
                tf.string,
            config.opinions_key:
                tfds.features.Sequence(
                    tfds.features.FeaturesDict({
                        "key": tf.string,
                        "value": tf.string
                    })),
        }),
        supervised_keys=(config.opinions_key, config.summary_key),
        homepage="http://www.ccs.neu.edu/home/luwang/data.html",
        citation=_CITATION,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    path = os.path.join(dl_path, "opinion_abstracts",
                        self.builder_config.filename)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": path},
        ),
    ]

  def _generate_examples(self,
                         path: Text = None
                        ) -> Iterator[Tuple[Text, Dict[Text, Any]]]:
    """Yields examples."""
    with tf.io.gfile.GFile(path, "rb") as f:
      for example in json.load(f):
        config = self.builder_config
        opinions = example[config.opinions_key].items()
        opinions = [{"key": k, "value": v} for k, v in opinions]
        features = {config.opinions_key: opinions}
        for k in [config.name_key, config.id_key, config.summary_key]:
          features[k] = example[k]
        yield example[config.id_key], features

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

"""Opinion Abstracts Dataset."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, Iterator, List, Optional, Text, Tuple

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_URL = "https://web.eecs.umich.edu/~wangluxy/datasets/opinion_abstracts.zip"


class OpinionAbstractsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for OpinionAbstracts."""

  def __init__(
      self,
      *,
      filename: Optional[Text] = None,
      name_key: Optional[Text] = None,
      id_key: Optional[Text] = None,
      opinions_key: Optional[Text] = None,
      summary_key: Optional[Text] = None,
      **kwargs,
  ):
    """BuilderConfig for OpinionAbstracts."""
    super(OpinionAbstractsConfig, self).__init__(
        version=tfds.core.Version("1.0.0"), **kwargs
    )
    self.filename = filename
    self.name_key = name_key
    self.id_key = id_key
    self.opinions_key = opinions_key
    self.summary_key = summary_key


class Builder(tfds.core.GeneratorBasedBuilder):
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
      ),
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    config = self.builder_config
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            config.name_key: np.str_,
            config.id_key: np.str_,
            config.summary_key: np.str_,
            config.opinions_key: tfds.features.Sequence(
                tfds.features.FeaturesDict({"key": np.str_, "value": np.str_})
            ),
        }),
        supervised_keys=(config.opinions_key, config.summary_key),
        homepage="https://web.eecs.umich.edu/~wangluxy/data.html",
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    dl_path = dl_manager.download_and_extract(_URL)
    path = os.path.join(
        dl_path, "opinion_abstracts", self.builder_config.filename
    )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": path},
        ),
    ]

  def _generate_examples(
      self, path: Optional[Text] = None
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

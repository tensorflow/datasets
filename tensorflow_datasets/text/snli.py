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

"""The Stanford NLI Corpus."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{snli:emnlp2015,
	Author = {Bowman, 
              Samuel R. and Angeli, 
              Gabor and Potts, Christopher, 
              and Manning, Christopher D.
            },
	Booktitle = {Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
	Publisher = {Association for Computational Linguistics},
	Title = {A large annotated corpus for learning natural language inference},
	Year = {2015}
}
"""

_DESCRIPTION = """\
The SNLI corpus (version 1.0) is a collection of 570k human-written English sentence
pairs manually labeled for balanced classification with the labels entailment, contradiction,
and neutral, supporting the task of natural language inference (NLI), also known as recognizing
textual entailment (RTE). We aim for it to serve both as a benchmark for evaluating representational
systems for text, especially including those induced by representation learning methods,
as well as a resource for developing NLP models of any kind.
"""


class SNLIConfig(tfds.core.BuilderConfig):
  """BuilderConfig for SNLI."""

  @api_utils.disallow_positional_args
  def __init__(self, text_encoder_config=None, **kwargs):
    """BuilderConfig for SNLI.

    Args:
      text_encoder_config: `tfds.features.text.TextEncoderConfig`, configuration
        for the `tfds.features.text.TextEncoder` used for the features feature.
      **kwargs: keyword arguments forwarded to super.
    """
    super(SNLIConfig, self).__init__(**kwargs)
    self.text_encoder_config = (
        text_encoder_config or tfds.features.text.TextEncoderConfig())





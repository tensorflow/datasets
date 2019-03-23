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

"""The Stanford Question Answering Dataset - 2.0"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

from absl import logging
import tensorflow as tf
from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{DBLP:journals/corr/abs-1806-03822,
  author    = {Pranav Rajpurkar and
               Robin Jia and
               Percy Liang},
  title     = {Know What You Don't Know: Unanswerable Questions for SQuAD},
  journal   = {CoRR},
  volume    = {abs/1806.03822},
  year      = {2018},
  url       = {http://arxiv.org/abs/1806.03822},
  archivePrefix = {arXiv},
  eprint    = {1806.03822},
  timestamp = {Mon, 13 Aug 2018 16:48:21 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1806-03822},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
"""

_DESCRIPTION = """\
The Stanford Question Answering Dataset - 2.0 combines the 100,000 questions in SQuAD1.1 \
with over 50,000 new, unanswerable questions written adversarially by crowdworkers to look similar \
to answerable ones. To do well on dataset, systems must not only answer \
questions when possible, but also determine when no answer is supported by \
the paragraph and abstain from answering. SQuAD2.0 is a challenging natural \
language understanding task for existing models.
"""




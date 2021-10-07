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

"""Yelp Polarity Reviews dataset."""

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
Large Yelp Review Dataset.
This is a dataset for binary sentiment classification. \
We provide a set of 560,000 highly polar yelp reviews for training, and 38,000 for testing. \

ORIGIN
The Yelp reviews dataset consists of reviews from Yelp. It is extracted
from the Yelp Dataset Challenge 2015 data. For more information, please
refer to http://www.yelp.com/dataset

The Yelp reviews polarity dataset is constructed by
Xiang Zhang (xiang.zhang@nyu.edu) from the above dataset.
It is first used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks
for Text Classification. Advances in Neural Information Processing Systems 28
(NIPS 2015).


DESCRIPTION

The Yelp reviews polarity dataset is constructed by considering stars 1 and 2
negative, and 3 and 4 positive. For each polarity 280,000 training samples and
19,000 testing samples are take randomly. In total there are 560,000 trainig
samples and 38,000 testing samples. Negative polarity is class 1,
and positive class 2.

The files train.csv and test.csv contain all the training samples as
comma-sparated values. There are 2 columns in them, corresponding to class
index (1 and 2) and review text. The review texts are escaped using double
quotes ("), and any internal double quote is escaped by 2 double quotes ("").
New lines are escaped by a backslash followed with an "n" character,
that is "\n".
"""

_CITATION = """\
@article{zhangCharacterlevelConvolutionalNetworks2015,
  archivePrefix = {arXiv},
  eprinttype = {arxiv},
  eprint = {1509.01626},
  primaryClass = {cs},
  title = {Character-Level {{Convolutional Networks}} for {{Text Classification}}},
  abstract = {This article offers an empirical exploration on the use of character-level convolutional networks (ConvNets) for text classification. We constructed several large-scale datasets to show that character-level convolutional networks could achieve state-of-the-art or competitive results. Comparisons are offered against traditional models such as bag of words, n-grams and their TFIDF variants, and deep learning models such as word-based ConvNets and recurrent neural networks.},
  journal = {arXiv:1509.01626 [cs]},
  author = {Zhang, Xiang and Zhao, Junbo and LeCun, Yann},
  month = sep,
  year = {2015},
}

"""

_DOWNLOAD_URL = "https://s3.amazonaws.com/fast-ai-nlp/yelp_review_polarity_csv.tgz"


class YelpPolarityReviews(tfds.core.GeneratorBasedBuilder):
  """Yelp Polarity reviews dataset."""

  VERSION = tfds.core.Version("0.2.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "text": tfds.features.Text(),
            "label": tfds.features.ClassLabel(names=["1", "2"]),
        }),
        supervised_keys=("text", "label"),
        homepage="https://course.fast.ai/datasets",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    arch_path = dl_manager.download_and_extract(_DOWNLOAD_URL)
    train_file = os.path.join(arch_path, "yelp_review_polarity_csv",
                              "train.csv")
    test_file = os.path.join(arch_path, "yelp_review_polarity_csv", "test.csv")
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"filepath": train_file}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST, gen_kwargs={"filepath": test_file}),
    ]

  def _generate_examples(self, filepath):
    """Generate Yelp examples."""
    with tf.io.gfile.GFile(filepath) as f:
      for line_id, line in enumerate(f):
        # The format of the line is:
        # "1", "The text of the review."
        yield line_id, {"text": line[5:-2].strip(), "label": line[1]}

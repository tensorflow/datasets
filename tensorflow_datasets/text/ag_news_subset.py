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

"""The ag_news_subset dataset."""

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@misc{zhang2015characterlevel,
    title={Character-level Convolutional Networks for Text Classification},
    author={Xiang Zhang and Junbo Zhao and Yann LeCun},
    year={2015},
    eprint={1509.01626},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""

_DESCRIPTION = """
AG is a collection of more than 1 million news articles.
News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity.
ComeToMyHead is an academic news search engine which has been running since July, 2004.
The dataset is provided by the academic comunity for research purposes in data mining (clustering, classification, etc),
information retrieval (ranking, search, etc), xml, data compression, data streaming,
and any other non-commercial activity.
For more information, please refer to the link http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html .

The AG's news topic classification dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the dataset above.
It is used as a text classification benchmark in the following paper:
Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).

The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.
Each class contains 30,000 training samples and 1,900 testing samples.
The total number of training samples is 120,000 and testing 7,600.
"""

_HOMEPAGE_URL = "https://arxiv.org/abs/1509.01626"
_DOWNLOAD_URL = "https://drive.google.com/uc?export=download&id=0Bz8a_Dbh9QhbUDNpeUdjb0wxRms"

_LABEL_NAMES = ["World", "Sports", "Business", "Sci/Tech"]


class AGNewsSubset(tfds.core.GeneratorBasedBuilder):
  """This is a dataset for classifying news articles into 4 classes."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "label": tfds.features.ClassLabel(names=_LABEL_NAMES),
            "title": tfds.features.Text(),
            "description": tfds.features.Text(),
        }),
        supervised_keys=("description", "label"),
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_paths = dl_manager.download_and_extract({"ag_news_csv": _DOWNLOAD_URL})
    # Name of the extracted folder is 'ag_news_csv'
    base_path = os.path.join(dl_paths["ag_news_csv"], "ag_news_csv")

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={"path": os.path.join(base_path, "train.csv")},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={"path": os.path.join(base_path, "test.csv")},
        ),
    ]

  def _generate_examples(self, path):
    """Yeilds Examples.

    Args:
      path: The path of the file to be read for this split

    Yields:
      Generator yielding the next examples
    """
    with tf.io.gfile.GFile(path) as f:
      reader = csv.reader(f)
      # CSV files : class label (as number), title, description
      for index, row in enumerate(reader):
        key = index
        # The values in the csv file do not have quotes
        example = {
            # The class labels start from 1 in this dataset
            "label": (int(row[0]) - 1),
            "title": row[1],
            "description": row[2],
        }
        yield key, example

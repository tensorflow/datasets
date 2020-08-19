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

"""Amazon Customer Reviews Dataset --- MULTILINGUAL REVIEWS DATASET"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import OrderedDict
import csv
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import api_utils
import tensorflow_datasets.public_api as tfds


_CITATION = """\
"""


_DESCRIPTION = """\
Amazon Customer Reviews (a.k.a. Product Reviews) is one of Amazon’s iconic products. In a period of over two decades since the first review in 1995, millions of Amazon customers have contributed over a hundred million reviews to express opinions and describe their experiences regarding products on the Amazon.com website. This makes Amazon Customer Reviews a rich source of information for academic researchers in the fields of Natural Language Processing (NLP), Information Retrieval (IR), and Machine Learning (ML), amongst others. Accordingly, we are releasing this data to further research in multiple disciplines related to understanding customer product experiences. Specifically, this dataset was constructed to represent a sample of customer evaluations and opinions, variation in the perception of a product across geographical regions, and promotional intent or bias in reviews.

Each line in the data files corresponds to an individual review (tab delimited, with no quote and escape characters).

Each Dataset contains the following columns : 
  marketplace       - 2 letter country code of the marketplace where the review was written.
  customer_id       - Random identifier that can be used to aggregate reviews written by a single author.
  review_id         - The unique ID of the review.
  product_id        - The unique Product ID the review pertains to. In the multilingual dataset the reviews
                      for the same product in different countries can be grouped by the same product_id.
  product_parent    - Random identifier that can be used to aggregate reviews for the same product.
  product_title     - Title of the product.
  product_category  - Broad product category that can be used to group reviews 
                      (also used to group the dataset into coherent parts).
  star_rating       - The 1-5 star rating of the review.
  helpful_votes     - Number of helpful votes.
  total_votes       - Number of total votes the review received.
  vine              - Review was written as part of the Vine program.
  verified_purchase - The review is on a verified purchase.
  review_headline   - The title of the review.
  review_body       - The review text.
  review_date       - The date the review was written.
"""


_DATA_OPTIONS = ["US", "UK", "JP", "FR", "DE"]  
  
  
_DL_URLS = {name: "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_" + name + "_v1_00.tsv.gz" for name in _DATA_OPTIONS}


class AmazonMultilingualReviewsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for AmazonMultilingualReviews.""" 

  @api_utils.disallow_positional_args
  def __init__(self, data=None, **kwargs):
    """Constructs a AmazonMultilingualReviewsConfig. 
    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    super(AmazonMultilingualReviewsConfig, self).__init__(**kwargs)
    self.data = data 


class AmazonMultilingualReviews(tfds.core.GeneratorBasedBuilder):
  """AmazonMultilingualReviews dataset.""" 

  BUILDER_CONFIGS = [
      AmazonMultilingualReviewsConfig( 
          name=config_name,
          description="A dataset consisting of reviews of various Amazon products in " + config_name + " marketplace. Each product has its own version as specified with it.", 
          version="0.1.0",
          data=config_name,
      ) for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "data": OrderedDict([('marketplace', tf.string), 
                                 ('customer_id', tf.string),
                                 ('review_id', tf.string), 
                                 ('product_id', tf.string), 
                                 ('product_parent', tf.string), 
                                 ('product_title', tf.string), 
                                 ('product_category', tf.string), 
                                 ('star_rating', tf.int32), 
                                 ('helpful_votes', tf.int32), 
                                 ('total_votes', tf.int32), 
                                 ('vine', tfds.features.ClassLabel(names=['Y', 'N'])), 
                                 ('verified_purchase', tfds.features.ClassLabel(names=['Y', 'N'])),  
                                 ('review_headline', tf.string), 
                                 ('review_body', tf.string), 
                                 ('review_date', tf.string)])
        }),
        supervised_keys=None, 
        urls=["https://s3.amazonaws.com/amazon-reviews-pds/readme.html"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    url = _DL_URLS[self.builder_config.name]
    path = dl_manager.download_and_extract(url) 

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name="train",
            gen_kwargs={"file_path": path,} 
        ),
    ]

  def _generate_examples(self, file_path): 
    """Generate features given the directory path.
    
    Args:
      file_path: path where the tsv file is stored
      
    Yields:
      The features. 
    """
    
    with tf.io.gfile.GFile(file_path) as tsvfile:
      # Need to disable quoting - as dataset contains invalid double quotes.
      reader = csv.DictReader(
          tsvfile, dialect="excel-tab", quoting=csv.QUOTE_NONE)
      for i, row in enumerate(reader):
        yield i, {
            "data": row,
        }


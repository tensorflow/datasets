# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""Amazon Per-category Review Dataset v2 (2018) --- US REVIEWS DATASET."""

import json

import numpy as np
import tensorflow_datasets.public_api as tfds


_DATA_OPTIONS = [
    "AMAZON_FASHION",               # reviews (883,636 reviews)     metadata (186,637 products)
    "All_Beauty",                   # reviews (371,345 reviews)     metadata (32,992 products)
    "Appliances",                   # reviews (602,777 reviews)     metadata (30,459 products)
    "Arts_Crafts_and_Sewing",       # reviews (2,875,917 reviews)   metadata (303,426 products)
    "Automotive",                   # reviews (7,990,166 reviews)   metadata (932,019 products)
    "Books",                        # reviews (51,311,621 reviews)  metadata (2,935,525 products)
    "CDs_and_Vinyl",                # reviews (4,543,369 reviews)   metadata (544,442 products)
    "Cell_Phones_and_Accessories",  # reviews (10,063,255 reviews)  metadata (590,269 products)
    "Clothing_Shoes_and_Jewelry",   # reviews (32,292,099 reviews)  metadata (2,685,059 products)
    "Digital_Music",                # reviews (1,584,082 reviews)   metadata (465,392 products)
    "Electronics",                  # reviews (20,994,353 reviews)  metadata (786,868 products)
    "Gift_Cards",                   # reviews (147,194 reviews)     metadata (1,548 products)
    "Grocery_and_Gourmet_Food",     # reviews (5,074,160 reviews)   metadata (287,209 products)
    "Home_and_Kitchen",             # reviews (21,928,568 reviews)  metadata (1,301,225 products)
    "Industrial_and_Scientific",    # reviews (1,758,333 reviews)   metadata (167,524 products)
    "Kindle_Store",                 # reviews (5,722,988 reviews)   metadata (493,859 products)
    "Luxury_Beauty",                # reviews (574,628 reviews)     metadata (12,308 products)
    "Magazine_Subscriptions",       # reviews (89,689 reviews)      metadata (3,493 products)
    "Movies_and_TV",                # reviews (8,765,568 reviews)   metadata (203,970 products)
    "Musical_Instruments",          # reviews (1,512,530 reviews)   metadata (120,400 products)
    "Office_Products",              # reviews (5,581,313 reviews)   metadata (315,644 products)
    "Patio_Lawn_and_Garden",        # reviews (5,236,058 reviews)   metadata (279,697 products)
    "Pet_Supplies",                 # reviews (6,542,483 reviews)   metadata (206,141 products)
    "Prime_Pantry",                 # reviews (471,614 reviews)     metadata (10,815 products)
    "Software",                     # reviews (459,436 reviews)     metadata (26,815 products)
    "Sports_and_Outdoors",          # reviews (12,980,837 reviews)  metadata (962,876 products)
    "Tools_and_Home_Improvement",   # reviews (9,015,203 reviews)   metadata (571,982 products)
    "Toys_and_Games",               # reviews (8,201,231 reviews)   metadata (634,414 products)
    "Video_Games",                  # reviews (2,565,349 reviews)   metadata (84,893 products)
]

_DL_URLS = {
    name: f"https://datarepo.eng.ucsd.edu/mcauley_group/data/amazon_v2/categoryFiles/{name}.json.gz"
    for name in _DATA_OPTIONS
}


class AmazonUSReviewsConfig(tfds.core.BuilderConfig):
  """BuilderConfig for AmazonUSReviews."""

  def __init__(self, *, data=None, **kwargs):
    """Constructs a AmazonUSReviewsConfig.

    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    super(AmazonUSReviewsConfig, self).__init__(**kwargs)
    self.data = data


class Builder(tfds.core.GeneratorBasedBuilder):
  """AmazonUSReviews dataset."""

  BUILDER_CONFIGS = [
      AmazonUSReviewsConfig(  # pylint: disable=g-complex-comprehension
          name=config_name,
          description="A dataset consisting of reviews of Amazon "
          + config_name
          + " products in US marketplace. Each product has its own version as"
          " specified with it.",
          version="2.0.0",
          data=config_name,
      )
      for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {
                "unixReviewTime": np.int32,
                "reviewTime": np.str_,
                "reviewerID": np.str_,
                "reviewerName": np.str_,
                "asin": np.str_,
                "overall": np.int32,
                "summary": np.str_,
                "reviewText": np.str_,
                "verified": np.bool_,
                "style": np.str_,
                "vote": np.int32,
                "image": np.str_,
            }
        ),
        supervised_keys=None,
        homepage="https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/",
    )

  def _split_generators(self, dl_manager):
    url = _DL_URLS[self.builder_config.name]
    path = dl_manager.download_and_extract(url)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name="train",
            gen_kwargs={
                "file_path": path,
            },
        ),
    ]

  def _generate_examples(self, file_path):
    """Generate features given the directory path.

    Args:
      file_path: path where the json file is stored

    Yields:
      The features.
    """

    with open(file_path, "r", encoding="utf-8") as json_file:
        for i, row in enumerate(json_file):
            example = json.loads(row)
            yield i, {
                "unixReviewTime": int(example["unixReviewTime"]),
                "reviewTime": example["reviewTime"],
                "reviewerID": example["reviewerID"],
                "reviewerName": example["reviewerName"],
                "asin": example["asin"],
                "overall": int(example["overall"]),
                "summary": example["summary"],
                "reviewText": example["reviewText"],
                "verified": example.get("verified", False),
                "style": str(example.get("style", {})),
                "vote": int(example.get("vote", 0)),
                "image": str(example.get("image", "")),
            }

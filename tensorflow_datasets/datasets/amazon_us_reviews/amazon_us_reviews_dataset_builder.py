# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Amazon Customer Reviews Dataset --- US REVIEWS DATASET."""

import collections
import csv

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DATA_OPTIONS_V1_00 = [
    "Wireless",
    "Watches",
    "Video_Games",
    "Video_DVD",
    "Video",
    "Toys",
    "Tools",
    "Sports",
    "Software",
    "Shoes",
    "Pet_Products",
    "Personal_Care_Appliances",
    "PC",
    "Outdoors",
    "Office_Products",
    "Musical_Instruments",
    "Music",
    "Mobile_Electronics",
    "Mobile_Apps",
    "Major_Appliances",
    "Luggage",
    "Lawn_and_Garden",
    "Kitchen",
    "Jewelry",
    "Home_Improvement",
    "Home_Entertainment",
    "Home",
    "Health_Personal_Care",
    "Grocery",
    "Gift_Card",
    "Furniture",
    "Electronics",
    "Digital_Video_Games",
    "Digital_Video_Download",
    "Digital_Software",
    "Digital_Music_Purchase",
    "Digital_Ebook_Purchase",
    "Camera",
    "Books",
    "Beauty",
    "Baby",
    "Automotive",
    "Apparel",
]

_DATA_OPTIONS_V1_01 = ["Digital_Ebook_Purchase", "Books"]

_DATA_OPTIONS_V1_02 = ["Books"]

_DATA_OPTIONS = []

for entry in _DATA_OPTIONS_V1_00:
  _DATA_OPTIONS.append(entry + "_v1_00")

for entry in _DATA_OPTIONS_V1_01:
  _DATA_OPTIONS.append(entry + "_v1_01")

for entry in _DATA_OPTIONS_V1_02:
  _DATA_OPTIONS.append(entry + "_v1_02")

_DL_URLS = {
    name: f"https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_{name}.tsv.gz"
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
          version="0.1.0",
          data=config_name,
      )
      for config_name in _DATA_OPTIONS
  ]

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict(
            {
                "data": collections.OrderedDict([
                    ("marketplace", np.str_),
                    ("customer_id", np.str_),
                    ("review_id", np.str_),
                    ("product_id", np.str_),
                    ("product_parent", np.str_),
                    ("product_title", np.str_),
                    ("product_category", np.str_),
                    ("star_rating", np.int32),
                    ("helpful_votes", np.int32),
                    ("total_votes", np.int32),
                    ("vine", tfds.features.ClassLabel(names=["Y", "N"])),
                    (
                        "verified_purchase",
                        tfds.features.ClassLabel(names=["Y", "N"]),
                    ),
                    ("review_headline", np.str_),
                    ("review_body", np.str_),
                    ("review_date", np.str_),
                ])
            }
        ),
        supervised_keys=None,
        homepage="https://s3.amazonaws.com/amazon-reviews-pds/readme.html",
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
      file_path: path where the tsv file is stored

    Yields:
      The features.
    """

    with epath.Path(file_path).open() as tsvfile:
      # Need to disable quoting - as dataset contains invalid double quotes.
      reader = csv.DictReader(
          tsvfile, dialect="excel-tab", quoting=csv.QUOTE_NONE
      )
      for i, row in enumerate(reader):
        yield i, {
            "data": row,
        }

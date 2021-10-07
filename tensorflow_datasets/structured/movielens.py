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

"""MovieLens dataset."""

import os
import textwrap
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple

from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured import movielens_parsing

_CITATION = """
@article{10.1145/2827872,
author = {Harper, F. Maxwell and Konstan, Joseph A.},
title = {The MovieLens Datasets: History and Context},
year = {2015},
issue_date = {January 2016},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {5},
number = {4},
issn = {2160-6455},
url = {https://doi.org/10.1145/2827872},
doi = {10.1145/2827872},
journal = {ACM Trans. Interact. Intell. Syst.},
month = dec,
articleno = {19},
numpages = {19},
keywords = {Datasets, recommendations, ratings, MovieLens}
}
"""

_DESCRIPTION = """
This dataset contains a set of movie ratings from the MovieLens website, a movie
recommendation service. This dataset was collected and maintained by [GroupLens]
(https://grouplens.org/), a research group at the University of Minnesota. There
are 5 versions included: "25m", "latest-small", "100k", "1m", "20m". In all
datasets, the movies data and ratings data are joined on "movieId". The 25m
dataset, latest-small dataset, and 20m dataset contain only movie data and
rating data. The 1m dataset and 100k dataset contain demographic data in
addition to movie and rating data.

- "25m": This is the latest stable version of the MovieLens dataset. It is
recommended for research purposes.
- "latest-small": This is a small subset of the latest version of the MovieLens
dataset. It is changed and updated over time by GroupLens.
- "100k": This is the oldest version of the MovieLens datasets. It is a small
dataset with demographic data.
- "1m": This is the largest MovieLens dataset that contains demographic data.
- "20m": This is one of the most used MovieLens datasets in academic papers
along with the 1m dataset.

For each version, users can view either only the movies data by adding the
"-movies" suffix (e.g. "25m-movies") or the ratings data joined with the movies
data (and users data in the 1m and 100k datasets) by adding the "-ratings"
suffix (e.g. "25m-ratings").

The features below are included in all versions with the "-ratings" suffix.

- "movie_id": a unique identifier of the rated movie
- "movie_title": the title of the rated movie with the release year in
parentheses
- "movie_genres": a sequence of genres to which the rated movie belongs
- "user_id": a unique identifier of the user who made the rating
- "user_rating": the score of the rating on a five-star scale
- "timestamp": the timestamp of the ratings, represented in seconds since
midnight Coordinated Universal Time (UTC) of January 1, 1970

The "100k-ratings" and "1m-ratings" versions in addition include the following
demographic features.

- "user_gender": gender of the user who made the rating; a true value
corresponds to male
- "bucketized_user_age": bucketized age values of the user who made the rating,
the values and the corresponding ranges are:
  - 1: "Under 18"
  - 18: "18-24"
  - 25: "25-34"
  - 35: "35-44"
  - 45: "45-49"
  - 50: "50-55"
  - 56: "56+"
- "user_occupation_label": the occupation of the user who made the rating
represented by an integer-encoded label; labels are preprocessed to be
consistent across different versions
- "user_occupation_text": the occupation of the user who made the rating in
the original string; different versions can have different set of raw text
labels
- "user_zip_code": the zip code of the user who made the rating

In addition, the "100k-ratings" dataset would also have a feature "raw_user_age"
which is the exact ages of the users who made the rating

Datasets with the "-movies" suffix contain only "movie_id", "movie_title", and
"movie_genres" features.
"""

_FORMAT_VERSIONS = ['25m', 'latest-small', '20m', '100k', '1m']
_TABLE_OPTIONS = ['movies', 'ratings']


class MovieLensConfig(tfds.core.BuilderConfig):
  """BuilderConfig for MovieLens dataset."""

  def __init__(self,
               format_version: Optional[str] = None,
               table_option: Optional[str] = None,
               download_url: Optional[str] = None,
               parsing_fn: Optional[Callable[[str], Iterator[Tuple[int, Dict[
                   str, Any]]],]] = None,
               **kwargs) -> None:
    """Constructs a MovieLensConfig.

    Args:
      format_version: a string to identify the format of the dataset, one of
        '_FORMAT_VERSIONS'.
      table_option: a string to identify the table to expose, one of
        '_TABLE_OPTIONS'.
      download_url: a string url for downloading the dataset.
      parsing_fn: a callable for parsing the data.
      **kwargs: keyword arguments forwarded to super.

    Raises:
      ValueError: if format_version is not one of '_FORMAT_VERSIONS' or if
          table_option is not one of '_TABLE_OPTIONS'.
    """
    if format_version not in _FORMAT_VERSIONS:
      raise ValueError('format_version must be one of %s.' % _FORMAT_VERSIONS)
    if table_option not in _TABLE_OPTIONS:
      raise ValueError('table_option must be one of %s.' % _TABLE_OPTIONS)
    super(MovieLensConfig, self).__init__(**kwargs)
    self._format_version = format_version
    self._table_option = table_option
    self._download_url = download_url
    self._parsing_fn = parsing_fn

  @property
  def format_version(self) -> str:
    return self._format_version

  @property
  def table_option(self) -> str:
    return self._table_option

  @property
  def download_url(self) -> str:
    return self._download_url

  @property
  def parsing_fn(
      self) -> Optional[Callable[[str], Iterator[Tuple[int, Dict[str, Any]]],]]:
    return self._parsing_fn


class Movielens(tfds.core.GeneratorBasedBuilder):
  """MovieLens rating dataset."""

  BUILDER_CONFIGS = [
      MovieLensConfig(
          name='25m-ratings',
          description=textwrap.dedent("""\
              This dataset contains 25,000,095 ratings across 62,423 movies,
              created by 162,541 users between January 09, 1995 and November 21,
              2019. This dataset is the latest stable version of the MovieLens
              dataset, generated on November 21, 2019.

              Each user has rated at least 20 movies. The ratings are in
              half-star increments. This dataset does not include demographic
              data."""),
          version='0.1.0',
          format_version='25m',
          table_option='ratings',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-25m.zip'),
          parsing_fn=movielens_parsing.parse_current_ratings_data,
      ),
      MovieLensConfig(
          name='25m-movies',
          description=textwrap.dedent("""\
              This dataset contains data of 62,423 movies rated in the 25m
              dataset."""),
          version='0.1.0',
          format_version='25m',
          table_option='movies',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-25m.zip'),
          parsing_fn=movielens_parsing.parse_current_movies_data,
      ),
      # The latest-small dataset is changed over time. Its checksum might need
      # updating in the future.
      MovieLensConfig(
          name='latest-small-ratings',
          description=textwrap.dedent("""\
              This dataset contains 100,836 ratings across 9,742 movies, created
              by 610 users between March 29, 1996 and September 24, 2018. This
              dataset is generated on September 26, 2018 and is the a subset of
              the full latest version of the MovieLens dataset. This dataset
              is changed and updated over time.

              Each user has rated at least 20 movies. The ratings are in
              half-star increments. This dataset does not include demographic
              data."""),
          version='0.1.0',
          format_version='latest-small',
          table_option='ratings',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-latest-small.zip'),
          parsing_fn=movielens_parsing.parse_current_ratings_data,
      ),
      MovieLensConfig(
          name='latest-small-movies',
          description=textwrap.dedent("""\
              This dataset contains data of 9,742 movies rated in the
              latest-small dataset."""),
          version='0.1.0',
          format_version='latest-small',
          table_option='movies',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-latest-small.zip'),
          parsing_fn=movielens_parsing.parse_current_movies_data,
      ),
      MovieLensConfig(
          name='100k-ratings',
          description=textwrap.dedent("""\
              This dataset contains 100,000 ratings from 943 users on 1,682
              movies. This dataset is the oldest version of the MovieLens
              dataset.

              Each user has rated at least 20 movies. Ratings are in whole-star
              increments. This dataset contains demographic data of users in
              addition to data on movies and ratings."""),
          version='0.1.0',
          format_version='100k',
          table_option='ratings',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-100k.zip'),
          parsing_fn=movielens_parsing.parse_100k_ratings_data,
      ),
      MovieLensConfig(
          name='100k-movies',
          description=textwrap.dedent("""\
              This dataset contains data of 1,682 movies rated in the 100k
              dataset."""),
          version='0.1.0',
          format_version='100k',
          table_option='movies',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-100k.zip'),
          parsing_fn=movielens_parsing.parse_100k_movies_data,
      ),
      MovieLensConfig(
          name='1m-ratings',
          description=textwrap.dedent("""\
              This dataset contains 1,000,209 anonymous ratings of approximately
              3,900 movies made by 6,040 MovieLens users who joined MovieLens in
              2000. This dataset is the largest dataset that includes
              demographic data.

              Each user has rated at least 20 movies. Ratings are in whole-star
              increments. In demographic data, age values are divided into
              ranges and the lowest age value for each range is used in the data
              instead of the actual values."""),
          version='0.1.0',
          format_version='1m',
          table_option='ratings',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-1m.zip'),
          parsing_fn=movielens_parsing.parse_1m_ratings_data,
      ),
      MovieLensConfig(
          name='1m-movies',
          description=textwrap.dedent("""\
              This dataset contains data of approximately 3,900 movies rated in
              the 1m dataset."""),
          version='0.1.0',
          format_version='1m',
          table_option='movies',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-1m.zip'),
          parsing_fn=movielens_parsing.parse_1m_movies_data,
      ),
      MovieLensConfig(
          name='20m-ratings',
          description=textwrap.dedent("""\
              This dataset contains 20,000,263 ratings across 27,278
              movies, created by 138,493 users between January 09, 1995 and
              March 31, 2015. This dataset was generated on October 17, 2016.

              Each user has rated at least 20 movies. Ratings are in half-star
              increments. This dataset does not contain demographic data."""),
          version='0.1.0',
          format_version='20m',
          table_option='ratings',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-20m.zip'),
          parsing_fn=movielens_parsing.parse_current_ratings_data,
      ),
      MovieLensConfig(
          name='20m-movies',
          description=textwrap.dedent("""\
              This dataset contains data of 27,278 movies rated in the 20m
              dataset"""),
          version='0.1.0',
          format_version='20m',
          table_option='movies',
          download_url=('http://files.grouplens.org/datasets/movielens/'
                        'ml-20m.zip'),
          parsing_fn=movielens_parsing.parse_current_movies_data,
      ),
  ]

  VERSION = tfds.core.Version('0.1.0')

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns DatasetInfo according to self.builder_config."""
    movie_features_dict = {
        'movie_id':
            tf.string,
        'movie_title':
            tf.string,
        'movie_genres':
            tfds.features.Sequence(
                tfds.features.ClassLabel(names=[
                    'Action',
                    'Adventure',
                    'Animation',
                    'Children',
                    'Comedy',
                    'Crime',
                    'Documentary',
                    'Drama',
                    'Fantasy',
                    'Film-Noir',
                    'Horror',
                    'IMAX',
                    'Musical',
                    'Mystery',
                    'Romance',
                    'Sci-Fi',
                    'Thriller',
                    'Unknown',
                    'War',
                    'Western',
                    '(no genres listed)',
                ]),),
    }
    rating_features_dict = {
        'user_id': tf.string,
        'user_rating': tf.float32,
        # Using int64 since tfds currently does not support float64.
        'timestamp': tf.int64,
    }
    demographic_features_dict = {
        'user_gender':
            tf.bool,
        'bucketized_user_age':
            tf.float32,
        'user_occupation_label':
            tfds.features.ClassLabel(names=[
                'academic/educator',
                'artist',
                'clerical/admin',
                'customer service',
                'doctor/health care',
                'entertainment',
                'executive/managerial',
                'farmer',
                'homemaker',
                'lawyer',
                'librarian',
                'other/not specified',
                'programmer',
                'retired',
                'sales/marketing',
                'scientist',
                'self-employed',
                'student',
                'technician/engineer',
                'tradesman/craftsman',
                'unemployed',
                'writer',
            ]),
        'user_occupation_text':
            tf.string,
        'user_zip_code':
            tf.string,
    }

    features_dict = {}
    if self.builder_config.table_option == 'movies':
      features_dict.update(movie_features_dict)
    # For the other cases, self.builder_config.table_option == 'ratings'.
    # Older versions of MovieLens (1m, 100k) have demographic features.
    elif self.builder_config.format_version == '1m':
      features_dict.update(movie_features_dict)
      features_dict.update(rating_features_dict)
      features_dict.update(demographic_features_dict)
    elif self.builder_config.format_version == '100k':
      # Only the 100k dataset contains exact user ages. The 1m dataset
      # contains only bucketized age values.
      features_dict.update(movie_features_dict)
      features_dict.update(rating_features_dict)
      features_dict.update(demographic_features_dict)
      features_dict.update(raw_user_age=tf.float32)
    else:
      features_dict.update(movie_features_dict)
      features_dict.update(rating_features_dict)
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,
        homepage='https://grouplens.org/datasets/movielens/',
        citation=_CITATION,
    )

  def _split_generators(
      self, dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract(
        self.builder_config.download_url,)
    dir_path = os.path.join(
        extracted_path,
        'ml-%s' % self.builder_config.format_version,
    )
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'dir_path': dir_path},
        ),
    ]

  def _generate_examples(
      self,
      dir_path: Optional[str] = None) -> Iterator[Tuple[int, Dict[str, Any]]]:
    """Yields examples by calling the corresponding parsing function."""
    for ex in self.builder_config.parsing_fn(dir_path):
      yield ex


class MovieLens(Movielens):
  """MovieLens rating dataset (deprecated handle version)."""

  def __init__(self, **kwargs):
    logging.warning(
        'The handle "movie_lens" for the MovieLens dataset is deprecated. '
        'Prefer using "movielens" instead.')
    super(MovieLens, self).__init__(**kwargs)

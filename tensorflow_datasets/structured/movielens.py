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
"""movielens dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import textwrap
import codecs
from typing import Any, Dict, Iterator, List, Optional, Tuple

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

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
This dataset describes 5-star rating from MovieLens,
a movie recommendation service.
Users were selected at random for inclusion.
"""

_DATASET_OPTIONS = ['20m', 'latest-small', '1m']


class MovieLensConfig(tfds.core.BuilderConfig):
  """BuilderConfig for MovieLens dataset."""

  def __init__(self, data_option: Optional[str] = None, **kwargs) -> None:
    """Constructs a MovieLensConfig.

    Args:
      data_option: a string, one of '_DATASET_OPTIONS'.
      **kwargs: keyword arguments forwarded to super.

    Raises:
      ValueError: if data_option is not one of '_DATASET_OPTIONS'.
    """
    if data_option not in _DATASET_OPTIONS:
      raise ValueError('data_option must be one of %s.' % _DATASET_OPTIONS)
    super(MovieLensConfig, self).__init__(**kwargs)
    self._data_option = data_option

  @property
  def data_option(self) -> str:
    return self._data_option


class MovieLens(tfds.core.GeneratorBasedBuilder):
  """MovieLens rating dataset"""

  BUILDER_CONFIGS = [
      MovieLensConfig(
          name='20m',
          description=textwrap.dedent("""\
              This dataset contains contains 20000263 ratings
              across 27278 movies.
              These data were created by 138493 users between
              January 09, 1995 and March 31, 2015.
              This dataset was generated on October 17, 2016."""),
          version='0.1.0',
          data_option='20m',
      ),
      MovieLensConfig(
          name='latest-small',
          description=textwrap.dedent("""\
              This dataset contains 100836 ratings across 9742 movies
              These data were created by 610 users between March 29, 1996
              and September 24, 2018.
              This dataset was generated on September 26, 2018."""),
          version='0.1.0',
          data_option='latest-small',
      ),
      MovieLensConfig(
          name='1m',
          description=textwrap.dedent("""\
              This dataset contains 1,000,209 anonymous ratings of
              approximately 3,900 movies made by 6,040 MovieLens users
              who joined MovieLens in 2000."""),
          version='0.1.0',
          data_option='1m',
      ),
  ]

  VERSION = tfds.core.Version('0.1.0')

  def _info(self) -> tfds.core.DatasetInfo:
    """Return a DatasetInfo according to self.builder_config."""
    features_dict = {
        'movie_id': tf.string,
        'movie_title': tf.string,
        'movie_genres': tfds.features.Sequence(
            tfds.features.ClassLabel(names=[
                'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
                'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                'Horror', 'IMAX', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                'Thriller', 'War', 'Western', '(no genres listed)',
            ])
        ),
        'user_id': tf.string,
        'user_rating': tf.float32,
        'timestamp': tf.float32,
    }
    # Older versions of MovieLens have different sets of genres
    if self.builder_config.name in ['1m']:
      features_dict['user_gender'] = tf.bool
      features_dict['user_age'] = tf.int32
      features_dict['user_occupation'] = tfds.features.ClassLabel(
          num_classes=21
      )
      features_dict['user_zip_code'] = tf.string
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,
        # Homepage of the dataset for documentation
        homepage='https://grouplens.org/datasets/movielens/',
        citation=_CITATION,
    )

  def _split_generators(
      self,
      dl_manager: tfds.download.DownloadManager
  ) -> List[tfds.core.SplitGenerator]:
    """Returns SplitGenerators."""
    url = (
        'http://files.grouplens.org/datasets/movielens/'
        'ml-%s.zip' % self.builder_config.name
    )
    extracted_path = dl_manager.download_and_extract(url)
    dir_path = os.path.join(extracted_path, 'ml-%s' % self.builder_config.name)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'dir_path': dir_path},
        ),
    ]

  def _generate_examples(
      self,
      dir_path: Optional[str] = None
  ) -> Iterator[Tuple[int, Dict[str, Any]]]:
    """Yields examples by calling the corresponding parsing function."""
    if self.builder_config.name in ['20m', 'latest-small']:
      yield from _parse_current_format(dir_path)
    elif self.builder_config.name == '1m':
      yield from _parse_1m_format(dir_path)

def _parse_current_format(
    dir_path: str
) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parse the data in current format (20m and latest)"""
  movies_file_path = os.path.join(dir_path, 'movies.csv')
  ratings_file_path = os.path.join(dir_path, 'ratings.csv')
  movie_genre_map = {}
  movie_title_map = {}
  with tf.io.gfile.GFile(movies_file_path) as movies_file:
    movies_reader = csv.DictReader(movies_file)
    for row in movies_reader:
      movie_title_map[row['movieId']] = row['title']
      movie_genre_map[row['movieId']] = row['genres']

  with tf.io.gfile.GFile(ratings_file_path) as ratings_file:
    ratings_reader = csv.DictReader(ratings_file)
    for i, row in enumerate(ratings_reader):
      yield i, {
          'movie_id': row['movieId'],
          'movie_title': movie_title_map[row['movieId']],
          'movie_genres': movie_genre_map[row['movieId']].split('|'),
          'user_id': row['userId'],
          'user_rating': row['rating'],
          'timestamp': row['timestamp'],
      }

def _parse_1m_format(
    dir_path: str
) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parse the 1m data"""
  movies_file_path = os.path.join(dir_path, 'movies.dat')
  users_file_path = os.path.join(dir_path, 'users.dat')
  ratings_file_path = os.path.join(dir_path, 'ratings.dat')

  movie_genre_map = {}
  movie_title_map = {}
  with tf.io.gfile.GFile(movies_file_path, mode='rb') as movies_file:
    movies_lines = movies_file.readlines()
  for line in movies_lines:
    line = codecs.decode(line, encoding='ISO-8859-1')
    # Row format: movie id::movie title:: movie genres
    row_args = line.strip().split('::')
    movie_title_map[row_args[0]] = row_args[1]
    genre_list = row_args[2].split('|')
    # 1m dataset labels Children genre as Children's
    for idx, genre in enumerate(genre_list):
      if genre == 'Children\'s':
        genre_list[idx] = 'Children'
    movie_genre_map[row_args[0]] = genre_list

  user_info_map = {}
  with tf.io.gfile.GFile(users_file_path, mode='rb') as users_file:
    users_lines = users_file.readlines()
  for line in users_lines:
    line = codecs.decode(line, encoding='ISO-8859-1')
    row_args = line.strip().split('::')
    user_info_map[row_args[0]] = {
        'gender': row_args[1] == 'M',
        'age': row_args[2],
        'occupation': row_args[3],
        'zip_code': row_args[4],
    }

  with tf.io.gfile.GFile(ratings_file_path, mode='rb') as ratings_file:
    ratings_lines = ratings_file.readlines()
  for i, line in enumerate(ratings_lines):
    line = codecs.decode(line, encoding='ISO-8859-1')
    row_args = line.strip().split('::')
    user_id = row_args[0]
    movie_id = row_args[1]
    user_info = user_info_map[user_id]
    yield i, {
        'movie_id': movie_id,
        'movie_title': movie_title_map[movie_id],
        'movie_genres': movie_genre_map[movie_id],
        'user_id': user_id,
        'user_rating': row_args[2],
        'timestamp': row_args[3],
        'user_gender': user_info['gender'],
        'user_age': user_info['age'],
        'user_occupation': user_info['occupation'],
        'user_zip_code': user_info['zip_code'],
    }

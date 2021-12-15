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

"""Utilities for parsing the MovieLens dataset."""

import codecs
import csv
import os
from typing import Any, Dict, Iterator, Tuple

import tensorflow as tf


def parse_current_movies_data(
    dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the movies data in current format (20m, 25m, and latest-small)."""
  movies_file_path = os.path.join(dir_path, 'movies.csv')
  with tf.io.gfile.GFile(movies_file_path) as movies_file:
    movies_reader = csv.DictReader(movies_file)
    for row_num, row in enumerate(movies_reader):
      yield row_num, {
          'movie_id': row['movieId'],
          'movie_title': row['title'],
          'movie_genres': row['genres'].split('|'),
      }


def parse_current_ratings_data(
    dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the ratings data in current format (20m, 25m, and latest-small)."""
  movie_info_map = {}
  for _, movie_example in parse_current_movies_data(dir_path):
    movie_info_map[movie_example['movie_id']] = movie_example

  ratings_file_path = os.path.join(dir_path, 'ratings.csv')
  with tf.io.gfile.GFile(ratings_file_path) as ratings_file:
    ratings_reader = csv.DictReader(ratings_file)
    for row_num, row in enumerate(ratings_reader):
      ex = {
          'user_id': row['userId'],
          'user_rating': row['rating'],
          'timestamp': row['timestamp'],
      }
      ex.update(movie_info_map[row['movieId']])
      yield row_num, ex


def parse_1m_movies_data(dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the 1m movies data."""
  movies_file_path = os.path.join(dir_path, 'movies.dat')
  with tf.io.gfile.GFile(movies_file_path, mode='rb') as movies_file:
    for row_num, line in enumerate(movies_file):
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      # Row format: <movie id>::<movie title>::<movie genres>.
      movie_id, movie_title, movie_genres_str = line.split('::')
      genre_list = movie_genres_str.split('|')
      # 1m dataset labels "Children" genre as "Children's".
      # However "Children" and "Children's" should represent the same genre.
      for idx, genre in enumerate(genre_list):
        if genre == 'Children\'s':
          genre_list[idx] = 'Children'
      yield row_num, {
          'movie_id': movie_id,
          'movie_title': movie_title,
          'movie_genres': genre_list,
      }


def parse_1m_ratings_data(
    dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the 1m ratings data."""
  movie_info_map = {}
  for _, movie_example in parse_1m_movies_data(dir_path):
    movie_info_map[movie_example['movie_id']] = movie_example

  users_file_path = os.path.join(dir_path, 'users.dat')
  # A list for converting occupation index to occupation string for 1M
  # dataset.
  occupation_index_to_label = [
      'other/not specified',
      'academic/educator',
      'artist',
      'clerical/admin',
      'college/grad student',
      'customer service',
      'doctor/health care',
      'executive/managerial',
      'farmer',
      'homemaker',
      'K-12 student',
      'lawyer',
      'programmer',
      'retired',
      'sales/marketing',
      'scientist',
      'self-employed',
      'technician/engineer',
      'tradesman/craftsman',
      'unemployed',
      'writer',
  ]
  user_info_map = {}
  with tf.io.gfile.GFile(users_file_path, mode='rb') as users_file:
    for line in users_file:
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      user_id, gender_str, age, occupation_index, zip_code = line.split('::')
      occupation_str = occupation_index_to_label[int(occupation_index)]
      # Combine "K-12 student" and "college/grad student" labels.
      if occupation_str in ['K-12 student', 'college/grad student']:
        occupation_label = 'student'
      else:
        occupation_label = occupation_str
      user_info_map[user_id] = {
          'user_gender': gender_str == 'M',
          'bucketized_user_age': age,
          'user_occupation_label': occupation_label,
          'user_occupation_text': occupation_str,
          'user_zip_code': zip_code,
      }

  ratings_file_path = os.path.join(dir_path, 'ratings.dat')
  with tf.io.gfile.GFile(ratings_file_path, mode='rb') as ratings_file:
    for row_num, line in enumerate(ratings_file):
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      user_id, movie_id, rating, timestamp = line.split('::')
      movie_info = movie_info_map[movie_id]
      user_info = user_info_map[user_id]
      ex = {
          'user_id': user_id,
          'user_rating': rating,
          'timestamp': timestamp,
      }
      ex.update(movie_info)
      ex.update(user_info)
      yield row_num, ex


def parse_100k_movies_data(
    dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the 100k movies data."""
  movies_file_path = os.path.join(dir_path, 'u.item')
  # A list for converting genre index to genre label for 100K dataset.
  # "Children's" changed to "Children" in the list for consistency.
  all_genre_list = [
      'Unknown',
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
      'Musical',
      'Mystery',
      'Romance',
      'Sci-Fi',
      'Thriller',
      'War',
      'Western',
  ]
  with tf.io.gfile.GFile(movies_file_path, mode='rb') as movies_file:
    for row_num, line in enumerate(movies_file):
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      # Row format: <movie id>|<movie title>|<release date>|\
      # <video release date>|<IMDb URL>|<19 fields for each genre>|.
      # movie_id, movie_title, _, _, _, *genre_bools = line.split('|')
      categories = line.split('|')
      movie_id = categories[0]
      movie_title = categories[1]
      genre_bools = categories[5:]
      genre_list = []
      for index, genre_indicator in enumerate(genre_bools):
        if genre_indicator == '1':
          genre_list.append(all_genre_list[index])
      yield row_num, {
          'movie_id': movie_id,
          'movie_title': movie_title,
          'movie_genres': genre_list,
      }


def parse_100k_ratings_data(
    dir_path: str) -> Iterator[Tuple[int, Dict[str, Any]]]:
  """Parses the 100k ratings data."""
  movie_info_map = {}
  for _, movie_example in parse_100k_movies_data(dir_path):
    movie_info_map[movie_example['movie_id']] = movie_example

  users_file_path = os.path.join(dir_path, 'u.user')
  # A list of thresholds for bucketizing user age.
  age_thresholds_list = [18, 25, 35, 45, 50, 56]
  # A dictionary for converting 100K occupation labels to standardized labels.
  # These labels are consistent across the 100k and 1m datasets. Some labels are
  # merged according to the labels in the 1m dataset.
  occupation_label_conversion_map = {
      'administrator': 'clerical/admin',
      'artist': 'artist',
      'doctor': 'doctor/health care',
      'educator': 'academic/educator',
      'engineer': 'technician/engineer',
      'entertainment': 'entertainment',
      'executive': 'executive/managerial',
      'healthcare': 'doctor/health care',
      'homemaker': 'homemaker',
      'lawyer': 'lawyer',
      'librarian': 'librarian',
      'marketing': 'sales/marketing',
      'none': 'other/not specified',
      'other': 'other/not specified',
      'programmer': 'programmer',
      'retired': 'retired',
      'salesman': 'sales/marketing',
      'scientist': 'scientist',
      'student': 'student',
      'technician': 'technician/engineer',
      'writer': 'writer',
  }
  user_info_map = {}
  with tf.io.gfile.GFile(users_file_path, mode='rb') as users_file:
    for line in users_file:
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      user_id, age_str, gender_str, occupation_str, zip_code = line.split('|')
      raw_age = int(age_str)
      bucketized_age = 1
      for age_threshold in age_thresholds_list:
        if raw_age >= age_threshold:
          bucketized_age = age_threshold
        else:
          break
      user_info_map[user_id] = {
          'user_gender':
              gender_str == 'M',
          'bucketized_user_age':
              bucketized_age,
          'raw_user_age':
              raw_age,
          'user_occupation_label':
              occupation_label_conversion_map[occupation_str],
          'user_occupation_text':
              occupation_str,
          'user_zip_code':
              zip_code,
      }

  ratings_file_path = os.path.join(dir_path, 'u.data')
  with tf.io.gfile.GFile(ratings_file_path, mode='rb') as ratings_file:
    for row_num, line in enumerate(ratings_file):
      line = codecs.decode(line, encoding='ISO-8859-1').strip()
      user_id, movie_id, rating, timestamp = line.split('\t')
      movie_info = movie_info_map[movie_id]
      user_info = user_info_map[user_id]
      ex = {
          'user_id': user_id,
          'user_rating': rating,
          'timestamp': timestamp,
      }
      ex.update(movie_info)
      ex.update(user_info)
      yield row_num, ex

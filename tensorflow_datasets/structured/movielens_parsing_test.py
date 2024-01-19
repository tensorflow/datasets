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

"""Tests for movielens_parsing."""

import os

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured import movielens_parsing


class MovieLensUtilsTest(tfds.testing.TestCase):
  """Tests for helper functions in movielens_parsing."""

  def test_parse_current_movies_data(self):
    """Test for parse_current_movies_data."""
    latest_small_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-latest-small',
    )
    movies_generator = movielens_parsing.parse_current_movies_data(
        latest_small_path
    )
    expected_result = [
        (
            0,
            {
                'movie_id': '1',
                'movie_genres': ['Fantasy', 'War'],
                'movie_title': 'Horse Movie (2011)',
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Adventure', 'Documentary'],
                'movie_title': 'Eagle Movie (1999)',
            },
        ),
        (
            2,
            {
                'movie_id': '3',
                'movie_genres': ['(no genres listed)'],
                'movie_title': 'Test Movie (2014)',
            },
        ),
        (
            3,
            {
                'movie_id': '4',
                'movie_genres': ['Fantasy', 'Horror', 'Musical'],
                'movie_title': 'Fake Movie (2007)',
            },
        ),
        (
            4,
            {
                'movie_id': '5',
                'movie_genres': ['Mystery'],
                'movie_title': 'Squirrel Movie (2017)',
            },
        ),
        (
            5,
            {
                'movie_id': '6',
                'movie_genres': ['Drama', 'War'],
                'movie_title': 'Test Movie (2003)',
            },
        ),
        (
            6,
            {
                'movie_id': '7',
                'movie_genres': ['Horror'],
                'movie_title': 'Rabbit Movie (1999)',
            },
        ),
        (
            7,
            {
                'movie_id': '8',
                'movie_genres': ['Mystery', 'War'],
                'movie_title': 'Tree Movie (2001)',
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)

  def test_parse_current_ratings_data(self):
    """Test for parse_current_ratings_data."""
    fake_dir_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-latest-small',
    )
    movies_generator = movielens_parsing.parse_current_ratings_data(
        fake_dir_path
    )
    expected_result = [
        (
            0,
            {
                'movie_id': '5',
                'movie_genres': ['Mystery'],
                'movie_title': 'Squirrel Movie (2017)',
                'user_id': '1',
                'user_rating': '2.5',
                'timestamp': '1329800589',
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Adventure', 'Documentary'],
                'movie_title': 'Eagle Movie (1999)',
                'user_id': '2',
                'user_rating': '1.5',
                'timestamp': '1128006292',
            },
        ),
        (
            2,
            {
                'movie_id': '3',
                'movie_genres': ['(no genres listed)'],
                'movie_title': 'Test Movie (2014)',
                'user_id': '2',
                'user_rating': '3.0',
                'timestamp': '1029868117',
            },
        ),
        (
            3,
            {
                'movie_id': '4',
                'movie_genres': ['Fantasy', 'Horror', 'Musical'],
                'movie_title': 'Fake Movie (2007)',
                'user_id': '2',
                'user_rating': '0.5',
                'timestamp': '1589647790',
            },
        ),
        (
            4,
            {
                'movie_id': '5',
                'movie_genres': ['Mystery'],
                'movie_title': 'Squirrel Movie (2017)',
                'user_id': '2',
                'user_rating': '5.0',
                'timestamp': '1553439546',
            },
        ),
        (
            5,
            {
                'movie_id': '1',
                'movie_genres': ['Fantasy', 'War'],
                'movie_title': 'Horse Movie (2011)',
                'user_id': '3',
                'user_rating': '1.5',
                'timestamp': '1580974707',
            },
        ),
        (
            6,
            {
                'movie_id': '2',
                'movie_genres': ['Adventure', 'Documentary'],
                'movie_title': 'Eagle Movie (1999)',
                'user_id': '3',
                'user_rating': '2.0',
                'timestamp': '820693640',
            },
        ),
        (
            7,
            {
                'movie_id': '4',
                'movie_genres': ['Fantasy', 'Horror', 'Musical'],
                'movie_title': 'Fake Movie (2007)',
                'user_id': '4',
                'user_rating': '1.0',
                'timestamp': '1496507328',
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)

  def test_parse_100k_movies_data(self):
    """Test for parse_100k_movies_data."""
    fake_dir_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-100k',
    )
    movies_generator = movielens_parsing.parse_100k_movies_data(fake_dir_path)
    expected_result = [
        (
            0,
            {
                'movie_id': '1',
                'movie_genres': ['Unknown', 'Children'],
                'movie_title': 'Fake Movie (1996)',
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Western'],
                'movie_title': 'Dog Movie (1994)',
            },
        ),
        (
            2,
            {
                'movie_id': '3',
                'movie_genres': ['Adventure'],
                'movie_title': 'Non-existent Movie (1995)',
            },
        ),
        (
            3,
            {
                'movie_id': '4',
                'movie_genres': ['Documentary', 'Film-Noir', 'Musical'],
                'movie_title': 'Owl Movie (1997)',
            },
        ),
        (
            4,
            {
                'movie_id': '5',
                'movie_genres': ['Crime', 'Musical'],
                'movie_title': 'Cat Movie (1998)',
            },
        ),
        (
            5,
            {
                'movie_id': '6',
                'movie_genres': ['Mystery', 'Romance'],
                'movie_title': 'Test Movie (2003)',
            },
        ),
        (
            6,
            {
                'movie_id': '7',
                'movie_genres': ['Action', 'Comedy', 'Fantasy', 'Romance'],
                'movie_title': 'Rabbit Movie (1999)',
            },
        ),
        (
            7,
            {
                'movie_id': '8',
                'movie_genres': ['Documentary'],
                'movie_title': 'Tree Movie (2001)',
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)

  def test_parse_100k_ratings_data(self):
    """Test for parse_100k_ratings_data."""
    fake_dir_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-100k',
    )
    movies_generator = movielens_parsing.parse_100k_ratings_data(fake_dir_path)
    expected_result = [
        (
            0,
            {
                'movie_id': '1',
                'movie_title': 'Fake Movie (1996)',
                'movie_genres': ['Unknown', 'Children'],
                'user_id': '1',
                'user_rating': '1',
                'timestamp': '867969113',
                'user_gender': False,
                'bucketized_user_age': 50,
                'user_occupation_text': 'technician',
                'user_occupation_label': 'technician/engineer',
                'user_zip_code': '10278',
                'raw_user_age': 54,
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Western'],
                'movie_title': 'Dog Movie (1994)',
                'user_id': '1',
                'user_rating': '1',
                'timestamp': '1058848127',
                'user_gender': False,
                'bucketized_user_age': 50,
                'user_occupation_text': 'technician',
                'user_occupation_label': 'technician/engineer',
                'user_zip_code': '10278',
                'raw_user_age': 54,
            },
        ),
        (
            2,
            {
                'movie_id': '4',
                'movie_genres': ['Documentary', 'Film-Noir', 'Musical'],
                'movie_title': 'Owl Movie (1997)',
                'user_id': '1',
                'user_rating': '3',
                'timestamp': '997136856',
                'user_gender': False,
                'bucketized_user_age': 50,
                'user_occupation_text': 'technician',
                'user_occupation_label': 'technician/engineer',
                'user_zip_code': '10278',
                'raw_user_age': 54,
            },
        ),
        (
            3,
            {
                'movie_id': '2',
                'movie_genres': ['Western'],
                'movie_title': 'Dog Movie (1994)',
                'user_id': '2',
                'user_rating': '4',
                'timestamp': '1188937963',
                'user_gender': True,
                'bucketized_user_age': 1,
                'user_occupation_text': 'other',
                'user_occupation_label': 'other/not specified',
                'user_zip_code': '34729',
                'raw_user_age': 16,
            },
        ),
        (
            4,
            {
                'movie_id': '1',
                'movie_genres': ['Unknown', 'Children'],
                'movie_title': 'Fake Movie (1996)',
                'user_id': '3',
                'user_rating': '5',
                'timestamp': '1083844839',
                'user_gender': True,
                'bucketized_user_age': 25,
                'user_occupation_text': 'librarian',
                'user_occupation_label': 'librarian',
                'user_zip_code': '20112',
                'raw_user_age': 29,
            },
        ),
        (
            5,
            {
                'movie_id': '5',
                'movie_genres': ['Crime', 'Musical'],
                'movie_title': 'Cat Movie (1998)',
                'user_id': '3',
                'user_rating': '3',
                'timestamp': '1042582463',
                'user_gender': True,
                'bucketized_user_age': 25,
                'user_occupation_text': 'librarian',
                'user_occupation_label': 'librarian',
                'user_zip_code': '20112',
                'raw_user_age': 29,
            },
        ),
        (
            6,
            {
                'movie_id': '3',
                'movie_genres': ['Adventure'],
                'movie_title': 'Non-existent Movie (1995)',
                'user_id': '4',
                'user_rating': '2',
                'timestamp': '803797344',
                'user_gender': False,
                'bucketized_user_age': 45,
                'user_occupation_text': 'none',
                'user_occupation_label': 'other/not specified',
                'user_zip_code': '09583',
                'raw_user_age': 47,
            },
        ),
        (
            7,
            {
                'movie_id': '4',
                'movie_genres': ['Documentary', 'Film-Noir', 'Musical'],
                'movie_title': 'Owl Movie (1997)',
                'user_id': '4',
                'user_rating': '1',
                'timestamp': '1235956810',
                'user_gender': False,
                'bucketized_user_age': 45,
                'user_occupation_text': 'none',
                'user_occupation_label': 'other/not specified',
                'user_zip_code': '09583',
                'raw_user_age': 47,
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)

  def test_parse_1m_movies_data(self):
    """Test for parse_1m_movies_data."""
    fake_dir_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-1m',
    )
    movies_generator = movielens_parsing.parse_1m_movies_data(fake_dir_path)
    expected_result = [
        (
            0,
            {
                'movie_id': '1',
                'movie_genres': ['Fantasy', 'Children'],
                'movie_title': 'Fake Movie (2005)',
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Crime', 'Sci-Fi', 'Western'],
                'movie_title': 'Dog Movie (1994)',
            },
        ),
        (
            2,
            {
                'movie_id': '3',
                'movie_genres': ['Film-Noir'],
                'movie_title': 'Non-existent Movie (2003)',
            },
        ),
        (
            3,
            {
                'movie_id': '4',
                'movie_genres': ['Comedy', 'Drama', 'Romance'],
                'movie_title': 'Owl Movie (2018)',
            },
        ),
        (
            4,
            {
                'movie_id': '5',
                'movie_genres': ['Comedy', 'Romance'],
                'movie_title': 'Cat Movie (2018)',
            },
        ),
        (
            5,
            {
                'movie_id': '6',
                'movie_genres': ['Drama', 'War'],
                'movie_title': 'Test Movie (2003)',
            },
        ),
        (
            6,
            {
                'movie_id': '7',
                'movie_genres': ['Horror'],
                'movie_title': 'Rabbit Movie (1999)',
            },
        ),
        (
            7,
            {
                'movie_id': '8',
                'movie_genres': ['Mystery', 'War'],
                'movie_title': 'Tree Movie (2001)',
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)

  def test_parse_1m_ratings_data(self):
    """Test for parse_1m_ratings_data."""
    fake_dir_path = os.path.join(
        tfds.testing.fake_examples_dir(),
        'movielens',
        'ml-1m',
    )
    movies_generator = movielens_parsing.parse_1m_ratings_data(fake_dir_path)
    expected_result = [
        (
            0,
            {
                'movie_id': '1',
                'movie_genres': ['Fantasy', 'Children'],
                'movie_title': 'Fake Movie (2005)',
                'user_id': '1',
                'user_rating': '1',
                'timestamp': '867969113',
                'user_gender': False,
                'bucketized_user_age': '50',
                'user_occupation_text': 'retired',
                'user_occupation_label': 'retired',
                'user_zip_code': '10278',
            },
        ),
        (
            1,
            {
                'movie_id': '2',
                'movie_genres': ['Crime', 'Sci-Fi', 'Western'],
                'movie_title': 'Dog Movie (1994)',
                'user_id': '1',
                'user_rating': '1',
                'timestamp': '1058848127',
                'user_gender': False,
                'bucketized_user_age': '50',
                'user_occupation_text': 'retired',
                'user_occupation_label': 'retired',
                'user_zip_code': '10278',
            },
        ),
        (
            2,
            {
                'movie_id': '4',
                'movie_genres': ['Comedy', 'Drama', 'Romance'],
                'movie_title': 'Owl Movie (2018)',
                'user_id': '1',
                'user_rating': '3',
                'timestamp': '997136856',
                'user_gender': False,
                'bucketized_user_age': '50',
                'user_occupation_text': 'retired',
                'user_occupation_label': 'retired',
                'user_zip_code': '10278',
            },
        ),
        (
            3,
            {
                'movie_id': '2',
                'movie_genres': ['Crime', 'Sci-Fi', 'Western'],
                'movie_title': 'Dog Movie (1994)',
                'user_id': '2',
                'user_rating': '4',
                'timestamp': '1188937963',
                'user_gender': True,
                'bucketized_user_age': '18',
                'user_occupation_text': 'college/grad student',
                'user_occupation_label': 'student',
                'user_zip_code': '34729',
            },
        ),
        (
            4,
            {
                'movie_id': '1',
                'movie_genres': ['Fantasy', 'Children'],
                'movie_title': 'Fake Movie (2005)',
                'user_id': '3',
                'user_rating': '5',
                'timestamp': '1083844839',
                'user_gender': True,
                'bucketized_user_age': '1',
                'user_occupation_text': 'scientist',
                'user_occupation_label': 'scientist',
                'user_zip_code': '20112',
            },
        ),
        (
            5,
            {
                'movie_id': '5',
                'movie_genres': ['Comedy', 'Romance'],
                'movie_title': 'Cat Movie (2018)',
                'user_id': '3',
                'user_rating': '3',
                'timestamp': '1042582463',
                'user_gender': True,
                'bucketized_user_age': '1',
                'user_occupation_text': 'scientist',
                'user_occupation_label': 'scientist',
                'user_zip_code': '20112',
            },
        ),
        (
            6,
            {
                'movie_id': '3',
                'movie_genres': ['Film-Noir'],
                'movie_title': 'Non-existent Movie (2003)',
                'user_id': '4',
                'user_rating': '2',
                'timestamp': '803797344',
                'user_gender': False,
                'bucketized_user_age': '56',
                'user_occupation_text': 'other/not specified',
                'user_occupation_label': 'other/not specified',
                'user_zip_code': '09583',
            },
        ),
        (
            7,
            {
                'movie_id': '4',
                'movie_genres': ['Comedy', 'Drama', 'Romance'],
                'movie_title': 'Owl Movie (2018)',
                'user_id': '4',
                'user_rating': '1',
                'timestamp': '1235956810',
                'user_gender': False,
                'bucketized_user_age': '56',
                'user_occupation_text': 'other/not specified',
                'user_occupation_label': 'other/not specified',
                'user_zip_code': '09583',
            },
        ),
    ]
    parsed_example_list = list(movies_generator)
    self.assertEqual(expected_result, parsed_example_list)


if __name__ == '__main__':
  tfds.testing.test_main()

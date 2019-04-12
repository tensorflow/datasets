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

"""Data downloads using the Kaggle CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess as sp

import ipywidgets.widgets as widgets
import IPython.display as display

from absl import logging
import tensorflow as tf

from tensorflow_datasets.core import utils

_ERR_MSG = """\
To download Kaggle data through TFDS, follow the instructions to install the \
kaggle API and get API credentials:
https://github.com/Kaggle/kaggle-api#installation

Additionally, you must join the competition through the Kaggle competition's \
website:
https://www.kaggle.com/c/%s
"""

_NOT_FOUND_ERR_MSG = """\
Competition %s not found. Please ensure you have spelled the competition name \
correctly.
"""

_NOT_ACCEPT_RULES_ERR_MSG = """\
You must accept the competition rules through the Kaggle competition's website:
https://www.kaggle.com/c/%s/rules
"""


class KaggleFile(object):
  """Represents a Kaggle competition file."""
  _URL_PREFIX = "kaggle://"

  def __init__(self, competition_name, filename):
    self._competition_name = competition_name
    self._filename = filename

  @property
  def competition(self):
    return self._competition_name

  @property
  def filename(self):
    return self._filename

  @classmethod
  def from_url(cls, url):
    if not KaggleFile.is_kaggle_url(url):
      raise TypeError("Not a valid kaggle URL")
    competition_name, filename = url[len(cls._URL_PREFIX):].split("/", 1)
    return cls(competition_name, filename)

  @staticmethod
  def is_kaggle_url(url):
    return url.startswith(KaggleFile._URL_PREFIX)

  def to_url(self):
    return "%s%s/%s" % (self._URL_PREFIX, self._competition_name,
                        self._filename)


class KaggleCompetitionDownloader(object):
  """Downloader for a Kaggle competition.

  Usage:

  ```
  downloader = KaggleCompetitionDownloader(competition_name)
  for fname in downloader.competition_files:
    downloader.download_file(fname, make_file_output_path(fname))
  ```
  """

  def __init__(self, competition_name):
    self._competition_name = competition_name

  @utils.memoized_property
  def competition_files(self):
    """List of competition files."""
    command = [
        "kaggle",
        "competitions",
        "files",
        "-v",
        self._competition_name,
    ]
    output = _run_kaggle_command(command, self._competition_name)
    return sorted([
        line.split(",")[0] for line in output.split("\n")[1:] if line != ""
    ])

  @utils.memoized_property
  def competition_urls(self):
    """Returns 'kaggle://' urls."""
    return [
        KaggleFile(self._competition_name, fname).to_url()
        for fname in self.competition_files  # pylint: disable=not-an-iterable
    ]

  def download_file(self, fname, output_dir):
    """Downloads competition file to output_dir."""
    if fname not in self.competition_files:  # pylint: disable=unsupported-membership-test
      raise ValueError("%s is not one of the competition's "
                       "files: %s" % (fname, self.competition_files))
    command = [
        "kaggle",
        "competitions",
        "download",
        "--file",
        fname,
        "--path",
        output_dir,
        "-c",
        self._competition_name,
    ]
    _run_kaggle_command(command, self._competition_name)
    return os.path.join(output_dir, fname)


def _run_kaggle_command(command_args, competition_name=None):
  """Run kaggle command with subprocess."""
  try:
    output = sp.check_output(command_args)
    return tf.compat.as_text(output)
  except sp.CalledProcessError as err:
    output = err.output
    _log_command_output(output, error=True)
    if output.startswith(b"404"):
      logging.error(_NOT_FOUND_ERR_MSG, competition_name)
      raise
    if output.startswith(b'403'):
      logging.error(_NOT_ACCEPT_RULES_ERR_MSG, competition_name)
      raise
    logging.error(_ERR_MSG, competition_name)
    raise


def _log_command_output(output, error=False):
  log = logging.error if error else logging.info
  log("kaggle command output:\n%s", tf.compat.as_text(output))


class KaggleSearch(object):
  """Searcher for a Kaggle Competitions and Datasets."""
  def __init__(self, where='competitions', search=None, group=None,
               category=None,
               sort_by_competitions=None, sort_by_datasets=None, size=None,
               file_type=None, tag=None, user=None):
    self.search = search
    self.group = group
    self.category = category
    self.sort_by_competitions = sort_by_competitions
    self.where = where
    self.sort_by_datasets = sort_by_datasets
    self.size = size
    self.file_type = file_type
    self.tag = tag
    self.user = user

  # TODO add page number
  @property
  def searching(self):
    """Run kaggle search with subprocess."""
    command = ["kaggle", self.where, 'list']

    competitions_parameters = {'--search': self.search, '--group': self.group,
                               '--category': self.category,
                               '--sort-by': self.sort_by_competitions}
    datasets_parameters = {'--sort-by': self.sort_by_datasets,
                           '--size': self.size, '--file-type': self.file_type,
                           '--tags': self.tag, '--user': self.user}

    if self.where == 'competitions':
      parameters = competitions_parameters
    else:
      parameters = datasets_parameters

    for i, j in parameters.items():
      if j is not None or '':
        command.extend([i, j])

    if self.where != 'competitions':
      # Fit to the dataset table.
      display.display(display.HTML("<style>.container { width:80% !important; }"
                                   "</style>"))

    output = _run_kaggle_command(command)
    return output


# TODO error handling
def search_and_download():
  """Kaggle Searcher and Downloader extension for Jupyter Notebook"""

  tf.logging.set_verbosity(tf.logging.ERROR)

  options = {'where': ['competitions', 'datasets'],
             'group': ['general', 'entered', 'inClass'],
             'category': ['all', 'featured', 'research', 'recruitment',
                          'gettingStarted', 'masters', 'playground'],
             'sort-by-competition': ['grouped', 'prize', 'earliestDeadline',
                                     'latestDeadline', 'numberOfTeams',
                                     'recentlyCreated'],
             'sort-by-dataset': ['hottest', 'votes', 'updated', 'active'],
             'size': ['all', 'small', 'medium', 'large'],
             'file-type': ['all', 'csv', 'sqlite', 'json'],

             }
  where = widgets.Dropdown(options=options['where'], description="Where",
                           layout=widgets.Layout(width='auto',
                                                 grid_area='where'))
  search_input = widgets.Text(placeholder='Search on Kaggle',
                              description='Search:',
                              layout=widgets.Layout(width='auto',
                                                    grid_area='search'))

  # Competitions arguments
  group = widgets.Dropdown(options=options['group'], description="Group",
                           layout=widgets.Layout(width='auto',
                                                 grid_area='group'))
  category = widgets.Dropdown(options=options['category'],
                              description="Category",
                              layout=widgets.Layout(width='auto',
                                                    grid_area='category'))
  sort_by_competitions = widgets.Dropdown(
      options=options['sort-by-competition'], description="Sort-by",
      layout=widgets.Layout(width='auto', grid_area='sort-by'))
  search_button = widgets.Button(description="Search",
                                 style=widgets.ButtonStyle(
                                     button_color='lightblue'))

  # Dataset arguments
  sort_by_datasets = widgets.Dropdown(options=options['sort-by-dataset'],
                                      description="Sort-by",
                                      layout=widgets.Layout(width='auto',
                                                            grid_area='sort-by')
                                      )
  size = widgets.Dropdown(options=options['size'], description="File Size",
                          layout=widgets.Layout(width='auto', grid_area='size')
                          )
  file_type = widgets.Dropdown(options=options['file-type'],
                               description="File type",
                               layout=widgets.Layout(width='auto',
                                                     grid_area='file_type')
                               )
  tag = widgets.Text(placeholder='Dataset Tag', description='Filter by tag:',
                     layout=widgets.Layout(width='auto', grid_area='search')
                     )
  user = widgets.Text(placeholder='User', description='Filter by user:',
                      layout=widgets.Layout(width='auto', grid_area='search')
                      )

  def on_change(change):
    """Change search options based on datasets or competitions"""
    if change['type'] == 'change' and change['new'] == 'competitions':
      display.clear_output(wait=True)
      display.display(search_input, group, category, sort_by_competitions,
                      search_button)
    elif change['type'] == 'change' and change['new'] == 'datasets':
      display.clear_output(wait=True)
      display.display(where, sort_by_datasets, size, file_type, tag, user,
                      search_button)

  where.observe(on_change)
  display.display(where)
  display.display(search_input, group, category, sort_by_competitions,
                  search_button)

  def handle_submit(sender):  # pylint: disable=unused-argument
    display.clear_output(wait=True)

    results = KaggleSearch(where=where.value,
                     search=search_input.value,
                     group=group.value,
                     category=category.value,
                     sort_by_competitions=sort_by_competitions.value,
                     sort_by_datasets=sort_by_datasets.value,
                     size=size.value, file_type=file_type.value, tag=tag.value,
                     user=user.value)

    print(results.searching)
    dataset_name = widgets.Text(placeholder=where.value.capitalize() + ' Name',
                                description='Download:')
    display.display(dataset_name)
    download_button = widgets.Button(description="Download",
                                     style=widgets.ButtonStyle(
                                         button_color='lightblue'))
    display.display(download_button)

    def kag_downloader(sender):  # pylint: disable=unused-argument
      """Download all files."""
      downloader = KaggleCompetitionDownloader(dataset_name.value)
      print('Downloading...')
      for fname in downloader.competition_files:
        downloader.download_file(fname, dataset_name.value)
        print('Downloaded ', fname)
      print('Download Completed!')

    download_button.on_click(kag_downloader)

  search_button.on_click(handle_submit)

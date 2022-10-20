# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""CNN/DailyMail Summarization dataset, non-anonymized version."""

import hashlib
import os
from typing import Dict, List

from absl import logging
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
CNN/DailyMail non-anonymized summarization dataset.

There are two features:
  - article: text of news article, used as the document to be summarized
  - highlights: joined text of highlights with <s> and </s> around each
    highlight, which is the target summary
"""

# The second citation introduces the source data, while the first
# introduces the specific form (non-anonymized) we use here.
_CITATION = """\
@article{DBLP:journals/corr/SeeLM17,
  author    = {Abigail See and
               Peter J. Liu and
               Christopher D. Manning},
  title     = {Get To The Point: Summarization with Pointer-Generator Networks},
  journal   = {CoRR},
  volume    = {abs/1704.04368},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.04368},
  archivePrefix = {arXiv},
  eprint    = {1704.04368},
  timestamp = {Mon, 13 Aug 2018 16:46:08 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SeeLM17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}

@inproceedings{hermann2015teaching,
  title={Teaching machines to read and comprehend},
  author={Hermann, Karl Moritz and Kocisky, Tomas and Grefenstette, Edward and Espeholt, Lasse and Kay, Will and Suleyman, Mustafa and Blunsom, Phil},
  booktitle={Advances in neural information processing systems},
  pages={1693--1701},
  year={2015}
}
"""

_DL_URLS = {
    # pylint: disable=line-too-long
    'cnn_stories':
        'https://drive.google.com/uc?export=download&id=0BwmD_VLjROrfTHk4NFg2SndKcjQ',
    'dm_stories':
        'https://drive.google.com/uc?export=download&id=0BwmD_VLjROrfM1BxdkxVaTY2bWs',
    'test_urls':
        'https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_test.txt',
    'train_urls':
        'https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_train.txt',
    'val_urls':
        'https://raw.githubusercontent.com/abisee/cnn-dailymail/master/url_lists/all_val.txt',
    # pylint: enable=line-too-long
}

_HIGHLIGHTS = 'highlights'
_ARTICLE = 'article'
_PUBLISHER = 'publisher'
_ID = 'id'


def _get_url_hashes(path):
  """Get hashes of urls in file."""
  urls = _read_text_file(path)

  def url_hash(u):
    h = hashlib.sha1()
    try:
      u = u.encode('utf-8')
    except UnicodeDecodeError:
      logging.error('Cannot hash url: %s', u)
    h.update(u)
    return h.hexdigest()

  return {url_hash(u): True for u in urls}


def _find_files(dl_paths, publisher, url_dict):
  """Find files corresponding to urls."""
  if publisher == 'cnn':
    top_dir = os.path.join(dl_paths['cnn_stories'], 'cnn', 'stories')
  elif publisher == 'dm':
    top_dir = os.path.join(dl_paths['dm_stories'], 'dailymail', 'stories')
  else:
    logging.fatal('Unsupported publisher: %s', publisher)
  files = tf.io.gfile.listdir(top_dir)

  ret_files = []
  for p in files:
    basename = os.path.basename(p)
    if basename[0:basename.find('.story')] in url_dict:
      ret_files.append(os.path.join(top_dir, p))
  return ret_files


def _subset_filenames(dl_paths, split):
  """Get filenames for a particular split."""
  assert isinstance(dl_paths, dict), dl_paths
  # Get filenames for a split.
  if split == tfds.Split.TRAIN:
    urls = _get_url_hashes(dl_paths['train_urls'])
  elif split == tfds.Split.VALIDATION:
    urls = _get_url_hashes(dl_paths['val_urls'])
  elif split == tfds.Split.TEST:
    urls = _get_url_hashes(dl_paths['test_urls'])
  else:
    logging.fatal('Unsupported split: %s', split)
  cnn = _find_files(dl_paths, 'cnn', urls)
  dm = _find_files(dl_paths, 'dm', urls)
  return {'cnn': cnn, 'dm': dm}


DM_SINGLE_CLOSE_QUOTE = u'\u2019'  # unicode
DM_DOUBLE_CLOSE_QUOTE = u'\u201d'
# acceptable ways to end a sentence
END_TOKENS = [
    '.', '!', '?', '...', "'", '`', '"', DM_SINGLE_CLOSE_QUOTE,
    DM_DOUBLE_CLOSE_QUOTE, ')'
]


def _read_text_file(text_file):
  lines = []
  with tf.io.gfile.GFile(text_file, 'r') as f:
    for line in f:
      lines.append(line.strip())
  return lines


def _get_art_abs(story_file):
  """Get abstract (highlights) and article from a story file path."""
  # Based on https://github.com/abisee/cnn-dailymail/blob/master/
  #     make_datafiles.py

  lines = _read_text_file(story_file)

  # The github code lowercase the text and we removed it in 3.0.0.

  # Put periods on the ends of lines that are missing them
  # (this is a problem in the dataset because many image captions don't end in
  # periods; consequently they end up in the body of the article as run-on
  # sentences)
  def fix_missing_period(line):
    """Adds a period to a line that is missing a period."""
    if '@highlight' in line:
      return line
    if not line:
      return line
    if line[-1] in END_TOKENS:
      return line
    return line + '.'

  lines = [fix_missing_period(line) for line in lines]

  # Separate out article and abstract sentences
  article_lines = []
  highlights = []
  next_is_highlight = False
  for line in lines:
    if not line:
      continue  # empty line
    elif line.startswith('@highlight'):
      next_is_highlight = True
    elif next_is_highlight:
      highlights.append(line)
    else:
      article_lines.append(line)

  # Make article into a single string
  article = ' '.join(article_lines)
  abstract = '\n'.join(highlights)

  return article, abstract


class CnnDailymail(tfds.core.GeneratorBasedBuilder):
  """CNN/DailyMail non-anonymized summarization dataset."""

  VERSION = tfds.core.Version('3.4.0')
  RELEASE_NOTES = {
      '1.0.0':
          'New split API (https://tensorflow.org/datasets/splits)',
      '2.0.0':
          """
      Separate target sentences with newline. (Having the model predict newline
      separators makes it easier to evaluate using summary-level ROUGE.)
      """,
      '3.0.0':
          'Using cased version.',
      '3.1.0':
          'Removed BuilderConfig',
      '3.2.0':
          """
      Remove extra space before added sentence period.
      This shouldn't affect ROUGE scores because punctuation is removed.
      """,
      '3.3.0':
          'Add publisher feature.',
      '3.4.0':
          'Add ID feature.'
  }

  def _info(self):
    # Should return a tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _ARTICLE: tfds.features.Text(),
            _HIGHLIGHTS: tfds.features.Text(),
            _PUBLISHER: tfds.features.Text(),
            _ID: tfds.features.Text(),
        }),
        supervised_keys=(_ARTICLE, _HIGHLIGHTS),
        homepage='https://github.com/abisee/cnn-dailymail',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_paths = dl_manager.download_and_extract(_DL_URLS)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'files': _subset_filenames(dl_paths,
                                                   tfds.Split.TRAIN)}),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'files': _subset_filenames(dl_paths, tfds.Split.VALIDATION)
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'files': _subset_filenames(dl_paths, tfds.Split.TEST)})
    ]

  def _generate_examples(self, files: Dict[str, List[str]]):
    for pub, file_list in files.items():
      for p in file_list:
        article, highlights = _get_art_abs(p)
        if not article or not highlights:
          continue
        fname = os.path.basename(p)
        clean_id = fname
        if fname.endswith('.story'):
          clean_id = clean_id[:-6]
        yield fname, {
            _ARTICLE: article,
            _HIGHLIGHTS: highlights,
            _PUBLISHER: pub,
            _ID: clean_id,
        }

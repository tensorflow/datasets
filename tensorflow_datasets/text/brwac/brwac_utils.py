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

"""Utilities for the brwac dataset."""

import re
from typing import Dict

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tqdm import tqdm

ftfy = tfds.core.lazy_imports.ftfy

paragraph_pattern = re.compile('<p> (.*?) </p>', flags=re.DOTALL)
sentence_pattern = re.compile('<s> (.*?) </s>', flags=re.DOTALL)


def extract_ids(line, fix_title=True):
  matches = re.findall('<doc docid="(.*?)" title="(.*?)" uri="(.*?)">', line)
  assert len(matches) == 1
  doc_id, title, uri = matches[0]
  if fix_title:
    title = ftfy.fix_text(title)
  return dict(doc_id=doc_id, title=title, uri=uri)


def parse_single_doc(doc_string: str) -> Dict:
  """Parses single brwac document"""
  doc_header, doc_body = doc_string.split('\n', maxsplit=1)
  doc_body = ' '.join(doc_body.replace('\n<g/>\n', '').split())
  paragraphs = [
      list(map(ftfy.fix_text, re.findall(sentence_pattern, sentences)))
      for sentences in re.findall(paragraph_pattern, doc_body)
  ]
  return_dict = extract_ids(doc_header)
  return_dict.update({'text': {'paragraphs': paragraphs}})
  return return_dict


def parse_vert_file(path: str, show_progress: bool = True):
  """Parses brwac vert file.

    Args:
        path: path for file
        show_progress (bool): if we should show a progress bar

    Yields:
        dict with a BrWac document contents
    """
  doc_buffer = ''
  doc_count = 0
  with tf.io.gfile.GFile(path, 'r') as fin:
    pbar = tqdm(
        fin,
        desc=f'Parsing BrWac vert file {path}.',
        disable=not (show_progress),
        unit=' lines processed'
    )
    for line in pbar:
      doc_buffer += line
      if line == '</doc>\n':  # end of document
        parsed_doc = parse_single_doc(doc_buffer)
        parsed_doc['doc_idx'] = doc_count
        yield parsed_doc
        del parsed_doc
        doc_buffer = ''
        doc_count += 1
        pbar.set_postfix(**{'Documents processed': doc_count})

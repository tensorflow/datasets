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

"""TriviaQA: A Reading Comprehension Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import os
from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """
@article{2017arXivtriviaqa,
       author = {{Joshi}, Mandar and {Choi}, Eunsol and {Weld},
                 Daniel and {Zettlemoyer}, Luke},
        title = "{triviaqa: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension}",
      journal = {arXiv e-prints},
         year = 2017,
          eid = {arXiv:1705.03551},
        pages = {arXiv:1705.03551},
archivePrefix = {arXiv},
       eprint = {1705.03551},
}
"""
_DOWNLOAD_URL = (
    "http://nlp.cs.washington.edu/triviaqa/data/triviaqa-rc.tar.gz")
_TOP_LEVEL_DIRNAME = "qa"
_EVIDENCE_DIRNAME = "evidence"
_TRAIN_FILE_FORMAT = os.path.join(_TOP_LEVEL_DIRNAME, "*-train.json")
_HELDOUT_FILE_FORMAT = os.path.join(_TOP_LEVEL_DIRNAME,
                                    "*test-without-answers.json")
_WEB_EVIDENCE_DIR = os.path.join(_EVIDENCE_DIRNAME, "web")
_WIKI_EVIDENCE_DIR = os.path.join(_EVIDENCE_DIRNAME, "wikipedia")

_DESCRIPTION = """\
TriviaqQA is a reading comprehension dataset containing over 650K
question-answer-evidence triples. TriviaqQA includes 95K question-answer
pairs authored by trivia enthusiasts and independently gathered evidence
documents, six per question on average, that provide high quality distant
supervision for answering the questions.
"""


def _train_data_filenames(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _TRAIN_FILE_FORMAT))


def _test_data_filenames(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _HELDOUT_FILE_FORMAT))


def _web_evidence_dir(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _WEB_EVIDENCE_DIR))


def _wiki_evidence_dir(tmp_dir):
  return tf.io.gfile.glob(os.path.join(tmp_dir, _WIKI_EVIDENCE_DIR))


class TriviaQA(tfds.core.GeneratorBasedBuilder):
  """TriviaQA is a reading comprehension dataset.

  It containss over 650K question-answer-evidence triples.
  """

  VERSION = tfds.core.Version("0.1.0",
                              experiments={tfds.core.Experiment.S3: False})

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "question":
                tfds.features.Text(),
            "question_id":
                tfds.features.Text(),
            "question_source":
                tfds.features.Text(),
            "entity_pages":
                tfds.features.Sequence({
                    "doc_source": tfds.features.Text(),
                    "file_name": tfds.features.Text(),
                    "title": tfds.features.Text(),
                    "wiki_context": tfds.features.Text(),
                }),
            "search_results":
                tfds.features.Sequence({
                    "description":
                        tfds.features.Text(),
                    "file_name":
                        tfds.features.Text(),
                    "rank":
                        tf.int32,
                    "title":
                        tfds.features.Text(),
                    "url":
                        tfds.features.Text(),
                    "search_context":
                        tfds.features.Text(),
                }),
            "answer":
                tfds.features.FeaturesDict({
                    "aliases":
                        tfds.features.Sequence(tfds.features.Text()),
                    "normalized_aliases":
                        tfds.features.Sequence(tfds.features.Text()),
                    "matched_wiki_entity_name":
                        tfds.features.Text(),
                    "normalized_matched_wiki_entity_name":
                        tfds.features.Text(),
                    "normalized_value":
                        tfds.features.Text(),
                    "type":
                        tfds.features.Text(),
                    "value":
                        tfds.features.Text(),
                }),
        }),

        supervised_keys=None,
        urls=["http://nlp.cs.washington.edu/triviaqa/"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    trivia_path = dl_manager.download_and_extract(_DOWNLOAD_URL)

    train_files = _train_data_filenames(trivia_path)
    test_files = _test_data_filenames(trivia_path)
    web_evidence_dir = _web_evidence_dir(trivia_path)
    wiki_evidence_dir = _wiki_evidence_dir(trivia_path)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=100,
            gen_kwargs={"files": train_files,
                        "web_dir": web_evidence_dir,
                        "wiki_dir": wiki_evidence_dir}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            num_shards=10,
            gen_kwargs={"files": test_files,
                        "web_dir": web_evidence_dir,
                        "wiki_dir": wiki_evidence_dir}),
    ]

  def _generate_examples(self, files, web_dir, wiki_dir):
    """This function returns the examples."""
    for filepath in files:
      logging.info("generating examples from = %s", filepath)
      with tf.io.gfile.GFile(filepath) as f:
        triviaqa = json.load(f)
        for article in triviaqa["Data"]:
          if "Answer" in article:
            answer = article["Answer"]
            aliases = [alias.strip() for alias in answer["Aliases"]]
            normalized_aliases = [
                alias.strip() for alias in answer["NormalizedAliases"]
            ]
            matched_wiki_entity_name = answer.get("MatchedWikiEntryName",
                                                  "").strip()
            normalized_matched_wiki_entity_name = answer.get(
                "NormalizedMatchedWikiEntryName", "").strip()
            normalized_value = answer["NormalizedValue"].strip()
            type_ = answer["Type"].strip()
            value = answer["Value"].strip()

            answer_dict = {
                "aliases":
                    aliases,
                "normalized_aliases":
                    normalized_aliases,
                "matched_wiki_entity_name":
                    matched_wiki_entity_name,
                "normalized_matched_wiki_entity_name":
                    normalized_matched_wiki_entity_name,
                "normalized_value":
                    normalized_value,
                "type":
                    type_,
                "value":
                    value,
            }
          else:
            answer_dict = {
                "aliases":
                    [],
                "normalized_aliases":
                    [],
                "matched_wiki_entity_name":
                    "<unk>",
                "normalized_matched_wiki_entity_name":
                    "<unk>",
                "normalized_value":
                    "<unk>",
                "type":
                    "",
                "value":
                    "<unk>",
            }

          if "SearchResults" in article:
            descriptions = [search_result["Description"].strip() for
                            search_result in article["SearchResults"]]
            search_file_names = [
                search_result["Filename"].strip() for
                search_result in article["SearchResults"]
            ]
            ranks = [
                search_result["Rank"] for
                search_result in article["SearchResults"]
            ]
            titles = [
                search_result["Title"].strip() for
                search_result in article["SearchResults"]
            ]
            urls = [
                search_result["Url"].strip() for
                search_result in article["SearchResults"]
            ]
            search_contexts = []
            for file_name in search_file_names:
              try:
                search_file = os.path.join(web_dir[0], file_name)
                with tf.io.gfile.GFile(search_file) as f:
                  text = f.read()
                  search_contexts.append(text)
              except (IOError, tf.errors.NotFoundError):
                logging.info("File does not exist, skipping: %s", file_name)
                search_contexts.append("")
          else:
            descriptions = []
            search_file_names = []
            ranks = []
            titles = []
            urls = []
            search_contexts = []

          question = article["Question"].strip()
          question_id = article["QuestionId"]
          question_source = article["QuestionSource"].strip()

          if article["EntityPages"]:
            doc_sources = [
                entitypage["DocSource"] for entitypage in article["EntityPages"]
            ]
            file_names = [
                entitypage["Filename"] for entitypage in article["EntityPages"]
            ]
            wiki_titles = [
                entitypage["Title"] for entitypage in article["EntityPages"]
            ]
            wiki_contexts = []
            for file_name in file_names:
              try:
                wiki_file = os.path.join(wiki_dir[0], file_name)
                with tf.io.gfile.GFile(wiki_file) as f:
                  text = f.read()
                  wiki_contexts.append(text)
              except (IOError, tf.errors.NotFoundError):
                logging.info("File does not exist, skipping: %s", file_name)
                wiki_contexts.append("")
          else:
            doc_sources = []
            file_names = []
            wiki_titles = []
            wiki_contexts = []

          yield {
              "entity_pages": {
                  "doc_source": doc_sources,
                  "file_name": file_names,
                  "title": wiki_titles,
                  "wiki_context": wiki_contexts,
              },
              "search_results": {
                  "description": descriptions,
                  "file_name": search_file_names,
                  "rank": ranks,
                  "title": titles,
                  "url": urls,
                  "search_context": search_contexts,
              },
              "question": question,
              "question_id": question_id,
              "question_source": question_source,
              "answer": answer_dict,
          }

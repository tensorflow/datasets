# coding=utf-8
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

"""web_nlg dataset."""

import os
import xml.etree.ElementTree as etree

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{gardent2017creating,
    title = ""Creating Training Corpora for {NLG} Micro-Planners"",
    author = ""Gardent, Claire  and
      Shimorina, Anastasia  and
      Narayan, Shashi  and
      Perez-Beltrachini, Laura"",
    booktitle = ""Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)"",
    month = jul,
    year = ""2017"",
    address = ""Vancouver, Canada"",
    publisher = ""Association for Computational Linguistics"",
    doi = ""10.18653/v1/P17-1017"",
    pages = ""179--188"",
    url = ""https://www.aclweb.org/anthology/P17-1017.pdf""
}
"""

_DESCRIPTION = """
The data contains sets of 1 to 7 triples of the form subject-predicate-object
extracted from (DBpedia)[https://wiki.dbpedia.org/] and natural language text
that's a verbalisation of these triples.
The test data spans 15 different domains where only 10 appear in the training
data.
The dataset follows a standarized table format.
"""

_URL = 'https://drive.google.com/uc?export=download&id=1C3d0a1wPkJqI3SVyYNtl99J1lErYYhsc'


class UnexpectedFormatError(Exception):
  """The specification of the sample set is malformed."""


class WebNlg(tfds.core.GeneratorBasedBuilder):
  """Set of triples subject-predicate-object to text."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table':  # Each row will be one triple fact.
                    tfds.features.Sequence({
                        # we'll only have subject/predicate/object headers
                        'column_header': tf.string,
                        'row_number': tf.int16,
                        'content': tf.string,
                    }),
                # context will be the category
                'context':
                    tf.string,
            },
            'target_text': tf.string,
        }),
        supervised_keys=('input_text', 'target_text'),
        # Homepage of the dataset for documentation
        homepage='https://webnlg-challenge.loria.fr/challenge_2017/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    def get_files_in_dir(directory):
      all_files = []
      for path, _, files in tf.io.gfile.walk(directory):
        for name in files:
          all_files.append(os.path.join(path, name))
      return all_files

    extracted_path = os.path.join(
        dl_manager.download_and_extract(_URL), 'webnlg-dataset-master',
        'webnlg_challenge_2017')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'list_files':
                    get_files_in_dir(os.path.join(extracted_path, 'train')),
                'set_name':
                    'train'
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'list_files':
                    get_files_in_dir(os.path.join(extracted_path, 'dev')),
                'set_name':
                    'validation'
            },
        ),
        tfds.core.SplitGenerator(
            name='test_unseen',
            gen_kwargs={
                'list_files': [
                    os.path.join(extracted_path, 'test',
                                 'testdata_unseen_with_lex.xml')
                ],
                'set_name': 'test_unseen'
            },
        ),
        tfds.core.SplitGenerator(
            name='test_all',
            gen_kwargs={
                'list_files': [
                    os.path.join(extracted_path, 'test',
                                 'testdata_with_lex.xml')
                ],
                'set_name': 'test_all'
            },
        ),
    ]

  def _generate_examples(self, list_files, set_name):
    """Yields examples."""
    for file in list_files:
      xml_file = etree.parse(file)
      xml_root = xml_file.getroot()
      for entry in list(xml_root)[0]:
        category = entry.attrib['category']
        entry_id = '{}_{}'.format(file, entry.attrib['eid'])
        triples_set = []
        target_text_i = 0
        for child_element in entry:
          if child_element.tag == 'modifiedtripleset':
            for i, triple in enumerate(child_element):
              for header, content in zip(['subject', 'predicate', 'object'],
                                         triple.text.split(' | ')):
                triples_set.append({
                    'column_header': header,
                    'row_number': i,
                    'content': content,
                })
          elif child_element.tag == 'lex':
            if not triples_set:
              raise UnexpectedFormatError(
                  'Found language expresion with no previous triplesets.')
            yield '{}_#{}'.format(entry_id, target_text_i), {
                'input_text': {
                    'table': triples_set,
                    'context': category
                },
                'target_text': child_element.text
            }
            target_text_i += 1

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

"""e2e_cleaned dataset."""

import csv

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = r"""
@inproceedings{dusek-etal-2019-semantic,
    title = "Semantic Noise Matters for Neural Natural Language Generation",
    author = "Du{\v{s}}ek, Ond{\v{r}}ej  and
      Howcroft, David M.  and
      Rieser, Verena",
    booktitle = "Proceedings of the 12th International Conference on Natural Language Generation",
    month = oct # "{--}" # nov,
    year = "2019",
    address = "Tokyo, Japan",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-8652",
    doi = "10.18653/v1/W19-8652",
    pages = "421--426",
    abstract = "Neural natural language generation (NNLG) systems are known for their pathological outputs, i.e. generating text which is unrelated to the input specification. In this paper, we show the impact of semantic noise on state-of-the-art NNLG models which implement different semantic control mechanisms. We find that cleaned data can improve semantic correctness by up to 97{\%}, while maintaining fluency. We also find that the most common error is omitting information, rather than hallucination.",
}
"""

_DESCRIPTION = """
An update release of E2E NLG Challenge data with cleaned MRs. The E2E data
contains dialogue act-based meaning representation (MR) in the restaurant domain
and up to 5 references in natural language, which is what one needs to predict.
"""

_HOMEPAGE_URL = 'https://github.com/tuetschek/e2e-cleaning'

_TRAIN_URL = 'https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/train-fixed.no-ol.csv'
_DEV_URL = 'https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/devel-fixed.no-ol.csv'
_TEST_URL = 'https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/test-fixed.csv'


def _get_table_from_mr(mr):
  """Converts a meaningful representation from e2e_cleaned dataset in a table."""
  mr_as_table = []
  for type_value in mr.split(', '):
    type_value_delimiter = type_value.find('[')
    type_ = type_value[0:type_value_delimiter]
    value = type_value[type_value_delimiter + 1:-1]
    mr_as_table.append({
        'column_header': type_,
        'row_number': 1,
        'content': value,
    })
  return mr_as_table


class E2eCleaned(tfds.core.GeneratorBasedBuilder):
  """MR in the restaurant domain and target utterances describing it."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table':
                    tfds.features.Sequence({
                        'column_header': tf.string,
                        'row_number': tf.int16,
                        'content': tf.string,
                    })
            },
            'target_text': tf.string,
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('input_text', 'target_text'),
        # Homepage of the dataset for documentation
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract({
        'train_path': _TRAIN_URL,
        'dev_path': _DEV_URL,
        'test_path': _TEST_URL
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'csv_path': extracted_path['train_path']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'csv_path': extracted_path['dev_path']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            # These kwargs will be passed to _generate_examples
            gen_kwargs={'csv_path': extracted_path['test_path']},
        ),
    ]

  def _generate_examples(self, csv_path):
    """Yields examples."""
    with tf.io.gfile.GFile(csv_path) as f:
      reader = csv.DictReader(f)
      for i, row in enumerate(reader):
        yield i, {
            'input_text': {
                'table': _get_table_from_mr(row['mr']),
            },
            'target_text': row['ref']
        }

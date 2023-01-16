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

"""wiki_table_text dataset."""

from __future__ import annotations

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Wikipedia tables with at least 3 rows and 2 columns, 3 random rows for each
table were selected for further annotation. Each row was annotated by a
different person, so the dataset is composed by (one row table, text
description) pairs. Annotations include at least 2 cells of the row, but do not
require to include them all.
The dataset follows a standarized table format.
"""

_CITATION = """
@inproceedings{bao2018table,
  title={Table-to-Text: Describing Table Region with Natural Language},
  author={Junwei Bao and Duyu Tang and Nan Duan and Zhao Yan and Yuanhua Lv and Ming Zhou and Tiejun Zhao},
  booktitle={AAAI},
  url={https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/download/16138/16782},
  year={2018}
}
"""

_TRAIN_URL = 'https://raw.githubusercontent.com/msra-nlc/Table2Text/master/MSRA_NLC.Table2Text.train'
_DEV_URL = 'https://raw.githubusercontent.com/msra-nlc/Table2Text/master/MSRA_NLC.Table2Text.dev'
_TEST_URL = 'https://raw.githubusercontent.com/msra-nlc/Table2Text/master/MSRA_NLC.Table2Text.test'


class WikiTableText(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wiki_table_text dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table': tfds.features.Sequence({
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                }),
            },
            'target_text': np.str_,
        }),
        supervised_keys=('input_text', 'target_text'),
        homepage='https://github.com/msra-nlc/Table2Text',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract(
        {'train_path': _TRAIN_URL, 'dev_path': _DEV_URL, 'test_path': _TEST_URL}
    )
    return {
        tfds.Split.TRAIN: self._generate_examples(extracted_path['train_path']),
        tfds.Split.VALIDATION: self._generate_examples(
            extracted_path['dev_path']
        ),
        tfds.Split.TEST: self._generate_examples(extracted_path['test_path']),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    with epath.Path(path).open() as f:
      for i, example_line in enumerate(f):
        _, headers, values, text = example_line.split('\t')
        headers = [h.replace('_$$_', ' ') for h in headers.split('_||_')]
        values = [v.replace('_$$_', ' ') for v in values.split('_||_')]
        # The tables only have one row and we specify it because the dataset
        # follows a standarized table format.
        table = []
        for header_i, value_i in zip(headers, values):
          table.append(
              {'column_header': header_i, 'row_number': 1, 'content': value_i}
          )
        text = text.replace('_$$_', ' ').replace(' .', '')
        yield i, {'input_text': {'table': table}, 'target_text': text}

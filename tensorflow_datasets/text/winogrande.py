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

"""The Winogrande Challenge."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{sakaguchi2019winogrande,
    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
    journal={arXiv preprint arXiv:1907.10641},
    year={2019}
}
"""

_DESCRIPTION = """\
The  WinoGrande, a large-scale dataset of 44k problems, inspired by the original
 Winograd Schema Challenge design, but adjusted to improve both the scale and
 the hardness of the dataset.
"""

_DATA_URL = 'https://storage.googleapis.com/ai2-mosaic/public/winogrande/winogrande_1.1.zip'


class Winogrande(tfds.core.GeneratorBasedBuilder):
  """The Winogrande challenge."""

  VERSION = tfds.core.Version('1.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'sentence': tfds.features.Text(),
            'option1': tfds.features.Text(),
            'option2': tfds.features.Text(),
            'label': tfds.features.ClassLabel(names=['1', '2']),
        }),
        # No default supervised_keys (as we have to pass both the sentence
        # and options as input).
        supervised_keys=None,
        homepage='http://winogrande.allenai.org/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    dl_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(dl_dir, 'winogrande_1.1')

    # Winogrande has different standardized training data sizes and reports
    # numbers for each of these data sizes, so make those available.
    data_sizes = ['xs', 's', 'm', 'l', 'xl']
    train_splits = []
    for size in data_sizes:
      train_splits.append(
          tfds.core.SplitGenerator(
              name=tfds.Split('train_{}'.format(size)),
              gen_kwargs={
                  'filepath': os.path.join(
                      data_dir, 'train_{}.jsonl'.format(size)
                  )
              },
          )
      )
    return train_splits + [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={'filepath': os.path.join(data_dir, 'test.jsonl')},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'filepath': os.path.join(data_dir, 'dev.jsonl')},
        ),
    ]

  def _generate_examples(self, filepath):
    """This function returns the examples in the raw (text) form."""
    with epath.Path(filepath).open() as f:
      for row in f:
        row_fields = json.loads(row)
        yield row_fields['qID'], {
            'sentence': row_fields['sentence'],
            'option1': row_fields['option1'],
            'option2': row_fields['option2'],
            'label': row_fields.get('answer', -1),
        }

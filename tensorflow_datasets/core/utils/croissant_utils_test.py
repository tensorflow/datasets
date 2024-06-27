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

import mlcroissant as mlc
import pytest
from tensorflow_datasets.core.utils import croissant_utils


@pytest.mark.parametrize(
    'croissant_name,croissant_url,tfds_name',
    [
        (
            'Name+1',
            'https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k',
            'huggingfaceh4__ultrachat_200k',
        ),
        ('Name+1', 'bad_url', 'name_1'),
        ('Name+1', None, 'name_1'),
    ],
)
def test_get_tfds_dataset_name(croissant_name, croissant_url, tfds_name):
  metadata = mlc.Metadata(name=croissant_name, url=croissant_url)
  dataset = mlc.Dataset.from_metadata(metadata)
  assert croissant_utils.get_tfds_dataset_name(dataset) == tfds_name


def test_get_record_set_ids():
  metadata = mlc.Metadata(
      name='dummy_dataset',
      url='https://dummy_url',
      record_sets=[
          mlc.RecordSet(
              id='record_set_1',
              fields=[],
          ),
          mlc.RecordSet(
              id='record_set_2',
              data_types=['http://mlcommons.org/croissant/Split'],
              fields=[mlc.Field(name='name', data_types=mlc.DataType.TEXT)],
              data=[{'name': 'train'}, {'name': 'test'}],
          ),
      ],
  )
  record_set_ids = croissant_utils.get_record_set_ids(metadata=metadata)
  assert record_set_ids == ['record_set_1']

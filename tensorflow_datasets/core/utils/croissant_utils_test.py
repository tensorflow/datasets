# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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
  assert (
      croissant_utils.get_tfds_dataset_name(dataset) == tfds_name
  ), f'Expected TFDS name: {tfds_name}'


@pytest.mark.parametrize(
    'attribute,language,expected_text',
    [
        ({'en': 'English Text', 'fr': 'Texte Français'}, None, 'English Text'),
        (
            {'de': 'Deutscher Text', 'fr': 'Texte Français'},
            None,
            'Deutscher Text',
        ),
        (
            {'en': 'English Text', 'fr': 'Texte Français'},
            'fr',
            'Texte Français',
        ),
        ('Simple Text', None, 'Simple Text'),
        ('Simple Text', 'en', 'Simple Text'),
        (None, None, None),
    ],
)
def test_extract_localized_string(attribute, language, expected_text):
  assert (
      croissant_utils.extract_localized_string(attribute, language=language)
      == expected_text
  )


def test_extract_localized_string_raises():
  # Language not found.
  with pytest.raises(
      ValueError,
      match=r"Language 'de' not found in text field keys:",
  ):
    croissant_utils.extract_localized_string(
        {'en': 'English Text', 'fr': 'Texte Français'}, language='de'
    )

  # Empty dictionary.
  with pytest.raises(
      ValueError, match='Dataset `text field` dictionary is empty'
  ):
    croissant_utils.extract_localized_string({}, language=None)

  # Incorrect type.
  with pytest.raises(TypeError, match='must be a string, dictionary, or None'):
    croissant_utils.extract_localized_string(123)


@pytest.mark.parametrize(
    'croissant_name,language,expected_name',
    [
        ({'en': 'English Name', 'fr': 'Nom Français'}, None, 'English Name'),
        (
            {'de': 'Deutscher Name', 'fr': 'Nom Français'},
            None,
            'Deutscher Name',
        ),
        ({'en': 'English Name', 'fr': 'Nom Français'}, 'fr', 'Nom Français'),
        ('Simple Name', None, 'Simple Name'),
    ],
)
def test_get_dataset_name(croissant_name, language, expected_name):
  ctx = mlc.Context(conforms_to='http://mlcommons.org/croissant/1.1')
  metadata = mlc.Metadata(name=croissant_name, ctx=ctx, url=None)
  dataset = mlc.Dataset.from_metadata(metadata)
  assert (
      croissant_utils.get_dataset_name(dataset, language=language)
      == expected_name
  )


def test_get_dataset_name_raises():
  ctx = mlc.Context(conforms_to='http://mlcommons.org/croissant/1.1')
  # Test language not found in name.
  metadata_lang_not_found = mlc.Metadata(
      name={'en': 'English Name', 'fr': 'Nom Français'}, ctx=ctx, url=None
  )
  dataset_lang_not_found = mlc.Dataset.from_metadata(metadata_lang_not_found)
  with pytest.raises(
      ValueError, match=r"Language 'de' not found in name keys:"
  ):
    croissant_utils.get_dataset_name(dataset_lang_not_found, language='de')

  # Test empty dictionary name.
  metadata_empty_dict = mlc.Metadata(name={}, ctx=ctx, url=None)
  dataset_empty_dict = mlc.Dataset.from_metadata(metadata_empty_dict)
  with pytest.raises(ValueError, match='Dataset `name` dictionary is empty.'):
    croissant_utils.get_dataset_name(dataset_empty_dict, language=None)


def test_get_dataset_name_url_precedence():
  ctx = mlc.Context(conforms_to='http://mlcommons.org/croissant/1.1')
  # Test that URL prefix removal works and takes precedence over name.
  metadata = mlc.Metadata(
      name='Should Be Ignored',
      ctx=ctx,
      url='https://huggingface.co/datasets/user/dataset_name',
  )
  dataset = mlc.Dataset.from_metadata(metadata)
  assert croissant_utils.get_dataset_name(dataset) == 'user/dataset_name'

  # Test that URL precedence also works when the name is a dict.
  metadata_dict_name = mlc.Metadata(
      name={'en': 'Should Be Ignored'},
      ctx=ctx,
      url='https://huggingface.co/datasets/another/other_dataset',
  )
  dataset_dict_name = mlc.Dataset.from_metadata(metadata_dict_name)
  assert (
      croissant_utils.get_dataset_name(dataset_dict_name)
      == 'another/other_dataset'
  )

  # Test that non-HuggingFace URLs don't cause name to be ignored.
  metadata_other_url = mlc.Metadata(
      name='Not Ignored',
      ctx=ctx,
      url='https://example.com/dataset',
  )
  dataset_other_url = mlc.Dataset.from_metadata(metadata_other_url)
  assert croissant_utils.get_dataset_name(dataset_other_url) == 'Not Ignored'


@pytest.mark.parametrize(
    'croissant_version,tfds_version',
    [
        ('1.0', '1.0.0'),
        ('1.2', '1.2.0'),
        ('1.2.3', '1.2.3'),
        ('1.2.3.4', '1.2.3.4'),
        (None, None),
    ],
)
def test_get_croissant_version(croissant_version, tfds_version):
  assert (
      croissant_utils.get_croissant_version(croissant_version) == tfds_version
  )


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
              fields=[
                  mlc.Field(
                      id='record_set_2/name', data_types=mlc.DataType.TEXT
                  )
              ],
              data=[
                  {'record_set_2/name': 'train'},
                  {'record_set_2/name': 'test'},
              ],
          ),
      ],
  )
  record_set_ids = croissant_utils.get_record_set_ids(metadata=metadata)
  assert record_set_ids == ['record_set_1']


def test_get_split_recordset():
  record_sets = [
      mlc.RecordSet(
          id='records',
          fields=[
              mlc.Field(
                  id='records/split',
                  data_types=[mlc.DataType.TEXT],
                  source=mlc.Source(field='splits/name'),
                  references=mlc.Source(field='splits/name'),
              )
          ],
      ),
      mlc.RecordSet(
          id='splits',
          key='splits/name',
          data_types=[mlc.DataType.SPLIT],
          fields=[
              mlc.Field(
                  id='splits/name', name='name', data_types=mlc.DataType.TEXT
              )
          ],
          data=[{'splits/name': 'train'}, {'splits/name': 'test'}],
      ),
  ]
  metadata = mlc.Metadata(name='dummy', url='dum.my', record_sets=record_sets)
  dataset = mlc.Dataset.from_metadata(metadata)
  split_recordset = croissant_utils.get_split_recordset(
      record_set=dataset.metadata.record_sets[0], metadata=metadata
  )
  assert split_recordset is not None
  assert split_recordset.reference_field.id == 'records/split'
  assert split_recordset.split_record_set.id == 'splits'


def test_get_split_recordset_with_no_split_recordset():
  record_sets = [
      mlc.RecordSet(
          id='labels',
          key='labels/label',
          fields=[
              mlc.Field(
                  id='labels/label',
                  name='label',
                  data_types=mlc.DataType.TEXT,
              )
          ],
          data=[{'labels/label': 'bird'}, {'labels/label': 'bike'}],
      ),
      mlc.RecordSet(
          id='samples',
          fields=[
              mlc.Field(
                  id='samples/label',
                  data_types=mlc.DataType.TEXT,
                  source=mlc.Source(field='labels/label'),
                  references=mlc.Source(field='labels/label'),
              )
          ],
      ),
  ]
  metadata = mlc.Metadata(name='dummy', url='dum.my', record_sets=record_sets)
  split_recordset = croissant_utils.get_split_recordset(
      record_set=metadata.record_sets[0], metadata=metadata
  )
  assert split_recordset is None

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

"""Tests for croissant_builder."""

import numpy as np
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core.dataset_builders import croissant_builder
from tensorflow_datasets.core.features import bounding_boxes
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc

FileFormat = file_adapters.FileFormat


DUMMY_ENTRIES = [
    {
        "index": i,
        "text": f"Dummy example {i}",
        "split": "train" if i == 0 else "test",
    }
    for i in range(2)
]
DUMMY_ENTRIES_WITH_NONE_VALUES = [
    {"split": "train", "index": 0, "text": "Dummy example 0"},
    {"split": "test", "index": 1, "text": None},
]
DUMMY_ENTRIES_WITH_CONVERTED_NONE_VALUES = [
    {"split": "train", "index": 0, "text": "Dummy example 0"},
    {"split": "test", "index": 1, "text": ""},
]


@pytest.mark.parametrize(
    ["field", "expected_feature", "int_dtype", "float_dtype"],
    [
        (
            mlc.Field(
                data_types=mlc.DataType.INTEGER, description="Integer feature"
            ),
            np.int64,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.INT16, description="Int16 feature"
            ),
            np.int16,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.INTEGER, description="Integer feature"
            ),
            np.int8,
            np.int8,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.FLOAT, description="Float feature"
            ),
            np.float32,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.FLOAT16, description="Float16 feature"
            ),
            np.float16,
            None,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.FLOAT, description="Float feature"
            ),
            np.float64,
            None,
            np.float64,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.UINT16, description="Uint16 feature"
            ),
            np.uint16,
            None,
            np.uint16,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.BOOL, description="Boolean feature"
            ),
            np.bool_,
            None,
            None,
        ),
    ],
)
def test_simple_datatype_converter(
    field, expected_feature, int_dtype, float_dtype
):
  actual_feature = croissant_builder.datatype_converter(
      field,
      int_dtype=int_dtype or np.int64,
      float_dtype=float_dtype or np.float32,
  )
  assert actual_feature == expected_feature


@pytest.mark.parametrize(
    ["field", "feature_type", "subfield_types"],
    [
        (
            mlc.Field(data_types=mlc.DataType.TEXT, description="Text feature"),
            text_feature.Text,
            None,
        ),
        (
            mlc.Field(data_types=mlc.DataType.DATE, description="Date feature"),
            text_feature.Text,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.IMAGE_OBJECT,
                description="Image feature",
            ),
            image_feature.Image,
            None,
        ),
        (
            mlc.Field(
                data_types=mlc.DataType.BOUNDING_BOX,
                description="Bounding box feature",
            ),
            bounding_boxes.BBoxFeature,
            None,
        ),
        (
            mlc.Field(
                id="person",
                data_types=[],
                description="A field with subfields",
                sub_fields=[
                    mlc.Field(id="person/name", data_types=mlc.DataType.TEXT),
                    mlc.Field(id="person/age", data_types=mlc.DataType.INTEGER),
                ],
            ),
            features_dict.FeaturesDict,
            {
                "person/name": text_feature.Text,
                "person/age": tensor_feature.Tensor,
            },
        ),
    ],
)
def test_complex_datatype_converter(field, feature_type, subfield_types):
  actual_feature = croissant_builder.datatype_converter(field)
  assert actual_feature.doc.desc == field.description
  assert isinstance(actual_feature, feature_type)
  if subfield_types:
    for feature_name in actual_feature.keys():
      assert isinstance(
          actual_feature[feature_name], subfield_types[feature_name]
      )


def test_multidimensional_datatype_converter():
  field = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="2,2",
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, tensor_feature.Tensor)
  assert actual_feature.shape == (2, 2)
  assert actual_feature.dtype == np.str_


def test_multidimensional_datatype_converter_image_object():
  field = mlc.Field(
      data_types=mlc.DataType.IMAGE_OBJECT,
      description="Text feature",
      is_array=True,
      array_shape="2,2",
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature.feature, image_feature.Image)


def test_multidimensional_datatype_converter_plain_list():
  field = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="-1",
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, text_feature.Text)


def test_multidimensional_datatype_converter_unknown_shape():
  field = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="-1,2",
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature.feature, text_feature.Text)


def test_sequence_feature_datatype_converter():
  field = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      repeated=True,
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, text_feature.Text)


def test_version_converter(tmp_path):
  with testing.dummy_croissant_file(version="1.0") as croissant_file:
    builder = croissant_builder.CroissantBuilder(
        jsonld=croissant_file,
        file_format=FileFormat.ARRAY_RECORD,
        disable_shuffling=True,
        data_dir=tmp_path,
    )
    assert builder.version == "1.0.0"


@pytest.fixture(name="crs_builder")
def mock_croissant_dataset_builder(tmp_path, request):
  dataset_name = request.param["dataset_name"]
  with testing.dummy_croissant_file(
      dataset_name=dataset_name,
      entries=request.param["entries"],
      split_names=["train", "test"],
  ) as croissant_file:
    builder = croissant_builder.CroissantBuilder(
        jsonld=croissant_file,
        file_format=FileFormat.ARRAY_RECORD,
        disable_shuffling=True,
        data_dir=tmp_path,
    )
    yield builder


@pytest.mark.parametrize(
    "crs_builder",
    [
        {"dataset_name": "DummyDataset", "entries": DUMMY_ENTRIES},
        {
            "dataset_name": "DummyDatasetWithNoneValues",
            "entries": DUMMY_ENTRIES_WITH_NONE_VALUES,
        },
    ],
    indirect=True,
)
def test_croissant_builder(crs_builder):
  assert crs_builder.version == "1.2.0"
  assert (
      crs_builder._info().citation
      == "@article{dummyarticle, title={title}, author={author}, year={2020}}"
  )
  assert crs_builder._info().description == "Dummy description."
  assert crs_builder._info().homepage == "https://dummy_url"
  assert crs_builder._info().redistribution_info.license == "Public"
  # One `split` and one `jsonl` recordset.
  assert len(crs_builder.metadata.record_sets) == 2
  assert set([rs.id for rs in crs_builder.metadata.record_sets]) == {
      "jsonl",
      "split",
  }
  assert (
      crs_builder.metadata.ctx.conforms_to.value
      == "http://mlcommons.org/croissant/1.0"
  )


@pytest.mark.parametrize(
    "crs_builder,expected_entries",
    [
        (
            {"dataset_name": "DummyDataset", "entries": DUMMY_ENTRIES},
            DUMMY_ENTRIES,
        ),
        (
            {
                "dataset_name": "DummyDatasetWithNoneValues",
                "entries": DUMMY_ENTRIES_WITH_NONE_VALUES,
            },
            DUMMY_ENTRIES_WITH_CONVERTED_NONE_VALUES,
        ),
    ],
    indirect=["crs_builder"],
)
@pytest.mark.parametrize("split_name", ["train", "test"])
def test_download_and_prepare(crs_builder, expected_entries, split_name):
  crs_builder.download_and_prepare()
  data_source = crs_builder.as_data_source(split=split_name)
  expected_entries = [
      entry for entry in expected_entries if entry["split"] == split_name
  ]
  assert len(data_source) == 1
  assert len(expected_entries) == 1
  for entry, expected_entry in zip(data_source, expected_entries):
    assert entry["index"] == expected_entry["index"]
    assert entry["text"].decode() == expected_entry["text"]

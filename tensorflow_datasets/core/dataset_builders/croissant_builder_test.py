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

from typing import Any, Dict, List, Type
import numpy as np
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core.dataset_builders import croissant_builder
from tensorflow_datasets.core.features import audio_feature
from tensorflow_datasets.core.features import bounding_boxes
from tensorflow_datasets.core.features import bounding_boxes_utils as bb_utils
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.features import image_feature
from tensorflow_datasets.core.features import sequence_feature
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.features import text_feature
from tensorflow_datasets.core.features import video_feature
from tensorflow_datasets.core.utils.lazy_imports_utils import mlcroissant as mlc

FileFormat = file_adapters.FileFormat

DUMMY_DESCRIPTION = "Dummy description."


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


def _create_mlc_field(
    data_types: mlc.DataType | list[mlc.DataType],
    description: str,
    is_array: bool = False,
    array_shape: str | None = None,
    repeated: bool = False,
    source: mlc.Source | None = None,
    sub_fields: list[mlc.Field] | None = None,
) -> mlc.Field:
  field = mlc.Field(
      data_types=data_types,
      description=description,
      is_array=is_array,
      array_shape=array_shape,
      repeated=repeated,
      sub_fields=sub_fields,
  )
  if source is not None:
    field.source = source
  return field


@pytest.mark.parametrize(
    ["mlc_field", "expected_feature", "int_dtype", "float_dtype"],
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
    mlc_field: mlc.Field,
    expected_feature: type[Any],
    int_dtype: np.dtype | None,
    float_dtype: np.dtype | None,
):
  actual_feature = croissant_builder.datatype_converter(
      mlc_field,
      int_dtype=int_dtype or np.int64,
      float_dtype=float_dtype or np.float32,
  )
  assert actual_feature == expected_feature


def test_datatype_converter_bbox():
  field = _create_mlc_field(
      data_types=mlc.DataType.BOUNDING_BOX,
      description="Bounding box feature",
      source=mlc.Source(format="XYWH"),
  )
  actual_feature = croissant_builder.datatype_converter(field)
  assert isinstance(actual_feature, bounding_boxes.BBoxFeature)
  assert actual_feature.bbox_format == bb_utils.BBoxFormat.XYWH


def test_datatype_converter_bbox_with_invalid_format():
  field = _create_mlc_field(
      data_types=mlc.DataType.BOUNDING_BOX,
      description="Bounding box feature",
      source=mlc.Source(format="InvalidFormat"),
  )
  with pytest.raises(ValueError, match="Unsupported bounding box format"):
    croissant_builder.datatype_converter(field)


@pytest.mark.parametrize(
    ["mlc_field", "feature_type", "subfield_types"],
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
                data_types=mlc.DataType.DATETIME, description="DateTime feature"
            ),
            text_feature.Text,
            None,
        ),
        (
            mlc.Field(data_types=mlc.DataType.TIME, description="Time feature"),
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
                data_types=mlc.DataType.AUDIO_OBJECT,
                description="Audio feature",
            ),
            audio_feature.Audio,
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
                data_types=mlc.DataType.VIDEO_OBJECT,
                description="Video feature",
            ),
            video_feature.Video,
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
def test_datatype_converter_complex(
    mlc_field: mlc.Field,
    feature_type: Type[Any],
    subfield_types: Dict[str, Type[Any]] | None,
):
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  expected_description = mlc_field.description
  if isinstance(expected_description, dict):
    expected_description = expected_description.get(
        "en", next(iter(expected_description.values()))
    )
  assert actual_feature.doc.desc == expected_description
  assert isinstance(actual_feature, feature_type)
  if subfield_types is not None:
    for feature_name in actual_feature.keys():
      assert isinstance(
          actual_feature[feature_name], subfield_types[feature_name]
      )


def test_datatype_converter_multilingual_description():
  mlc_field = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description={"en": "English desc", "fr": "Description française"},
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert actual_feature.doc.desc == "English desc"

  mlc_field_no_en = mlc.Field(
      data_types=mlc.DataType.TEXT,
      description={
          "de": "Deutsche Beschreibung",
          "fr": "Description française",
      },
  )
  actual_feature_no_en = croissant_builder.datatype_converter(mlc_field_no_en)
  assert actual_feature_no_en.doc.desc == "Deutsche Beschreibung"


def test_datatype_converter_none():
  field = mlc.Field(
      name="my_field", id="my_field", description="Field with empty data type."
  )
  assert croissant_builder.datatype_converter(field) is None


def test_multidimensional_datatype_converter():
  mlc_field = _create_mlc_field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="2,2",
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert isinstance(actual_feature, tensor_feature.Tensor)
  assert actual_feature.shape == (2, 2)
  assert actual_feature.dtype == np.str_


def test_multidimensional_datatype_converter_image_object():
  mlc_field = _create_mlc_field(
      data_types=mlc.DataType.IMAGE_OBJECT,
      description="Text feature",
      is_array=True,
      array_shape="2,2",
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature.feature, image_feature.Image)


def test_multidimensional_datatype_converter_plain_list():
  mlc_field = _create_mlc_field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="-1",
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, text_feature.Text)


def test_multidimensional_datatype_converter_unknown_shape():
  mlc_field = _create_mlc_field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      is_array=True,
      array_shape="-1,2",
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature.feature, text_feature.Text)


def test_sequence_feature_datatype_converter():
  mlc_field = _create_mlc_field(
      data_types=mlc.DataType.TEXT,
      description="Text feature",
      repeated=True,
  )
  actual_feature = croissant_builder.datatype_converter(mlc_field)
  assert isinstance(actual_feature, sequence_feature.Sequence)
  assert isinstance(actual_feature.feature, text_feature.Text)


@pytest.mark.parametrize(
    ["license_", "expected_license"],
    [
        ("MIT", "MIT"),
        (
            mlc.CreativeWork(
                name="Creative Commons",
                description="Attribution 4.0 International",
                url="https://creativecommons.org/licenses/by/4.0/",
            ),
            (
                "[Creative Commons][Attribution 4.0"
                " International][https://creativecommons.org/licenses/by/4.0/]"
            ),
        ),
        (
            mlc.CreativeWork(
                name="Creative Commons",
            ),
            "[Creative Commons]",
        ),
        (
            mlc.CreativeWork(
                description="Attribution 4.0 International",
            ),
            "[Attribution 4.0 International]",
        ),
        (
            mlc.CreativeWork(
                url="https://creativecommons.org/licenses/by/4.0/",
            ),
            "[https://creativecommons.org/licenses/by/4.0/]",
        ),
        (
            mlc.CreativeWork(),
            "[]",
        ),
    ],
)
def test_extract_license(license_, expected_license):
  actual_license = croissant_builder._extract_license(license_)
  assert actual_license == expected_license


def test_extract_license_with_invalid_input():
  with pytest.raises(
      ValueError, match="^license_ should be mlc.CreativeWork | str"
  ):
    croissant_builder._extract_license(123)


def test_get_license():
  metadata = mlc.Metadata(license=["MIT", "Apache 2.0"])
  actual_license = croissant_builder._get_license(metadata)
  assert actual_license == "MIT, Apache 2.0"


def test_get_license_with_invalid_input():
  with pytest.raises(ValueError, match="metadata should be mlc.Metadata"):
    croissant_builder._get_license(123)


def test_get_license_with_empty_license():
  metadata = mlc.Metadata(license=[])
  assert croissant_builder._get_license(metadata) is None


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
def mock_croissant_dataset_builder(
    tmp_path, request
) -> croissant_builder.CroissantBuilder:
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
  assert crs_builder._info().description == DUMMY_DESCRIPTION
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
def test_download_and_prepare(
    crs_builder: croissant_builder.CroissantBuilder,
    expected_entries: List[Dict[str, Any]],
    split_name: str,
):
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
